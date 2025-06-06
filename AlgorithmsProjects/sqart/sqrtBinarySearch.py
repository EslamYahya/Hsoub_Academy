def SqrtBinarySearch(x):

    if (x == 0 or x == 1):
        return x

    start = 1
    end = x
    while (start <= end):
        mid = (start + end) // 2

        if (mid * mid == x):
            return mid

        if (mid * mid < x):
            start = mid + 1
            answer = mid

        else:
            end = mid - 1

    return answer


x = 11
print(SqrtBinarySearch(x))