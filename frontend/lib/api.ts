// Typed fetch wrappers for the decision-intel REST API. Kept dependency-free
// (no axios/swr/react-query) per the hackathon scope -- see useJob.ts for the
// polling pattern layered on top of these.

export const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type JobStatusValue = "running" | "done" | "failed";

export interface Job {
  job_id: string;
  status: JobStatusValue;
  result?: unknown;
  error?: string | null;
}

export interface SourceStatus {
  configured: boolean;
}

export interface SourcesStatus {
  github: SourceStatus;
  jira: SourceStatus;
  confluence: SourceStatus;
  notion: SourceStatus;
}

export interface SearchResult {
  doc_id: string;
  score: number;
  text: string;
  source: string;
  [key: string]: unknown;
}

export interface LinkedDocument {
  doc_id: string;
  confidence: number;
  [key: string]: unknown;
}

export interface GithubRepo {
  full_name: string;
  pushed_at: string;
  description: string;
}

export interface JiraBoard {
  id: number;
  name: string;
  type: string;
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}) as { error?: string });
    throw new Error(body.error || `Request failed (${res.status})`);
  }
  return res.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>("/health"),
  sourcesStatus: () => request<SourcesStatus>("/sources/status"),
  listGithubRepos: () => request<GithubRepo[]>("/sources/github/repos"),
  listJiraBoards: () => request<JiraBoard[]>("/sources/jira/boards"),

  collectGithub: (body: {
    repos?: string[];
    all_repos?: boolean;
    state?: string;
    max_issues?: number;
    max_prs?: number;
    max_commits?: number;
    since?: string;
  }) => request<{ job_id: string }>("/collect/github", { method: "POST", body: JSON.stringify(body) }),

  collectJira: (body: { jql?: string; boards?: string[]; max_results?: number }) =>
    request<{ job_id: string }>("/collect/jira", { method: "POST", body: JSON.stringify(body) }),

  collectConfluence: (body: { space_keys: string[]; max_pages?: number }) =>
    request<{ job_id: string }>("/collect/confluence", { method: "POST", body: JSON.stringify(body) }),

  collectNotion: (body: { database_ids?: string[]; page_ids?: string[]; max_pages?: number }) =>
    request<{ job_id: string }>("/collect/notion", { method: "POST", body: JSON.stringify(body) }),

  pipelineEnrich: () => request<{ job_id: string }>("/pipeline/enrich", { method: "POST" }),
  pipelineIndex: () => request<{ job_id: string }>("/pipeline/index", { method: "POST" }),
  pipelineGraph: (noHeuristics?: boolean) =>
    request<{ job_id: string }>("/pipeline/graph", {
      method: "POST",
      body: JSON.stringify({ no_heuristics: noHeuristics }),
    }),
  pipelineBuild: () => request<{ job_id: string }>("/pipeline/build", { method: "POST" }),

  getJob: (jobId: string) => request<Job>(`/jobs/${jobId}`),
  listJobs: () => request<Job[]>("/jobs"),

  search: (q: string, opts?: { topK?: number; source?: string; since?: string }) => {
    const params = new URLSearchParams({ q });
    if (opts?.topK) params.set("top_k", String(opts.topK));
    if (opts?.source) params.set("source", opts.source);
    if (opts?.since) params.set("since", opts.since);
    return request<SearchResult[]>(`/search?${params.toString()}`);
  },

  links: (docId: string, opts?: { minConfidence?: number; depth?: number }) => {
    const params = new URLSearchParams();
    if (opts?.minConfidence) params.set("min_confidence", String(opts.minConfidence));
    if (opts?.depth) params.set("depth", String(opts.depth));
    return request<LinkedDocument[]>(`/links/${encodeURIComponent(docId)}?${params.toString()}`);
  },

  doc: (path: string) => request<{ path: string; content: string }>(`/docs?path=${encodeURIComponent(path)}`),
};
