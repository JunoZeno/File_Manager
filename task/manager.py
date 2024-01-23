import os
import shutil

os.chdir('module/root_folder')


def move_up_one_dir():
    try:
        current_dir = os.getcwd()
        path_list = current_dir.split('/')
        path_list.pop()
        print(path_list[-1])
        new_path = '/'.join(path_list)
        os.chdir(new_path)
    except OSError:
        print("Please enter a valid path")


def move_to_path():
    user_dir = user_input.split(' ')
    if len(user_dir) > 2:
        print("Invalid command")
    else:
        try:
            os.chdir(user_dir[1])
            print(os.getcwd())
        except OSError:
            print("Please enter a valid path")


# Method to print list of subdirectories and files
def list_of_contents():
    user_dir = user_input.split(' ')
    if len(user_dir) >= 3:
        print("Invalid command")
    elif len(user_dir) == 1 and user_dir[0] == 'ls':
        dir_contents = os.listdir(os.getcwd())
        if not dir_contents:
            print("This Directory is empty")
            return
        # Use list comprehension to create two different lists
        files_with_dot = [file for file in dir_contents if '.' in file]
        files_without_dot = [file for file in dir_contents if '.' not in file]
        ordered_list = files_without_dot + files_with_dot
        for content in ordered_list:
            print(content)
            return
    # If ls command includes -l or -lh print the size of files
    elif len(user_dir) == 2 and (user_dir[1] == '-l' or user_dir[1] == '-lh'):
        with os.scandir(os.getcwd()) as entries:
            for entry in entries:
                # entry.stat().st_size gets the size of the file
                entry_size = entry.stat().st_size
                if len(user_dir) == 2 and user_dir[1] == '-l':
                    print(entry.name + " " + str(entry_size))
                    return
                elif len(user_dir) == 2 and user_dir[1] == '-lh':
                    print(entry.name + " " + str(human_readable_size(entry_size)))
                    return
    else:
        print("Invalid command")


# check file size, returns a human-readable file size
def human_readable_size(size):
    if size < 1024:
        return f"{size}B"
    elif size < 1024 * 1024:
        return f"{size // 1024}KB"
    elif size < 1024 * 1024 * 1024:
        return f"{size // (1024 * 1024)}MB"
    else:
        return f"{size // (1024 * 1024 * 1024)}GB"


def remove_dir(user_command):
    input_list = user_command.split()
    if len(input_list) <= 1:
        print("Specify the file or directory")
    elif len(input_list) == 2:
        # command list
        print(f"The command list is {input_list}")
        try:
            move_up_one_dir()
            current_directory = os.getcwd()
            path = os.path.join(current_directory, input_list[1])
            # print(f'Path to delete is {path}')
            # Removing directory
            shutil.rmtree(path)
            # printing directory again
            print(os.getcwd())
        except FileNotFoundError:
            print("No such file or directory")


def create_directory(user_command):
    input_list = user_command.split()
    if len(input_list) <= 1:
        print("Specify the name of the directory to be made")
    elif len(input_list) == 2:
        try:
            path = f'{os.getcwd()}/{input_list[1]}'
            print('The created path is ', path)
            os.mkdir(path)
        except FileExistsError:
            print("The directory already exists")
        except FileNotFoundError:
            print("No such file or directory")


def change_dir_name(user_command):
    input_list = user_command.split()

    if len(input_list) < 3:
        print("Specify the current name of the file or directory and the new name")
    else:
        old_name = input_list[1]
        new_name = input_list[2]
        current_directory = os.getcwd()
        old_path = os.path.join(current_directory, old_name)
        new_path = os.path.join(current_directory, new_name)

        if not os.path.exists(old_path):
            print("No such file or directory")
        elif os.path.exists(new_path):
            print("The file or directory already exists")
        else:
            shutil.move(old_path, new_path)
            print(f"{old_name} has been renamed to {new_name}")

def print_updates():
    # Printing current directory
    print('The current dir is ', os.getcwd())
    # Printing directory contents
    print('The current dir contents ', os.listdir(os.getcwd()))


print("Input the command")
user_input = input()

while user_input != 'quit':
    user_input_list = user_input.split()
    if len(user_input_list) <= 0:
        print("Invalid Command")
    if user_input_list[0] == 'pwd':
        print(os.getcwd())
    elif user_input_list[0] == 'cd ..':
        move_up_one_dir()
    elif 'mkdir' in user_input_list[0]:
        create_directory(user_input)
    elif 'cd' in user_input_list[0]:
        move_to_path()
    elif 'ls' in user_input_list[0]:
        list_of_contents()
    elif 'rm' in user_input_list[0]:
        remove_dir(user_input)
    elif 'mv' in user_input_list[0]:
        change_dir_name(user_input)
    elif 'cp' in user_input_list[0]:
        change_dir_name(user_input)
    else:
        print("Invalid Command")
    user_input = input()
