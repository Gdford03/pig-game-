'''
Garrett Langford
Brief description of the code for other programmers

I certify that this code is mine, and mine alone, in accordance with GVSU academic honesty policy.

10/23/2023
'''

import random


def validate_response(prompt, response_1, response_2):
    while True:

        # prints prompt
        print(f'{prompt}', end=" ")
        #  checks if responses are true
        if response_1 == 't' or response_2 == 't':
            return True
        # checks if responeses are false
        if response_1 == 'f' or response_2 == 'f':
            return False

        # if responses are neither true or false then tells user what response needs to be and continues
        else:
            print("Oops must be (t/f)")
            response_1 = input()
            response_2 = input()
            continue



def roll_dice():

    # represents the two six sided dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def computer_turn(game_score, goal):
    turn_total = 0

    # while loop is a design requirement  that repeats unless one of the if elif statements return a value
    while True:
        dice1, dice2 = roll_dice()
        turn_total += dice2 + dice1

        # checks if you rolled a double 1 and returns the new game score
        if dice1 == 1 and dice2 == 1:
            print(f'computer rolled {dice1}, {dice2} , and loss all points')
            return 0

        # checks is either dice is a 1 to see if you lose your points for this turn
        elif dice1 == 1 or dice2 == 1:
            print(f'computer rolled {dice1}, {dice2} , and losses turn')
            return game_score

        # checks if the computer needs to roll again or of it reached the goal
        if turn_total >= goal:
            print(f'Computer rolled {dice1},{dice2} Turn total: {turn_total}')
            game_score += turn_total
            return game_score

        # prints if turn total is less than goal
        else:
            print(f'Computer rolled {dice1},{dice2} Turn total: {turn_total}')
            continue


def human_turn(game_score):
    user_turn = 0

    # while is a design requirement for this definition but is similar to the computer
    # turn but only keeps rolling if the human wants too.
    while True:
        dice1, dice2 = roll_dice()
        user_turn += dice1 + dice2

        # checks if you rolled a double returns new game score
        if dice1 == 1 and dice2 == 1:
            print(f'You rolled {dice1}, {dice2} , and loss all points')
            return 0

        # check if you lose your turn or not
        elif dice1 == 1 or dice2 == 1:
            print(f'You rolled {dice1}, {dice2} , and losses turn')
            return game_score

        # if you pass and didn't roll a one it prints the score and ask if you want to roll again
        print(f"You rolled {dice1},{dice2}, Turn total: {user_turn}")
        print("Roll again (y/n)?")
        yes_no = input()

        # loop will keep going on if y is the input and if n is the input it adds turn total to your game score
        if yes_no == 'y':
            continue
        elif yes_no == 'n':
            game_score += user_turn
            return game_score


def human_vs_computer():
    human_score = 0
    computer_score = 0
    goal = 20

    # lets the human roll fist and then check if you won then lets the computer go and checks if it won
    while True:
        print(f'You: {human_score} Computer: {computer_score}')
        human_score = human_turn(human_score)

        # checks human score to see if you won
        if human_score >= 100:
            print(f'You: {human_score} Computer: {computer_score}')
            return print('Congratulations!')
        computer_score = computer_turn(computer_score, goal)

        # checks if computer won
        if computer_score >= 100:
            print(f'You: {human_score} Computer: {computer_score}')
            return print("you Lose")


def computer_solo(goal):
    computer_total = 0
    turn = 0

    # adds to turn before the scomputer goes so it starts at 1
    while True:
        turn += 1
        computer_total = computer_turn(computer_total, goal)

        # checks if computer won if not it keeps going and adds to turn each time
        if computer_total >= 100:
            print(f"Turn: {turn} Score: {computer_total}")
            return turn


def world_championship(games, goal_1, goal_2):
    player1_wins = 0
    player2_wins = 0

    # for nums in range of games it does each game until the games are reached
    for i in range(games):
        player1 = 0
        player2 = 0
        # use this while loop for each individual game
        while True:
            player1 = computer_turn(player1, goal_1)
            player2 = computer_turn(player2, goal_2)

            # checks if both players are above 100 this goes first because it needs both to be over 100
            # and if the individual player go then it's not going to check both
            if player1 >= 100 and player2 >= 100:

                # checks if player 1 has more points than player 2 after its over 100 and stops the while loop to rest
                if player1 > player2:
                    player1_wins += 1
                    break

                # does the same thing but for player 2 and stops the while loop to rest
                elif player1 < player2:
                    player2_wins += 1
                    break

            # checks if player 1 has won and stops the while loop to rest
            elif player1 >= 100:
                player1_wins += 1
                break

            # checks if player 2 won and stops the while loop to rest
            elif player2 >= 100:
                player2_wins += 1
                break

    # after the for loop is done prints the score and returns each players wins
    print(f"Alexa: {player1_wins} wins Siri: {player2_wins} wins")
    return player1_wins, player2_wins


# added for teacher testing
if __name__ == '__main__':
    pass
    # human_vs_computer()
    # human_turn(10)
    # validate_response("Does this work (t/f)?",'t','f')