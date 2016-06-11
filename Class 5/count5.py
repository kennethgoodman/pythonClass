def count_fives(number):
    if number < 5: # base case
        return 0
    else:
        return 1 + count_fives(number - 5) 