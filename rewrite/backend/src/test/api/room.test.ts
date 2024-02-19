import request from "supertest";
import type { Application } from "express";

import { createApp } from "../../express/app";

let app: Application;

beforeAll(async () => {
    ({ app } = await createApp());
}, 5000); // 5 seconds timeout

describe("Room API", () => {
    it("should create a new room", async () => {
        const response = await request(app).post("/room").send();
        expect(response.status).toBe(201);
        expect(response.body).toHaveProperty("roomId");
    });

    it("should get a room by ID", async () => {
        const createResponse = await request(app).post("/rooms").send({ name: "Room 1" });
        const roomId = createResponse.body.roomId;
        const getResponse = await request(app).get(`/rooms/${roomId}`);

        expect(getResponse.status).toBe(200);
        expect(getResponse.body).toHaveProperty("roomId", roomId);
        expect(getResponse.body).toHaveProperty("name", "Room 1");
    });
});
