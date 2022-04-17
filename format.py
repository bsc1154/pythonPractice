a = 2
b = 3

s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)
print(s)

# 직접 대입하기
s1 = 'name : {0}'.format('BlockDMask')
print(s1)

# 변수로 대입 하기
age = 55
s2 = 'age : {0}'.format(age)
print(s2)

# 이름으로 대입하기
s3 = 'number : {num}, gender : {gen}'.format(num=1234, gen='남')
print(s3)

# 인덱스를 입력하지 않으면?
s4 = 'name : {}, city : {}'.format('BlockDMask', 'seoul')
print(s4)

# 인덱스 순서가 바뀌면?
s5 = 'song1 : {1}, song2 : {0}'.format('nunu nana', 'ice cream')
print(s5)

# 인덱스를 중복해서 입력하면?
s6 = 'test1 : {0}, test2 : {1}, test3 : {0}'.format('인덱스0', '인덱스1')
print(s6)

# 나와라 중괄호
s7 = 'Format example. {{}}, {}'.format('test')
print(s7)

# 중괄호로 겹쳐진 인자값
s8 = 'This is value {{{0}}}'.format(1212)
print(s8)

# 왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
print(s9)

# 오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
print(s10)

# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
print(s11)
