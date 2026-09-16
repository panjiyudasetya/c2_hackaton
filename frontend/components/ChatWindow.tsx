"use client";

import { useEffect, useRef, useState } from "react";
import { FaBars } from "react-icons/fa";
import { API_URL } from "@/lib/api";
import MessageBubble, { ChatMessage } from "./MessageBubble";

interface AskEvent {
  token?: string;
  answer?: string;
  saved_to?: string | null;
  error?: string;
}

export default function ChatWindow({
  knowledgeAvailable,
  onExpandPanel,
  collapsed,
  onToggle,
}: {
  knowledgeAvailable: boolean | null; // null = still checking
  onExpandPanel: () => void;
  collapsed: boolean;
  onToggle: () => void;
}) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [streaming, setStreaming] = useState(false);
  const logRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    logRef.current?.scrollTo({ top: logRef.current.scrollHeight });
  }, [messages]);

  const send = async () => {
    const question = input.trim();
    if (!question || streaming) return;

    setInput("");
    const userMsg: ChatMessage = { id: crypto.randomUUID(), role: "user", text: question };
    const aiId = crypto.randomUUID();
    const aiMsg: ChatMessage = { id: aiId, role: "assistant", text: "", streaming: true };
    setMessages((m) => [...m, userMsg, aiMsg]);
    setStreaming(true);

    const update = (patch: Partial<ChatMessage>) =>
      setMessages((m) => m.map((msg) => (msg.id === aiId ? { ...msg, ...patch } : msg)));

    try {
      const res = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, save: true }),
      });

      if (!res.ok || !res.body) {
        const body = (await res.json().catch(() => ({}))) as { error?: string };
        throw new Error(body.error || `Request failed (${res.status})`);
      }

      // SSE-over-fetch: frames are "data: {...}\n\n", parsed by hand since
      // App Router SSE has to be consumed client-side (EventSource only
      // supports GET, and we're POSTing the question), not proxied through
      // a Route Handler.
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      let full = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        const frames = buffer.split("\n\n");
        buffer = frames.pop() ?? "";

        for (const frame of frames) {
          const line = frame.trim();
          if (!line.startsWith("data:")) continue;
          const payload = JSON.parse(line.slice(5).trim()) as AskEvent;

          if (payload.error) throw new Error(payload.error);
          if (typeof payload.token === "string") {
            full += payload.token;
            update({ text: full });
          }
          if (typeof payload.answer === "string") {
            full = payload.answer;
            update({ text: full, streaming: false, savedTo: payload.saved_to ?? null });
          }
        }
      }
      update({ streaming: false });
    } catch (err) {
      update({ text: `Error: ${(err as Error).message}`, streaming: false, error: true });
    } finally {
      setStreaming(false);
    }
  };

  const disabled = streaming || knowledgeAvailable === false;

  return (
    <div className="flex h-full flex-1 flex-col bg-bg">
      <header className="border-b border-border bg-surface px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              onClick={onToggle}
              className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-md text-subtle hover:bg-border/40 hover:text-text"
              aria-label={collapsed ? "Expand panel" : "Collapse panel"}
            >
              <FaBars
                className={`h-4 w-4 transition-transform duration-500 ${collapsed ? "rotate-[360deg]" : "rotate-0"}`}
              />
            </button>
            <h2 className="text-base font-semibold text-text">Ask a question</h2>
          </div>
          <span
            className="rounded-full px-2.5 py-1 text-xs font-medium"
            style={{
              background: knowledgeAvailable ? "var(--color-signal)" : "var(--color-border)",
              color: knowledgeAvailable ? "#0d3b2d" : "var(--color-muted)",
            }}
          >
            {knowledgeAvailable === null ? "Checking…" : knowledgeAvailable ? "Ready" : "Not indexed"}
          </span>
        </div>
      </header>

      <div ref={logRef} className="flex-1 space-y-4 overflow-y-auto px-6 py-6">
        {messages.length === 0 && (
          <p className="text-sm text-muted">
            Ask why a technical decision was made — evidence is pulled from the collected GitHub, JIRA,
            Confluence, and Notion data.
          </p>
        )}
        {messages.map((m) => (
          <MessageBubble key={m.id} message={m} />
        ))}
      </div>

      <div className="border-t border-border bg-surface px-6 py-4">
        {knowledgeAvailable === false && (
          <div className="mb-2 rounded-md bg-accent-soft px-3 py-2 text-xs text-subtle">
            Index not built yet —{" "}
            <button onClick={onExpandPanel} className="font-medium text-primary underline underline-offset-2">
              run the pipeline first
            </button>
            .
          </div>
        )}
        <div className="flex items-end gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                void send();
              }
            }}
            placeholder="Ask about a decision…"
            rows={1}
            disabled={disabled}
            className="max-h-24 flex-1 resize-none rounded-lg border border-border bg-surface px-3 py-2.5 text-sm text-text outline-none focus:border-primary disabled:opacity-60"
          />
          <button
            onClick={() => void send()}
            disabled={disabled || !input.trim()}
            className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-lg bg-primary text-white transition hover:bg-primary-dark disabled:opacity-50"
            aria-label="Send"
          >
            →
          </button>
        </div>
      </div>
    </div>
  );
}
