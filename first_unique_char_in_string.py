class Solution:
    def firstUniqChar(self, s: str) -> int:
        list1=[]
        list1[:0]=s
        for i in s:
            if s.count(i)==1:
                return list1.index(i)
        return -1
