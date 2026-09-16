"use client";

import { useEffect, useRef, useState } from "react";
import { FaConfluence, FaGithub, FaJira } from "react-icons/fa";
import type { IconType } from "react-icons";
import { SiNotion } from "react-icons/si";
import { api, SourcesStatus } from "@/lib/api";
import { useJob } from "@/lib/useJob";
import { useLocalStorage } from "@/lib/useLocalStorage";
import JobStatus from "./JobStatus";
import MultiSelectDropdown, { DropdownOption } from "./MultiSelectDropdown";

type SourceKey = "github" | "jira" | "confluence" | "notion";

const LABELS: Record<SourceKey, string> = {
  github: "GitHub",
  jira: "JIRA",
  confluence: "Confluence",
  notion: "Notion",
};

const ICONS: Record<SourceKey, IconType> = {
  github: FaGithub,
  jira: FaJira,
  confluence: FaConfluence,
  notion: SiNotion,
};

// GitHub and JIRA are picked from a live list fetched from the backend;
// Confluence and Notion (no "list all spaces/databases" endpoint yet) still
// take a typed, comma-separated list.
const PICKABLE: SourceKey[] = ["github", "jira"];

const TEXT_PLACEHOLDERS: Record<"confluence" | "notion", string> = {
  confluence: "Space keys, e.g. TC, PTO",
  notion: "Database IDs, comma-separated",
};

const ORDER: SourceKey[] = ["github", "jira", "confluence", "notion"];

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

/** GitHub/JIRA: fetch the real repo/board list once (when configured) and
 * let the user check which ones to sync, instead of typing names by hand. */
function usePickerOptions(source: "github" | "jira", configured: boolean) {
  const [options, setOptions] = useState<DropdownOption[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!configured) return;
    setLoading(true);
    setError(null);
    const load =
      source === "github"
        ? api.listGithubRepos().then((repos) =>
            repos.map((r) => ({ value: r.full_name, label: r.full_name, sublabel: r.description || r.pushed_at }))
          )
        : api.listJiraBoards().then((boards) =>
            boards.map((b) => ({ value: b.name, label: b.name, sublabel: b.type }))
          );
    load
      .then(setOptions)
      .catch((e: Error) => setError(e.message))
      .finally(() => setLoading(false));
  }, [source, configured]);

  return { options, loading, error };
}

function SourceRow({ source, configured, onDone }: { source: SourceKey; configured: boolean; onDone: () => void }) {
  const [lastSync, setLastSync] = useLocalStorage<string | null>(`decision-intel:lastRun:${source}`, null);
  const [selected, setSelected] = useState<string[]>([]);
  const [text, setText] = useState("");
  const [jobId, setJobId] = useState<string | null>(null);
  const job = useJob(jobId);
  const firedRef = useRef<string | null>(null);
  const Icon = ICONS[source];
  const isPickable = PICKABLE.includes(source);
  const picker = usePickerOptions(source as "github" | "jira", configured && isPickable);

  useEffect(() => {
    if (job?.status === "done" && jobId && firedRef.current !== jobId) {
      firedRef.current = jobId;
      setLastSync(new Date().toISOString());
      onDone();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [job?.status, jobId]);

  const chosen = isPickable
    ? selected
    : text
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);

  const sync = async () => {
    let res: { job_id: string };
    if (source === "github") res = await api.collectGithub({ repos: chosen });
    else if (source === "jira") res = await api.collectJira({ boards: chosen, max_results: 50 });
    else if (source === "confluence") res = await api.collectConfluence({ space_keys: chosen, max_pages: 100 });
    else res = await api.collectNotion({ database_ids: chosen, max_pages: 50 });
    setJobId(res.job_id);
  };

  const running = job?.status === "running";

  return (
    <div className="border-b border-border/60 py-3 last:border-b-0">
      <div className="mb-1.5 flex items-center gap-2">
        <Icon className="h-4 w-4 flex-shrink-0 text-muted" />
        <span className="text-sm font-medium text-text">{LABELS[source]}</span>
        <span
          className="ml-auto h-2 w-2 flex-shrink-0 rounded-full"
          style={{ background: configured ? "var(--color-primary)" : "var(--color-border)" }}
          title={configured ? "Configured" : "Not configured"}
        />
      </div>

      {!configured ? (
        <p className="pl-6 text-xs text-muted">Not configured</p>
      ) : (
        <div className="pl-6">
          {isPickable ? (
            <div className="mb-1.5">
              <MultiSelectDropdown
                options={picker.options}
                selected={selected}
                onChange={setSelected}
                placeholder={source === "github" ? "Pick repos to sync…" : "Pick boards to sync…"}
                loading={picker.loading}
                error={picker.error}
              />
            </div>
          ) : (
            <input
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder={TEXT_PLACEHOLDERS[source as "confluence" | "notion"]}
              className="mb-1.5 w-full rounded-md border border-border bg-surface px-2 py-1 text-xs text-text outline-none focus:border-primary"
            />
          )}
          <button
            onClick={sync}
            disabled={running || chosen.length === 0}
            className="w-full rounded-md bg-primary px-3 py-1.5 text-sm font-medium text-white transition hover:bg-primary-dark disabled:opacity-50"
          >
            Sync
          </button>
          <div className="mt-1 flex items-center justify-between">
            <span className="text-xs text-muted">Last sync: {formatTimestamp(lastSync)}</span>
            <JobStatus job={job} />
          </div>
        </div>
      )}
    </div>
  );
}

export default function SourcesSection({
  status,
  onJobDone,
}: {
  status: SourcesStatus | null;
  onJobDone: () => void;
}) {
  return (
    <div className="border-b border-border px-4 py-3">
      <h3 className="mb-1 text-xs font-semibold uppercase tracking-wide text-subtle">Sources</h3>
      {!status ? (
        <p className="py-2 text-xs text-muted">Checking…</p>
      ) : (
        ORDER.map((key) => (
          <SourceRow key={key} source={key} configured={!!status[key]?.configured} onDone={onJobDone} />
        ))
      )}
    </div>
  );
}
