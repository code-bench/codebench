import random


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr):
    arr.sort()


def main():
    random.seed(0)
    values = []
    for x in range(10000):
        values.append(random.randint(1, 10000))
    bubble_sort(values)


if __name__ == '__main__':
    main()
