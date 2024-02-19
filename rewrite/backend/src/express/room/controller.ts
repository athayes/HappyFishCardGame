import { Request, Response } from "express";
import { createRoom as createRoomModel, getRoom as getRoomModel } from "./model";

export async function createRoom({ db, req, res }: { db: any; req: Request; res: Response }) {
    const result = await createRoomModel({ db });
    res.status(201).json(result);
}

export async function getRoom({ db, req, res }: { db: any; req: Request; res: Response }) {
    const id = req.params.id;
    const result = await getRoomModel({ db, id });
    res.status(200).json(result);
}
