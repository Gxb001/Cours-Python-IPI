number_letter = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]


def read_phone_number(number):
    print("Number : ", number)
    print("Phone number: ", end="")
    for i in number:
        print(number_letter[int(i)], end=" ")


read_phone_number("0783740784")
