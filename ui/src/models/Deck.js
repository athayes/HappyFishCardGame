export const CARD_TYPES = {
  Nigiri: {
    name: "Nigiri",
    cards: ["Nigiri"]
  },
  Rolls: {
    name: "Rolls",
    cards: ["Temaki", "Uramaki", "Maki"]
  },
  Special: {
    name: "Special",
    cards: ["Chopsticks", "Tea", "Wasabi"] // spoon soy sauce menu
  },
  Appetizer: {
    name: "Appetizer",
    cards: ["Sashimi", "Tempura", "Dumpling"]
  },
  Dessert: {
    name: "Dessert",
    cards: ["Ice Cream", "Pudding"]
  }
};

export const EMPTY_DECK = [
  { name: "Nigiri", type: CARD_TYPES.Nigiri.name },
  { name: "Maki", type: CARD_TYPES.Rolls.name },
  { name: "Chopsticks", type: CARD_TYPES.Special.name },
  { name: "Wasabi", type: CARD_TYPES.Special.name },
  { name: "Dumpling", type: CARD_TYPES.Appetizer.name },
  { name: "Tempura", type: CARD_TYPES.Appetizer.name },
  { name: "Sashimi", type: CARD_TYPES.Appetizer.name },
  { name: "Pudding", type: CARD_TYPES.Dessert.name }
];

export function isImmutable(type) {
  if (type === "Nigiri") {
    return true;
  }
}
