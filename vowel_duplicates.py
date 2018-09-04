#function to count number of vowels in the string and return their duplicates
def vowels(word):
    new_word = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    #get number of duplicates using set function
    duplicates = len(word) - len(set(word))

    for x in set(word):
        if x in vowel and x not in new_word:
           new_word.append(x)
        else:
           continue
    new_string_word = new_word = "".join(new_word)
    return new_string_word, duplicates

#display new list
print (vowels("edahdah"))
print (vowels("drink water"))