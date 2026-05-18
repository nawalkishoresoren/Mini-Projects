#main.py
from calculate import Calculate
from cli import UI


if __name__ == "__main__":
    #start UI create an object for UI.
    ui = UI()

    while True:
        ui.show_ui()

        method = int(input("Choose you operation = "))

        if(method == 5):
            exit()

        num1 = int(input("Provide first number = "))
        num2 = int(input("Provide second number = "))

        calculator = Calculate(num1,num2)

        #operation mapping
        operation = {
            1 : calculator.add,
            2 : calculator.substrat,
            3 : calculator.multiply,
            4 : calculator.divide
        }

        #prints the answer.
        ui.decorate(operation[method]())

            
