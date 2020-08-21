'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
     # We have to remove all instances of words that have less than two characters.
    if len(word) < 2:
        return 0


    # If the first 2 indicies are th then we add 1 and move to the next index
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])

    # Otherwise, we will just start at the next index
    else:
        return count_th(word[1:])
