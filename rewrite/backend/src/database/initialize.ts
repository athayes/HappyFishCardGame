import { Database, verbose } from "sqlite3";
import { config } from "./config";
import { setupSchema } from "./schema"; 
import { z } from "zod";

let db: Database | null = null;

export function initializeDatabase(): Database {
    if (db !== null) {
        return db;
    }

    verbose();

    db = new Database(config.database.mode, (err) => {
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


/**
 * A simple function to test the db
 */
export function testLog({ db }: { db: Database }) {
    db.serialize(() => {
        db.each("SELECT name FROM sqlite_master WHERE type='table'", (err: any, row: any) => {
          if (err) {
            console.error(err.message);
          } else {
            console.log(row.name);
        }
        }) 
    });
}