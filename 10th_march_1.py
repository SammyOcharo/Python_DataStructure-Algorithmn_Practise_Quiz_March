###########################
l = [None] * 10
print(len(l))
######################################
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)
#################################
sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)
#################################
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']
newList = listOne + listTwo
print(newList)