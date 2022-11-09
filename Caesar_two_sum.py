#Caesar two_sum : used to find the target sum by adding two numbers in the list,
#When the sum is found , the program stops and gives the value of those two numbers in the list

def two_sum(L,T): #--> L=list and T=target
    s = 0
    add=0
    flag = False
    l = len(L) #--> range of the list
    while flag == False:
        for i in range(1, l):
            if flag:
                break
            sum = L[s] + L[i] #L[s]= first value to be checked , L[i] = second value to be checked
            if sum == T:
                add=f"{T} found by adding {L[s]} and {L[i]}"
                flag = True
                break
            elif sum!= T and i == (l - 1):
                s += 1
                if s == (l - 1):
                    print("Caesar sum not possible")
                    flag = True
    return add

a=two_sum([1,6,8,2,0],10)
b=two_sum([7,4,1,8,10],9)
print(a)
print(b)