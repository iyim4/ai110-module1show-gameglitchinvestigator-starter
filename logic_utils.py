def get_range_for_difficulty(difficulty: str):
    """Return the number range for a given difficulty level.

    Args:
        difficulty: The difficulty level as a string. Supported values are "Easy",
            "Normal", and "Hard". Case-sensitive.

    Returns:
        A tuple (low, high) representing the inclusive range of valid numbers
        for the given difficulty. Defaults to (1, 100) for unrecognized values.
            - "Easy": (1, 20)
            - "Normal": (1, 100)
            - "Hard": (1, 50)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse user input string into an integer guess.

    Attempts to convert the input string to an integer, handling decimal values
    by truncating to int. Validates that input is non-empty after stripping.

    Args:
        raw: User input string to parse. May contain leading/trailing whitespace
            or decimal notation (e.g., "42.7").

    Returns:
        A tuple (ok, guess_int, error_message) where:
            - ok (bool): True if parsing succeeded, False otherwise.
            - guess_int (int | None): The parsed integer value, or None if parsing failed.
            - error_message (str | None): An error description if parsing failed, or None on success.
    """
    raw = raw.strip()
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess against the secret number and return outcome feedback.

    Evaluates the guess relative to the secret number and provides appropriate
    feedback. Handles numeric string inputs by converting to integers.

    Args:
        guess: The guessed number (int, float, or numeric string).
        secret: The target secret number (int, float, or numeric string).

    Returns:
        A tuple (outcome, message) where:
            - outcome (str | None): One of "Win", "Too High", "Too Low", or None
              if conversion fails.
            - message (str): A user-friendly feedback message with emoji hint.
              Returns an error message if either input cannot be converted to int.
    """
    # check_guess does not assume input is positive
    # FIX: cast to int
    try:
        guess = int(guess)
        secret = int(secret)
    except (TypeError, ValueError):
        return None, "Invalid input: guess and secret must be numbers."

    # FIX: correct hints and simplify logic
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str | None, attempt_number: int):
    """Update the player's score based on the guess outcome.

    Applies point adjustments according to the outcome and attempt number.
    Winning awards scaled points based on efficiency, while incorrect guesses
    apply smaller penalties based on the direction guessed.

    Args:
        current_score: The player's current score before this attempt.
        outcome: The result of the guess: "Win", "Too High", "Too Low", or None.
            Only "Win", "Too High", and "Too Low" trigger score changes.
        attempt_number: The attempt count (0-indexed). Used to calculate win points
            and determine if a "Too High" guess earns or loses points.

    Returns:
        The updated score (int). If outcome is unrecognized, returns current_score
        unchanged. Win points = max(10, 100 - 10*(attempt_number+1)).
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    elif outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5
    elif outcome == "Too Low":
        return current_score - 5

    return current_score
