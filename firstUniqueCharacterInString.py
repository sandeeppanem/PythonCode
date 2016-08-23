class Solution(object):
    def firstUniqChar(self, s):
        temp=[0]*256
        for i in range(len(s)):
            asci_val=ord(s[i])
            temp[asci_val]=temp[asci_val]+1
      
        for i in range(len(s)):
        	asci_val=ord(s[i])
        	if temp[asci_val]==1:
        		return i
        return -1

if __name__ == '__main__':
	s = Solution()
	print s.firstUniqChar("loveleetcode")