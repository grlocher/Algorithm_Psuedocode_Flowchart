# Given an array of numbers, find the average of all the positive numbers. Ignore the negative numbers

START

    function positiveNumber(array):
        Set sum to = 0
        Set count to = 0

    for positive number in array:
        if number > 0:
            sum = sum + number
            count = count + 1

    if positive number in array == 0:
        print 'No numbers found'

    average = count / sum
    return average

END