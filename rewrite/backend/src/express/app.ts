import express, { Application } from "express";

import { createRoomRouter } from './routes/room';
import { createHelloRouter } from './routes/hello';
import { Database } from "sqlite";
import { initializeDatabase } from "../database/initialize";

export async function createApp(): Promise<Application> {
    // Initialize database first
    const db = await initializeDatabase();
    
    // Initialize express app
    const app = express();

    // Setup routes
    app.use(express.json());
    app.use('/hello', createHelloRouter());
    app.use('/rooms', createRoomRouter({ db }));
    
    // Determine port
    const port = process.env.PORT || 3000;

    // Start server
    app.listen(port, () => {
        console.log(`Server running at http://localhost:${port}`);
    });

    // return app for ease of testing
    return app;
}
