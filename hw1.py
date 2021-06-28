quizes = ( ("3+2", 5, 3) , ("6/2", 3, 5) , ("10-2", 8, 3) , ("2의 3승", 8, 4) , ("5-2*2", 1, 5))
numOfO = 0
numOfX = 0
score = 0

for i in range(0, len(quizes), 1):
    answer = input(quizes[i][0] + '   :   ') 

    if answer == str(quizes[i][1]):
        numOfO += 1
        score += int(quizes[i][2])
    else:
        numOfX += 1

print('정답수   :     ', numOfO)
print('오답수   :     ', numOfX)
print('점   수   :     ', score)
