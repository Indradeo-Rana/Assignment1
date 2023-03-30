# Write a command to get the Python version you are using.

# import sys
# print(sys.version)

class Solution(object):
    def maxsatisfcation (self, satisfcation):
        """
        :type satisfaction : List[int]
        :rtype: int
        """
    res=total=0
    satisfaction.sort()
    while satisfaction and satisfaction [-1] + total>0:
        total+= satisfaction.pop()
        rest=total
    return res