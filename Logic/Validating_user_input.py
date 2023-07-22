def user_choice():
    
    #Initial
    choice ='wrong'
    acceptable_range = range(0,10)
    within_range = False
    
    #Two Conditon to check
    #DIGIT OR WITHIN_RANGE == FALSE
    
    #mkaing sure that it enter digit nothing else
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10) :")
        
        #DIGIT CHECK
        if choice.isdigit() ==False:
            print("Sorry that is not a digit")
        
        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Not in the Range(0-10)")
                within_range = False
    
    return int(choice)


print(user_choice())



    