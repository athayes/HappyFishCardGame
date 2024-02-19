import express from 'express';
import { Room } from '../../types'; // Replace '../path/to/room-module' with the actual path to the module that exports the 'Room' type.

const router = express.Router();

/**
 * Todo get from backend
 */
let rooms: Record<string, Room> = {};

router.get('/:roomId', (req, res) => {
    const room = rooms[req.params.roomId];
    if (!room) {
        return res.status(400).json({ error: 'Room does not exist' });
    }
    res.json(room);
});

export default router;