class BinHeap:
	def __init__(self):
		self.curr_size=0
		self.temp=[0]



	def go_up(self,i):
		while i/2>0:
			if self.temp[i/2]>self.temp[i]:
				tmp=self.temp[i/2]
				self.temp[i/2]=self.temp[i]
				self.temp[i]=tmp
			i=i/2

	def min_child(self,i):
		if 2*i+1>self.curr_size:
			return 2*i
		else:
			if self.temp[2*i]>self.temp[2*i+1]:
				return 2*i+1
			else:
				return 2*i
	def go_down(self,i):
		while 2*i<=self.curr_size:
			mc=self.min_child(i)
			if self.temp[mc]<self.temp[i]:
				tmp=self.temp[mc]
				self.temp[mc]=self.temp[i]
				self.temp[i]=tmp
			i=mc

	def insert(self,k):
		self.temp.append(k)
		self.curr_size=self.curr_size+1
		self.go_up(self.curr_size)

	def delmin(self):
		ret_val=self.temp[1]
		self.temp[1]=self.temp[self.curr_size]
		self.temp.pop()
		self.curr_size=self.curr_size-1
		self.go_down(1)
		return ret_val

	

	def build_heap(self,u_list):
		i=len(u_list)/2
		self.curr_size=len(u_list)
		u_list=[0]+u_list[:]
		self.temp=u_list
		print self.temp
		while i>0:
			self.go_down(i)
			i=i-1
		return self.temp


if __name__ == "__main__":
	bh=BinHeap()
	user_list=[9,5,6,2,3]
	print bh.build_heap(user_list)
	print bh.delmin()
	print bh.delmin()
	bh.insert(2)
	print bh.delmin()



