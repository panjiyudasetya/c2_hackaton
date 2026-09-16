"use client";

import { useEffect, useState } from "react";
import { api, SourcesStatus } from "@/lib/api";
import PipelineSection from "./PipelineSection";
import SourcesSection from "./SourcesSection";

export default function ContextPanel({
  collapsed,
  onKnowledgeChange,
}: {
  collapsed: boolean;
  onKnowledgeChange: () => void;
}) {
  const [status, setStatus] = useState<SourcesStatus | null>(null);

  const refresh = () => {
    api
      .sourcesStatus()
      .then(setStatus)
      .catch(() => setStatus(null));
    onKnowledgeChange();
  };

  useEffect(() => {
    refresh();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <aside
      className={`flex h-full flex-shrink-0 flex-col bg-surface-alt transition-all duration-300 ${
        collapsed ? "w-0 overflow-hidden border-r-0" : "w-[300px] overflow-y-auto border-r border-border"
      }`}
    >
      <SourcesSection status={status} onJobDone={refresh} />
      <PipelineSection onJobDone={refresh} />
    </aside>
  );
}
