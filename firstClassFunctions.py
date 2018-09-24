def func1(text):
    return '<h1>' + text + '</h1>'

def func2(text):
    return '<h2>' + text + '</h2>'

def return_header(func,text):
    return func(text)

print return_header(h1,"Fonksiyon...")



def f1(param):
    def f2():
        print (param)

    return f2

f = f1('my param')
print (f())
