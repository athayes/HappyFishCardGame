from src.cards import pudding
from src.scoring_functions.dessert.is_dessert import is_dessert


def test_is_dessert_pudding():
    assert is_dessert(pudding)


def test_is_not_dessert():
    assert not is_dessert('not a dessert')