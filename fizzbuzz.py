#function fizzbuzz
def fizzbuzz(a, b):
    if isinstance((a and b), list):
        combined_length = len(a) + len(b)
        
        if ((len(a) + len(b)) % 3 == 0) and ((len(a) + len(b)) % 5 == 0):
            return "fizzbuzz"
        elif (len(a) + len(b)) % 3 == 0:
            return "fizz"
        elif (len(a) + len(b)) % 5 == 0:
            return "buzz"
        else:
            message = "The length of these lists isn't divisible by both 5 and 3, and it's:"
            return combined_length
    else:
        return "Invalid input"


#display result
print (fizzbuzz(['j','a','n','e','t'],['a','n','a','m','a']))