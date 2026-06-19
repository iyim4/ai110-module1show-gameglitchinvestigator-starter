# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game was impossible to win.
- List at least two concrete bugs you noticed at the start  
  - The hints were backwards.
  - When I failed a game, the New Game button did not work.

**Bug Reproduction Log**


| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| input 46 | hint 'go lower' (secret 42) | hint 'go higher' | none |
| input 20 | hint 'go higher' (secret 42) | hint 'go lower' | none |
| new game button pressed | history cleared | history persists, preventing guessing number from previous game | none |
| a number, pressed enter to apply | pressing enter key equivalent to submit guess button | nothing happens, number not applied | none |
| failed game | new game button resets state | nothing happends after new game button pressed | none |
| initial guess | attempts left -= 1| attempts left starts at 7 and updates on the 2nd number | none |
| numbers 1-11 | added to history, increase attempts | some numbers are not added to history, leading to more attempts than the limit | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  - Claude extension within VS Code. Model Haiku 4.5
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude identified that state variables (status, score, history) were not reset when the submit guess button was pressed. Verified correction through play testing.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Claude thought the incorrect hint bug was due to lexographical comparison due to mixed input type, instead of incorrect hint placement. Verified failed correction through play testing.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
  - I play tested for the Streamlit state fix and wrote a test cases for the incorrect hint bug. Streamlit is difficult to use with pytest, so I did not write a test for that.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - `check_guess` returns a tuple, so I had to unpack the values inside for testing.
- Did AI help you design or understand any tests? How? 
  - I asked Claude what a test for state would look like, which involved splitting logic into a redundant function and testing that. The change would not keep `logic_utils` separate from UI and clutter the interface, which is why I did not implement this test.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns the main Python file on every user interaction (button, text entry, etc), and uses a special dictionary called `session_state` as persistent storage between interactions. `session_state` ends when the page itself is reloaded. My friend, it appears that Python, or at least Streamlit, is *not* the ideal framework for interactive apps. [Try React](https://react.dev/)!

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? (This could be a testing habit, a prompting strategy, or a way you used Git.)
  - Prompting strategy: add more specific details. Clause provided an incomplete fix due to lack of detail in my prompt. I asked Claude how to improve my prompt (a good strategy I already use) to avoid this issue, and so next time, I will use a prompt that includes input + actual behavior + expected behavior + error message, like in the table of bugs above.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Add more detail in prompts
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I used the Claude extension within VS Code for the first time. Claude pauses when proposing an edit, which is nice, although I discovered that I prefer reading diffs and integrating specific changes myself.
