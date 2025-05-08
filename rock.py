import random

print("Welcome to Rock, Paper, Scissors! Best of 3 rounds.")

player_score = 0
bot_score = 0

for round_num in range(1, 4):
    print(f"\nRound {round_num}:")
    play1 = str(input("Rock, Paper, or Scissors? ")).capitalize()
    play2 = random.randint(1, 3)

    if play2 == 1:
        play2 = "Rock"
    elif play2 == 2:
        play2 = "Paper"
    elif play2 == 3:
        play2 = "Scissors"

    print("Bot:", play2)

    if play1 == play2:
        print("It's a tie!")
    elif (play1 == "Rock" and play2 == "Scissors") or (play1 == "Paper" and play2 == "Rock") or (play1 == "Scissors" and play2 == "Paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Bot wins this round!")
        bot_score += 1

print("\nFinal Scores:")
print(f"You: {player_score}")
print(f"Bot: {bot_score}")

if player_score > bot_score:
    print("Congratulations! You win the game!")
elif player_score < bot_score:
    print("The bot wins the game! Better luck next time.")
else:
    print("It's a tie game!")