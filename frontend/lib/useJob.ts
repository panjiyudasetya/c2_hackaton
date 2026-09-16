"use client";

import { useEffect, useRef, useState } from "react";
import { api, Job } from "./api";

/**
 * Polls GET /jobs/{jobId} every 2s until the job leaves the "running" state.
 * Pass `null` to disable polling (e.g. before a job has been started).
 */
export function useJob(jobId: string | null) {
  const [job, setJob] = useState<Job | null>(null);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    if (!jobId) {
      setJob(null);
      return;
    }

    let cancelled = false;

    const poll = async () => {
      try {
        const j = await api.getJob(jobId);
        if (cancelled) return;
        setJob(j);
        if (j.status !== "running" && timerRef.current) {
          clearInterval(timerRef.current);
          timerRef.current = null;
        }
      } catch {
        // Transient network errors while polling are ignored; the next tick retries.
      }
    };

    poll();
    timerRef.current = setInterval(poll, 2000);

    return () => {
      cancelled = true;
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [jobId]);

  return job;
}
