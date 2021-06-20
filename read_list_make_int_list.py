#Read a list as input and make it a list (integers)

lst = input("Enter elements of list")
lst = lst.replace("[","").replace("]","")
lst = lst.split(',')
lst = list(map(int, lst))
print(lst)