import type { Database } from "sqlite";

export const CREATE_ROOMS_TABLE = `
CREATE TABLE IF NOT EXISTS Rooms (
  ID INTEGER PRIMARY KEY AUTOINCREMENT
);`;

export const CREATE_GAMES_TABLE = `
CREATE TABLE IF NOT EXISTS Games (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  RoomID INTEGER,
  Data TEXT NOT NULL,
  FOREIGN KEY(RoomID) REFERENCES Rooms(ID)
);`;

export function setupSchema(db: Database) {
  db.run(CREATE_ROOMS_TABLE);
  db.run(CREATE_GAMES_TABLE);
}
