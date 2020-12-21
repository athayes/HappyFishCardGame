export function cardFactory(name) {
  if (name === "Egg") {
    return {
      name: "Egg Nigiri",
      image: "/assets/egg.png",
      description: "Each egg nigiri is worth 1 point. An egg Nigiri on a Wasibi card is worth 3 points",
      hint: "1"
    };
  }

  if (name === "Salmon") {
    return {
      name: "Salmon Nigiri",
      image: "/assets/salmon.png",
      description: "Each salmon nigiri is worth 2 points. A salmon Nigiri on a Wasibi card is worth 6 points",
      hint: "2"
    };
  }

  if (name === "Squid") {
    return {
      name: "Squid Nigiri (3)",
      image: "/assets/squid.png",
      description: "Each squid nigiri is worth 3 points. A squid Nigiri on a Wasibi card is worth 9 points",
      hint: "3"
    };
  }

  if (name === "Wasabi") {
    return {
      name: name,
      image: "/assets/wasabi.png",
      description: "When you play a wasabi card, it has no effect. However, the next nigiri card that you play must be placed on top of the wasabi card. This means that the nigiri will be worth triple points at the end of the round!",
      hint: "Next Nigiri x3"
    };
  }

  if (name === "Chopsticks") {
    return {
      name: name,
      image: "/assets/chopsticks.png",
      description: "Chopsticks let you take 2 cards on a future turn. Nothing happens on the turn when you initially play chopsticks. However, you may use it on a future turn to take a bonus action.",
      hint: "Swap for 2"
    };
  }

  if (name === "IceCream") {
    return {
      name: "Green Tea Ice Cream",
      image: "/assets/ice-cream.png",
      description: "A dessert: You keep this until the end of the game. If at the end of the game you have 4 Green Tea ice cream, you score 12 points",
      hint: "x4 = 12"
    };
  }

  if (name === "Sashimi") {
    return {
      name: name,
      image: "/assets/sashimi.png",
      description: "A set of 3 sashimi cards scores 10 points. A single sashimi card or a set of only 2 is worth nothing. You may score multiple sets of sashimi in a round, although this is very hard to do!",
      hint: "x3 = 10"
    };
  }

  if (name === "Maki") {
    return {
      name: name,
      image: "/assets/maki.png",
      description: "Whoever has the most Maki scores 6 points. Whoever has second most scores 3. If multiple players tie for most or second most, all players receive the full points",
      hint: "Most: 6 / 4 / 2"
    };
  }

  if (name === "Temaki") {
    return {
      name: name,
      image: "/assets/temaki.png",
      description: "The player with the most scores 4 points. The player with the fewest (including 0) loses 4 points.",
      hint: "Most = 4, Least = -4",
      played: false
    };
  }

  if (name === "Tempura") {
    return {
      name: name,
      image: "/assets/tempura.png",
      description: "A set of 2 tempura cards scores 5 points. A single tempura card is worth nothing. You may score multiple sets of tempura in a round.",
      hint: "x2 = 5"
    };
  }

  if (name === "Dumpling") {
    return {
      name: name,
      image: "/assets/dumpling.png",
      description: "The more dumpling cards you have, the more points you will score, as follows: 1,3,6,10,15",
      hint: "1 3 6 10 15"
    };
  }

  if (name === "Pudding") {
    return {
      name: name,
      image: "/assets/pudding.png",
      description: "At the end of the game, players compare how many pudding cards they have. The player with the most scores 6 points. The player with the fewest (including 0) loses 6 points.",
      hint: "Most: 6, Least -6"
    };
  }

  throw "Invalid card type " + name;
}
