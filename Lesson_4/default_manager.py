# 'with' statement
# It helps simplify some common resource management patterns by abstracting their functionality.



def main():
    with open('test.txt', 'w') as f:

        f.write('Hello World!')
        f.write('Hello World!')    

    with open('test.txt', 'r') as f:
        print(f.read())


if __name__ == "__main__":
    main()