def binarySearch(arr,val):

	if len(arr)==0 or (len(arr)==1 and arr[0]!=val):
		return False

	mid=arr[len(arr/2)]

	if val==mid: return True
	if val<mid: return binarySearch(arr[len(arr)/2], val)
	if val>mid: return binarySearch(arr[len(arr)/2+1], val)
	
	