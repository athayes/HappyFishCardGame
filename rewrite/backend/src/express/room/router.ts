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
        const id = Number(req.params.id);
        if (isNaN(id)) {
            res.status(400).json({ error: "Invalid ID" });
            return;
        }
        const room = await getRoom({ db, req, res });
        res.status(200).json(room);
    } catch (err) {
        next(err);
    }
}

async function handleCreateRoom(req: Request, res: Response, next: NextFunction, db: Database) {
    try {
        const roomId = await createRoom({ db, req, res });
        res.status(201).json({ roomId });
    } catch (error) {
        next(error);
    }
}

export { createRoomRouter };
