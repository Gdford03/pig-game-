import random

dice1 = 0
dice2 = 0


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2
def computer_turn(game_score, goal):
    turn_total = 0
    while True:
        dice1, dice2 = roll_dice()
        turn_total += dice2 + dice1
        print(f'Computer rolled {dice1},{dice2} Turn total: {turn_total}')
        if dice1 == 1 and dice2 == 1:
            print(f'computer rolled {dice1}, {dice2} , and loss all points')
            return 0
        elif dice1 == 1 or dice2 == 1:
            print(f'computer rolled {dice1}, {dice2} , and losses turn')
            return game_score
        if turn_total >= goal:
            game_score += turn_total
            return game_score
def human_turn(game_score):
    user_turn = 0
    while True:
        dice1, dice2 = roll_dice()
        user_turn += dice1 + dice2
        if dice1 == 1 and dice2 == 1:
            print(f'You rolled {dice1}, {dice2} , and loss all points')
            return 0
        elif dice1 == 1 or dice2 == 1:
            print(f'You rolled {dice1}, {dice2} , and losses turn')
            return game_score
        print(f"You rolled {dice1},{dice2}, Turn total: {user_turn}")
        print("Roll again (y/n)?")
        yes_no = input()
        if yes_no == 'y':
            continue
        elif yes_no == 'n':
            game_score += user_turn
            return game_score
def human_vs_computer():
    human_score = 0
    computer_score = 0
    goal = 20
    while True:
        print(f'You: {human_score} Computer: {computer_score}')
        human_score = human_turn(human_score)
        if human_score >= 100:
            print(f'You: {human_score} Computer: {computer_score}')
            return print('Congratulations!')
        computer_score = computer_turn(computer_score, goal)
        if computer_score >= 100:
            print(f'You: {human_score} Computer: {computer_score}')
            return print("you Lose")
def computer_solo(goal):
    computer_total = 0
    turn = 0
    while True:
        turn += 1
        computer_total = computer_turn(computer_total, goal)
        if computer_total >= 100:
            print(f"Turn: {turn} Score: {computer_total}")
            return turn
# if __name__ == '__main__':
# computer_solo(20)
def world_championship(games, goal_1, goal_2):
    computer_1_wins = 0
    computer_2_wins = 0
    computer1 = 0
    computer2 = 0
    for total_games in range(games+1):
        computer1 = computer_turn(computer1, goal_1)
        computer2 = computer_turn(computer2, goal_2)
        if computer1 >= 100 and computer2 >= 100:
            if computer1 > computer2:
                computer1 = 0
                computer2 = 0
                computer_1_wins += 1
            elif computer1 < computer2:
                computer1 = 0
                computer2 = 0
                computer_2_wins += 1
        elif computer1 > computer2:
            computer1 = 0
            computer2 = 0
            computer_1_wins += 1
        elif computer1 < computer2:
            computer1 = 0
            computer2 = 0
            computer_2_wins += 1
    if computer_1_wins > computer_2_wins:
        print(f"Alexa: {computer_1_wins} wins Siri: {computer_2_wins} wins")
        return computer_1_wins
    elif computer_1_wins < computer_2_wins:
        print(f"Alexa: {computer_1_wins} wins Siri: {computer_2_wins} wins")
        return computer_2_wins


if __name__ == '__main__':
    human_vs_computer()