result = 0
a = 0
while a <= 50:
    if a % 2 == 0:
        result += a
    a += 1
print("0~50偶数求和结果 = %d" % result)