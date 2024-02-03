def find_union(list1, list2):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    # Find the union by taking the union of the sets
    union = set1.union(set2)

    return list(list1+list2)


def find_intersection(list1, list2):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection by taking the intersection of the sets
    intersection = []

    for i in list1:
        if i in list2:
            intersection.append(i)

    return list(intersection)


# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find and print the union
union = find_union(list1, list2)
print("Union:", union)

# Find and print the intersection
intersection = find_intersection(list1, list2)
print("Intersection:", intersection)
