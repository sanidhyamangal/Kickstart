test_cases = int(input())

for i in range(test_cases):
    n, m, q = [int(c) for c in input().strip().split(" ")]
    M = [int(c) for c in input().strip().split(" ")]
    R = [int(c) for c in input().strip().split(" ")]

    # check error for if more pages entered
    if len(M) != m or max(M) > n:
        raise MemoryError("Torn Pages doesnt match")
    if len(R) != q:
        raise MemoryError("Readers does not match")

    # to find the sum of values
    sum = 0

    # major logic for the code
    for i in R:
        for j in range(1, (n // i) + 1):
            if (i * j) not in M:
                sum += 1

    # print the result of the sum
    print("Case#{}: {}".format(i + 1, sum))
