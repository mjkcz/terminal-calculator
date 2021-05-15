import time
class Colours:
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    default = '\033[0m'

print(f"{Colours.green}Welcome to {Colours.red}Terminal Calculator 1.0! {Colours.default} ")
print(" ")

while True:
    
    command = input(f"{Colours.green}Please enter your command. {Colours.yellow}(calc, quit){Colours.default} >> ")
    
    if command == "calc":
        firstDigit = int(input(f"{Colours.green}Please enter your{Colours.red} first digit.{Colours.default} >> "))
        operator = int(input(f"{Colours.green}Please enter the{Colours.red} operator. {Colours.yellow}(1 for +, 2 for -, 3 for ×, 4 for ÷){Colours.default} >> "))

        
        if operator == 1:
            operatorSymbol = "+"
            secondDigit = int(input(f"{Colours.green}Please enter your{Colours.red} second digit. {Colours.default} >> "))
            print(f"{Colours.green}Result:{Colours.red}", firstDigit, "+", secondDigit, "=", firstDigit+secondDigit)
            
        elif operator == 2:
            operatorSymbol = "-"
            secondDigit = int(input(f"{Colours.green}Please enter your{Colours.red} second digit. {Colours.default} >> "))
            print(f"{Colours.green}Result:{Colours.red}", firstDigit, "-", secondDigit, "=", firstDigit-secondDigit)
            
        elif operator == 3:
            operatorSymbol = "×"
            secondDigit = int(input(f"{Colours.green}Please enter your{Colours.red} second digit. {Colours.default} >> "))
            print(f"{Colours.green}Result:{Colours.red}", firstDigit, "×", secondDigit, "=", firstDigit * secondDigit)
            
        elif operator == 4:
            operatorSymbol = "÷"
            secondDigit = int(input(f"{Colours.green}Please enter your{Colours.red} second digit. {Colours.default} >> "))
            print(f"{Colours.green}Result:{Colours.red}", firstDigit, "÷", secondDigit, "=", firstDigit / secondDigit)
            
        else:
            print(f"{Colours.red}Invalid operator.{Colours.default}")

    elif command == "quit":
        break
        
    else:
        print(f"{colours.green}This command is {colours.red}invalid. {colours.yellow}Valid commands: calc, quit.{colours.default}")
