<template>
    <div class="drafting">
        <div class="hand">
            <div class="card"
                 v-for="(card, index) in hand"
                 :key="card"
                 @click.stop="chooseCard(card, index)">
                <!-- div contents-->
                {{ card.name }}
            </div>
        </div>

        <div class="tableau">
            <div class="card"
                 v-for="(card, index) in tableau"
                 :key="card"
                 v-bind:class="styleIfChosen(card)"
                 @click.stop="returnCard(card, index)">
                {{ card.name }}
            </div>
        </div>

        <div class="buttons">
            <button @click.stop="okay()">
                Continue
            </button>
        </div>
    </div>
</template>

<script>
    import Card from "../models/Card";

    export default {
        // Data for the page. If this data changes, the page will update automatically
        data() {
            return {
                hand: [new Card("card1"), new Card("card2")],
                tableau: [new Card("card3"), new Card("card4"), new Card("card5")],
                cardChosen: false,
            };
        },

        methods: {
            // When you select a card
            chooseCard: function (card, index) {
                // "this" is whole component (Drafting)
                if (!this.cardChosen) {
                    this.hand.splice(index, 1); // remove the card we chose from the hand
                    card.picked = true; // update the style of the card
                    this.tableau.push(card);
                    this.cardChosen = true;
                }
            },

            // If you return the card
            returnCard: function (card, index) {
                if (this.cardChosen) {
                    this.tableau.splice(index, 1);
                    card.picked = false;
                    this.hand.push(card);
                    this.cardChosen = false;
                }
            },

            // Update the style of the card if selected
            styleIfChosen(card) {
                return {'picked': card.picked};
            },

            // Go to the next page
            okay: function () {
                alert("Continue was pressed");
            }
        }
    };
</script>

<style>
    .hand {
        display: flex;
        flex-wrap: nowrap;
        background-color: DodgerBlue;
        align-items: center;
        justify-content: center;
    }

    .tableau {
        display: flex;
        flex-wrap: nowrap;
        background-color: #66ff00;
        align-items: center;
        justify-content: center;
    }

    .card {
        background-color: #f1f1f1;
        width: 150px;
        margin: 10px;
        text-align: center;
        line-height: 300px;
        font-size: 30px;
    }

    .picked {
        background-color: red;
    }
</style>
