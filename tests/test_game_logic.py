from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, outcome should be a win and hint correct
    result = check_guess(50, 50)
    outcome, hint = result
    assert outcome == "Win"
    assert "correct" in hint.lower()


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and hint go lower
    result = check_guess(guess=60, secret=50)
    outcome, hint = result
    assert outcome == "Too High"
    assert "go lower" in hint.lower()


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and hint go higher
    result = check_guess(guess=40, secret=50)
    outcome, hint = result
    assert outcome == "Too Low"
    assert "go higher" in hint.lower()


def test_easy_difficulty_range():
    # get_range_for_difficulty("Easy") should return range 1 to 20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_difficulty_range():
    # get_range_for_difficulty("Normal") should return range 1 to 100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_hard_difficulty_range():
    # get_range_for_difficulty("Hard") should return range 1 to 50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_invalid_difficulty_defaults_to_normal():
    # get_range_for_difficulty with unknown difficulty should default to (1, 100)
    low, high = get_range_for_difficulty("UnknownDifficulty")
    assert low == 1
    assert high == 100


def test_parse_valid_integer():
    # parse_guess with valid integer should return (True, int_value, None)
    ok, guess, error = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_valid_float():
    # parse_guess with float string should convert to int and return (True, int_value, None)
    ok, guess, error = parse_guess("42.7")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_empty_string():
    # parse_guess with empty string should return (False, None, error_message)
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_non_numeric():
    # parse_guess with non-numeric input should return (False, None, "That is not a number.")
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_update_score_win():
    # update_score with "Win" outcome should add points based on attempt number (min 10)
    score = update_score(100, "Win", attempt_number=2)
    assert score == 100 + (100 - 10 * 3)  # 100 + 70 = 170
    assert score == 170


def test_update_score_too_high_even_attempt():
    # update_score with "Too High" on even attempt should add 5 points
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 105


def test_update_score_too_low():
    # update_score with "Too Low" outcome should subtract 5 points
    score = update_score(100, "Too Low", attempt_number=1)
    assert score == 95


def test_update_score_none_outcome():
    # update_score with None outcome should return score unchanged
    score = update_score(100, None, attempt_number=1)
    assert score == 100


def test_update_score_invalid_outcome():
    # update_score with invalid outcome should return score unchanged
    score = update_score(100, "invalid", attempt_number=1)
    assert score == 100


#######################################
########### Edge case tests ###########
#######################################


def test_check_guess_with_negative_numbers():
    # check_guess should handle negative numbers correctly
    outcome, _ = check_guess(-10, -10)
    assert outcome == "Win"


def test_check_guess_with_zero():
    # check_guess with zero should compare correctly
    outcome, _ = check_guess(0, 0)
    assert outcome == "Win"


def test_check_guess_negative_vs_positive():
    # check_guess should correctly compare negative and positive numbers
    outcome, _ = check_guess(-5, 10)
    assert outcome == "Too Low"


def test_check_guess_with_very_large_numbers():
    # check_guess should handle very large numbers without overflow
    outcome, _ = check_guess(999999, 1000000)
    assert outcome == "Too Low"


def test_check_guess_string_inputs():
    # check_guess should handle string inputs that convert to numbers
    outcome, _ = check_guess("50", "50")
    assert outcome == "Win"


def test_check_guess_mixed_inputs_1():
    # check_guess should handle string inputs that convert to numbers
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"


def test_check_guess_mixed_inputs_2():
    # check_guess should handle string inputs that convert to numbers
    outcome, _ = check_guess("50", 50)
    assert outcome == "Win"


# Edge case tests for get_range_for_difficulty
def test_difficulty_case_sensitivity():
    # get_range_for_difficulty case-sensitive; lowercase "easy" defaults to Normal
    low, high = get_range_for_difficulty("easy")
    assert (low, high) == (1, 100)


def test_difficulty_empty_string():
    # get_range_for_difficulty with empty string should default to (1, 100)
    low, high = get_range_for_difficulty("")
    assert (low, high) == (1, 100)


def test_difficulty_with_whitespace():
    # get_range_for_difficulty with "Easy " (trailing space) should default to (1, 100)
    low, high = get_range_for_difficulty("Easy ")
    assert (low, high) == (1, 100)


# Edge case tests for parse_guess
def test_parse_negative_number():
    # parse_guess should handle negative numbers
    ok, guess, error = parse_guess("-42")
    assert ok is True
    assert guess == -42
    assert error is None


def test_parse_negative_float():
    # parse_guess should handle negative floats correctly
    ok, guess, error = parse_guess("-3.14")
    assert ok is True
    assert guess == -3
    assert error is None


def test_parse_zero():
    # parse_guess should handle zero
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None


def test_parse_very_large_number():
    # parse_guess should handle very large numbers
    ok, guess, error = parse_guess("999999999")
    assert ok is True
    assert guess == 999999999
    assert error is None


def test_parse_leading_trailing_whitespace():
    # parse_guess with whitespace "  42  " succeeds with strip()
    ok, guess, _ = parse_guess("  42  ")
    assert ok is True
    assert guess == 42


def test_parse_multiple_decimals():
    # parse_guess with "1.2.3" should fail gracefully
    ok, _, error = parse_guess("1.2.3")
    assert ok is False
    assert error == "That is not a number."


def test_parse_just_decimal_point():
    # parse_guess with "." should fail gracefully
    ok, _, error = parse_guess(".")
    assert ok is False
    assert error == "That is not a number."


def test_parse_scientific_notation():
    # parse_guess with "1e5" will not parse as float then convert to int
    ok, _, _ = parse_guess("1e5")
    assert not ok


# Edge case tests for update_score
def test_update_score_high_attempt_number():
    # update_score with high attempt (20) caps Win points at minimum 10
    score = update_score(100, "Win", attempt_number=20)
    # 100 - 10 * 21 = -110, capped at 10, so total = 100 + 10 = 110
    assert score == 110


def test_update_score_zero_attempt():
    # update_score with attempt 0 should give maximum points (90)
    score = update_score(0, "Win", attempt_number=0)
    # 100 - 10 * 1 = 90
    assert score == 90


def test_update_score_negative_current_score():
    # update_score should handle negative current scores
    score = update_score(-50, "Win", attempt_number=1)
    # -50 + (100 - 10 * 2) = -50 + 80 = 30
    assert score == 30


def test_update_score_too_high_odd_attempt():
    # update_score with "Too High" on odd attempt (1) should subtract 5
    score = update_score(100, "Too High", attempt_number=1)
    assert score == 95


def test_update_score_negative_attempt_number():
    # update_score with negative attempt; -1 is odd so subtract 5 for "Too High"
    score = update_score(100, "Too High", attempt_number=-1)
    assert score == 95


def test_update_score_outcome_case_sensitivity():
    # update_score is case-sensitive; "win" doesn't match "Win"
    score = update_score(100, "win", attempt_number=1)
    assert score == 100


def test_update_score_very_negative_final_score():
    # update_score should allow scores to go deeply negative
    score = update_score(-1000, "Too Low", attempt_number=5)
    assert score == -1005
