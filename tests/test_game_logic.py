from logic_utils import check_guess


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
