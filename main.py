from operator import itemgetter

# Sort Books According to their scores
def sortBooks(booksAvailable, bookScore):
    score = []
    for i in range(len(booksAvailable)):
        score.append((booksAvailable[i], bookScore[booksAvailable[i]]))
    score.sort(key=itemgetter(1))
    score.reverse()
    return(score)


# Input
file = open("a_example.txt", "r")
# file = open("b_read_on.txt", "r")
# file = open("c_incunabula.txt", "r")
# file = open("d_tough_choices.txt", "r")
# file = open("e_so_many_books.txt", "r")
# file = open("f_libraries_of_the_world.txt", "r")

books, noOflibraries, scanDays = map(int, file.readline().strip().split())
bookScore = list(map(int,file.readline().strip().split()))
libraries = []
for library in range(noOflibraries):
    noOfBooks, processTym, booksShip = map(int,file.readline().strip().split())
    booksAvailable = list(map(int,file.readline().strip().split()))
    
    # Calculating Worth
    sumScores = 0
    for i in range(noOfBooks):
        sumScores += bookScore[booksAvailable[i]]

    worth = ((sumScores/noOfBooks)*booksShip)/processTym
    booksAvailable = sortBooks(booksAvailable, bookScore)
    
    libraries.append([library, processTym, booksShip, booksAvailable, worth])

# Sort to find the library with least signup time required
libraries.sort(key=itemgetter(1))

signingUp = False
scannedScore = 0

bookScanned = []
currScanning = []

# Add the first library manually which requires least time to signup
if len(libraries)>0:
    temp = libraries.pop(0)
    currProcessing = temp
    signingUp = True
    
# Iterate over total no. of Scan Days
for i in range(scanDays):
    
    if len(libraries) == 0:
        break
    
    libraries.sort(key=itemgetter(4))
    libraries.reverse()
    
    currProcessing[1] = currProcessing[1] - 1
    
    if signingUp == False:
        temp = libraries.pop(0)
        # currScanning.append(temp)
        signingUp = True
        currProcessing = temp
    
    else:
        # Signup process Finished?
        if currProcessing[1] == 0:
            currScanning.append(temp)
            signingUp = False
        
    # Check for currently scanning books and add score
    for process in currScanning:
        if len(process[3])>0:
            for book in range(process[2]):
                try:                
                    while process[3][book] in bookScanned and len(process[3]) != 0:
                        process[3].pop(book)
                    
                    tempBookScanned = process[3].pop(0)
                    scannedScore += tempBookScanned[1]
                    bookScanned.append(tempBookScanned)
                
                except:
                    pass
        # If all books scanned of a library then remove them from currently scanning
        else:
            x = currScanning.index(process)
            currScanning.pop(x)
                
print(scannedScore)