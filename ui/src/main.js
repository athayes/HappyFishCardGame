import { createApp } from "vue";
import router from "./router";
import store from "./store";
import myapp from "./App";

const app = createApp(myapp);
app.use(store);
app.use(router);

app.mount("#app");
