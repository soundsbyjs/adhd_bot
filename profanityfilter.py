# read in an array of strings, for loop it, replace with 
# family friendly language lnao
# uses many tik tok conventions such as "unalive" for "kill"

def censor(words):
    profanity_dict = {
        "fuck": "f",
        "fucking": "fucked",
        "fucked": "effed",
        "shit": "poop",
        "shitting": "pooping",
        "shits": "craps",
        "bitch": "b-word",
        "bitches": "b-words",
        "bitching": "b-wording",
        "cunt": "see you next tuesday",
        "cock": "weiner",
        "cocks": "weiners",
        "cocksucker": "chickenhead",
        "motherfuck": "mf",
        "motherfucker": "mf",
        "tit": "breast",
        "tits": "breasts",
        "cunt": "see you next tuesday",
        "kill": "unalive",
        "kys": "unalive yourself",
        "sex": "s-eggs",
        # Add more words as needed
    }

    censored_words = []
    for word in words:
        lower_word = word.lower()
        if lower_word in profanity_dict:
            censored_words.append(profanity_dict[lower_word])
        else:
            censored_words.append(word)

    return censored_words
