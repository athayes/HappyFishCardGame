interface User {
    name: string;
    token: string;
}

export interface Room {
    users: User[];
    games: Game[];
}

export type Round = {};

export type Game = {
    users: User[];
    rounds: Round[];
    currentRound : number;
};
