interface User {
    id: string;
    name: string;
    token: string;
}

export interface Room {
    id: string;
    users: User[];
    games: Game[];
}

export type Round = {};

export type Game = {
    users: User[];
    rounds: Round[];
    currentRound : number;
};
