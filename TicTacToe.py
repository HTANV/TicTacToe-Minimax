# Function in this Code Represents and initializes the Panel where the TicTacToe is Played
def TicTacToe(Panel):
#3x3 TicTacToe Panel
    print(Panel[1] + ' || ' + Panel[2] + ' || ' + Panel[3])
    print('===========')
    print(Panel[4] + ' || ' + Panel[5] + ' || ' + Panel[6])
    print('===========')
    print(Panel[7] + ' || ' + Panel[8] + ' || ' + Panel[9])
    print("\n")

# This Code Show user the numbers to use for putting value in Game Panel
Panel = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# This fuction checks if there is free space in the 3x3 Panel.
def FreeSpaceInGrid(pos):
    if Panel[pos] == ' ':
        return True
    else:
        return False

#Function to check available spaces in Grid. This also shows who wins the game!
def PutSign(letter, pos):
#If there is free space in Grid, the Sign is placed else there will be error message displayed
    if FreeSpaceInGrid(pos):
        Panel[pos] = letter
        TicTacToe(Panel)
        if (checkDraw()):
            print("The Game is Draw!")
            exit()
        if WinnerCheck():
            if letter == 'X':
                print("Computer Bot Won!")
                exit()
            else:
                print("Player Won. Congrats!")
                exit()

        return


    else:
        print("Unable to Insert There!")
        pos = int(input("Enter the New Position:  "))
        PutSign(letter, pos)
        return

#Fucntion to check in vertical, horizontal, diagonal positions that who has won!
def WinnerCheck():
    if (Panel[1] == Panel[2] and Panel[1] == Panel[3] and Panel[1] != ' '):
        return True
    elif (Panel[4] == Panel[5] and Panel[4] == Panel[6] and Panel[4] != ' '):
        return True
    elif (Panel[7] == Panel[8] and Panel[7] == Panel[9] and Panel[7] != ' '):
        return True
    elif (Panel[1] == Panel[4] and Panel[1] == Panel[7] and Panel[1] != ' '):
        return True
    elif (Panel[2] == Panel[5] and Panel[2] == Panel[8] and Panel[2] != ' '):
        return True
    elif (Panel[3] == Panel[6] and Panel[3] == Panel[9] and Panel[3] != ' '):
        return True
    elif (Panel[1] == Panel[5] and Panel[1] == Panel[9] and Panel[1] != ' '):
        return True
    elif (Panel[7] == Panel[5] and Panel[7] == Panel[3] and Panel[7] != ' '):
        return True
    else:
        return False

#Function to check which Sign has won
def WinnerSignCheck(Sign):
    if Panel[1] == Panel[2] and Panel[1] == Panel[3] and Panel[1] == Sign:
        return True
    elif (Panel[4] == Panel[5] and Panel[4] == Panel[6] and Panel[4] == Sign):
        return True
    elif (Panel[7] == Panel[8] and Panel[7] == Panel[9] and Panel[7] == Sign):
        return True
    elif (Panel[1] == Panel[4] and Panel[1] == Panel[7] and Panel[1] == Sign):
        return True
    elif (Panel[2] == Panel[5] and Panel[2] == Panel[8] and Panel[2] == Sign):
        return True
    elif (Panel[3] == Panel[6] and Panel[3] == Panel[9] and Panel[3] == Sign):
        return True
    elif (Panel[1] == Panel[5] and Panel[1] == Panel[9] and Panel[1] == Sign):
        return True
    elif (Panel[7] == Panel[5] and Panel[7] == Panel[3] and Panel[7] == Sign):
        return True
    else:
        return False


#Take playerInput and inserts it
def PlayerInput():
    pos = int(input("Enter the pos for 'O':  "))
    PutSign(player, pos)
    return


def ComputerInput():
#We have to maximize the score, so we start with low score
    TopScore = -900
    TopMove = 0
#Represents each possible move
    for key in Panel.keys():
        if (Panel[key] == ' '):
            Panel[key] = bot
            score = MiniMaxFunction(Panel, 0, False)
            Panel[key] = ' '
            if (score > TopScore):
                TopScore = score
                TopMove = key
#Finds the best move and put it in the Grid
    PutSign(bot, TopMove)
    return

#To check if the game is draw or not
def checkDraw():
    for key in Panel.keys():
        if (Panel[key] == ' '):
            return False
    return True


def MiniMaxFunction(Panel, depth, isMaximizing):
    if (WinnerSignCheck(bot)):
        return 1
    elif (WinnerSignCheck(player)):
        return -1
    elif (checkDraw()):
        return 0

#Find Top Score. Maximizing
    if (isMaximizing):
        TopScore = -900
        for key in Panel.keys():
            if (Panel[key] == ' '):
                Panel[key] = bot
                score = MiniMaxFunction(Panel, depth + 1, False)
                Panel[key] = ' '
                if (score > TopScore):
                    TopScore = score
        return TopScore
#Find Top Score. Minimizing
    else:
        TopScore = 900
        for key in Panel.keys():
            if (Panel[key] == ' '):
                Panel[key] = player
                score = MiniMaxFunction(Panel, depth + 1, True)
                Panel[key] = ' '
                if (score < TopScore):
                    TopScore = score
        return TopScore



TicTacToe(Panel)
print("Computer Bot's Turn First!")
print("Use the following numbers for positions:")
print("1, 2, 3, 4, 5, 6, 7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not WinnerCheck():
    ComputerInput()
    PlayerInput()