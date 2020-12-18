from day2 import Day2
import pytest


@pytest.fixture
def day2():
    return Day2()


@pytest.fixture
def formatted_test():
    return format_input()


def test_sample_rules(day2):
    ruleset = [
        ["1-3 a: abcde"],
        ["1-3 b: cdefg"],
        ["2-8 c: ccccccccc"],
        ["2-9 c: ccccccccc"],
    ]

    assert day2.count_valid_passwords(ruleset) == 2


def format_input():
    ruleset = []
    with open("input.txt", "r") as file_handle:
        for row in file_handle:
            rowv = row.strip("\n")
            ruleset.append([f"{rowv}"])
    return ruleset


def test_day2_rules(day2, formatted_test):
    assert day2.count_valid_passwords(formatted_test) == 645

def test_positional(day2):
    ruleset = [
        ["1-3 a: abcde"],
        ["1-3 b: cdefg"],
        ["2-9 c: ccccccccc"],
        ["4-8 f: cccfccccc"],
    ]

    assert day2.count_valid_positions(ruleset) == 2

def test_day2_part2(day2, formatted_test):
    assert day2.count_valid_positions(formatted_test) == 737
