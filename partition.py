
def partition(A, p, r):
	q = j = p
	while j < r:
		if A[j] <= A[r]:
			A[q], A[j] = A[j], A[q]
			q += 1
		j += 1
	A[q], A[r] = A[r], A[q]
	return q

A = [74, 82, 68, 18, 79, 27, 89, 24, 52, 70]
partition(A, 0, len(A)-1)
print(A)