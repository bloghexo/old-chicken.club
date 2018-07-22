# Python基础入门完整版教程
## while 语句的基本语法
```
初始条件设置 -- 重复执行的计数器
    while 条件（判断 计数器 是否达到目标次数）
    当条件满足时，执行
    当条件满足时，执行
    当条件满足时，执行
    当条件满足时，执行
处理条件（计数器+1）
```
## while循环打印实例hello word 7次：
```
a = 0
while a <= 7:
    print("hello word")
    a = a + 1
print("循环结束 a = %d" % a)
```
## while累加求和（0～50）
```
result = 0
a = 0
while a <= 50:
    result += a
    a = a + 1
print("0~100的数字求和 = %d" % result)
```
## while偶数求和
```
result = 0
a = 0
while a <= 50:
    if a % 2 == 0:
        result += a
    a += 1
print("0~50偶数求和结果 = %d" % result)
```
