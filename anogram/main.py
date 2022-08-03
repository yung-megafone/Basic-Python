s1 = input('what\'s the first word?:\n')
s2 = input('what\'s the second word?:\n')
def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

are_anagrams()