export function cardFactory(name, numPlayers) {
  if (name === "Egg Nigiri") {
    return {
      name: "Egg Nigiri",
      image: "/assets/egg.png",
      description:
        "Each egg nigiri is worth 1 point. An egg Nigiri on a Wasabi card is worth 3 points.",
      hint: "1",
      backgroundColor: "#ffdfdf"
    };
  }

  if (name === "Salmon Nigiri") {
    return {
      name: "Salmon Nigiri",
      image: "/assets/salmon.png",
      description:
        "Each salmon nigiri is worth 2 points. A salmon Nigiri on a Wasabi card is worth 6 points.",
      hint: "2",
      backgroundColor: "#ffdfdf"
    };
  }

  if (name === "Squid Nigiri") {
    return {
      name: "Squid Nigiri",
      image: "/assets/squid.png",
      description:
        "Each squid nigiri is worth 3 points. A squid Nigiri on a Wasabi card is worth 9 points.",
      hint: "3",
      backgroundColor: "#ffdfdf"
    };
  }

  if (name === "Wasabi") {
    return {
      name: name,
      image: "/assets/wasabi.png",
      description:
        "When you pick a wasabi card it has no effect. However, the next nigiri card you pick (in the same round) will be worth triple its usual points.",
      hint: "Next Nigiri x3",
      backgroundColor: "#ffdfdf"
    };
  }

  if (name === "Chopsticks") {
    return {
      name: name,
      image: "/assets/chopsticks.png",
      description:
        "Chopsticks let you take 2 cards on a future turn. Nothing happens on the turn when you initially play chopsticks. However, you may use it on a future turn to take a bonus action.",
      hint: "Swap for 2",
      backgroundColor: "#eeeeff"
    };
  }

  if (name === "Ice Cream") {
    return {
      name: "Ice Cream",
      image: "/assets/ice-cream.png",
      description:
        "Keep this until the end of the game. At the end of the game, if you have 4 Ice Cream, you score 12 points.",
      hint: "x4: 12",
      backgroundColor: "#f1feed"
    };
  }

  if (name === "Tea") {
    return {
      name: "Tea",
      image: "/assets/tea.png",
      description:
        "End of the round: Count the number of cards in your largest (or tied for largest) set of cards with the same background color. Tea is worth " +
        "1 point per card in that set",
      hint: "same color cards",
      backgroundColor: "#fff2d2"
    };
  }

  if (name === "Sashimi") {
    return {
      name: name,
      image: "/assets/sashimi.png",
      description:
        "A set of 3 sashimi cards scores 10 points. A single sashimi card or a set of only 2 is worth nothing. You may score multiple sets of sashimi in a round, although this is very hard to do!",
      hint: "x3: 10",
      backgroundColor: "aliceblue"
    };
  }

  if (["Maki 1", "Maki 2", "Maki 3"].includes(name)) {
    let hint, description;
    if (numPlayers >= 6) {
      description =
        "6 or more player game: At the end of the round, whoever has the most Maki scores 6 points. Whoever has second most scores 4 and whoever has the third most scores 2. If multiple players tie, all players receive the full points.";
      hint = "Most: 6, 2nd: 4, 3rd: 2";
    } else {
      description =
        "At the end of the round, whoever has the most Maki scores 6 points. Whoever has second most scores 3. If multiple players tie for most or second most, all players receive the full points.";
      hint = "Most: 6, 2nd: 3";
    }
    return {
      name: name,
      image: "/assets/maki.png",
      description: description,
      hint: hint,
      backgroundColor: "#f4d2f4"
    };
  }

  if (name === "Temaki") {
    let description, hint;
    if (numPlayers === 2) {
      description =
        "Two player game: The player with the most scores 4 points.";
      hint = "Most: 4";
    } else {
      description =
        "The player with the most scores 4 points. The player with the fewest (including 0) loses 4 points.";
      hint = "Most: 4, Least: -4";
    }

    return {
      name: name,
      image: "/assets/temaki.png",
      description: description,
      hint: hint,
      backgroundColor: "#ccaa"
    };
  }

  if (name === "Edamame") {
    let description, hint;
    description = "1 point per card for every opponent (up to 4) with edamame.";
    hint = "1 * opponent";

    return {
      name: name,
      image: "/assets/edamame.png",
      description: description,
      hint: hint,
      backgroundColor: "#e0ffff"
    };
  }

  if (name === "Eel") {
    let description, hint;
    description =
      "If you have 1 eel, you lose 3 points. If you have 2 or more eel, you score 7 points.";
    hint = "1: -3, 2+: 7";

    return {
      name: name,
      image: "/assets/eel.png",
      description: description,
      hint: hint,
      backgroundColor: "#fef0c2"
    };
  }

  if (name === "Tempura") {
    return {
      name: name,
      image: "/assets/tempura.png",
      description:
        "A set of 2 tempura cards scores 5 points. A single tempura card is worth nothing. You may score multiple sets of tempura in a round.",
      hint: "x2: 5",
      backgroundColor: "#fffbdf"
    };
  }

  if (name === "Dumpling") {
    return {
      name: name,
      image: "/assets/dumpling.png",
      description:
        "The more dumpling cards you have, the more points you will score, as follows: 1,3,6,10,15",
      hint: "1 3 6 10 15",
      backgroundColor: "#ffe6d0"
    };
  }

  if (name === "Pudding") {
    let description, hint;

    if (numPlayers === 2) {
      description =
        "2 player game: At the end of the game, players compare how many pudding cards they have. The player with the most scores 6 points.";
      hint = "Most: 6";
    } else {
      description =
        "At the end of the game, players compare how many pudding cards they have. The player with the most scores 6 points. The player with the fewest (including 0) loses 6 points.";
      hint = "Most: 6, Least: -6";
    }

    return {
      name: name,
      image: "/assets/pudding.png",
      description: description,
      hint: hint,
      backgroundColor: "#f1feed"
    };
  }

  throw "Invalid card type " + name;
}

export function cardDetails(card) {
  card = card === "Maki" ? "Maki 1" : card;
  card = card === "Nigiri" ? "Squid Nigiri" : card;
  return cardFactory(card);
}
