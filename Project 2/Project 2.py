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