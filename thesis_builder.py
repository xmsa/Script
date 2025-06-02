import argparse
import re


def read_file(file_path):
    """
    Reads the content of a file and returns it as a list of lines.
    Uses UTF-8 encoding to support Persian and English characters.
    Handles file not found and other exceptions gracefully.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error reading file: {e}"


def pre_processing(file_contents):
    """
    Processes the list of lines to filter only relevant parts before 'appendix'.
    Starts collecting lines from the first occurrence of 'chapter'.
    Includes lines containing 'input' or 'include' only after a chapter has started.
    """
    filtered_contents = []
    chapter_started = False

    for line in file_contents:
        if "appendix" in line:
            break  # Stop processing at appendix

        if "chapter" in line:
            filtered_contents.append(line)
            chapter_started = True
        elif chapter_started and ("input" in line or "include" in line):
            filtered_contents.append(line)

    return filtered_contents


def extract_file_path(input_line):
    """
    Extracts the file path from a LaTeX \\input{} command using regex.
    If the file path has no extension, appends '.tex' by default.
    Returns None if no valid \\input{} pattern is found.
    """
    match = re.search(r'\\input\{([^}]+)\}', input_line)
    if match:
        file_path = match.group(1)
        # Add '.tex' extension if missing
        if not re.search(r'\.[a-zA-Z0-9]+$', file_path):
            file_path += '.tex'
        return file_path
    else:
        return None


def read_data(file_contents):
    """
    Recursively reads and expands the content of files referenced by \\input{} commands.
    If a line contains an \\input command, it extracts the file path,
    reads the referenced file, and inserts its content in place.
    Otherwise, it adds the line directly to the content list.
    """
    content = []
    for line in file_contents:
        if "input" in line:
            if str.startswith(line.strip(), "%"):
                continue
            result = extract_file_path(line)
            if result:
                # Recursively read referenced file content
                included_content = read_data(read_file(result))
                content.extend(included_content)
            else:
                # If no valid file path found, just append the original line
                content.append(line)
        else:
            content.append(line)
    return content


def save_text_list_to_file(text_list, filename):
    """
    Saves a list of text lines to a specified file.
    Adds extra newlines before lines containing page breaks or chapter/section markers for readability.
    Writes the file with UTF-8 encoding.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in text_list:
                # Insert extra spacing before these commands for better formatting
                if any(keyword in line for keyword in ["newpage", "chapter", "section"]):
                    f.write("\n\n")
                f.write(line+"\n")
        print(f"Successfully saved text to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")


def remove_latex_comments(lines):
    """
    Removes LaTeX-style comments from a list of text lines.

    This function processes each line of LaTeX source code and removes anything 
    following a '%' character, which denotes a comment in LaTeX. Escaped percent 
    signs (e.g., '\\%') are preserved. Lines that are completely comments or become 
    empty after comment removal are excluded from the result.

    Args:
        lines (list of str): A list of strings representing lines of LaTeX code.

    Returns:
        list of str: A list of lines with LaTeX comments removed.
    """
    cleaned_lines = []
    for line in lines:
        # Remove everything after '%' unless it is escaped like '\%'
        line_without_comment = re.split(r'(?<!\\)%', line)[0].rstrip()
        if line_without_comment.strip():  # Only add non-empty lines
            cleaned_lines.append(line_without_comment)

    return cleaned_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a LaTeX file and expand \\input commands.")
    parser.add_argument('input_file', type=str,
                        help="Path to the input LaTeX file")
    parser.add_argument('-o', '--output', type=str, default='output.tex',
                        help="Path to the output file (default: output.tex)")

    args = parser.parse_args()

    file_content = read_file(args.input_file)
    if isinstance(file_content, list):
        filtered_content = pre_processing(file_content)
        expanded_content = read_data(filtered_content)
        cleaned_lines = remove_latex_comments(expanded_content)

        save_text_list_to_file(cleaned_lines, args.output)
    else:
        print(file_content)
