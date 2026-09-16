"use client";

import { useEffect, useRef, useState } from "react";
import { api } from "@/lib/api";
import { useJob } from "@/lib/useJob";
import { useLocalStorage } from "@/lib/useLocalStorage";
import JobStatus from "./JobStatus";

function formatTimestamp(iso: string | null): string {
  if (!iso) return "Never";
  return new Date(iso).toLocaleString(undefined, {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

/** A pipeline step's own last-run stamp + job polling, shared by the single
 * Build button and each of the Advanced (enrich/index/graph) buttons. */
function useStampedJob(storageKey: string, onDone: () => void) {
  const [lastRun, setLastRun] = useLocalStorage<string | null>(storageKey, null);
  const [jobId, setJobId] = useState<string | null>(null);
  const job = useJob(jobId);
  const firedRef = useRef<string | null>(null);

  useEffect(() => {
    if (job?.status === "done" && jobId && firedRef.current !== jobId) {
      firedRef.current = jobId;
      setLastRun(new Date().toISOString());
      onDone();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [job?.status, jobId]);

  return { lastRun, job, setJobId };
}

export default function PipelineSection({ onJobDone }: { onJobDone: () => void }) {
  const [advanced, setAdvanced] = useState(false);

  const build = useStampedJob("decision-intel:lastRun:build", onJobDone);
  const enrich = useStampedJob("decision-intel:lastRun:enrich", onJobDone);
  const index = useStampedJob("decision-intel:lastRun:index", onJobDone);
  const graph = useStampedJob("decision-intel:lastRun:graph", onJobDone);

  const anyRunning = [build, enrich, index, graph].some((s) => s.job?.status === "running");

  return (
    <div className="px-4 py-3">
      <h3 className="mb-1 text-xs font-semibold uppercase tracking-wide text-subtle">Pipeline</h3>

      <button
        onClick={async () => build.setJobId((await api.pipelineBuild()).job_id)}
        disabled={anyRunning}
        className="w-full rounded-md bg-primary px-3 py-2 text-sm font-medium text-white transition hover:bg-primary-dark disabled:opacity-50"
      >
        Build
      </button>
      <div className="mt-1 flex items-center justify-between">
        <span className="text-xs text-muted">Last run: {formatTimestamp(build.lastRun)}</span>
        <JobStatus job={build.job} />
      </div>

      <button
        onClick={() => setAdvanced((v) => !v)}
        className="mt-2 text-xs text-primary underline underline-offset-2"
      >
        {advanced ? "Hide advanced" : "Advanced"}
      </button>

      {advanced && (
        <div className="mt-2 space-y-2 border-t border-border pt-2">
          {(
            [
              { label: "Enrich", state: enrich, run: api.pipelineEnrich },
              { label: "Index", state: index, run: api.pipelineIndex },
              { label: "Graph", state: graph, run: () => api.pipelineGraph() },
            ] as const
          ).map(({ label, state, run }) => (
            <div key={label}>
              <button
                onClick={async () => state.setJobId((await run()).job_id)}
                disabled={anyRunning}
                className="w-full rounded-md border border-border bg-surface px-3 py-1.5 text-sm text-text transition hover:border-primary disabled:opacity-50"
              >
                {label}
              </button>
              <div className="mt-1 flex items-center justify-between">
                <span className="text-xs text-muted">Last run: {formatTimestamp(state.lastRun)}</span>
                <JobStatus job={state.job} />
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
