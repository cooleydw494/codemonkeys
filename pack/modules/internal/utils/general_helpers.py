import Levenshtein


def levenshtein_distance(str1, str2):

    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)