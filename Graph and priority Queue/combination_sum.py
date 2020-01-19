def comb(arr, target):
    arr = sorted(list(set(arr)))
    def comb_util(target, comb, start):
        if target == 0:
            result.append(comb)
            return
        for i in range(start, len(arr)):
            if target < arr[i]:
                return
            comb_util( target - arr[i], comb + [arr[i]], i)
    result = []
    comb_util(target, [], 0)
    return result

def comb_util(arr, result, target, comb, index):
    if target == 0:
        result.append(comb)
        index += 1
        return

    if target < 0:
        index += 1
        return

    while index < len(arr):
        comb_util(arr, result, target-arr[index], comb + [arr[index]], index)
        index += 1




def combination(arr, target):
    arr = sorted(list(set(arr)))
    result = []
    comb = []
    index = 0
    comb_util(arr, result, target, comb, index)
    return result



arr = [ 2, 3, 6 ,7]
target = 7
print(comb(arr, target))
print(combination(arr, target))





