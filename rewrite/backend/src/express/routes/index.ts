import { Application } from "express";
import { createHelloRouter } from "./hello";
import { createRoomRouter } from "./room";
import { Database } from "sqlite";

export function setupRoutes({ app, db }: { app: Application; db: Database }) {
    app.use("/hello", createHelloRouter());
    app.use("/rooms", createRoomRouter({ db }));
}
