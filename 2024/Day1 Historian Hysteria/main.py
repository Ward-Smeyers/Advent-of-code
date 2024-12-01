# list1 = (3,4,2,1,3,3)
# list2 = (4,3,5,3,9,3)


def Historian_Hysteria():
    list1 = []
    list2 = []
    with open("lists") as f:
        for line in f:
            temp = line.split()
            list1.append(int(temp[0]))
            list2.append(int(temp[1]))

    list1=sorted(list1)
    list2=sorted(list2)

    i=result=0
    while i < len(list1):
        result += abs(list1[i]-list2[i])
        i+=1
    return result

print(Historian_Hysteria())