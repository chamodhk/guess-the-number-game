from random import randrange


banner = ''' 
####################################################################################################
                                                                                                                    
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗███████╗███████╗███████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗██║   ██║█████╗  ███████╗███████╗
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝███████╗███████║███████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                                                    
############# a Game By chamodh ####################################################################
                                                                                                                         
                                                                       
'''

class Number():
    def __init__(self,level):
        self.level = level
        self.range = level*5
        self.number = randrange(self.range)


    def get_hints(self):
        hints = []
        #GET FIRST HINT
        hints.append("number is <= "+str(self.range))

        #GET SECOND HINT
        if self.level >=1:
            if self.number % 2 == 0:
                hints.append("Number is even")

            else:
                hints.append("Number is odd")
        else:
            pass

        #GET THIRD HINT
        if self.level >=3:
            if self.number % 3 == 0:
                hints.append("The Number can be divided by 3")
            else:
                hints.append("The Number cannot be divided by 3")

        else:
            pass

        #GET FOURTH HINT
        if self.level >=5:
            if self.number % 5 == 0:
                hints.append("The Number can be divided by 5")

            else:
                hints.append("The number cannot be divided by 5")
        else: 
            pass

        #GET FIFTH HINT
        if self.level >=6:
            param = round(self.range/2)
            if self.number > param:
                hints.append(f"Number is Highr than {param} ")
            else:
                hints.append(f"Number is <= {param}")

        else:
            pass




        return hints

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
                points += 15*level
                break
            else:
                points -= 5*level
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
            print("You Lost!\n\n Total points: "+str(points)+f"\n The chosen number was {number.number}\n\n")
            if input("Do you want to play again (y/n)?: ") == 'y':
                start()
            else:
                break

start()




