import os
import socket

numWords = 0
totalWords = 0
max1 = 0
max2 = 0
max3 = 0
maxWord1 = ""
maxWord2 = ""
maxWord3 = ""
wordCounts = {}

result = open('result.txt', 'w')

path = r"/home/data"
file_list = os.listdir(path)
filename = ""

result.write("\nFiles: ")
for file in file_list:
    filename = file
    result.write("'" + filename + "' ")

for file in file_list:
    fileLocation = path + '/' + file
    filename = file
    with open(fileLocation, 'r') as file:
        data = file.read()
        lines = data.split()
        numWords += len(lines)
        totalWords += numWords
        if filename == "IF.txt":
            for word in lines:
                if word in wordCounts:
                    wordCounts[word] += 1
                else:
                    wordCounts[word] = 1

            for word in wordCounts:
                if wordCounts[word] > max1:
                    max1 = wordCounts[word]
                    maxWord1 = word
                elif wordCounts[word] > max2 and wordCounts[word] < max1:
                    max2 = wordCounts[word]
                    maxWord2 = word
                elif wordCounts[word] > max3 and wordCounts[word] < max2:
                    max3 = wordCounts[word]
                    maxWord3 = word

    result.write("\nFile: '" + filename + "' Number of words: " + str(numWords))
    file.close()


result.write("\nTotal words in both files: " + str(totalWords))
result.write("\nTop 3 words with the maximum number of counts: '" + maxWord1 + "' was found " + str(max1) + " times, '" + maxWord2 + "' was found " + str(max2) + " times, '" + maxWord3 + "' was found " + str(max3) + " times\n")

iPAddress=socket.gethostbyname(socket.gethostname())
result.write("Machine's IP Address: " + iPAddress + "\n")

result.close()

results = open('result.txt', 'r')

for line in (results.readlines()):
    print(line)

results.close()
