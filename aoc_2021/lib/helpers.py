from pathlib import Path

def load_input(file: str, input_file_name:str='input.txt'):
    input_path = Path(file).parent.absolute() / input_file_name

    with input_path.open('r') as file:
        return [line.strip() for line in file.readlines() if line.strip() != '']

def load_input_chunked(file: str, input_file_name:str='input.txt'):
    input_path = Path(file).parent.absolute() / input_file_name

    with input_path.open('r') as file:
        lines = file.readlines()
    
    data = []
    chunk = []
    for line in lines:
        if line.strip() == '':
            data.append(chunk)
            chunk = []
        else:
            chunk.append(line.strip())
    if chunk not in data:
        data.append(chunk)
    return data