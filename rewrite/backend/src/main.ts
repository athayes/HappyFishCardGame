import { createApp } from "./express/app";

createApp().then(({ start }) => {
    start();
});
