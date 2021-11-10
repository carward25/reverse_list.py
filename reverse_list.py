#name: Cassidy Ward
#date:11/10/2021
#description: this program takes as a parameter a list and and reverses the order of the elements in that list

def reverse_list(lst):
    i = 0
    j = len(lst)-1
    while (i<j):
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i+=1
        j-=1
