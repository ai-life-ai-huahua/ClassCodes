"""
gradient(f, *varargs, **kwargs)
    |- 两边的梯度：左边：下一个值-当前知 ，右边：当前值-上一个值
    |- 中间：（下一个 - 上一个）/2

"""
import numpy as np

a = [
    [1, 5, 6],
    [2, 6, 8],
    [6, 8, 10]
]

# print(np.sum(a, axis=0))
# print(np.prod(a, axis=0))
# a = [
#     [1, 5, 6],
#     [2, np.NaN, 8],
#     [6, 8, 10]
# ]

# print(np.nansum(a, axis=0))
# print(np.diff(a))   #
# print(np.gradient(a, axis=1))

b = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]
"""
    1,5,6
    1,2,3
    
    3 = 1*5 - 1*2
    3 = 1*6 - 1*3
"""
#    0  1  2
x = [1, 5, 6]
y = [1, 2, 3]

"""
[1, 5, 6]
[1, 2, 3] 

[ 3  3 -3]
 56  16  15
 23  13  13
 5*3-2*6=3    1+2=3 奇数 *1 
 1*3-1*6=-3*-1=3 * 0+2=2 偶数 *-1
 1*2-1*5 =-3  0+1= 奇数 *1    
"""
# print(np.cross(x, y))

print(np.trapz([1, 2, 3]))
