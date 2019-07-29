s = input()
lst = ['.'+i for i in s if i not in 'AEIOYUaeioyu']
s = (''.join(lst)).lower()
print(s)
