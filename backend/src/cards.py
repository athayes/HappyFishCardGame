# Static card names
maki_1 = "Maki 1"
maki_2 = "Maki 2"
maki_3 = "Maki 3"
egg_nigiri = "Egg Nigiri"
salmon_nigiri = "Salmon Nigiri"
squid_nigiri = "Squid Nigiri"
wasabi = "Wasabi"
dumpling = "Dumpling"
tempura = "Tempura"
sashimi = "Sashimi"
pudding = "Pudding"
ice_cream = "Ice Cream"
chopsticks = "Chopsticks"
tea = "Tea"


def is_maki(card):
    return card in (maki_1, maki_2, maki_3)


def get_maki_number(maki_card):
    if maki_card == maki_1:
        return 1
    if maki_card == maki_2:
        return 2
    if maki_card == maki_3:
        return 3
    raise Exception("Only accepts Maki cards!")


def is_nigiri(card):
    return card in (egg_nigiri, salmon_nigiri, squid_nigiri)

def get_nigiri_score(nigiri_card):
    if nigiri_card == egg_nigiri:
        return 1
    if nigiri_card == salmon_nigiri:
        return 2
    if nigiri_card == squid_nigiri:
        return 3
    raise Exception("Only accepts Nigiri cards!")