import os

def delete_all_files(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)

if __name__ == "__main__":
    target_directory = r"C:\Users\Admin\PycharmProjects\pythonProject\testv1\del"
    delete_all_files(target_directory)
