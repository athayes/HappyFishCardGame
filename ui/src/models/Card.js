export function cardFactory(name) {
  if (name === "Egg") {
    return {
      name: name,
      image: "/assets/egg.png",
      description: "Egg Description",
      played: false
    };
  }

  if (name === "Chopsticks") {
    return {
      name: name,
      image: "/assets/chopsticks.png",
      description: "Chopsticks Description",
      played: false
    };
  }

  if (name === "IceCream") {
    return {
      name: "Ice Cream",
      image: "/assets/ice-cream.png",
      description: "Ice Cream Description",
      played: false
    };
  }

  if (name === "Sashimi") {
    return {
      name: name,
      image: "/assets/sashimi.png",
      description: "Sashimi Description",
      played: false
    };
  }

  if (name === "Maki") {
    return {
      name: name,
      image: "/assets/maki.png",
      description: "Maki Description",
      played: false
    };
  }

  if (name === "Temaki") {
    return {
      name: name,
      image: "/assets/temaki.png",
      description: "Temaki Description",
      played: false
    };
  }

  if (name === "Wasabi") {
    return {
      name: name,
      image: "/assets/wasabi.png",
      description: "Wasabi Description",
      played: false
    };
  }

  if (name === "Tempura") {
    return {
      name: name,
      image: "/assets/tempura.png",
      description: "Tempura Description",
      played: false
    };
  }

  if (name === "Dumpling") {
    return {
      name: name,
      image: "/assets/dumpling.png",
      description: "Dumpling Description",
      played: false
    };
  }

  if (name === "Squid") {
    return {
      name: name,
      image: "/assets/squid.png",
      description: "Squid Description",
      played: false
    };
  }

  if (name === "Pudding") {
    return {
      name: name,
      image: "/assets/pudding.png",
      description: "Pudding Description",
      played: false
    };
  }

  if (name === "Salmon") {
    return {
      name: name,
      image: "/assets/salmon.png",
      description: "Salmon Description",
      played: false
    };
  }

  throw "Invalid card type " + name;
}
