class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
            
        array = [0] * ( n + 2 )

        array[1] = 1
        array[2] = 1

        for i in range(3, n+2):
            array[i] = array[i-1] + array[i-2] + array[i-3]
        
        return array[n]
