import express from "express";
import { v4 as uuidv4 } from "uuid";
import { rooms } from "../../database/fakeConsts";

const router = express.Router();

router.post("/", (req, res) => {
    const { name, room } = req.body;
    const token = uuidv4();

    if (room) {
        if (!rooms[room]) {
            return res.status(400).json({ error: "Room does not exist" });
        }
        rooms[room].users.push({ name, token });
    } else {
        const newRoom = uuidv4();
        rooms[newRoom] = { users: [{ name, token }], games: [] };
    }

    res.json({ token });
});

export { router };
