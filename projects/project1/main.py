from game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        result = game.play_round()
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
