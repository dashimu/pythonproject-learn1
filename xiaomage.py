'''
整数运算
'''

#加法
add = 3 + 4
# format 方法是{} 替换变量的值
print('3+4的值是{}'.format(add))

# x 的n次方

power = 7 ** 2.0

print('7**2.0 is {}'.format(power))

print(True and 'a')

print('welcome to learn python, \n')
print('\thi, to test')

#string

log_1_str = 'The error is a bug.'
log_2_str = ' we should fix it.'
log_str = log_1_str + log_2_str
print('\nThe whole sentence is :', log_str)

welcome = 'Hello, welcome to learn python.'

# title(), 每个单词的首字母大写
print('\n每个单词的首字母大写：', welcome.title())

print('\n段落的首字母大写：', welcome.capitalize())

print('\nall lower letter: ',welcome.lower())

print('\nall uppper letter: ',welcome.upper())

print('\nswapcase letter: ',welcome.swapcase())

print('\nalphanumeric: ', welcome.isalnum())

print('\nstring all digit: ', welcome.isdigit())

love_python = ' Hello, python love you  '

#strip
print('delete both side blank:',love_python.strip())

#rstrip
print('delete right side blank:',love_python.rstrip())

#lstrip
print('delete left side blank:',love_python.lstrip())

#slice
word = 'python'

print(word[0])
print(word[-1])
print(word[::-1])
print(word[1:2])
print(word[-2:])