from math import e as euler_num, factorial

def Poisson(average, maximum):
    final_list = []
    for entry in range(0, maximum + 1):
        temp = (euler_num ** (-1 * average)) * average ** entry
        temp = temp / factorial(entry)
        final_list.append(temp)
    n = 0
    for final_entry in final_list:
        print(str(n) + " : " + str(round(final_entry, 4)))
        n += 1
    
Poisson(5, 12)   

        