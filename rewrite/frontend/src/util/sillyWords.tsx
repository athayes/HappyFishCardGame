export const sillyWords: {  
  nouns: string[];
  adjectives: string[];
} = {
  nouns: ["Sushi", "Fish", "Restaurant", "Chef", "Dinner"],
  adjectives: ["Happy", "Exciting", "Excellent", "Delicious", "Good Taste"]
};

export function getRandomItem(array: string[]): string {
  return array[Math.floor(Math.random() * array.length)];
}

export function sillyGameName(): string {
  return (
    `${getRandomItem(sillyWords.adjectives)}` +
    ` ${getRandomItem(sillyWords.nouns)}` +
    ` ${getRandomItem(sillyWords.adjectives)}` +
    " Game"
  );
}