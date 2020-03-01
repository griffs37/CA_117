class PQ(object):
	
	def __init__(self):
		self.d = {}
		self.N = 0
	
	def exch(self, i, j):
		self.d[i], self.d[j] = self.d[j], self.d[i]
	
	def swim(self, k):
		while k > 1 and self.d[k//2] < self.d[k]:
			self.exch(k, k//2)
			k = k//2

	def insert(self, v):
		self.N += 1
		self.d[self.N] = v
		self.swim(self.N)

	def bigger(self, i, j):
		try:
			return max([i, j], key=self.d.__getitem__)
		except KeyError:
			return i

pq = PQ()
pq.insert(5)
pq.insert(6)
pq.insert(12)
pq.insert(3)
pq.insert(15)
pq.insert(9)