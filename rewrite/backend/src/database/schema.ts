import type { Database } from "sqlite3";

export const CREATE_GAMES_TABLE = `
CREATE TABLE IF NOT EXISTS games (
  id INTEGER PRIMARY KEY,
  players TEXT,
  rounds TEXT,
  current_round INTEGER
)
`;

export function setupSchema(db: Database): void {
    db.run(CREATE_GAMES_TABLE, (err) => {
        if (err) {
            console.error(err.message);
        }
    });
}
