# read in an array of strings, for loop it, replace with 
# family friendly language lnao
# uses many tik tok conventions such as "unalive" for "kill"
def censor(words):
    for word in words:
        if word == "fuck": 
            word = "f"
        if word == "fucking": 
            word = "fucked"
        if word == "fucked": 
            word = "effed" 
        if word == "shit": 
            word = "poop"
        if word == "shitting": 
            word = "pooping"
        # as in, couldn't give two shits!
        # as you can tell this is a *lot* of anticipation
        if word == "shits": 
            word = "craps"
        if word == "bitch": 
            word = "b-word"
        if word == "bitches": 
            word = "b-words"
        if word == "bitching": 
            word = "b-wording"
        if word == "cunt":
            word = "see you next tuesday"
        if word == "cock":
            word = "weiner"
        if word == "cocks":
            word = "weiner"
            # "a fallatious woman... er, person!"
        if word == "cocksucker":
            word = "chickenhead"
        if word == "motherfucker":
            word = "mf"
        if word == "tit":
            word = "breast"
        if word == "tits":
            word = "breasts"
        if word == "":
            word = "see you next tuesday"
        if word == "kill": 
            word = "unalive"
        if word == "kys": 
            word = "unalive yourself"

        # what do I do about racial slurs?
