import type { Database } from "sqlite";
import { setupSchema, SETUP_SCHEMA } from "./schema";

describe("setupSchema", () => {
    it("should create the games table if it does not exist", async () => {
        const dbMock: Database = {
            run: jest.fn(),
        } as unknown as Database;

        await setupSchema(dbMock);
        expect(dbMock.run).toHaveBeenNthCalledWith(1, "PRAGMA foreign_keys = ON;");
        expect(dbMock.run).toHaveBeenNthCalledWith(2, SETUP_SCHEMA);
    });
});
