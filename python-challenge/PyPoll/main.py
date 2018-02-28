text_file = open("paragraph.txt")
text = text_file.read()
text.close()

print(text)

numLines = 0
numWords = 0
numChars = 0
numSent = 0
avgletter = 0
avgsent = 0

    for line in file:
        #creating list for words
        wordslist = line.split()
        numLines += 1
        numWords += len(wordsList) 
        numChars += len(line)

print("Paragraph Analysis")
print("Word Count: ", numWords) 
print("Line Count: ", numLines)
print("Charcheter Count: ", numChars)
