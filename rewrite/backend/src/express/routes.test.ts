import { setupRoutes } from "./routes";
import { createHelloRouter } from "./hello/router";
import { createRoomRouter } from "./room/router";

jest.mock("./hello/router", () => ({
    createHelloRouter: jest.fn().mockReturnValue("helloRouter"),
}));

jest.mock("./room/router", () => ({
    createRoomRouter: jest.fn().mockReturnValue("roomRouter"),
}));

describe("setupRoutes", () => {
    let app: any;
    let db: any;

    beforeEach(() => {
        app = { use: jest.fn() };
        db = {};
    });

    it("should set up hello router", () => {
        const helloRouter = createHelloRouter();
        setupRoutes({ app, db });
        // Assert that the hello router is added to the app
        expect(app.use).toHaveBeenCalledWith("/hello", helloRouter);
    });

    it("should set up room router", () => {
        const roomRouter = createRoomRouter({ db });
        setupRoutes({ app, db });
        // Assert that the room router is added to the app
        expect(app.use).toHaveBeenCalledWith("/rooms", roomRouter);
    });
});
