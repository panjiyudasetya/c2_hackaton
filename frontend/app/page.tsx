"use client";

import { useEffect, useState } from "react";
import ChatWindow from "@/components/ChatWindow";
import ContextPanel from "@/components/ContextPanel";
import { API_URL } from "@/lib/api";

export default function Home() {
  const [collapsed, setCollapsed] = useState(false);
  const [knowledgeAvailable, setKnowledgeAvailable] = useState<boolean | null>(null);

  // Simpler heuristic (per spec): a dummy POST /ask with an empty question
  // returns 503 if the index itself is missing, or a 4xx (400, question
  // required) if the index exists and validation was merely reached.
  const checkKnowledge = async () => {
    try {
      const res = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: "" }),
      });
      setKnowledgeAvailable(res.status !== 503);
    } catch {
      setKnowledgeAvailable(false);
    }
  };

  useEffect(() => {
    void checkKnowledge();
  }, []);

  return (
    <div className="flex h-screen flex-col overflow-hidden">
      <header className="flex flex-shrink-0 items-center bg-navy px-6 py-3">
        <h1 className="text-lg font-semibold text-white">
          MAP.<span className="text-sky-400">ANSWER</span>
        </h1>
      </header>

      <div className="flex flex-1 overflow-hidden">
        <ContextPanel collapsed={collapsed} onKnowledgeChange={checkKnowledge} />
        <ChatWindow
          knowledgeAvailable={knowledgeAvailable}
          onExpandPanel={() => setCollapsed(false)}
          collapsed={collapsed}
          onToggle={() => setCollapsed((c) => !c)}
        />
      </div>
    </div>
  );
}
