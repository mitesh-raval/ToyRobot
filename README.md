=================
Toy Robot Program
=================

How to run:
1) Open the directory where toyrobot.py is located (assuming it has been
   downloaded from provided source location) on command line console.
2) Execute the following at the command line prompt:
    python3 toyrobot.py
3) Enter commands on the console to exercise the toy robot.
4) First command must be a valid PLACE command of the form PLACE X,Y,F.
5) Following are other valid commands (case-insensitive):
    MOVE   : Moves the robot one square in F (Facing) direction
    LEFT   : Rotate F by 90 degrees to left e.g. NORTH changes to WEST
    RIGHT  : Rotate F by 90 degrees to right e.g. NORTH changes to EAST
    REPORT : Provides current values for X,Y,F e.g. 0,0,WEST
    END    : Ends the program gracefully

==================================
