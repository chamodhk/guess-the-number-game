from random import randrange


banner = '''                       __        ___ _  _                    
   ____  __  ______ ___  / /_  ___  _____   / ______  _____  __________
  / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/
 / / / / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  (__  ) 
/_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/  
                                                                       
'''

class Number():
    def __init__(self,level):
        self.range = level*5
        self.number = randrange(self.range)

    def first_hint(self):
        return "number is <= "+str(self.range)

    def second_hint(self):
        if self.number % 2 == 0:
            return "Number is even"

        else:
            return "Number is odd"

    def third_hint(self):
        param = round(self.range/2)
        if self.number > param:
            return f"Number is Highr than {param} "
        else:
            return f"Number is <= {param}"

    def fourth_hint(self):
        if self.number % 5 == 0:
            return "The Number can be divided by 5"

        else:
            return "The number cannot be divided by 5"


    def get_hints(self):
        return [self.first_hint(),
                self.second_hint(),
                self.third_hint(),
                self.fourth_hint()]

def handle_input(hint,number):
    trial = int(input("Try! ----"+ hint+" : "))
    if trial == number.number:
        return True
    else:
        return False



def start():
    print(banner)
    print("""Welocme to Number Guess-The Game\nThe Computer has chosen a number\nYou have to guess the number with the help of the hints provided\nIf you fail you are given another hint and your points will be reduced by 5 \n""")

    level=1
    points = 15

    while True:

        print(f'\nLEVEL: {level}\n')

        
        number = Number(level)
        hints= number.get_hints()

    
        

        won = False
        for hint in hints:
            if handle_input(hint,number):
                won = True
                points += 15
                break
            else:
                points -= 5
                print("You're wrong! Try Again\n")
        

        if won:
            print("""
            Congratulations!!! You Won the Game
            You earned """+str(points)+' points\n\n')

            if input('Want to go the next level (y/n) ?: ') =='n':

                print('''GOOD BYE\n
                    points earned: '''+str(points)+'!\n')
                break

            else:
                print("\ngoing to next level...........\n")
                level +=1
        else:
            print("You Lost!\n\n Total points: "+str(points)+"\n")
            break

start()




