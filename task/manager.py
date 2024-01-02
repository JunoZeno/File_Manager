import os

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
        # Use list comprehension to create two different lists
        files_with_dot = [file for file in dir_contents if '.' in file]
        files_without_dot = [file for file in dir_contents if '.' not in file]
        ordered_list = files_without_dot + files_with_dot
        for content in ordered_list:
            print(content)
    # If ls command includes -l or -lh print the size of files
    elif len(user_dir) == 2 and (user_dir[1] == '-l' or user_dir[1] == '-lh'):
        with os.scandir(os.getcwd()) as entries:
            for entry in entries:
                # entry.stat().st_size gets the size of the file
                entry_size = entry.stat().st_size
                if len(user_dir) == 2 and user_dir[1] == '-l':
                    print(entry.name + " " + str(entry_size))
                elif len(user_dir) == 2 and user_dir[1] == '-lh':
                    print(entry.name + " " + str(human_readable_size(entry_size)))
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


print("Input the command")
user_input = input()

while user_input != 'quit':
    if user_input == 'pwd':
        print(os.getcwd())
    elif user_input == 'cd ..':
        move_up_one_dir()
    elif 'cd' in user_input:
        move_to_path()
    elif 'ls' in user_input:
        list_of_contents()
    else:
        print("Invalid command")
    user_input = input()
