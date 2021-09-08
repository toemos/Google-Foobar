def solution(x,y):
    # Sorting list (x) and creating enumerated index for comparison with second list (y)
    for i, j in enumerate(sorted(x)):
        # Referencing index 'twin' in second sorted list
        k = sorted(y)[i]
        if j != k:
            # When twin indexes do not have matching values, return lower value as lists are sorted
            if j < k:
                return j
            else:
                return k
