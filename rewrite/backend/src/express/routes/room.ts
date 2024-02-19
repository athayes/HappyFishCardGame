import express, { Router, Request, Response } from 'express';
import { getRoom } from '../../models/room'; // Assuming getRoom is defined in './room'
import { Database } from 'sqlite';

function createRoomRouter({db}: {db: Database}): Router {
    const router = express.Router();

    router.get('/:roomId', async (req: Request, res: Response) => {
        try {
            const str = req.params.roomId;
            const roomId = Number(str);
            // parse roomId string as as number
            if (isNaN(roomId)) {
                return res.status(400).json({ error: 'Invalid room ID' });
            }
            
            const room = await getRoom({ db, roomId });
            if (!room) {
                return res.status(400).json({ error: 'Room does not exist' });
            }
            res.json(room);
        } catch (error) {
            // Handle error
            console.error(error);
            res.status(500).json({ error: 'An error occurred' });
        }
    });

    return router;
}

export { createRoomRouter };