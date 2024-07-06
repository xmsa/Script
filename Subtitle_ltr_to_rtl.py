#!/usr/bin/python

import argparse
import os
import re

def read_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(output_file, line):
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(line)

def convert_ltr_to_rtl(input_file, output_file):
    
    content = read_file(input_file)

    # Pattern to match each subtitle block
    pattern = re.compile(r'(\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n(?:[^\n]+\n?)*)', re.MULTILINE)
    matches = pattern.findall(content)

    for match in matches:
        parts = match.split('\n')
        for i in range(len(parts)):
            if not parts[i].isdigit() and not re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', parts[i]):
                parts[i] = '\u202b' + parts[i].strip() + '\u202c'
        text = '\n'.join(parts) + '\n\n'
        write_file(output_file,text)
    else:
        print(f"successful({output_file}) ...")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Convert LTR subtitles to RTL.')
        parser.add_argument('input_file',default='', type=str, help='The input subtitle file or directory in LTR.')
        args = parser.parse_args()
        files = []
        if os.path.isdir(args.input_file):
            for i in os.listdir(args.input_file):
                if i.endswith(".srt") and not i.endswith("_rtl.srt"):
                    files.append(os.path.join(args.input_file, i))
        elif str(args.input_file).endswith(".srt"):
            files.append(args.input_file)
        else:
            print("Invalid input file")
            exit(1)
        
        for input_file in files:
            output_file = input_file.replace(".srt", "_rtl.srt")
            if os.path.exists(output_file):
                flag = input(f"File '{output_file}' already exists, do you want to overwrite it? (Y/n): ")
                if flag.lower() == "y" or flag == "":
                    os.remove(output_file)
                else:
                    continue
            convert_ltr_to_rtl(input_file, output_file)
    except KeyboardInterrupt:
        exit()
    except Exception as ex:
        print(ex)
