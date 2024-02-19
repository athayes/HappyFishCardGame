import express from "express";
import { createApp } from "./app";
import exp from "constants";

describe("createApp", () => {
    it("should return an instance of express.Application", async () => {
        const app = await createApp();
        expect(app).toBeInstanceOf(express);
    });

    it("should initialize the database", async () => {
        const mockInitializeDatabase = jest.spyOn(initializeDatabase, "initialize");
        await createApp();
        expect(mockInitializeDatabase).toHaveBeenCalled();
    });

    it("should register the room router", async () => {
        const app = await createApp();
        expect(app._router.stack.some((layer) => layer.route.path === "/room")).toBe(true);
    });

    it("should register the hello router", async () => {
        const app = await createApp();
        expect(app._router.stack.some((layer) => layer.route.path === "/hello")).toBe(true);
    });
});

