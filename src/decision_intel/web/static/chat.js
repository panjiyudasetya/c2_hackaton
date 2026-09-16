// Wires the MAP.ANSWER-style template to the real decision-intel Flask
// backend: /api/status for the header indicator, /api/ask (SSE-over-POST)
// for real streamed answers. No fake setTimeout replies.

const chatBox = document.getElementById('chatBox');
const chatList = document.getElementById('chatList');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');

const WELCOME_HTML = `
    <div class="message bot">
        <div class="avatar"><i class="fa-solid fa-robot"></i></div>
        <div class="msg-content">
            Hi — I'm the <strong>decision-intel</strong> assistant. Ask me why a technical decision
            was made and I'll search the collected GitHub, JIRA, Confluence, and Notion data and
            cite my sources.
        </div>
    </div>
`;

let questionCount = 0;

// ── status indicator ─────────────────────────────────────────────────────────

async function checkStatus() {
    try {
        const res = await fetch('/api/status');
        const data = await res.json();
        if (!data.index_ready) {
            statusDot.style.color = '#F87171';
            statusText.textContent = 'No index yet — run `decision-intel build`';
        } else if (!data.graph_ready) {
            statusDot.style.color = '#FBBF24';
            statusText.textContent = 'Index ready, graph missing (links disabled)';
        } else {
            statusDot.style.color = '#22C55E';
            statusText.textContent = 'Ready to answer';
        }
    } catch {
        statusDot.style.color = '#F87171';
        statusText.textContent = 'Backend unreachable';
    }
}

// ── tiny markdown renderer ───────────────────────────────────────────────────
// Covers the subset the agent's system prompt actually asks it to use:
// headings, bold, bullet/numbered lists, inline code, paragraphs.

function renderMarkdown(text) {
    const escapeHtml = (s) =>
        s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

    const lines = escapeHtml(text).split('\n');
    let html = '';
    let inList = null; // "ul" | "ol" | null

    const closeList = () => {
        if (inList) {
            html += `</${inList}>`;
            inList = null;
        }
    };

    const inline = (s) =>
        s
            .replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    for (const raw of lines) {
        const line = raw.trimEnd();
        const heading = line.match(/^(#{1,6})\s+(.*)/);
        const bullet = line.match(/^[-*]\s+(.*)/);
        const numbered = line.match(/^\d+\.\s+(.*)/);

        if (heading) {
            closeList();
            const level = Math.min(heading[1].length + 2, 6); // keep headings modest in a chat bubble
            html += `<h${level}>${inline(heading[2])}</h${level}>`;
        } else if (bullet) {
            if (inList !== 'ul') { closeList(); html += '<ul>'; inList = 'ul'; }
            html += `<li>${inline(bullet[1])}</li>`;
        } else if (numbered) {
            if (inList !== 'ol') { closeList(); html += '<ol>'; inList = 'ol'; }
            html += `<li>${inline(numbered[1])}</li>`;
        } else if (line === '') {
            closeList();
        } else {
            closeList();
            html += `<p>${inline(line)}</p>`;
        }
    }
    closeList();
    return html;
}

// ── message rendering ─────────────────────────────────────────────────────────

function appendMessage(text, sender, iconHTML) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.id = `msg-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;

    const avatarDiv = document.createElement('div');
    avatarDiv.classList.add('avatar');
    avatarDiv.innerHTML = iconHTML;

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('msg-content');
    if (sender === 'user') {
        contentDiv.textContent = text;
    } else {
        contentDiv.innerHTML = text;
    }

    messageDiv.appendChild(avatarDiv);
    messageDiv.appendChild(contentDiv);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    return { row: messageDiv, content: contentDiv };
}

function addToSidebar(question, targetId) {
    if (questionCount === 0) {
        chatList.innerHTML = '';
    }
    questionCount += 1;

    const item = document.createElement('div');
    item.classList.add('chat-item');
    item.innerHTML = `<i class="fa-regular fa-message"></i> <span>${question}</span>`;
    item.onclick = () => {
        document.querySelectorAll('.chat-item').forEach((el) => el.classList.remove('active'));
        item.classList.add('active');
        document.getElementById(targetId)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };
    chatList.prepend(item);
}

// ── send flow (real backend, streamed) ────────────────────────────────────────

async function sendMessage() {
    const text = userInput.value.trim();
    if (text === '') return;

    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;

    appendMessage(text, 'user', '<i class="fa-solid fa-user"></i>');
    const { row, content: bubble } = appendMessage('', 'bot', '<i class="fa-solid fa-robot"></i>');
    bubble.classList.add('pending');
    addToSidebar(text, row.id);

    let full = '';
    try {
        const res = await fetch('/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: text }),
        });

        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.error || `Request failed (${res.status})`);
        }

        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });

            // SSE frames are separated by a blank line.
            const frames = buffer.split('\n\n');
            buffer = frames.pop(); // last (possibly incomplete) frame stays buffered

            for (const frame of frames) {
                const line = frame.trim();
                if (!line.startsWith('data:')) continue;
                const payload = JSON.parse(line.slice(5).trim());

                if (payload.error) throw new Error(payload.error);
                if (payload.text) {
                    full += payload.text;
                    bubble.innerHTML = renderMarkdown(full);
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
                if (payload.done) {
                    bubble.classList.remove('pending');
                }
            }
        }

        if (!full) {
            bubble.textContent = '(no answer returned)';
        }
    } catch (err) {
        bubble.classList.remove('pending');
        bubble.classList.add('error');
        bubble.textContent = `Error: ${err.message}`;
    } finally {
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function useSuggestion(text) {
    userInput.value = text;
    sendMessage();
}

function startNewChat() {
    chatBox.innerHTML = WELCOME_HTML;
    chatList.innerHTML = '<div class="chat-list-empty">Questions you ask will show up here.</div>';
    questionCount = 0;
}

checkStatus();
