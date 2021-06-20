# Write a function that accepts a list of numbers, finds the greatest number in the list and replaces the entire list with that number and returns the new list 
# my_new_list([6,4,8,9,7]) should return [9,9,9,9,9]

#Solution 1
def max_func(l):
    return [max(l)]*len(l)

print(max_func([6,4,8,9,7]))

#Solution 2
lst = [10, 5, 12, 299, 135, 75, 98, 2]
length = len(lst)
max = 0
for i in range(length):
    if max < lst[i]:
        max = lst[i]
print(f'maximum value in list is {max}')
for i in range(length):
    lst[i] = max
print(f'Updated list {lst}')
