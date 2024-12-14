
def Red_nosed_Reports():
    total_safe = 0
    with open("unusual data") as data:
        l = 0
        for report in data:
            list_numbers = []
            for x in report.split():
                list_numbers.append(int(x))
            print("-"*len(list_numbers)*4)
            print(list_numbers)

            safe = 0
            i = 0
            y = list_numbers[0]
            if len(list_numbers) == len(set(list_numbers)):
                sorted_list = list(list_numbers)
                sorted_list.sort()
                print(sorted_list)
                print("bigest number = ", sorted_list[-1])

                while i < len(list_numbers)-1:
                    x = list_numbers[i+1]
                    if x > y:
                        while i < len(list_numbers)-1:
                            x = list_numbers[i+1]
                            print(y, x)
                            if y < x <= y+3:
                                print("Safe +3")
                                safe += 1
                            y = x
                            i += 1
                    elif x < y:
                        while i < len(list_numbers)-1:
                            x = list_numbers[i+1]
                            print(y, x)
                            if y > x >= y-3:
                                print("Safe -3")
                                safe += 1
                            y = x
                            i += 1
                    else:
                        print("WTF "*40)

                print(safe, len(list_numbers)-1)
            else:
                print("Dubble number")
            l += 1
            print("total", l)
            if safe == len(list_numbers)-1:
                total_safe += 1
            elif safe != 0:
                print("*"*40)
            print("total_safe", total_safe)
            if l >= 1530:
                break
            

            
    return total_safe

def Red_nosed_Reports2():
    total_safe = 0
    with open("unusual data test") as data:
        l = 0
        for report in data:
            list_numbers = []
            for x in report.split():
                list_numbers.append(int(x))
            print("-"*len(list_numbers)*4)
            print(list_numbers)

            

    return total_safe

  
print(Red_nosed_Reports2())