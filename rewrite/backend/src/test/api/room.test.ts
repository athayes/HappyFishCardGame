import request from 'supertest';
import { Application } from 'express';

import { createApp } from '../../express/app';

let app: Application;

beforeAll(async () => {
    app = await createApp();
});

describe('Room API', () => {
    it('should create a new room', async () => {
        const response = await request(app)
            .post('/api/rooms')
            .send({ name: 'Room 1' });

        expect(response.status).toBe(201);
        expect(response.body).toHaveProperty('roomId');
    });

    it('should get a room by ID', async () => {
        const createResponse = await request(app)
            .post('/api/rooms')
            .send({ name: 'Room 1' });

        const roomId = createResponse.body.roomId;

        const getResponse = await request(app).get(`/api/rooms/${roomId}`);

        expect(getResponse.status).toBe(200);
        expect(getResponse.body).toHaveProperty('roomId', roomId);
        expect(getResponse.body).toHaveProperty('name', 'Room 1');
    });
});
