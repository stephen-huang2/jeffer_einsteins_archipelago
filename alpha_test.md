# Alpha Testing — Text Adventure Game

## Checklist

| # | What I tested | Result |

| 1 | Main menu works (tutorial, runs, play) | Pass |
| 2 | Picking "Steve" loads the game correctly | Pass |
| 3 | Moving around the map works | Pass |
| 4 | Can't walk off the edge of the map | Pass |
| 5 | Hunger goes down every time you move | Pass |
| 6 | Starving to death triggers game over | Pass |
| 7 | Islands unlock as you level up | Pass |
| 8 | Picking up items puts them in your jacket | Pass |
| 9 | Can't pick up items when inventory is full | Pass |
| 10 | Eating food restores the right amount of hunger | Pass |
| 11 | Hunger display shows the correct numbers | Pass |
| 12 | Dryad riddle works (needs Magical Branch first) | Pass |
| 13 | Kraken riddle works | Pass |
| 14 | Demon's Palace riddle works (needs Eye of Hell first) | Pass |
| 15 | Failing 3 riddles in a row ends the game | Pass |
| 16 | Using a key unlocks the room | Pass |
| 17 | Game resets properly when you restart | Pass |
| 18 | Runs get saved to the CSV file correctly | Pass |
| 19 | Blank input / weird input doesn't break the game | Pass |
| 20 | Typing a number out of range gives feedback | Fail |

---

## Stress Testing

I tried to break the game by doing things a normal player wouldn't.

- Walked around until I starved — worked fine
- Filled up my inventory completely then tried to grab more — said "pockets full" - Pass
- Failed every riddle on purpose 3 times — game over triggered correctly - Pass
- Typed garbage/random input at every prompt — some crashed or looped silently - Fail
- Restarted the game 5 times in a row — everything reset properly - Pass
- Pressed Enter without typing anything — some menus broke - Fail

---

## Results Summary

Most of the game works fine. The main issues I found were:

**Bug 1 — Hunger display is broken**
The hunger bar always shows `{self.max_points}` and `{percentage:.0f}%` as plain text instead of the actual numbers. This is because the second part of the string isn't an f-string. Easy fix.

**Bug 2 — Blank or weird input breaks some menus**
If you press Enter without typing anything, or add a space before your input like " move", some menus don't handle it and either loop silently or show "invalid choice" when it shouldn't. All inputs should be stripped and lowercased before being checked.

**Bug 3 — No feedback for out-of-range numbers**
If you type "99" at a riddle or loot menu, the game either treats it as a wrong answer or does nothing. It should tell you the valid options instead.

**Bug 4 — Key comparison is wrong in one place**
In the main map loop, the game checks `item[0][-3:]` to match a key name, which only works if the key is exactly 3 letters long. Keys like "Magical Branch" will never match. Should use `in item[0]` instead, like the rest of the code does.

---

## Changes to Make

- Fix the f-string in `get_status()` in `hunger.py`
- Strip and lowercase all user input inside `type_write()` so it's fixed everywhere at once
- Add a check for out-of-range input at riddle and loot prompts
- Fix the key comparison in the main map loop to use `in item[0]`
- Include `tutorial.txt` with the game so the tutorial option doesn't just say "file not found"