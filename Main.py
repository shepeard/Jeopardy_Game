def main():
    player_info = introduction()
    game_info = init_variables()
    game_info = select_category(game_info)
    final_jeopardy(game_info, player_info)


def init_variables():
    player_points = 0  # game_info[0]
    american_history_clue = 0  # game_info[1]
    science_clue = 0  # game_info[2]
    before_and_after_clue = 0  # game_info[3]
    total_clue = 0  # game_info[4]
    game_info = [player_points, american_history_clue, science_clue,
                 before_and_after_clue, total_clue]
    return game_info


def introduction():
    player_name = input(
        "This is Jeopardy! Please enter your name to start playing: ")
    times = int(input(
        "How many times have you watched Jeopardy!? Please enter a number: "))
    age = int(input("How old are you?: "))
    if times < 10:
        times **= 2
        # Give an advantage to less experienced players by increasing
        # this component of the ELO score exponentially.
    age **= 2
    elo = times + age * 5 / 2 - 50 + 100
    # Calculates player ELO score to be used at the end of the game when
    # determining points. Adds the values of number of times and age,
    # multiplies by 5, divides by 2, subtracts 50, adds 100.
    print("\nYour Jeopardy! ELO is: ", elo, sep='')
    print("\nWelcome,",
          player_name + ". Let's get started with the Jeopardy round.")
    player_info = [player_name, elo]
    return player_info


def select_category(game_info):
    while game_info[4] < 9:
        category = input(
            "\nEnter one of the following categories - American History, Science, Before and After: ").lower()
        # Planning on removing categories from the input statement depending on
        # whether a player has completed them or not later on.
        if category == "american history":
            if game_info[1] < 3:
                game_info[4] += 1
                game_info = execute_american_history_clue(game_info)
            else:
                print("You have already completed this category!")
                select_category(game_info)
        elif category == "science":
            if game_info[2] < 3:
                game_info[4] += 1
                game_info = execute_science_clue(game_info)
            else:
                print("You have already completed this category!")
                select_category(game_info)
        elif category == "before and after":
            if game_info[3] < 3:
                game_info[4] += 1
                game_info = execute_before_and_after_clue(game_info)
            else:
                print("You have already completed this category!")
                select_category(game_info)
        else:
            print("You entered an invalid category.")
            select_category(game_info)
    return game_info


def execute_american_history_clue(game_info):
    if game_info[1] == 0:
        game_info[1] += 1
        answer = input(
            "\nFor 500, here's the first clue: \nThis founding father "
            "drafted the Declaration of Independence in 1776: ").lower()
        if "jefferson" in answer:
            print("\nYou got it!")
            game_info[0] += 500
        else:
            print("\nSorry, no. The correct response was Thomas Jefferson")
            game_info[0] -= 500
    elif game_info[1] == 1:
        game_info[1] += 1
        answer = input("\nFor 750, here's the clue: \nThis state was the last "
                       "to be admitted to the United States in 1959: ").lower()
        if answer == "hawaii":
            print("\nCorrect!")
            game_info[0] += 750
            select_category(game_info)
        if answer != "hawaii" or answer != "Hawaii":
            print("\nSorry, that's not right. We were looking for Hawaii.")
            game_info[0] -= 750
            select_category(game_info)
    elif game_info[1] == 2:
        game_info[1] += 1
        answer = input(
            "\nFor 1000 to finish the category: \nEstablished in the "
            "1803 Supreme Court case Marbury v. Madison, this allows "
            "the courts to strike down unconstitutional laws: ").lower()
        if answer == "judicial review":
            print("\nCorrect!")
            game_info[0] += 1000
            select_category(game_info)
        if answer != "judicial review":
            print("\nNope, sorry. The correct response was judicial review.")
            game_info[0] -= 1000
            select_category(game_info)
    return game_info


def execute_science_clue(game_info):
    if game_info[2] == 0:
        game_info[2] += 1
        answer = input(
            "\nFor 500, here's the first clue. \nThis machine makes "
            "audible 'beeps' as it measures the amount of radiation in the air: ").lower()
        if "geiger" in answer:
            print("\nYou got it!")
            game_info[0] += 500
        else:
            print("\nNo, sorry. The correct response was Geiger Counter.")
            game_info[0] -= 500
        select_category(game_info)
    elif game_info[2] == 1:
        game_info[2] += 1
        answer = input("\nFor 750, here's your next clue. \nA person who is "
                       "considered to be a 'universal donor' has this blood type: ").lower()
        if "o negative" in answer:
            print("\nThat's correct!")
            game_info[0] += 750
        else:
            print("\nThat's not it. We were looking for O Negative.")
            game_info[0] -= 500
        select_category(game_info)
    elif game_info[2] == 2:
        game_info[2] += 1
        answer = input(
            "\nHere's the 1000 science clue. \nJesse, wanna cook? This pioneer of quantum mechanics is also the pseudonym of a famous TV protagonist: ").lower()
        if "heisenberg" or "heisenburg" in answer:
            print("\nYou got it!")
            game_info[0] += 1000
        else:
            print("\nSorry, that's not it.")
            game_info[0] -= 1000
        select_category(game_info)
    return game_info


