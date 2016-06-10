def count_fives(number):
    if number < 5: # base case
        return 0
    elif number == 5:
        return 1 
    else:
        return 1 + count_fives(number - 5) 