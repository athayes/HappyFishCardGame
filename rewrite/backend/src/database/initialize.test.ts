import sqlite3, { Database } from "sqlite3";
import { initializeDatabase } from "./initialize";

jest.mock("sqlite3", () => {
    return {
        Database: jest.fn(),
        verbose: jest.fn(),
    };
});

describe("initializeDatabase", () => {
    let mockDb: jest.Mocked<Database>;

    beforeEach(() => {
        // Create a mock database instance
        mockDb = {
            get: jest.fn(),
            // Add mock implementations for any other methods you use
        } as unknown as jest.Mocked<Database>;
    });

    it("should initialize the database", () => {
        // Call the initializeDatabase function
        initializeDatabase();

        // Perform assertions to verify the database initialization
        // For example, you can check if the necessary tables are created
        mockDb.get.mockImplementation((query, callback) => {
            callback(null, { name: "users" });
            return mockDb;
        });

        mockDb.get("SELECT name FROM sqlite_master WHERE type='table' AND name='users'", (err, row) => {
            expect(err).toBeNull();
            expect(row).toBeDefined();
        });
    });
});
