def sound():
    print("sound")
def pamyat():
    print("что нужно найти? (Мощность алфавита, колво символов в тексте, инф объём текста)")
    print("pamayt")
def isobr():
    print("isobr")
print("Какой тип задачи нужно решить? (звук, инфа, изобр)")
A=input()
if A=="звук":
    sound()
if A=="инфа":
    pamyat()
if A=="изобр":
    isobr()
