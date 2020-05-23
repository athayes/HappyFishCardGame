export default class Card {
  constructor(name, played) {
    this.name = name; // String: name of the card
    this.played = played; // Boolean: Already played, can't be returned to hand.
  }
}
