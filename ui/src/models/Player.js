import { cardFactory } from "@/models/Card";

export function findPlayer(players, playerName) {
  const index = players.findIndex(player => player.playerName === playerName);
  return { index, player: players[index] };
}

export function findPlayerUnderscore(players, playerName) {
  const index = players.findIndex(player => player.player_name === playerName);
  return { index, player: players[index] };
}

export function formatPlayers(players) {
  players = players.map(player => {
    return {
      playerName: player.player_name,
      tableau: formatCards(player.tableau),
      dessert: formatCards(player.dessert),
      hand: formatCards(player.hand),
      score: player.score,
      chosen: player.chosen,
      scoreReport: player.score_report
    };
  });
  return players;
}

export function formatCards(hand) {
  return hand.map(card => cardFactory(card));
}
