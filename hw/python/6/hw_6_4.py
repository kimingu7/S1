import collections
str = ['eat','tea','tan','ate','nat','bat']
def group_anagrams(str):
    anagrams = collections.defaultdict(list)
    for word in str:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
print(group_anagrams(str))