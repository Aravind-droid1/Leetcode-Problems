#412. Fizz Buzz
#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true

class Solution(object):
    def fizzBuzz(self, n):
        
        a=[0]*n
        for i in range(1,n+1):
            if (i%3==0):
                if (i%5==0):
                    a[i-1]="FizzBuzz"
                else:
                    a[i-1]="Fizz"
            elif(i%5==0):
                a[i-1]="Buzz"
            else:
                a[i-1]=str(i)
        return a

obj=Solution()
print(obj.fizzBuzz(15))