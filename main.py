# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from calc import calc
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    val1 = input("Enter value1= ")
    val2 = input("Enter value2= ")
    calc1=calc(val1,val2)
    print(calc1.sub())
    print(calc1.pow())
    calc2=calc(val2,val1)
    print(calc2.sub())
    print(calc2.pow())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
