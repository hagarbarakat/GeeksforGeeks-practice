def getStarAndSuperStar(arr, n):
    stack = []
    super_star = max(arr)
    for i in reversed(range(n)):
        if len(stack) == 0 or stack[-1] < arr[i]:
            stack.append(arr[i])
        elif super_star == arr[i]:
            super_star = -1
    stack.append(super_star)
    return stack[::-1]
