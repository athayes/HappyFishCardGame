import { cardFactory } from "./Card";

export const CARD_TYPES = {
  Nigiri: {
    name: "Nigiri",
    cards: ["Nigiri"]
  },
  Rolls: {
    name: "Rolls",
    cards: [
      "Temaki",
      //"Uramaki",
      "Maki"
    ]
  },
  Special: {
    name: "Special",
    cards: ["Chopsticks", "Tea", "Wasabi"] // spoon soy sauce menu
  },
  Appetizer: {
    name: "Appetizer",
    cards: ["Sashimi", "Tempura", "Dumpling", "Edamame", "Eel"]
  },
  Dessert: {
    name: "Dessert",
    cards: ["Ice Cream", "Pudding"]
  }
};

export const EMPTY_DECK = [
  {
    name: "Nigiri",
    image: cardFactory("Squid Nigiri").image,
    type: CARD_TYPES.Nigiri.name
  },
  {
    name: "Maki",
    image: cardFactory("Maki 1").image,
    type: CARD_TYPES.Rolls.name
  },
  {
    name: "Chopsticks",
    image: cardFactory("Chopsticks").image,
    type: CARD_TYPES.Special.name
  },
  {
    name: "Wasabi",
    image: cardFactory("Wasabi").image,
    type: CARD_TYPES.Special.name
  },
  {
    name: "Dumpling",
    image: cardFactory("Dumpling").image,
    type: CARD_TYPES.Appetizer.name
  },
  {
    name: "Tempura",
    image: cardFactory("Tempura").image,
    type: CARD_TYPES.Appetizer.name
  },
  {
    name: "Sashimi",
    image: cardFactory("Sashimi").image,
    type: CARD_TYPES.Appetizer.name
  },
  {
    name: "Pudding",
    image: cardFactory("Pudding").image,
    type: CARD_TYPES.Dessert.name
  }
];

export function isImmutable(type) {
  if (type === "Nigiri") {
    return true;
  }
}
