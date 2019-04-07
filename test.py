with open('somefile.txt') as f:
    print(f.read(7))
    print(f.read(4))
    print(f.read())

with open('somefile.txt')as f:
    for i in range(3):
        print(str(i)+':'+f.readline(),end='')

with open('somefile.txt')as f:
    import pprint
    pprint.pprint(f.readlines())


def process(string):
    print('Processing:', string)

#处理每个字符
with open('somefile.txt')as f:
    # char = f.read(1)
    # while char:
    #     process(char)
    #     char = f.read(1)
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)

#处理每一段内容
with open('somefile.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)

#一次读取所有内容，处理其中字符
with open('somefile.txt') as f:
    for char in f.read():
        process(char)


#一次读取所有行，再分别处理每行

with open('somefile.txt') as f:
    for line in f.readlines():
        process(line)

#延迟行迭代
import fileinput
for line in fileinput.input('somefile.txt'):
    process(line)

#文件迭代器
with open('somefile.txt') as f:
    for line in f:
        process(line)

