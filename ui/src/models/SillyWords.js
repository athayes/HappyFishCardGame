export const sillyWords = {
  nouns: ["Sushi", "Restaurant", "Chef", "Dinner"],
  adjectives: ["Happy", "Exciting", "Delicious", "Good Taste"]
};

export function getRandomItem(array) {
  return array[Math.floor(Math.random() * array.length)];
}
