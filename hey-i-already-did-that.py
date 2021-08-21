def solution(n, b):
    # Define variables that cumulate through recursive function
    results = {}
    j = 0
    return calculate(n, b, j, results)


def calculate(n, b, j, results):
    # Define iteration tally and create sorted ascending and descending strings from minion id
    i = ''
    k = len(str(n))
    x = ''.join(sorted([i for i in str(n)])[::-1])
    y = x[::-1]
    # Subtract ascending id string from descending in specified base
    z = int(x, b) - int(y, b)
    # Convert result to specified base
    while z:
        i = int(str(z % b) + str(i))
        z = z // b
    # Prefix leading zeros where necessary
    i = '0'*(k-len(str(i))) + str(i)
    # Add result to results array if not already present
    if i not in results.values():
        results[j] = i
        j += 1
        # Recursively calculate next result
        s = calculate(i, b, j, results)
        return s
    # Return solution by indexing last calculated result
    else:
        return len(results.keys()) - list(results.keys())[list(results.values()).index(i)]

