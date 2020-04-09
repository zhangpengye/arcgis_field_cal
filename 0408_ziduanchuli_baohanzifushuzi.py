import re
def Cal(a):
    list = a.split('/')
    a = list[len(list)-1]
    a = a.replace('-','')
    a = re.sub('[0-9a-zA-Z]','',a)
    return a