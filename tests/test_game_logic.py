from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    """Verify check_guess returns 'Win' outcome when guess equals secret."""
    result = check_guess(50, 50)
    outcome, hint = result
    assert outcome == "Win"
    assert "correct" in hint.lower()


def test_guess_too_high():
    """Verify check_guess returns 'Too High' outcome when guess exceeds secret."""
    result = check_guess(guess=60, secret=50)
    outcome, hint = result
    assert outcome == "Too High"
    assert "go lower" in hint.lower()


def test_guess_too_low():
    """Verify check_guess returns 'Too Low' outcome when guess is below secret."""
    result = check_guess(guess=40, secret=50)
    outcome, hint = result
    assert outcome == "Too Low"
    assert "go higher" in hint.lower()


def test_easy_difficulty_range():
    """Verify get_range_for_difficulty returns (1, 20) for 'Easy' difficulty."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_difficulty_range():
    """Verify get_range_for_difficulty returns (1, 100) for 'Normal' difficulty."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_hard_difficulty_range():
    """Verify get_range_for_difficulty returns (1, 50) for 'Hard' difficulty."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_invalid_difficulty_defaults_to_normal():
    """Verify get_range_for_difficulty defaults to (1, 100) for unknown difficulty."""
    low, high = get_range_for_difficulty("UnknownDifficulty")
    assert low == 1
    assert high == 100


def test_parse_valid_integer():
    """Verify parse_guess successfully parses valid integer strings."""
    ok, guess, error = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_valid_float():
    """Verify parse_guess converts and truncates float strings to integers."""
    ok, guess, error = parse_guess("42.7")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_empty_string():
    """Verify parse_guess rejects empty strings with appropriate error message."""
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_non_numeric():
    """Verify parse_guess rejects non-numeric input with error message."""
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_update_score_win():
    """Verify update_score awards points based on attempt efficiency on win."""
    score = update_score(100, "Win", attempt_number=2)
    assert score == 100 + (100 - 10 * 3)  # 100 + 70 = 170
    assert score == 170


def test_update_score_too_high_even_attempt():
    """Verify update_score awards 5 points for 'Too High' on even attempts."""
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 105


def test_update_score_too_low():
    """Verify update_score deducts 5 points for 'Too Low' outcome."""
    score = update_score(100, "Too Low", attempt_number=1)
    assert score == 95


def test_update_score_none_outcome():
    """Verify update_score returns unchanged score for None outcome."""
    score = update_score(100, None, attempt_number=1)
    assert score == 100


def test_update_score_invalid_outcome():
    """Verify update_score returns unchanged score for unrecognized outcomes."""
    score = update_score(100, "invalid", attempt_number=1)
    assert score == 100


#######################################
########### Edge case tests ###########
#######################################


def test_check_guess_with_negative_numbers():
    """Verify check_guess correctly handles and compares negative numbers."""
    outcome, _ = check_guess(-10, -10)
    assert outcome == "Win"


def test_check_guess_with_zero():
    """Verify check_guess correctly handles zero as guess and secret."""
    outcome, _ = check_guess(0, 0)
    assert outcome == "Win"


def test_check_guess_negative_vs_positive():
    """Verify check_guess correctly compares negative guess against positive secret."""
    outcome, _ = check_guess(-5, 10)
    assert outcome == "Too Low"


def test_check_guess_with_very_large_numbers():
    """Verify check_guess handles very large numbers without overflow."""
    outcome, _ = check_guess(999999, 1000000)
    assert outcome == "Too Low"


def test_check_guess_string_inputs():
    """Verify check_guess accepts and converts numeric string inputs."""
    outcome, _ = check_guess("50", "50")
    assert outcome == "Win"


def test_check_guess_mixed_inputs_1():
    """Verify check_guess handles mixed int and string numeric inputs."""
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"


def test_check_guess_mixed_inputs_2():
    """Verify check_guess handles mixed string and int numeric inputs."""
    outcome, _ = check_guess("50", 50)
    assert outcome == "Win"


def test_difficulty_case_sensitivity():
    """Verify get_range_for_difficulty is case-sensitive; defaults on lowercase input."""
    low, high = get_range_for_difficulty("easy")
    assert (low, high) == (1, 100)


def test_difficulty_empty_string():
    """Verify get_range_for_difficulty defaults to (1, 100) for empty string input."""
    low, high = get_range_for_difficulty("")
    assert (low, high) == (1, 100)


def test_difficulty_with_whitespace():
    """Verify get_range_for_difficulty is sensitive to whitespace and defaults accordingly."""
    low, high = get_range_for_difficulty("Easy ")
    assert (low, high) == (1, 100)


def test_parse_negative_number():
    """Verify parse_guess successfully parses negative integer strings."""
    ok, guess, error = parse_guess("-42")
    assert ok is True
    assert guess == -42
    assert error is None


def test_parse_negative_float():
    """Verify parse_guess converts and truncates negative float strings."""
    ok, guess, error = parse_guess("-3.14")
    assert ok is True
    assert guess == -3
    assert error is None


def test_parse_zero():
    """Verify parse_guess correctly parses zero."""
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None


def test_parse_very_large_number():
    """Verify parse_guess handles very large numbers without overflow."""
    ok, guess, error = parse_guess("999999999")
    assert ok is True
    assert guess == 999999999
    assert error is None


def test_parse_leading_trailing_whitespace():
    """Verify parse_guess strips leading and trailing whitespace from input."""
    ok, guess, _ = parse_guess("  42  ")
    assert ok is True
    assert guess == 42


def test_parse_multiple_decimals():
    """Verify parse_guess rejects malformed numbers with multiple decimal points."""
    ok, _, error = parse_guess("1.2.3")
    assert ok is False
    assert error == "That is not a number."


def test_parse_just_decimal_point():
    """Verify parse_guess rejects single decimal point as non-numeric."""
    ok, _, error = parse_guess(".")
    assert ok is False
    assert error == "That is not a number."


def test_parse_scientific_notation():
    """Verify parse_guess rejects scientific notation format."""
    ok, _, _ = parse_guess("1e5")
    assert not ok


def test_update_score_high_attempt_number():
    """Verify update_score caps win points at minimum 10 for high attempt numbers."""
    score = update_score(100, "Win", attempt_number=20)
    # 100 - 10 * 21 = -110, capped at 10, so total = 100 + 10 = 110
    assert score == 110


def test_update_score_zero_attempt():
    """Verify update_score awards maximum points (90) for first attempt win."""
    score = update_score(0, "Win", attempt_number=0)
    # 100 - 10 * 1 = 90
    assert score == 90


def test_update_score_negative_current_score():
    """Verify update_score correctly handles negative starting scores."""
    score = update_score(-50, "Win", attempt_number=1)
    # -50 + (100 - 10 * 2) = -50 + 80 = 30
    assert score == 30


def test_update_score_too_high_odd_attempt():
    """Verify update_score deducts 5 points for 'Too High' on odd attempts."""
    score = update_score(100, "Too High", attempt_number=1)
    assert score == 95


def test_update_score_negative_attempt_number():
    """Verify update_score handles negative attempt numbers correctly."""
    score = update_score(100, "Too High", attempt_number=-1)
    assert score == 95


def test_update_score_outcome_case_sensitivity():
    """Verify update_score is case-sensitive for outcome matching."""
    score = update_score(100, "win", attempt_number=1)
    assert score == 100


def test_update_score_very_negative_final_score():
    """Verify update_score allows scores to go deeply negative."""
    score = update_score(-1000, "Too Low", attempt_number=5)
    assert score == -1005
