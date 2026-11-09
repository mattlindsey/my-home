import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    // Listen on all interfaces so other machines on the LAN can connect.
    host: true,
    // Accept requests addressed to the Pi's hostname (Vite blocks unknown hosts).
    allowedHosts: ["matt-pi-4", "matt-pi-4.local"],
    // Forward /api calls to the FastAPI backend.
    proxy: { "/api": "http://127.0.0.1:8000" },
  },
});
