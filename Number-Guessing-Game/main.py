from cli import UI
from generator import Generator


def check(input:int,output:int):
    if(input == output):
        return True
    elif(input>output):
        print("Guess is High")
    else:
        print("Guess is low")
    return False


if __name__ == "__main__":
    ui = UI()


    while(1):
        ui.show_ui()

        level = int(input("Please select Level = "))
        generate = Generator(level)
        result = generate.generate_random()

        while(1):
            user_guess = int(input("Please guess a number = "))
            if(check(user_guess,result)):
                ui.ui_decorate("Congratulations you have won!!")
                break
        
        new_game = str(input("Do you want to play another round [Y/N] "))
        if(new_game.upper() == "Y"):
            continue
        else:
            break

