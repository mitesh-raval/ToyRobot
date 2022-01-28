#!/usr/bin/env python3

def printPrompt():
    print("## ", end='')

def printWelcomeMsg():
    print("## ", "TOY ROBOT: Please start with a PLACE command.\n")

''' As (0,0) is the SOUTH WEST most corner and robot will be moving
    along the edges, valid points for an axis of length n are
    [0,1,2...n] '''
''' range(n) == (0...n-1) inclusive, hence for 5x5 dimension board, n=6 '''
MAX = {'X':6,'Y':6}

def ValidPlaceCmd(cmd, argsDict):
    ''' ValidPlaceCmd() : Accepts string 'cmd' and for any valid PLACE cmd
        (with valid arguments) populates X,Y,F (X,Y coordinates and F 
        direction) in 'argsDict' and returns True, else returns False ''' 
    if not cmd.startswith('PLACE '):
        return False
    args = cmd.split(' ')[1].split(',')
    if '' in args or len(args) != 3:
        return False
    argsDict['X'] = int(args[0])
    argsDict['Y'] = int(args[1])
    argsDict['F'] = str(args[2])
    if argsDict['F'] not in ['NORTH','SOUTH','EAST','WEST']:
        return False
    if argsDict['X'] not in range(MAX['X']) or \
       argsDict['Y'] not in range(MAX['Y']):
        return False
    return True

''' Global dictionaries to rotate the robot 90 degrees '''
LEFT = {'NORTH':'WEST','EAST':'NORTH','SOUTH':'EAST','WEST':'SOUTH'}
RIGHT = {'NORTH':'EAST','EAST':'SOUTH','SOUTH':'WEST','WEST':'NORTH'}

''' Global dictionaries to move the robot one unit in appropriate dimension '''
MOVES = {'NORTH':1,'SOUTH':-1,'WEST':-1,'EAST':1}
DIM = {'NORTH':'Y','SOUTH':'Y','WEST':'X','EAST':'X'}

def Execute(cmd, currPos):
    ''' Executes valid 'cmd' strings and updates dictionary 'currPos' 
        (current position) with new X,Y or F '''
    if ValidPlaceCmd(cmd, currPos):
        return

    elif cmd == 'MOVE':
        F = currPos['F']
        ''' calculate 'newPos' (newPosition) and if within valid range
            update appropriate dimension within 'currPos' with 'newPos' '''
        newPos = currPos[DIM[F]] + MOVES[F]
        if newPos in range(MAX[DIM[F]]):
            currPos[DIM[F]] = newPos
        return

    elif cmd == 'LEFT':
        currPos['F'] = LEFT[currPos['F']]
        return
    
    elif cmd == 'RIGHT':
        currPos['F'] = RIGHT[currPos['F']]
        return
    
    elif cmd == 'REPORT':
        print(f"{currPos['X']},{currPos['Y']},{currPos['F']}")    
        return
    
    else:
        return

def GetCommand():
    return input().strip().upper()

######################################################
# Program flow begins here, ask user for input
######################################################
def main() : 
    printWelcomeMsg()
    printPrompt()
    currentPos = {}   # empty dictionary for keeping track of current position
    cmd = GetCommand()     # store input from console

    ''' First command must be a valid PLACE cmd '''
    while not ValidPlaceCmd(cmd, currentPos) :
        printPrompt()
        cmd = GetCommand()
    
    ''' After a valid PLACE cmd execute other commands. 
        'END' cmd terminates the program '''
    while cmd != 'END':
        printPrompt()
        cmd = GetCommand()
        Execute(cmd, currentPos)
        
main()