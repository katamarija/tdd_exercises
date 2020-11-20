import pytest

from coffee import Coffee

def test_coffee_is_ground():
    coffee = Coffee()
    assert coffee.grind == "ground"


@pytest.mark.parametrize("brew,expected_grind_level", [("pour-over", "fine"), ("french-press", "medium"), ("cold-brew", "coarse")])
def test_coffee_can_have_different_brews(brew, expected_grind_level):
    coffee = Coffee(brew_type=brew)
    assert coffee.grind == expected_grind_level
