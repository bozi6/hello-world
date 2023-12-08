from cprint import *


def binary_search(tomb, keresett):
    """
    Bináris keresés

    :param tomb: a tömb amiben keresünk
    :type tomb: list
    :param keresett: keresett érték
    :type keresett: str
    :return: a megtalált elem
    :rtype: str

    """
    low = 0
    high = len(tomb) - 1
    mid = 0

    while low <= high:
        print(f"low: {low} - mid: {mid} - high: {high}")
        mid = (high + low) // 2
        if tomb[mid] < keresett:
            low = mid + 1
        elif tomb[mid] > keresett:
            high = mid - 1
        else:
            return mid
    return -1


def main():
    arr = [
        2,
        3,
        4,
        10,
        40,
        6,
        8,
        43,
        67,
        87,
        12,
        99,
        120,
        345,
        543,
        657,
        87,
        9876,
        2435,
        465,
        6575,
        6575,
        5865,
        46454,
    ]
    arr.sort()
    sorsz = len(arr)
    neo = {}
    for egy in range(sorsz):
        neo[egy] = arr[egy]
    for egy in range(sorsz):
        cprint.info(f"{egy}-", neo[egy])
    x = 87

    result = binary_search(arr, x)

    if result != -1:
        print("Az elem indexe:", str(result))
    else:
        print("Az elem nem található a tömbben.")


if __name__ == "__main__":
    main()