def execute_before_and_after_clue(game_info):
    if game_info[3] == 0:
        game_info[3] += 1
        answer = input(
            "For 500, let's start off the category. \nThis nighttime "
            "directional beacon is visible to Captain Kirk and crew: ").lower()
        if "north star trek" in answer:
            print("\nYou got it!")
            game_info[0] += 500
        else:
            print(
                "\nThat's not it. The directional beacon is the North Star Trek. ")
            game_info[0] -= 500
        select_category(game_info)
    elif game_info[3] == 1:
        game_info[3] += 1
        answer = input(
            "For 750, here you go. \nThis triage's the injured while "
            "bringing them food in their beds: ").lower()
        if "emergency room service" in answer:
            print("\nThat's correct!")
            game_info[0] += 750
        else:
            print(
                "\nSorry, no. The correct response was what is Emergency Room Service. ")
            game_info[0] -= 750
        select_category(game_info)
    elif game_info[3] == 2:
        game_info[3] += 1
        answer = input("Finishing off Before and After, here's your "
                       "clue. \nThe final resting place in honor of "
                       "unidentified deceased veterans is moved from Arlington "
                       "National Cemetery to the Chicago Bears' stadium: ").lower()
        if "tomb of the unknown soldier field" in answer:
            print("\nGood for you!")
            game_info[0] += 1000
        else:
            print(
                "\nSorry, no. The correct response was Tomb of the Unknown Soldier Field. ")
            game_info[0] -= 1000
        select_category(game_info)
    return game_info


# noinspection PyUnusedLocal
def final_jeopardy(game_info, player_info):
    from time import sleep
    # import threading
    if game_info[0] < 0:
        calculate_final_score(game_info, player_info)
    else:
        print(
            "\nThat's the end of the Jeopardy round. \nThe Final Jeopardy category is...")
        sleep(2)
        print("\nAmerican Universities. Make your wager, up to", game_info[0],
              "points:")
        wager = int(input())
        # countdown_timer = None
        final_answer = None
        if wager < game_info[0]:
            sleep(3)
            print(
                "\nThis Florida university was dubbed "'Dunk City'" when its basketball "
                "team made it to the sweet 16 during the 2013 NCAA tournament. \nGood luck, you have 30 seconds.")
            sleep(3)
            for seconds in range(30, 0, -1):
                sleep(1)
                while final_answer is None:
                    final_answer = input("Enter your answer: ").lower()
                break
            if "florida gulf" in final_answer or "fgcu" in final_answer:
                print(
                    "\nThat's right! Stay tuned to learn your final score.")
                game_info[0] += wager
                calculate_final_score(game_info, player_info)
            else:
                print(
                    "\nSorry, that's incorrect. We were looking for Florida Gulf Coast University.")
                game_info[0] -= wager
                calculate_final_score(game_info, player_info)
        else:
            print(
                "You are unable to wager more than you have. Try again!")
            print("\nAmerican Universities. Make your wager, up to",
                  game_info[0],
                  "points:")
            # noinspection PyUnusedLocal
            wager = int(input())
        return wager


def calculate_final_score(game_info, player_info):
    from time import sleep
    sleep(3)
    print("\nCongratulations,", player_info[0], ". You have finished this "
                                                "version of the Jeopardy! game!")
    final_score = float(game_info[0])
    bonus = player_info[1]
    if float(final_score) <= float(0):
        print("\nYou finished with", int(final_score),
              "points. You accrued ", int(bonus),
              " bonus points which gives you a final score of",
              int(final_score) + int(bonus),
              ". Better luck next time" + "." * 3)
        # * operator turns the single period into an ellipsis.
        print("\nThe game will terminate in 15 seconds.")
        sleep(15)
        exit()
    else:
        print("\nYou finished with", int(final_score), "points. Well done!")
        print("\nThe game will terminate in 15 seconds.")
        sleep(15)
        exit()


main()
