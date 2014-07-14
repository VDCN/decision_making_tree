__author__ = 'xiaoyu'


a='abc'
b='def'
c='ghi'

t=a,b,c
print t

for i in vars().keys():
    if vars()[i]=='def':
        print 'var:',i