export function cardFactory(name) {
  if (name === "Egg") {
    return {
      name: name,
      image: "/assets/egg.png",
      description: "Egg Description",
      played: false
    }
  }

  if (name === "Chopsticks") {
    return {
      name: name,
      image: "/assets/chopsticks.png",
      description: "Chopsticks Description",
      played: false
    }
  }

  if (name === "Ice Cream") {
    return {
      name: name,
      image: "/assets/ice-cream.png",
      description: "Ice Cream Description",
      played: false
    }
  }

  if (name === "Sashimi") {
    return {
      name: name,
      image: "/assets/ice-cream.png",
      description: "Sashimi Description",
      played: false
    }
  }

  if (name === "Maki") {
    return {
      name: name,
      image: "/assets/maki.png",
      description: "Maki Description",
      played: false
    }
  }

  if (name === "Temaki") {
    return {
      name: name,
      image: "/assets/temaki.png",
      description: "Temaki Description",
      played: false
    }
  }

  if (name === "Wasabi") {
    return {
      name: name,
      image: "/assets/wasabi.png",
      description: "Wasabi Description",
      played: false
    }
  }

  throw("Invalid card type");
}