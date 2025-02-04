# Given a string of parentheses s, return the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
def complete_prantha(string):
    counter=0
    for i in string:
        if i =='(':
            counter+=1
        else:
            counter-=1
    return abs(counter)



