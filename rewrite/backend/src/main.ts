import { app, port } from "./express/app";
import { initializeDatabase } from "./database/initialize";

const db = initializeDatabase();

app.listen(port, () => {


    console.log(`Server running at http://localhost:${port}`);
});
