"use client";

import { useEffect, useState } from "react";

/**
 * localStorage-backed state with an SSR guard: reads/writes only happen in
 * the browser (Next.js renders this hook's initial pass on the server too,
 * where `window` doesn't exist), so the value starts at `initial` and is
 * hydrated from storage on mount.
 */
export function useLocalStorage<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(initial);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(key);
      if (raw !== null) setValue(JSON.parse(raw) as T);
    } catch {
      // Malformed JSON or storage blocked (private mode) -- fall back to `initial`.
    }
    setHydrated(true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  useEffect(() => {
    if (!hydrated) return;
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // Storage blocked or quota exceeded -- the value just won't persist.
    }
  }, [key, value, hydrated]);

  return [value, setValue] as const;
}
