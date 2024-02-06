import time
def Merge(li):
    if len(li) > 1:
        m = len(li) // 2  
        l = li[:m]
        r = li[m:]

        Merge(l)
        Merge(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                li[k] = l[i]
                i += 1
            else:
                li[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            li[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            li[k] = r[j]
            j += 1
            k += 1

    return li

# Testing the algorithm with the given array [5,2,4,7,1,3,2,6]
li = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original array:", li)
sorted_list = Merge(li.copy())
print("Sorted array:", sorted_list)

start = time.time()  
sorted_list = Merge(li.copy()) 
end = time.time() 

print("Time taken:", end - start, "seconds")


'''Code by 
Sandeep Sanagala
UTA ID:- 1002157289'''