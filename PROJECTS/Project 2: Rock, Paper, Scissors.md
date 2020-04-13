
# Project 2: Rock, Paper, Scissors
 
## Assignment Overview
The purpose of this project is to familiarize you with the use of Boolean logic, branching statements and loops. For this assignment, you will create a program that plays the game “Rock, Paper, Scissors.”
 
 
## Background
Rock, Paper, Scissors (also known by several other names, see http://en.wikipedia.org/wiki/Rock_paper_scissors) is an extremely popular hand game most often played by children. Often, it is used as a method of selection similar to flipping a coin or throwing dice to randomly select a person for some purpose. Of course, this game is not truly random since a skilled player can often recognize and exploit the non-random behavior of an opponent; for instance, if you notice that your opponent chooses Paper most frequently, you may choose Scissors (which beats Paper) most often in an effort to win.
 
 
## Rules of the Game:
The objective of Rock, Paper, and Scissors is to defeat your opponent by selecting a weapon that defeats their choice under the following rules:
 
   - Rock smashes (or blunts) Scissors, so Rock wins
   - Scissors cut Paper, so Scissors win
   - Paper covers Rock, so Paper wins
   - If players choose the same weapon, neither win and the game is played again
 
## Program Specifications

This project requires you to use:

- input to prompt the user
- print to print results
- at least one branching mechanism (if statement)
- at least one loop (while loop)
- Boolean logic
 
<p>Your program will allow a human user to play Rock, Paper, Scissors with the computer.  Each round of the game will have the following structure:</p>
   
- The program will choose a weapon (Rock, Paper, Scissors), but its choice will not be displayed until later, so the user doesn’t see it.
- The program will announce the beginning of the round and ask the user for his/her weapon choice
- The two weapons will be compared to determine the winner (or a tie) and the results will be displayed by the program
- The next round will begin, and the game will continue until the user chooses to quit
- The computer will keep score and print the score when the game ends



<p>The computer should select the weapon most likely to beat the user, based on the user’s previous choice of weapons. For instance, if the user has selected Paper 3 times but Rock and Scissors only 1 time each, the computer should choose Scissors as the weapon most likely to beat Paper, which is the user’s most frequent choice so far. To accomplish this, your program must keep track of how often the user chooses each weapon. Note that you do not need to remember the order in which the weapons were used. Instead, you simply need to keep a count of how many times the user has selected each weapon (Rock, Paper or Scissors). Your program should then use this playing history (the count of how often each weapon has been selected by the user) to determine if the user currently has a preferred weapon; if so, the computer should select the weapon most likely to beat the users preferred weapon. During rounds when the user does not have a single preferred weapon, the computer may select any weapon. For instance, if the user has selected Rock and Paper 3 times each and Scissors only 1 time, or if the user has selected each of the weapons an equal number of times, then there is no single weapon that has been used most frequently by the user; in this case the computer may select any of the weapons.</p>
 
<p>At the beginning of the game, the user should be prompted for his/her input. The valid choices for input are:</p>
    
- R or r (Rock)
- P or p (Paper)
- S or s (Scissors)
- Q or q (Quit)
 
<p>At the beginning of each round your program should ask the user for an input. If the user inputs something other than r, R, p, P, s, S, q or Q, the program should detect the invalid entry and ask the user to make another choice.</p>
 
Your program should remember the game history (whether the user wins, the computer wins, or the round is tied).

- At the end of the game (when the user chooses `q` or `Q`), your program should display the following:    
- The number of rounds the computer has won
- The number of rounds the user has won
- The number of rounds that ended in a tie
- The number of times the user selected each weapon (Rock, Paper, Scissors)
 
## Deliverables
You must turn in a file called proj02.py – this is your source code solution; be sure to include your names, the project number and comments describing your code.
 
## Assignment Notes
1. input should be used for prompting. It returns a string containing the user’s choice.
2. There is a string method called lower. It converts the string to all characters to lower case. This might prove helpful for user input checking.
 
 
## Getting Started
1. Do all the standard startup things. Create a new file called proj02.py. Put your comments in at the top, save it.
2. Now you need to break the problem down into parts. Read the description and identify the subtasks that need to be solved. For example, one subtask would be to get proper user input. Mark in the empty program, using comments, all the subtasks you need to solve.
3. Now address one subtask, getting user input. Do this in stages as well. Can you:
  a. Prompt for and get a choice (a string) from the user?
  b. Once you can do that, can you repeatedly prompt for a character until you see a ‘q’ or ‘Q’ for quit?
  c. Once you can do that, can you check for “legal” character responses from the user, and print an error message when an illegal response is given?
  d. Next, can you check for legal responses that are in both upper and lower case?
   Once you can do all that, move on to the next subtask.
4. Remember, save the file and run it all the time! It will make debugging the program easier.
 
 
> Credit: This project was developed by Michigan State University Professors William Punch and Richard Enbody and is being used under the Creative Commons Attribution-Share Alike 3.0 United States License from the CS1 Python Programming Project Archive.

### :neckbeard: Programming Language: PYTHON
```python
import random

random.seed()

player_weapon = 'r'
computer_weapon = 'r'
keep_playing = 'y'
rock_played = 0
paper_played = 0
scissors_played = 0
weapon_valid = False
tie_score = 0
computer_score = 0
player_score = 0

while keep_playing != 'q':
    
    # Weapon choice
    while weapon_valid == False:
        print('Please choose your weapon: (r)ock, (p)aper or (s)cissor\n')
        player_weapon = input().lower()

        # Weapon validation
        if (player_weapon != ('r')) and (player_weapon != ('p')) and (player_weapon != ('s')):
            print('You have choosen an invalid weapon, please type again\n')
        else:
            weapon_valid = True
    
    # Reset weapon validation flag
    weapon_valid = False

    # Computer weapon choice
    if (rock_played > paper_played) and (rock_played > scissors_played):
        computer_weapon = 'p'
    elif (paper_played > rock_played) and (paper_played > scissors_played):
        computer_weapon = 's'
    elif (scissors_played > rock_played) and (scissors_played > paper_played):
        computer_weapon = 'r'
    elif (rock_played == paper_played) and (rock_played > scissors_played):
        computer_weapon = random.choice(['p','s'])
    elif (scissors_played == rock_played) and (scissors_played > paper_played):
        computer_weapon = random.choice(['r','p'])
    elif (scissors_played == paper_played) and (scissors_played > rock_played):
        computer_weapon = random.choice(['r','s'])        
    else:
        computer_weapon = random.choice(['r','p','s'])

    # Update weapon counter
    if (player_weapon == 'r'):
        rock_played += 1
    elif (player_weapon == 'p'):
        paper_played += 1
    else:
        scissors_played += 1

    # Show the weapons
    if (player_weapon == 'r'):
        print('You have choosen rock')
    # Needs to be finished

    # Show the result
    if (player_weapon == computer_weapon):
        print('This round is a tie!')
        tie_score += 1
    elif ((player_weapon == 'r') and (computer_weapon == 's')) or ((player_weapon == 'p') and (computer_weapon == 'r')) or ((player_weapon == 's') and (computer_weapon == 'p')):
        print('You win this round!')
        player_score += 1
    else:
        print('The computer wins this round!')
        computer_score += 1

    # Keep playing?
    print("Do you want to keep playing? If you don't want, type 'q':\n")
    keep_playing = input().lower()

print('Here is the final score:')
print('Tie: ' + str(tie_score))
print('Won: ' + str(player_score))
print('Lost: ' + str(computer_score))
print('Rocks played: ' + str(rock_played))
print('Papers played: ' + str(paper_played))
print('Scissors played: ' + str(scissors_played))
print('Thank you for playing!\n')
```

