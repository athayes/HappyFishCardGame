import { Router, Response } from "express";

export const createHelloRouter = () => {
    const router = Router();

    router.get("/", (_, res: Response) => {
        res.send("Hello World!");
    });

    return router;
};
