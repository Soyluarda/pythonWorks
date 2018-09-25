def outer(msg):
    free_variable = "this is a free variable."

    def inner():
        print free_variable
        print msg
    return inner

f = outer("hello from other side")
f()
k  =outer("hello from our side")
k()
