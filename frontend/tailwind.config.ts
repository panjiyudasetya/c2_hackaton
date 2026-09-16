import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        bg: "var(--color-bg)",
        surface: "var(--color-surface)",
        "surface-alt": "var(--color-surface-alt)",
        border: "var(--color-border)",
        text: "var(--color-text)",
        muted: "var(--color-muted)",
        subtle: "var(--color-subtle)",
        primary: "var(--color-primary)",
        "primary-dark": "var(--color-primary-dark)",
        navy: "var(--color-navy)",
        "accent-soft": "var(--color-accent-soft)",
        signal: "var(--color-signal)",
        "bubble-bot": "var(--color-bubble-bot)",
      },
      fontFamily: {
        sans: ["var(--font-poppins)", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
