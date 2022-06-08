export const sillyWords = {
  nouns: ["Sushi", "Fish", "Restaurant", "Chef", "Dinner"],
  adjectives: ["Happy", "Exciting", "Excellent", "Delicious", "Good Taste"]
};

export function getRandomItem(array) {
  return array[Math.floor(Math.random() * array.length)];
}

export function sillyGameName() {
  return (
    `${getRandomItem(sillyWords.adjectives)}` +
    ` ${getRandomItem(sillyWords.nouns)}` +
    ` ${getRandomItem(sillyWords.adjectives)}` +
    " Game"
  );
}
