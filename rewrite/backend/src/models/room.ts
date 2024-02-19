import { open, Database } from 'sqlite';

export async function getRoom({db, roomId}: {db: Database, roomId: number}) {
    try {
        const row = await db.get('SELECT * FROM room WHERE ID = ?', roomId);
        return row;
    } catch (err) {
        throw err;
    }
}

// Add more functions as needed for other room operations...