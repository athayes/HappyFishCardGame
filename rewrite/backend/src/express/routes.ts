import { Application } from "express";
import { createHelloRouter } from "./hello/router";
import { createRoomRouter } from "./room/router";
import { Database } from "sqlite";

export function setupRoutes({ app, db }: { app: Application; db: Database }) {
    app.use("/hello", createHelloRouter());
    app.use("/rooms", createRoomRouter({ db }));
}
