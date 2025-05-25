import random
import time

dataset = ""
rawText = ""
ignoreset = [".", ",", "!", "'", '"', "?"]

with open('dataset.txt', 'r') as file:
    rawText = file.read().lower()
    
dataset = rawText.replace('\n', ' ').replace('\r', ' ')

def chunkdata(data):
    words = []
    currentword = ""
    for letter in data:
        if letter == " ":
            words.append(currentword)
            currentword = ""
        elif letter not in ignoreset:
            currentword += letter

    if currentword != "":
        words.append(currentword)
    return words

def pairset(words):
    pairs = {}
    currentPair = ()
    currentIndex = 0

    for word in words:
        if currentIndex == 2:
            pairs[(currentPair)] = 1
            currentPair = ()
            currentIndex = 0
        currentPair += (word,)
        currentIndex += 1
    if len(currentPair) != 0:
        pairs[(currentPair)] = 1
    return pairs

def suggest(word, pairs):
    matchingPairs = []
    samePriorityPairs = []
    highestPriority = 1
    samePriority = 0

    heldPair = False

    for pair in pairs:
        if len(pair) < 2:
            continue

        if pair[0] == word or heldPair:
            if heldPair:
                matchingPairs.append([pair[0], pairs[pair]])
            else:
                matchingPairs.append([pair[1], pairs[pair]])
            heldPair = False
        elif pair[1] == word:
            heldPair = True

    for pair in matchingPairs:
        if pair[1] > highestPriority:
            highestPriority = pair[1]
    for pair in matchingPairs:
        if pair[1] == highestPriority:
            samePriority += 1
            samePriorityPairs.append(pair[0])
    print(matchingPairs)
    if len(samePriorityPairs) > 1:
        return samePriorityPairs[random.randrange(len(samePriorityPairs))]
    elif len(samePriorityPairs) == 1:
        return samePriorityPairs[0]

words = chunkdata(dataset)
pairs = pairset(words)
userinput = ""

while userinput.lower() != "end":
    userinput = input("Enter a sentence or word (enter end to stop): ")
    userWords = chunkdata(userinput)
    lastWord = userWords[len(userWords) - 1]
    suggestion = suggest(lastWord, pairs)
    print(f"{userinput} {suggestion}?")
    if suggestion:
        time.sleep(0.1)
        correct = input("Was the suggestion correct (y/n): ").lower()
        if correct == "y":
            print("success!")
        else:
            correctSuggestion = input("Enter what WORD would come after your phrase: ")
            heldPair = False
            foundInPairs = False
            for pair in pairs:
                if heldPair:
                    heldPair = False
                    if pair[0] == correctSuggestion:
                        pairs[pair] += 1
                        foundInPairs = True
                if pair[0] == lastWord and pair[1] == correctSuggestion:
                    pairs[pair] += 1
                    foundInPairs = True
                elif pair[1] == lastWord:
                    heldPair = True
            if not foundInPairs:
                pairs[(lastWord, correctSuggestion)] = 1
    else:
        print("No suggestion found")
        time.sleep(0.1)
        correctSuggestion = input("Enter what WORD would come after your phrase: ")
        pairs[(lastWord, correctSuggestion)] = 1
