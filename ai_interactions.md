# AI Interactions Log


## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

I used the following prompt to generate a set of testcases 4 categories: *identify potention edgecases for all four functions from logic_utils (e.g., negative numbers, decimals, or extremely large values)  that may break the game. then, add testcases.* In addition to negative numbers, decimals, extreme values, the AI also added string input, leading/trailing whitespace, and case mismatch.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| negative input | see above | test_check_guess_with_negative_numbers | yes | check_guess should handle all numbers, and be agnostic to game assumptions (positive numbers) |
| whitespace | see above | test_difficulty_with_whitespace | not initially | I added a call to strip() on the input to trim whitespace, because the input is not guaranteed to be trimmed already |
| fail gracefully | see above | test_parse_multiple_decimals | yes | all programs with user input should fail gracefully, and not crash but prompt the user again |
