export interface User {
    name: string;
    token: string;
}

export interface Room {
    users: User[];
}

let rooms: Record<string, Room> = {};

export type GameState = {
    currentRound: number;
};

export type Round = {};

export type Game = {
    users: User[];
    rounds: Round[];
    state: GameState;
};
