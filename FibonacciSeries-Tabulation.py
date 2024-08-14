class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        stored = [-1] * (n+1)

        def Fibonacci(curr, array):
            if curr == 0 or curr == 1:
                return curr
            
            if array[curr] != -1:
                return array[curr]
            
            array[curr] = Fibonacci(curr - 1, array) + Fibonacci(curr - 2, array)
            return array[curr]
        
        return Fibonacci(n, stored)
