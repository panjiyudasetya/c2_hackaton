"use client";

import { useEffect, useRef, useState } from "react";

export interface DropdownOption {
  value: string;
  label: string;
  sublabel?: string;
}

/** A checkbox-list dropdown for picking zero or more options -- used for
 * "which repos" / "which boards" instead of typing names by hand. Options
 * are supplied already-fetched; this component only handles the open/closed
 * picker UI and the selection itself. */
export default function MultiSelectDropdown({
  options,
  selected,
  onChange,
  placeholder,
  loading,
  error,
}: {
  options: DropdownOption[];
  selected: string[];
  onChange: (values: string[]) => void;
  placeholder: string;
  loading?: boolean;
  error?: string | null;
}) {
  const [open, setOpen] = useState(false);
  const [filter, setFilter] = useState("");
  const rootRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const onClickOutside = (e: MouseEvent) => {
      if (rootRef.current && !rootRef.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener("mousedown", onClickOutside);
    return () => document.removeEventListener("mousedown", onClickOutside);
  }, [open]);

  const toggle = (value: string) => {
    onChange(selected.includes(value) ? selected.filter((v) => v !== value) : [...selected, value]);
  };

  const filtered = options.filter(
    (o) =>
      o.label.toLowerCase().includes(filter.toLowerCase()) ||
      o.sublabel?.toLowerCase().includes(filter.toLowerCase())
  );

  const summary =
    selected.length === 0
      ? placeholder
      : selected.length === 1
        ? options.find((o) => o.value === selected[0])?.label || selected[0]
        : `${selected.length} selected`;

  return (
    <div ref={rootRef} className="relative">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className={`flex w-full items-center justify-between rounded-md border border-border bg-surface px-2 py-1 text-left text-xs outline-none focus:border-primary ${
          selected.length === 0 ? "text-muted" : "text-text"
        }`}
      >
        <span className="truncate">{summary}</span>
        <span className="ml-1 flex-shrink-0 text-muted">{open ? "▲" : "▼"}</span>
      </button>

      {open && (
        <div className="absolute z-20 mt-1 w-full rounded-md border border-border bg-surface shadow-lg">
          <input
            autoFocus
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
            placeholder="Filter…"
            className="w-full border-b border-border bg-transparent px-2 py-1.5 text-xs text-text outline-none"
          />
          <div className="max-h-40 overflow-y-auto py-1">
            {loading && <p className="px-2 py-1.5 text-xs text-muted">Loading…</p>}
            {error && <p className="px-2 py-1.5 text-xs text-red-400">{error}</p>}
            {!loading && !error && filtered.length === 0 && (
              <p className="px-2 py-1.5 text-xs text-muted">No matches.</p>
            )}
            {!loading &&
              !error &&
              filtered.map((o) => (
                <label
                  key={o.value}
                  className="flex cursor-pointer items-start gap-2 px-2 py-1.5 text-xs text-text hover:bg-border/40"
                >
                  <input
                    type="checkbox"
                    checked={selected.includes(o.value)}
                    onChange={() => toggle(o.value)}
                    className="mt-0.5 flex-shrink-0"
                  />
                  <span className="min-w-0">
                    <span className="block truncate">{o.label}</span>
                    {o.sublabel && <span className="block truncate text-muted">{o.sublabel}</span>}
                  </span>
                </label>
              ))}
          </div>
        </div>
      )}
    </div>
  );
}
