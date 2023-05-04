import re

# numCapitalized
# function that accepts sentence of words and spaces (no punctuation) 
# and returns number of words in the sentence that are capitalized.
# Note: NOT the total number of capitals in the string
def numCapitalized(text):
    no_punct = re.sub(r'[^\w\s]','',text)
    words_list = no_punct.split()

    return len([word for word in words_list if word[0].isupper()])

    # returns total number of capitalized characters
    # count = 0 
    # for word in no_punct:
    #     if word[0].isupper():
    #         count += 1
    # return count

# exec(open('midtermPractice.py').read()) 
if __name__=='__main__':
    import doctest
    print( doctest.testfile('midtermPracticeTEST.py'))