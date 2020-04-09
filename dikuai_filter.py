#主要是在python2环境下对字符串的处理
import sys
def Cal(a):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    a = a.replace('地块','')
    return a
    