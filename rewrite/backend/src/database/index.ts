import sqlite3, { Database } from "sqlite3";
import { config } from "./config";
import { setupSchema } from "./schema";

let db: Database | null = null;

export function initializeDatabase(): Database {
    sqlite3.verbose();

    db = new sqlite3.Database(config.database.mode, (err) => {
        if (err) {
            console.error(err.message);
            process.exit(1);
        }
        console.log("Connected to the SQLite database.");

        if (db === null) {
            throw new Error("Failed to initialize the database.");
        }

        // Set up the database schema
        setupSchema(db);
    });

    return db;
}
