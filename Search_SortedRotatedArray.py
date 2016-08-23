def BinSearch(input_list,low,high,key):
	if high<low:
		return -1

	mid=(low+high)/2
	if input_list[mid]==key:
		return mid
	if key>input_list[mid]:
		return BinSearch(input_list,mid+1,high,key)
	else:
		return BinSearch(input_list,low,mid-1,key)

def findPivot(input_list,low,high):
	if high<low:
		return -1
	if high==low:
		return low
	mid = (low+high)/2
	if mid<high and input_list[mid]>input_list[mid+1]:
		return mid
	if mid>low and input_list[mid]<input_list[mid-1]:
		return (mid-1)

	if input_list[low]>=input_list[mid]:
		return findPivot(input_list,low,mid-1)
	else:
		return findPivot(input_list,mid+1,high)

def findElement(input_list,n,key):
	pivot=findPivot(input_list,0,n-1)
	if pivot==-1:
		return BinSearch(input_list,0,n-1,key)
	if input_list[pivot]==key:
		return pivot

	if input_list[0]<=key:
		return BinSearch(input_list,0,pivot-1,key)
	else:
		return BinSearch(input_list,pivot+1,n-1,key)

if __name__ == '__main__':
	input_list=[3,4,5,1,2]
	n=len(input_list)
	key=2;
	index=findElement(input_list,n,key)
	print index