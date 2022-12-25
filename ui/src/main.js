import { createApp } from "vue";
import router from "./router";
import store from "./store";

const app = createApp({
  router,
  store
});

app.use(router);

app.mount("#app");
