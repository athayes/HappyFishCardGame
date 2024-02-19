import express, { Router, Request, Response, NextFunction } from "express";
import { getRoom, createRoom } from "./controller"; // Assuming getRoom is defined in './room'
import { Database } from "sqlite";

function createRoomRouter({ db }: { db: Database }): Router {
    const router = express.Router();

    router.get("/:id", (req, res, next) => handleGetRoom(req, res, next, db));
    router.post("/", (req, res, next) => handleCreateRoom(req, res, next, db));

    return router;
}

async function handleGetRoom(req: Request, res: Response, next: NextFunction, db: Database) {
    try {
        const room = await getRoom({ db, req, res });
    } catch (err) {
        next(err);
    }
}

async function handleCreateRoom(req: Request, res: Response, next: NextFunction, db: Database) {
    try {
        const roomId = await createRoom({ db, req, res });
    } catch (error) {
        next(error);
    }
}

export { createRoomRouter };
