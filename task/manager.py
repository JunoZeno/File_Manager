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


def remove_dir(user_command):
    input_list = user_command.split()

    if len(input_list) <= 1:
        print("Specify the file or directory")
    elif len(input_list) == 2 and is_extension(input_list[1]):
        extension = input_list[1]
        current_directory = os.getcwd()
        files_to_remove = [file for file in os.listdir(current_directory) if file.endswith(extension)]

        if not files_to_remove:
            print(f"File extension {extension} not found in this directory.")
        else:
            for file in files_to_remove:
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
                # print(f"Deleted: {file}")
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
        print("Specify the current name of the file or directory and the new location and/or name")
    elif len(input_list) >= 2 and is_extension(input_list[1]):
        # print("Reached the extension check block")
        extension = input_list[1]
        # print("The extension is ", extension)
        destination = input_list[2]
        # print("The destination is ", destination)
        current_directory = os.getcwd()
        # print("The current directory is ", current_directory)
        source_files = [file for file in os.listdir(current_directory) if file.endswith(extension)]
        # print("The source files are ", source_files)

        if not source_files:
            print(f"File extension {extension} not found in this directory.")
        else:
            for file in source_files:
                source_path = os.path.join(current_directory, file)
                # print("The source file is ", source_path)
                destination_path = os.path.join(destination, file)
                # print("The destination is ", destination_path)

                if os.path.exists(destination_path):
                    user_response = input(f"{file} already exists in this directory. Replace? (y/n): ").lower()
                    if user_response == 'y':
                        shutil.move(source_path, destination_path)
                        print(f"Moved: {file} to {destination}")
                    elif user_response != 'n':
                        print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    shutil.move(source_path, destination)
                    print(f"Moved: {file} to {destination}")
    else:
        source = os.path.normpath(str(input_list[1]))
        destination = os.path.normpath(str(input_list[2]))

        if not os.path.exists(source):
            print("No such file or directory")
        elif os.path.exists(destination) and os.path.isdir(destination):
            destination_path = os.path.join(destination, os.path.basename(source))

            if os.path.exists(destination_path):
                print("The file or directory already exists")
            else:
                shutil.move(source, destination_path)
                print(f"{os.path.basename(source)} has been moved to {destination}")
        elif os.path.exists(destination) and os.path.isfile(destination):
            print("The file or directory already exists")
        else:
            shutil.move(source, destination)
            print(f"{os.path.basename(source)} has been moved to {destination} line 161")


def print_updates():
    # Printing current directory
    print('The current dir is ', os.getcwd())
    # Printing directory contents
    print('The current dir contents ', os.listdir(os.getcwd()))


def is_extension(extension):
    if extension[0] == '.' and extension[1] != '/':
        return True
    else:
        return False


def copy_files(user_command):
    input_list = user_command.split(' ')
    if len(input_list) >= 2 and is_extension(input_list[1]):
        current_directory = os.getcwd()
        extension = input_list[1]
        destination = input_list[2]
        source_files = [file for file in os.listdir(current_directory) if file.endswith(extension)]

        if not source_files:
            print(f"File extension {extension} not found in this directory.")
        else:
            for file in source_files:
                source_path = os.path.join(current_directory, file)
                destination_path = os.path.join(destination, file)

                if os.path.exists(destination_path):
                    user_response = input(f"{file} already exists in this directory. Replace? (y/n): ").lower()
                    if user_response == 'y':
                        shutil.copy(source_path, destination_path)
                        print(f"Replaced: {file}")
                    elif user_response != 'n':
                        print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    shutil.copy(source_path, destination)
                    print(f"Copied: {file} to {destination}")
    elif len(input_list) <= 2:
        print("Specify the file")
    elif len(input_list) > 3:
        print("Specify the current name of the file or directory and the new location and/or name")
    else:

        try:
            input_list.pop(0)  # removing cp command
            copy_directory = input_list.pop(-1)  # removing copy dir from end of list

            if len(input_list) > 1:
                path = " ".join(input_list)
                path_split = path.split('/')
                file_name = path_split.pop(-1)
                path = '/'.join(path_split)

            else:
                path = os.getcwd()
                file_name = input_list[0]

            path_with_file = os.path.join(path, file_name)
            dst_directory = os.path.join(path, copy_directory)
            file_exists_check = dst_directory + '/' + file_name

            if not os.path.exists(path_with_file) or not os.path.exists(dst_directory):
                print("No such file or directory")
            elif os.path.exists(file_exists_check):
                print(f"{file_name} already exists in this directory")
            else:
                shutil.copy2(path_with_file, dst_directory)

        except IndexError:
            print("Invalid")


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
        copy_files(user_input)
    else:
        print("Invalid Command")
    user_input = input()
