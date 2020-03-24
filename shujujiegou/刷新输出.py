import time

one = '这是输出的第一句话，。。。。。。'
two = '这是瞎几把打的第二句话。。。。。'

print('\r'+ one, end='')
time.sleep(2)
print('\r'+ two, end='')
