# AI Interactions Log


## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

I used the following prompt to generate a set of testcases 4 categories: *identify potention edgecases for all four functions from logic_utils (e.g., negative numbers, decimals, or extremely large values)  that may break the game. then, add testcases.* In addition to negative numbers, decimals, extreme values, the AI also added string input, leading/trailing whitespace, and case mismatch.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| negative input | see above | test_check_guess_with_negative_numbers | yes | check_guess should handle all numbers, and be agnostic to game assumptions (positive numbers) |
| whitespace | see above | test_difficulty_with_whitespace | not initially | I added a call to strip() on the input to trim whitespace, because the input is not guaranteed to be trimmed already |
| fail gracefully | see above | test_parse_multiple_decimals | yes | all programs with user input should fail gracefully, and not crash but prompt the user again |

--- 

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

I was plesantly suprised that AI fixed most issues. It was most effective at adding text-based fixes like docstrings. I think that for other whitespace fixes, it would be more efficient to use an autoformatter like Black.

**Prompt used:**

Two prompts, in one session. Used Claude AI, model Haiku 4.5
```
in logic_utils.py, app.py, tests/test_game_logic.py, add professional-grade docstrings to every function

review code in logic_utils.py, app.py, tests/test_game_logic.py for PEP 8 style compliance, and resolve any formatting or naming issues. 
```

**Linting output before:**

*Pylint output before AI revision in `logic_utils.py`, `app.py`, `tests/test_game_logic.py`*

pylint on `logic_utils.py`
```
************* Module logic_utils
logic_utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
logic_utils.py:30:11: W0718: Catching too general exception Exception (broad-exception-caught)
logic_utils.py:51:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
logic_utils.py:61:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
logic_utils.py:63:8: R1731: Consider using 'points = max(points, 10)' instead of unnecessary if block (consider-using-max-builtin)

------------------------------------------------------------------
Your code has been rated at 8.89/10
```
pylint on `app.py`
```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 9.86/10
```

pylint on `test_game_logic.py`
```
************* Module test_game_logic
tests\test_game_logic.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests\test_game_logic.py:1:0: E0401: Unable to import 'logic_utils' (import-error)
tests\test_game_logic.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:95:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:101:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:107:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:124:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:130:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:136:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:142:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:148:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:154:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:160:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:167:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:173:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:179:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:186:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:194:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:202:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:218:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:225:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:232:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:239:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:246:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:253:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:260:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:267:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:273:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:279:0: C0116: Missing function or method docstring (missing-function-docstring)
tests\test_game_logic.py:285:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.95/10
```

**Changes applied:**

- Added doctrings to files and functions, and enhanced existing doctrings to be professional-grade.
- PEP 8 Compliance: added blank lines/whitespace where needed, verify snake case naming, reformat one >95 character line, 


**Linting output after:**

I was interested to see how AI changes impacted linting output. Most interestingly, AI decreased the score in `logic_utils.py`.

pylint on `logic_utils.py`
```
************* Module logic_utils
logic_utils.py:38:0: C0301: Line too long (101/100) (line-too-long)
logic_utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
logic_utils.py:52:11: W0718: Catching too general exception Exception (broad-exception-caught)
logic_utils.py:84:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
logic_utils.py:110:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
logic_utils.py:112:8: R1731: Consider using 'points = max(points, 10)' instead of unnecessary if block (consider-using-max-builtin)

------------------------------------------------------------------
Your code has been rated at 8.67/10 (previous run: 8.89/10, -0.22)
```

pylint on `app.py`
```
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.86/10, +0.14)
```

pylint on `test_game_logic.py`
```
************* Module test_game_logic
tests\test_game_logic.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests\test_game_logic.py:1:0: E0401: Unable to import 'logic_utils' (import-error)

------------------------------------------------------------------
Your code has been rated at 9.61/10 (previous run: 6.95/10, +2.66)
```

---
