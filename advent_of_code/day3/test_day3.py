from day3 import Day3
import pytest

@pytest.fixture
def day3():
    return Day3()

@pytest.fixture
def new_hill():
    return format_input()

def test_single_move(day3):
    hill = [
        [".", ".", ".", "."],
        [".", ".", ".", "#"],
    ]

    trees_hit = day3.count_trees_hit(hill, 3, 1)

    assert trees_hit == 1

def test_overwrap_move(day3):
    hill = [
        [".", ".", ".", "."],
        [".", ".", ".", "#"],
        [".", ".", "#", "."],
        [".", "#", ".", "."],
    ]

    trees_hit = day3.count_trees_hit(hill, 3, 1)

    assert trees_hit == 3

def test_day_3_sample(day3):
    hill = [
		[".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
		["#", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."],
		[".", "#", ".", ".", ".", ".", "#", ".", ".", "#", "."],
		[".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
		[".", "#", ".", ".", ".", "#", "#", ".", ".", "#", "."],
		[".", ".", "#", ".", "#", "#", ".", ".", ".", ".", "."],
		[".", "#", ".", "#", ".", "#", ".", ".", ".", ".", "#"],
		[".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
		["#", ".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
		["#", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#"],
		[".", "#", ".", ".", "#", ".", ".", ".", "#", ".", "#"]
	]

    trees_hit = day3.count_trees_hit(hill, 3, 1)

    assert trees_hit == 7


def format_input():
    ruleset = []
    with open("input.txt", "r") as file_handle:
        for row in file_handle:
            clean_row = row.strip("\n")
            new_row = []
            for chara in clean_row:
                new_row.append(chara)
            ruleset.append(new_row)
    return ruleset

def test_day_3_sample_questions(day3, new_hill):
    trees_hit = day3.count_trees_hit(new_hill, 3, 1)
    assert trees_hit == 167

def test_day_3_part2(day3, new_hill):
    my_sets = []
    r1 = day3.count_trees_hit(new_hill, 1, 1)
    my_sets.append(r1)
    assert r1 == 53

    r2 = day3.count_trees_hit(new_hill, 3, 1)
    my_sets.append(r2)
    assert r2 == 167

    r3 = day3.count_trees_hit(new_hill, 5, 1)
    my_sets.append(r3)
    assert r3 == 54

    r4 = day3.count_trees_hit(new_hill, 7, 1)
    my_sets.append(r4)
    assert r4 == 67

    r5 = day3.count_trees_hit(new_hill, 1, 2)
    my_sets.append(r5)
    assert r5 == 23
    print(my_sets)

    result = 1
    for r in my_sets:
        result = result * r

    assert result == 9
