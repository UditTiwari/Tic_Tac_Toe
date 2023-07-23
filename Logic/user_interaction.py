game_list = [0,1,2]

def display_game(game_list):
    print("Here is the cureent list :")
    print(game_list)
    
    
# print(game_list)



def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a postion(0,1,2) ")
        if choice not in ['0','1','2']:
            print("Sorry ,ivalid choice!")
    
    return int(choice)


# position_choice()


def replacement_choice(game_list,position):
    user_placement = input("TYPE A STRING TO PLACE AT POSTION : ")
    game_list[position] = user_placement
    
    return game_list


# print(replacement_choice(game_list,1))


def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Keep Playing ? (Y OR N) ")
        if choice not in ['Y','N']:
            print("Sorry ,I dont understand ,please select Y or N")
            
    if choice == 'Y':
        return True
    else:
        return False
    
    
# print(gameon_choice())


game_on = True
game_list = [0,1,2]

while game_on:
    #print the curent list
    display_game(game_list)
    
    #asking in which index u want to insert 
    position = position_choice()
    
    #passing list and index in whihc they need to insert and then input what to insert
    game_list = replacement_choice(game_list,position)
    
    #display the updated list
    display_game(game_list)
    
    #check that players still want to play or not
    game_on = gameon_choice()