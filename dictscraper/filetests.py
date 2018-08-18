import os

home_directory_path = os.path.expanduser("~")
file_path = os.path.join(home_directory_path, "testdir", "test.txt")

try:
    file = open(file_path, "a")
    for i in range(5):
        file.write("\n" + i.__str__())

finally:
    file.close()

