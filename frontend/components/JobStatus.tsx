"use client";

import { Job } from "@/lib/api";

export default function JobStatus({ job }: { job: Job | null }) {
  if (!job) return null;

  if (job.status === "running") {
    return (
      <span className="inline-flex items-center gap-1.5 text-xs text-muted">
        <span className="h-3 w-3 animate-spin rounded-full border-2 border-border border-t-primary" />
        Running…
      </span>
    );
  }

  if (job.status === "done") {
    return <span className="text-xs text-primary-dark">Done</span>;
  }

  return <span className="text-xs text-red-600">Failed: {job.error}</span>;
}
