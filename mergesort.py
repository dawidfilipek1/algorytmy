def mergesort(list: list[int]) -> int:

    swaps: int = 0

    if len(list) <= 1:
        return 0

    pivot: int = len(list)//2
    l: list[int] = list

    l[-1], l[pivot] = l[pivot], l[-1]

    t: int = l[-1]

    pivotL: int = 0
    pivotR: int = len(l)-2

    while pivotL <= pivotR:
        if l[pivotL] > t:
            while l[pivotR] >= t and pivotR > 0:
                pivotR -= 1

            if pivotL < pivotR:
                l[pivotL], l[pivotR] = l[pivotR], l[pivotL] 
                swaps += 1
        # if pivotR != pivotL:

        if pivotL <= pivotR:
            pivotL += 1

    pivot = pivotL
    if pivotL == 1 and pivotR == 0:
        pivot = pivotR
    l[-1], l[pivot] = l[pivot], l[-1]

    swaps += mergesort(l[:pivot])
    swaps += mergesort(l[pivot:])

    return swaps

if __name__ == "__main__":
    l: list[int] = [5, 2, 6, 4, 1, 3, 2]

    r: int = 0

    print(mergesort(l))
    print(l)



