class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield{'length': self.length}
        yield{'width': self.width}

def main():
    while True:
        try:
            length = int(input("Enter the length of the rectangle : "))
            width = int(input("Enter the width of the rectangle : "))
            break
        except ValueError:
            print("Invalid input. Please enter valid integer values for length and width. ")

    rect = Rectangle(length, width)

    for info in rect:
        print(info)


if __name__ == "__main__":
    main()