import { open } from "sqlite";
import { Database } from "sqlite3";
import { Database as DatabaseType } from "sqlite";
import { setupSchema } from "./schema";

let db: DatabaseType | null = null;

export async function initializeDatabase() {
    if (db !== null) {
        return db;
    }

    try {
        db = await open({
            filename: ":memory:",
            driver: Database,
        });

        console.log("Connected to the SQLite database.");
        await setupSchema(db);
        console.log("Database schema has been set up.");

        return db;
    } catch (err) {
        console.error((err as Error).message);
        process.exit(1);
    }
}
