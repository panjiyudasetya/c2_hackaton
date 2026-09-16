"use client";

import type { ComponentPropsWithoutRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  text: string;
  streaming?: boolean;
  savedTo?: string | null;
  error?: boolean;
}

// Assistant answers are markdown (the agent's system prompt asks for
// headings/bullets/bold) -- rendered properly here, the same way a chat
// bubble in Claude/ChatGPT/Gemini would, instead of showing raw "**text**"
// and "## Heading" characters.
const MARKDOWN_COMPONENTS = {
  h1: (props: ComponentPropsWithoutRef<"h1">) => <h3 className="mb-1 mt-2 text-base font-semibold" {...props} />,
  h2: (props: ComponentPropsWithoutRef<"h2">) => <h3 className="mb-1 mt-2 text-base font-semibold" {...props} />,
  h3: (props: ComponentPropsWithoutRef<"h3">) => <h3 className="mb-1 mt-2 text-sm font-semibold" {...props} />,
  p: (props: ComponentPropsWithoutRef<"p">) => <p className="mb-2 last:mb-0" {...props} />,
  ul: (props: ComponentPropsWithoutRef<"ul">) => <ul className="mb-2 list-disc space-y-0.5 pl-5 last:mb-0" {...props} />,
  ol: (props: ComponentPropsWithoutRef<"ol">) => <ol className="mb-2 list-decimal space-y-0.5 pl-5 last:mb-0" {...props} />,
  li: (props: ComponentPropsWithoutRef<"li">) => <li {...props} />,
  strong: (props: ComponentPropsWithoutRef<"strong">) => <strong className="font-semibold" {...props} />,
  a: (props: ComponentPropsWithoutRef<"a">) => (
    <a className="text-primary underline underline-offset-2 hover:text-primary-dark" target="_blank" rel="noreferrer" {...props} />
  ),
  code: ({ className, ...props }: ComponentPropsWithoutRef<"code">) =>
    className ? (
      // Fenced code block (has a language className from remark) -- keep as a <pre>-wrapped block.
      <code className={`${className} block overflow-x-auto rounded-md bg-black/30 p-2 text-xs`} {...props} />
    ) : (
      // Inline code.
      <code className="rounded bg-black/25 px-1 py-0.5 text-[0.9em]" {...props} />
    ),
  table: (props: ComponentPropsWithoutRef<"table">) => (
    <div className="mb-2 overflow-x-auto">
      <table className="border-collapse text-xs" {...props} />
    </div>
  ),
  th: (props: ComponentPropsWithoutRef<"th">) => <th className="border border-border px-2 py-1 text-left" {...props} />,
  td: (props: ComponentPropsWithoutRef<"td">) => <td className="border border-border px-2 py-1" {...props} />,
  blockquote: (props: ComponentPropsWithoutRef<"blockquote">) => (
    <blockquote className="mb-2 border-l-2 border-border pl-3 italic text-muted last:mb-0" {...props} />
  ),
};

export default function MessageBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div className="max-w-[75%]">
        <div
          className={
            isUser
              ? "rounded-[16px_16px_4px_16px] bg-primary px-4 py-2.5 text-sm text-white"
              : `rounded-[16px_16px_16px_4px] border px-4 py-2.5 text-sm ${
                  message.error
                    ? "border-red-800 bg-red-950/40 text-red-300"
                    : "border-border bg-bubble-bot text-text"
                }`
          }
        >
          {isUser || message.error ? (
            <span className="whitespace-pre-wrap">{message.text}</span>
          ) : (
            <ReactMarkdown remarkPlugins={[remarkGfm]} components={MARKDOWN_COMPONENTS}>
              {message.text}
            </ReactMarkdown>
          )}
          {message.streaming && <span className="stream-cursor" />}
        </div>
        {message.savedTo && <p className="mt-1 text-xs text-muted">Saved to {message.savedTo}</p>}
      </div>
    </div>
  );
}
