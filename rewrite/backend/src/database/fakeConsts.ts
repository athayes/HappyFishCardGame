import { Room } from "../types";

/**
 * refactor this to be read from the database
 */
let rooms: Record<string, Room> = {};

export { rooms };