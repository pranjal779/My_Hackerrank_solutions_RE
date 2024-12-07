if __name__ == '__main__':
    listOfN = []
    N = int(input())
    for i in range(0, N):
        elementInList = int(input())
        
        listOfN.append(elementInList)
    
    print(listOfN)
    
    listOfN.insert(2, 7)
    print(listOfN)
    listOfN.insert(1, 3)
    print(listOfN)
    listOfN.pop(0)
    print(listOfN)
    listOfN.append(64)
    print(listOfN)
    listOfN.sort()
    print(listOfN)
    listOfN.pop()
    print(listOfN)
    list.reverse(listOfN)
    print(listOfN)
