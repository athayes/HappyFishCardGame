import express, { Request, Response, NextFunction, Application } from "express";
import { initializeDatabase } from "../database/initialize";
import { setupRoutes } from "./routes";

export async function createApp(): Promise<{ app: Application; start: () => void }> {
    // Initialize database first
    const db = await initializeDatabase();

    // Initialize express app
    const app = express();

    app.use(express.json());

    // Setup routes
    setupRoutes({ app, db });

    // Error-handling middleware
    app.use((err: any, req: Request, res: Response, next: NextFunction) => {
        console.error(err.stack);
        res.status(500).send("Something broke!");
    });

    // Determine port
    const port = process.env.PORT || 3000;

    // return app and start function for ease of testing
    return {
        app,
        start: () => {
            // Start server
            app.listen(port, () => {
                console.log(`Server running at http://localhost:${port}`);
            });
        },
    };
}
