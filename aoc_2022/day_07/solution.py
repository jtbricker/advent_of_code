from lib.helpers import load_input

DIR_SIZE_THRESHOLD = 100000

class BashCommand:
    def __init__(self, command, output):
        self.command = command.split()[0]
        self.arg = command.split()[1] if self.command == 'cd' else None
        self.output = output
    
    def __str__(self):
        return f"BashCommand: \n\tcommand:{self.command}, \n\targ:{self.arg} \n\toutput:{self.output}"

directory_dict = {}

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = set()
        self.files = []
        self.dir_size = None
        
        full_path = self.get_full_path()
        if full_path not in directory_dict:
            directory_dict[full_path] = self

    def __str__(self):
        return f"""
        ==========================================================================
        Directory: {self.name} ({self.get_full_path()})
        ------------------------------------
            Parent: {self.parent.name if self.parent else "None"}
            Children: {[x.name for x in self.children]}
            Files: {self.files}
            Size: {self.dir_size}
        ==========================================================================    
        """
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def get_full_path(self):
        path = self.name
        node = self
        while node.parent:
            if node.parent.name == '/':
                path = node.parent.name + path
            else:
                path = node.parent.name + '/' + path
            node = node.parent
        return path

    def cd(self, command):
        new_dir_name = command.arg
        if new_dir_name == '..':
            return self.parent
        
        dir = Directory.get_or_add(new_dir_name, parent=self)
        self.children.add(dir)
        return dir
        

    def ls(self, command):
        for out in command.output:
            parts = out.split()
            
            # Lines in the output are either directories (starting with `dir`)
            if parts[0] == 'dir':
                dir_name = parts[1]
                dir = Directory.get_or_add(dir_name, parent=self)
                self.children.add(dir)

            # Or they are files of the format `<file size> <file name>`
            else:
                size = int(parts[0])
                name = parts[1]
                self.files.append((name, size, ))
    
    def calc_dir_size(self):
        # If, for some reason, we've already calculated this,
        # don't calculate it again
        if self.dir_size:
            return self.dir_size
        
        # Get size of files in this directory
        dir_size = sum([f[1] for f in self.files])

        # Get size of files in all child directories
        for child in self.children:
            dir_size += child.calc_dir_size()
        
        # Save dir_size to object
        self.dir_size = dir_size
        return dir_size
    
    @staticmethod
    def get_or_add(dir_name, parent):
        temp_dir = Directory(dir_name, parent)
        
        path = temp_dir.get_full_path()
        existing_dir = directory_dict.get(path)
        if existing_dir:
            return existing_dir
        else:
            directory_dict[path] = temp_dir
            return temp_dir
            


def parse_data(data):
    commands = []
    
    i=0
    assert(data[i][0]=='$')
    while i<len(data):
        command = data[i][1:].strip()
        output = None
        if command == 'ls':
            output = []
            j = i + 1
            while j<len(data) and data[j][0] != '$':
                output.append(data[j])
                j += 1
        else:
            j = i + 1
        i = j
        commands.append(BashCommand(command, output))
    return commands

def parse_commands_to_directory(commands):
    # The first command should always be a `cd /`, otherwise rest of code will fail
    assert(commands[0].command == 'cd')
    assert(commands[0].arg == '/')
    
    root_dir = Directory('/', None)
    directory_dict[root_dir.name] = root_dir
    curr_dir = root_dir

    for command in commands[1:]:
        if command.command == 'ls':
            curr_dir.ls(command)
        elif command.command == 'cd':
            curr_dir = curr_dir.cd(command)

    root_dir.calc_dir_size()

def part_1(data):
    """ Given a set of Bash-like commands (`cd`, and `ls`), determine
    the sum of directory sizes for directories of size 10000 or less

    Args:
        data (list[BashCommand]): List of BashCommand objects
                                  - If the command is `cd`, it will have an `arg` property
                                    representing the directory to change to
                                  - If the command is `ls`, it will have an `output` property
                                    with files (and sizes) and directories

    Returns:
        [int]: The sum of sizes of all directories, whose size is 100,000 or less
    """
    commands = parse_data(data)

    parse_commands_to_directory(commands)

    return sum([x.dir_size for x in directory_dict.values() if x.dir_size < DIR_SIZE_THRESHOLD])

def part_2(data):
    """ Given a set of Bash-like commands (`cd`, and `ls`) and a required unused disk disk size value, 
    determine the size of the smallest directory that has to be deleted to free up 30,000,000 disk space 
    (Assuming the total disk space is 70,000,000 )

    Args:
        data (list[BashCommand]): List of BashCommand objects
                                  - If the command is `cd`, it will have an `arg` property
                                    representing the directory to change to
                                  - If the command is `ls`, it will have an `output` property
                                    with files (and sizes) and directories

    Returns:
        [int]: The size of the smallest directory that needs to be deleted to free up 30,000,000 disk space
    """
    commands = parse_data(data)

    parse_commands_to_directory(commands)
    
    root_dir_size = directory_dict['/'].dir_size
    free_space = 70000000 - root_dir_size
    need_to_free = 30000000 - free_space

    min_dir_sizes = [d.dir_size for  d in directory_dict.values() if d.dir_size >= need_to_free]
    return min(min_dir_sizes)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()