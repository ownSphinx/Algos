# merges two sorted arrays using constant space

def merge(a, b):
    # code here
    n, m = len(a), len(b)
    i, j = n-1, 0
    while i >= 0 and j < m:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
        i -= 1
        j += 1

    a.sort()
    b.sort()


ar1 = [1, 5, 6, 10, 15]
ar2 = [2, 3, 6, 8, 9, 100, 340]

merge(ar1, ar2)
print(ar1)
print(ar2)
