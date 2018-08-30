#function to count number of vowels in the string and return their duplicates
def vowels(word):
    new_word = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    for x in word:
        if x in vowel:
           new_word.append(x)
           count = new_word.count(x)
           if count > 1:
               new_word.pop(1)
               count = count-1
               return new_word, count

    return new_word

#display new list
word = "edahdah"
print (vowels(word))