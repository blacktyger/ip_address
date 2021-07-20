import glob
import re
import os


def find_ips(input_file):
    output_file = f'IP_{input_file.split(".")[0]}.txt'
    ip_pattern = r'[0-9]+(?:\.[0-9]+){3}:[0-9]+'

    with open(input_file, 'r') as input:
        data = input.read()

    matcher = re.findall(ip_pattern, data)
    matcher = set(matcher)  # Remove duplicates

    with open(f'ips\\{output_file}', 'a') as file:
        for match in matcher:
            file.write("\n" + match)


def get_dir_files():
    files = glob.glob("*.log") + glob.glob("*.txt")
    print(f'FILES LIST: {files}')
    return files


def dump_ips():
    try:
        os.mkdir('ips')
    except:
        pass

    for file in get_dir_files():
        output_file = f'IP_{file.split(".")[0]}.txt'
        if os.path.isfile(f'ips\\{output_file}'):
            print(f'✓ {file} already completed')
        else:
            find_ips(file)
            print(f'✓ {output_file} finished')


if __name__ == "__main__":
    dump_ips()