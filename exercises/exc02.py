if __name__ == "__main__":
    # Solution 1
    number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    i = 0
    # get list's size
    n = len(number_list)
    # iterate list till i is smaller than n
    while i < n:
        # check if number is greater than 50
        if number_list[i] > 50:
            # delete current index from list
            del number_list[i]
            # reduce the list size
            n = n - 1
        else:
            # move to next item
            i = i + 1
    print(number_list)
    # Solution 2
    number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(len(number_list) - 1, -1, -1):
        if number_list[i] > 50:
            del number_list[i]
    print(number_list)
