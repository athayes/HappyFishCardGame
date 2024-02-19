import request from "supertest";
import { Server } from "http";

import { app, port } from "./app";

let server: Server;

beforeAll(() => {
    server = app.listen(port);
});

afterAll((done) => {
    server.close(done);
});

describe("server", () => {
    it("should return status code 200", async () => {
        const response = await request(app).get("/");
        expect(response.status).toBe(200);
    });

    it('should return "Hello, World!"', async () => {
        const response = await request(app).get("/");
        expect(response.text).toBe("Hello World!");
    });
});
