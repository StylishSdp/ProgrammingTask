def mySqrt(x):
    if x <= 0:
        return 0

    left = 1
    right = x
    mid = 1
    while left < right:
        mid = (right - left) // 2 + left
        if mid ** 2 == x:
            return mid
        elif mid ** 2 > x and (mid - 1) ** 2 <= x:
            return mid - 1
        elif mid ** 2 < x and (mid + 1) ** 2 > x:
            return mid
        elif mid ** 2 > x:
            right = mid - 1
        else:
            left = mid + 1

    return mid