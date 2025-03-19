def sortList(my_list):
    # bubble sort
    size = len(my_list)
    for k in range(size-1):
        for l in range(size-k-1):
            if my_list[l] > my_list[l+1]:
                temp = my_list[l]
                my_list[l] = my_list[l+1]
                my_list[l+1] = temp

def findIndex(my_list):
    size = len(my_list)
    for m in range(size):
        if my_list[m] == 30:
            return m

# creating empty list
my_list = []

# adding items to the list
i = 0
while i < 4:
    my_list.append((i+1)*10)
    i+=1

print("Added 10, 20, 30, 40")
print(my_list)

# inserting an item at 2nd position
my_list.insert(1,15)

print("\nInserted 15 at 2nd position")
print(my_list)

# adding more items to the list
j = 0
while j < 3:
    my_list.append((j+5)*10)
    j+=1

print("\nAdded 50, 60, 70 to the list")
print(my_list)

# removing the last item from the list
my_list.pop()

print("\nRemoved the last item from the list")
print(my_list)


# performing a sort
sortList(my_list)

print("\nSorted the list in ascending order")
print(my_list)

# finding an index
index = findIndex(my_list)
print(f"\nIndex of 30: {index}")

