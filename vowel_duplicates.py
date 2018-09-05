#function to count number of vowels in the string and return their duplicates
def vowels(word):
    #vowels set
    vowel = set("aeiou")

    #word without duplicates
    word_set = set(word)

    #get number of duplicates using set function
    duplicates = len(word) - len(word_set)

    #get the vowels in the word
    new_word = word_set.intersection(vowel)
    
    #change new_word to a string
    new_string_word = new_word = "".join(new_word)

    return new_string_word, duplicates

#display new list
print (vowels("edahdah"))
print (vowels("drink water"))