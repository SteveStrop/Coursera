def merge_sort(a):
    # print("Splitting ",a)
    if len(a) > 1:
        mid = len(a) // 2
        lefthalf = a[:mid] # need to remove slicing!!
        righthalf = a[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        # print("Merging ", a)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i = i + 1
            else:
                a[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            a[k] = righthalf[j]
            j = j + 1
            k = k + 1
        # print("Merged ",a)


def three_sum_bin(a):
    count = 0
    a = sorted(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if bin_search(a[j + 1:], -(a[i] + a[j])) != -1:
                # print(f"a[{i}]:{a[i]} , a[{j}]:{a[j]}, {a[bin_search(a[j+1:], -(a[i] + a[j]))]}")
                count += 1

    return count


def bin_search(a, key):
    lo, high = 0, len(a) - 1
    while lo <= high:
        mid = lo + (high - lo) // 2
        if a[mid] > key:
            high = mid - 1
        elif a[mid] < key:
            lo = mid + 1
        else:
            return mid
    return -1
