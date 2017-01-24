import random

def naval():
    # This is the matrix where the ship will be hidden.
    matrix = []

    # Generate a 5x5 matrix with '0's (zeros) as elements and print it out so the user.
    # can see it.
    for x in range(5):
        matrix.append(["0"] * 5)
        print " ".join(matrix[x])

    # Create the random coordinates x,y of the ship location.
    ship_coor_x = random.randint(0, 4)
    ship_coor_y = random.randint(0, 4)
    #print ship_coor_x, ship_coor_y

    # This loop give the user 5 attempts to guess.
    for attempt in range(1, 6):
        # Ask the user to guess the x,y coordinates.
        if attempt < 5:
            user_coor_x = int(raw_input("Choose the x coordinate: "))
            user_coor_y = int(raw_input("Choose the y coordinate: "))

            if user_coor_x < 5 and user_coor_y < 5:
                # If the user guess the coordinates win the game.
                if user_coor_x == ship_coor_x and user_coor_y == ship_coor_y:
                    print "[+] Fuck, you sunk my ship in the ocean. Wins the game, congratulations!"
                    break
                # If any of the guessed coordinates are wrong...
                elif (user_coor_x != ship_coor_x) or (user_coor_y != ship_coor_y):
                    # See if the user already try those coordinates.
                    if matrix[user_coor_x][user_coor_y] == "X":
                        print "[-] Already choos those coordinates."
                    # Else, put an "X" in the choosen coordinates.
                    else:
                        matrix[user_coor_x][user_coor_y] = "X"
                        print "[-] You miss the shot. My ship still afloat."
                        # Print the matrix again so the user can see the "X"
                        for x in matrix:
                            print " ".join(x)
                    print attempt
            else:
                print "[+] Your coordinates must to be less than 5."
        else:
            print "[-] You already try 5 times, you loose the game."

while True:
    print "[+] If you want to play pres 1 (one), else pres 2 (two). "
    choose = raw_input(">>> ")
    if choose == "1":
        print "Welcome to Naval Battle. Try to sunk my ship."
        naval()
    else:
        print "Thanks for trying. Bye."
        break
