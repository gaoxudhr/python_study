# n1 = 255
# n2 = 1000

# n3 = hex(n1)
# print(n3)
# print(hex(n2))

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny


import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    x1 = (-b + math.sqrt(b*b - 4 * a *c))/(2 * a)
    x2 = (-b - math.sqrt(b*b - 4 * a *c))/(2 * a)
    return x1, x2

print('quadratic(2,3,1) = ', quadratic(2,3,1))
print('quadratic(1,3,-4) = ', quadratic(1,3,-4))

if quadratic(2,3,1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1,3,-4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')