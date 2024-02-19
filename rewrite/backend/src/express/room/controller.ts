import { Request, Response } from "express";
import { createRoom as createRoomModel, getRoom as getRoomModel } from "./model";

export async function createRoom({ db, req, res }: { db: any; req: Request; res: Response }) {
    const room = await createRoomModel({ db });
    res.status(201).json(room);
}

export async function getRoom({ db, req, res }: { db: any; req: Request; res: Response }) {
    const id = Number(req.params.id);
    if (isNaN(id)) {
        res.status(400).json({ error: "Invalid ID" });
        return;
    }
    const room = await getRoomModel({ db, id });
    res.status(200).json(room);
}
