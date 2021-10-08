from src.cards import sashimi, wasabi, egg_nigiri, salmon_nigiri, squid_nigiri, chopsticks, tea, maki_1, maki_2, maki_3, \
    tempura, dumpling, pudding
from src.player import ReportEntry

card_group_map = {
    0: [wasabi, egg_nigiri, salmon_nigiri, squid_nigiri],
    1: [chopsticks],
    2: [tea],
    3: [sashimi],
    4: [maki_1, maki_2, maki_3],
    5: [tempura],
    6: [dumpling],
    7: [pudding]
}


def score_tea(player):
    indices = []
    personal_map = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }
    if tea in player.tableau:
        for index, card in enumerate(player.tableau):
            for key, group in card_group_map.items():
                if card in group:
                    personal_map[key] += 1
                    indices.append(index)
        score = max(personal_map.values())
        player.score += score
        player.score_report.report_entries.append(ReportEntry(f'Tea - biggest color group: {score}', score))

    player.tableau = [value for value in player.tableau if value != tea]
    return player
