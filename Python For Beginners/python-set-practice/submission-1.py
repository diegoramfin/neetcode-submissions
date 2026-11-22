from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set()
    for word in words:
        if word in my_set: # Following the below caveat, 
                           # if word has already been read then it is a dupe.
                return True
        my_set.add(word) # If this is the first time the word appears we add to list
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
