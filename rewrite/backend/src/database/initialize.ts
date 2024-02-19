import { open, Database } from "sqlite";
import { config } from "./config";
import { setupSchema } from "./schema";

let db: Database | null = null;

export async function initializeDatabase() {
    if (db !== null) {
        return db;
    }

    try {
        db = await open({
            filename: config.database.mode,
            driver: Database,
        });

        console.log("Connected to the SQLite database.");

        // Set up the database schema
        await setupSchema(db);

        return db;
    } catch (err) {
        console.error((err as Error).message);
        process.exit(1);
    }
}
