from random import randint


def three_sum(a):
    count = 0
    a = sorted(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                # print(a[i],a[j],a[k])
                if a[i] + a[j] + a[k] == 0:
                    # print(f"a[{i}] ({a[i]}) + a[{j}] ({a[j]}) + a[{k}] ({a[k]}) = 0")
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


def three_sum_bin(a):
    count = 0
    a = sorted(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if bin_search(a[j + 1:], -(a[i] + a[j])) != -1:
                # print(f"a[{i}]:{a[i]} , a[{j}]:{a[j]}, {a[bin_search(a[j+1:], -(a[i] + a[j]))]}")
                count += 1

    return count


def test_three_sum_bin():
    a = [randint(-100000, 100000) for _ in range(1000)]
    a = sorted(list(set(a)))
    print(three_sum_bin(a))


if __name__ == '__main__':
    test_three_sum_bin()
