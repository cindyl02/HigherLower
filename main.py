from art import logo, vs
from game_data import data
import random
from utils import clear_screen


def get_random_account():
    """
    Returns a random account from list of accounts
    :return: an account dict
    """
    return random.choice(data)


def get_formatted_description(acc):
    """
    Returns a formatted string containing account name, description and country
    :param acc: account
    :return: formatted string with the account name, description and country
    """
    return f"{acc['name']}, a {acc['description']}, from {acc['country']}."


def check_answer(user_guess, a_follower_count, b_follower_count):
    """
    Takes a user guess and compares it with two accounts' followers count to check if user has correctly guessed the higher following account
    :param user_guess: string representing the guess for which account has a higher following count
    :param a_follower_count: number of followers account has
    :param b_follower_count: number of followers other account has
    :return: True if the user guess the correct account that has more followers. Otherwise, returns False.
    """
    if a_follower_count == b_follower_count:
        return True
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"


def start_game():
    should_continue = True
    score = 0
    second_option = get_random_account()
    while should_continue:
        print(logo)
        first_option = second_option
        second_option = get_random_account()
        while first_option == second_option:
            second_option = get_random_account()
        print(f"Compare A: {get_formatted_description(first_option)}")
        print(vs)
        print(f"Against B: {get_formatted_description(second_option)}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if check_answer(user_guess, first_option["follower_count"], second_option["follower_count"]):
            clear_screen()
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return


if __name__ == '__main__':
    start_game()
