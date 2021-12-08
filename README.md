Nick Shepeard's Jeopardy! game

This program is a spin on the popular television quiz show "Jeopardy!". Test
your knowledge of three separate categories: American History,
Science, and Before and After.

![giphy](https://user-images.githubusercontent.com/68496022/145286083-98eddba5-554a-4d12-864a-ac3de52bc9b4.gif)
  
Functions:

- Introduction:
Controls the introduction portion where a user enters a name and other
    information necessary to calculate the ELO score. Returns player_info
    which is information about the player such as name, age, ELO, etc.

- Select_category:
Acts as the telephone operator for category selection. A user enters a
    number and is directed to the proper function which presents the user with
    the proper clue by calling functions for each specific category. Returns
    game_info which is explained in above docstrings.

- Execute category clue:
Presents user with the proper clue for each category corresponding to the clue
    number. Deducts points from user total score (game_info[0]) if the
    answer is incorrect, and adds points to user total score if the answer
    is correct. Returns game_info so the information can be properly tracked.

- Final_jeopardy:
If a user has a positive score, the game progresses to this stage. In
    this function, a user can wager however many points are available. If
    the user gets it wrong, the wager is deducted. If the user is correct,
    the wager is added. This uses game_info as a parameter because the
    player score is necessary to determine whether to proceed with Final
    Jeopardy or to skip it. The player wager is returned so it can be
    calculated in the next function.

- Calculate_final_score:
This is where the total user score after the wager amount has either
    been added or subtracted is calculated. Then, depending on if the user
    score is positive or negative, the ELO rating is either added or not to
    present the user with the final score.
