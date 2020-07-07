from candles import Candle


def test_candle_has_reasonable_defaults():
    candle = Candle()
    assert candle.color == "beige"
    assert candle.wicks == 1
    assert candle.burn_time_remaining == 10


def test_candles_can_have_different_wick_counts():
    small = Candle(wicks=2)
    big = Candle(wicks=3)

    assert small.wicks == 2
    assert small.burn_time_remaining == 20

    assert big.wicks == 3
    assert big.burn_time_remaining == 30


def test_candle_burn_time():
    candle = Candle()
    candle.burn()
    assert candle.burn_time_remaining == 9
