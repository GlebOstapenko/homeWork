from game_func_rules import get_choice, get_computer_choice, check_winner

if __name__ == '__main__':
    user_choice = get_choice("user")
    computer_choice = get_computer_choice()
    check_winner(user_choice, computer_choice)
