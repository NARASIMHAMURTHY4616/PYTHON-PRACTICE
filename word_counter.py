def strinG(): # a function that can be callable anytime in the program
    t = input("Enter your text here:") #taking input from the user
    length = len(t) # finding the len of the input string
    print("length is", length) 
    c = {} # creating a dict for storing the letter frequency
    for words in t: #loop for finding fr
        if words in c:
            c[words] += 1
        else:
            c[words] = 1
    print("number of words and how many time it would be repeated:", c)
    words = t.split() # by splitting the whole string it can be divided into words
    w = len(words)  # to count the words using len()
    print("number of words:", w) 
strinG() # function call
