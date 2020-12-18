"""Day 18 of advent of code"""
"""The key here is that the precendece of multiplication, addition, subtraction, etc. does not change - even if we change how the operator actually works"""
class new_ops :
    def __init__(self, nums) :
        self.nums = nums
    def __add__(self, new_num) :
        #adding is same same
        return new_ops(self.nums + new_num.nums)
    def __sub__(self, new_num):
        #change subtraction to multiplication so that the lines that are multiplication get evaluated in line left to right
        return new_ops(self.nums * new_num.nums)
    def __mul__(self, new_num):
        #change multiplication to addition for pt 2 so that the addition gets precedence over the multiplication lines
        return new_ops(self.nums + new_num.nums)

with open('day18input.txt') as f:
    d18input = f.read()

#creating a lsit of all the equations 
equations = [line for line in d18input.split('\n')]

#return value
sum_eq = 0

for eq in equations :
    for i in range(10) :
        #replace all instances of integers in our equation with my new integers
        eq = eq.replace(f"{i}", f"new_ops({i})")
    #replacing all of the multiplication with 'my version of subtraction'
    eq = eq.replace('*', '-')
    #replace all of the addition with my version of multiplication so that 'addition' (which is multiplication here) comes before the 'subtraction'
    eq = eq.replace('+', '*')
    #using python's built in 'eval' to evaluate the line haha
    sum_eq += eval(eq, {'new_ops': new_ops}).nums

print(sum_eq)