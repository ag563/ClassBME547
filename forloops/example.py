#unmutable
def update(a):
    a[0]=a[0]+2

#mutable
#def update(a):
#    a = a+2
#    return a
    
def main():
    #unmutable list
    b=[5]
    x=update(b)
    print(b)
    print(x)

def main():
    #mutable
    b=5
    b=update(b)
    print(b)

if __name__ == "__main__":
    main()


