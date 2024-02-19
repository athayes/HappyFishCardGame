import { createApp } from "./express/app";

jest.mock("./express/app", () => ({
    createApp: jest.fn().mockResolvedValue({
        start: jest.fn(),
        app: {},
    }),
}));

describe("main", () => {
    it("should call createApp", async () => {
        await import("./main");
        expect(createApp).toHaveBeenCalled();
    });
});
