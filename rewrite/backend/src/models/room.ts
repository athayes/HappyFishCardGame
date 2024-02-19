import { open, Database } from "sqlite";
import { Room } from "../types";

export async function getRoom({ db, roomId }: { db: Database; roomId: number }): Promise<Room> {
    try {
        const row = await db.get("SELECT * FROM room WHERE ID = ?", roomId);
        return row;
    } catch (err) {
        throw err;
    }
}

export async function createRoom({ db }: { db: Database }): Promise<string> {
    try {
        const id = Math.floor(Math.random() * Math.pow(16, 4))
            .toString(16)
            .padStart(4, "0");
        const info = await db.run("INSERT INTO game (id, room) VALUES (?, ?)", id, JSON.stringify({}));
        return id;
    } catch (err) {
        throw err;
    }
}

/**
 * Generates a unique 4-character hexadecimal ID.
 *
 * This function generates a random 4-character hexadecimal string and checks
 * if it already exists in the database. If the ID already exists, a new one
 * is generated. This continues until a unique ID is found.
 */
async function generateUniqueId(db: Database): Promise<string> {
    let id;
    let existingId;

    do {
        id = Math.floor(Math.random() * Math.pow(16, 4))
            .toString(16)
            .padStart(4, "0");
        existingId = await db.get("SELECT id FROM game WHERE id = ?", id);
    } while (existingId);

    return id;
}
