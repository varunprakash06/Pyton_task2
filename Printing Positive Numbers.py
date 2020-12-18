List1 = []
Length = int(input('Enter the range of list'))
for i in range(Length):
          X = int(input("Enter the numbers of list"))
          List1.append(X)
print(List1)
print('Before Finding Positive Numbers in the List',List1)
Positive_Numbers = list(filter(lambda Y: Y>0,List1))
print('The positive Numbers are = ',Positive_Numbers)
