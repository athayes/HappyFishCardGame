import express, { Application } from "express";
import { initializeDatabase } from "../database/initialize";
import { setupRoutes } from "./routes";

export async function createApp(): Promise<Application> {
    // Initialize database first
    const db = await initializeDatabase();

    // Initialize express app
    const app = express();

    app.use(express.json());

    // Setup routes
    setupRoutes({ app, db });

    // Determine port
    const port = process.env.PORT || 3000;

    // Start server
    app.listen(port, () => {
        console.log(`Server running at http://localhost:${port}`);
    });

    // return app for ease of testing
    return app;
}
