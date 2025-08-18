class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        Ch=''
        for i in digits:
            Ch=Ch+str(i)
        N=int(Ch)+1
        digits=[]
        for i in str(N):
            digits.append(int(i))
        return digits