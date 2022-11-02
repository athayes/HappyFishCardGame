from backend.src.cards import squid_nigiri


def squiD(cards):
    if squid_nigiri in cards:
        return cards.index(squid_nigiri)
    else:
        return 0
