export type GameState = {
    currentRound: number;
};

export type Round = {};

export type Game = {
    players: string[];
    rounds: Round[];
    state: GameState;
};
