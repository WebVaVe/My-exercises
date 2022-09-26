def announce(hello):
    def wrapper():
        print("about to run decorator funcation")
        hello()
        print("Ican add down function in this function")
    return wrapper

@announce
def h ():
    print("hello go on middel function wrapper")

h()