# NOT LEGAL
def average_list(start=None, values, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(values)
    result = 0.0
    i = start
    while i < end:
        result += values[i]
        i += 1
    return result / (end - start)

numbers = [1.0, 2.0, 5.0]
print '(', numbers, ') =>', average_list(numbers)
print '(', numbers, 1, ') =>', average_list(numbers, 1)
print '(', numbers, 1, 2, ') =>', average_list(numbers, 1, 2)
