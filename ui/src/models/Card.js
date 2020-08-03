export default class Card {
  constructor(name, image, played) {
    this.name = name; // String: name of the card
    this.image = image; // String: link to image
    this.played = played; // Boolean: Already played, can't be returned to hand.
  }
}
