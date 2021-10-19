from src.cards import pudding, ice_cream
from src.scoring_functions.dessert.is_dessert import is_dessert


def test_is_dessert_pudding():
    assert is_dessert(pudding)


def test_is_dessert_ice_cream():
    assert is_dessert(ice_cream)


def test_is_not_dessert():
    assert not is_dessert('not a dessert')