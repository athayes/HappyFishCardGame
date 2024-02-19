import type { Database } from "sqlite";

export const CREATE_ROOMS_TABLE = `
CREATE TABLE IF NOT EXISTS room (
  id INTEGER PRIMARY KEY
);`;

export const CREATE_GAMES_TABLE = `
CREATE TABLE IF NOT EXISTS game (
  id INTEGER PRIMARY KEY,
  roomId INTEGER,
  data TEXT NOT NULL,
  FOREIGN KEY(roomId) REFERENCES room(id)
);`;

export const SETUP_SCHEMA = 
`
${CREATE_ROOMS_TABLE}
${CREATE_GAMES_TABLE}
`;

export async function setupSchema(db: Database) {
    await db.run("PRAGMA foreign_keys = ON;");
    await db.run(SETUP_SCHEMA);
}
