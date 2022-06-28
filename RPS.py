    
patterns_occurrence = {} # creates a dictionary to store how many times each pattern happened

def player(prev_play, opponent_history=[]):
   
    if (prev_play) != False:
        opponent_history.append(prev_play)

    n=3 # number of plays to play randomly initially until we get a pattern, 
        # also the size of patterns that we will be looking for

    hist = opponent_history
    
    guess = 'R'

    if len(hist) > n:
       
        pattern = "".join(hist[-n:]) # save the last n plays as a pattern in a string 

        pattern_2 = "".join(hist[-(n + 1):]) # save the last n+1 plays as a pattern in a string

        if pattern_2 in patterns_occurrence.keys(): # if last n+1 plays are in patterns keys, add a counter to it
            patterns_occurrence[pattern_2] += 1
        
        else:                                    #else add it to the patterns dictionary and set initial value as 1
            patterns_occurrence[pattern_2] = 1 

        possibilities = [pattern + 'R', pattern + 'P', pattern + 'S'] #create a list of 3 possible pattern + play

        for i in possibilities:
            if not i in patterns_occurrence.keys():    #if the pattern + possibility is not in the pattern dictionary keys
                patterns_occurrence[i] = 0             #set the value of the pattern to 0

        predict = max(possibilities, key = lambda key: patterns_occurrence[key]) # get the possibility with the max pattern values, that which ocurred the most

        #print (predict)
        
        if predict[-1] == 'R':
            guess = 'P'
        if predict[-1] == 'P':
            guess = 'S'
        if predict[-1] == 'S':
            guess = 'R'
        
    
    return guess
