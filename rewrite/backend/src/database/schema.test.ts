import type { Database } from "sqlite3";
import { CREATE_GAMES_TABLE, setupSchema } from "./schema";

describe("setupSchema", () => {
    it("should create the games table if it does not exist", () => {
        // Mock the database object
        const dbMock: Database = {
            run: jest.fn(),
        } as unknown as Database;

        // Call the setupSchema function
        setupSchema(dbMock);

        // Verify that the createGamesTableQuery was executed
        expect(dbMock.run).toHaveBeenCalledWith(CREATE_GAMES_TABLE), expect.any(Function);
    });
});
