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
    cards: ["Egg Nigiri", "Salmon Nigiri", "Squid Nigiri", "Sashimi", "Tempura", "Dumpling"]
  },
  Dessert: {
    name: "Dessert",
    cards: ["Ice Cream", "Pudding"]
  }
};

export const EMPTY_DECK = [
  { name: "", type: CARD_TYPES.Nigiri.name },
  { name: "", type: CARD_TYPES.Rolls.name },
  { name: "", type: CARD_TYPES.Special.name },
  { name: "", type: CARD_TYPES.Special.name },
  { name: "", type: CARD_TYPES.Appetizer.name },
  { name: "", type: CARD_TYPES.Appetizer.name },
  { name: "", type: CARD_TYPES.Appetizer.name },
  { name: "", type: CARD_TYPES.Dessert.name }
];

export function isImmutable(type) {
  if (type === "Nigiri") {
    return true;
  }
}
