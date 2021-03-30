import os

def main():
    i = 0
    new_name = input("Enter the filename for the files: ")
    new_ext = input("Enter the extension for the files: ")
    path = "./Files/"
    for filename in os.listdir(path):
        my_dest = new_name + str(i) + "." + new_ext
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()