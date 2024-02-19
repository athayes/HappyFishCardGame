jest.mock("./express/app", () => {
    return {
        app: {
            listen: jest.fn(),
            get: jest.fn(),
        },
        port: 3000,
    };
});

describe("main", () => {
    it("calls serverApp.listen with correct arguments", async () => {
        const { app } = await import("./express/app");
        await import("./main");

        expect(app.listen).toHaveBeenCalledWith(3000, expect.any(Function));
    });
});
