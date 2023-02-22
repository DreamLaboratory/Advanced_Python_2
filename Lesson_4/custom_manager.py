def read_cvs_file(file_name):
    try:
        open_file = open(file_name, "r")
        return open_file.read()
    except FileNotFoundError:
        print(f"File {file_name} not found")
    finally:
        open_file.close()



def write_cvs_file(file_name, data):
    try:
        open_file = open(file_name, "a")
        open_file.write(data)
        #call read_cvs_file
        return data
    except FileNotFoundError:
        print(f"File {file_name} not found")
    finally:
        open_file.close()

if __name__ == "__main__":
    # read_cvs_file("output.csv")
    file_name = "output.csv"
    data = write_cvs_file(file_name, "Hello World\n")
    readed_data = read_cvs_file(file_name)
    print(readed_data)

