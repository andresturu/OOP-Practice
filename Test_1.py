print("this should work no matter what")
print(__name__)
x= 10

def main():
    print("this will only print out when main function is called")
    y = 5
if __name__ == '__main__':
    main()