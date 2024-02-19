import express from "express";

import { router as loginRouter } from './routes/login';
import { router as roomRouter } from './routes/room';

const port = 3000;

const app = express();

app.use(express.json());
app.use('/login', loginRouter);
app.use('/rooms', roomRouter);

app.get("/", (req, res) => {
    res.send("Hello World!");
});

export { app, port };
