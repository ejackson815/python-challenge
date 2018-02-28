import re
filename = "paragraph.txt"

#Holding Variables

numLines = 0
numWords = 0
numChars = 0
numSent = 0
Avglett = 0
Avgsent = 0

#Reading in Text file

with open(filename, 'r') as file:
    for line in file: 
        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)
        numChars += len(line)
        count = len(re.findall(r'\.',line))
        average = sum(len(word) for word in wordsList) / len(wordsList)
        average2 = numChars/numWords
        average3 = numWords / count

#Outputs 

print("Paragraph Analysis")
print("Number of Lines: ", numLines)
print("Number of Words: ", numWords)
print("Number of Characters: ", numChars)
print('Number of Sentences: ', count)
print('Average Word Count: ', average)
print('Average Letter Count: ', average2)
print('Average Sentence Length: ', average3)