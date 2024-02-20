import request from "supertest";
import type { Application } from "express";
import { createApp } from "../../express/app";

let app: Application;

beforeAll(async () => {
    ({ app } = await createApp());
}, 5000); // 5 seconds timeout

const createdRoomId = '';
const ROOMS = '/rooms';

describe("Room API", () => {
    it("should say hello", async () => {
        const response = await request(app).get("/hello");
        expect(response.status).toBe(200);
        expect(response.text).toBe("Hello World!");
    });

    it("should create a new room", async () => {
        const response = await request(app).post(ROOMS).send();
        expect(response.status).toBe(201);
        expect(response.body).toHaveProperty("id");
    });

    it("should get a room by ID", async () => {
        const { body: { id }} = await request(app).post(ROOMS).send();
        const getResponse = await request(app).get(`${ROOMS}/${id}`);

        expect(getResponse.status).toBe(200);
        expect(getResponse.body).toHaveProperty("id", id);
    });
});
