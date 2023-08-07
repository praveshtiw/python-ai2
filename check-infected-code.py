import re
import os
import openpyxl

def find_infected_code_in_php(directory):
    infected_code_list = []

    patterns = [
        (r'\$O00OO_0_O_=urldecode\("([^"]+)"\);\$O000OOO___=\$O00OO_0_O_\{(\d+)\}', 'Pattern 1'),
        (r'base64_decode\(\s*["\']([^"\']+)["\']\s*\)', 'Pattern 2'),
        (r'\b(eval|exec|system|shell_exec)\s*\(', 'Pattern 3'),
        (r'(?<![\w-])_POST\[["\'].*["\']\]', 'Pattern 4'),
        (r'(?<![\w-])_GET\[["\'].*["\']\]', 'Pattern 5'),
        (r'(?<![\w-])_REQUEST\[["\'].*["\']\]', 'Pattern 6'),
        (r'(?<![\w-])passthru\s*\(', 'Pattern 7'),
        (r'(?<![\w-])popen\s*\(', 'Pattern 8'),
        (r'(?<![\w-])proc_open\s*\(', 'Pattern 9'),
        (r'(?<![\w-])assert\s*\(', 'Pattern 10')
        # Add more patterns as needed
    ]

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".php"):
                file_path = os.path.join(root, file_name)
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        for pattern, pattern_name in patterns:
                            matches = re.findall(pattern, line)
                            if matches:
                                decoded_string = matches[0][0]
                                line_number = line_number
                                infected_code_list.append((file_path, decoded_string, line_number, pattern_name))
                                break  # Break the loop if a match is found for any pattern

    return infected_code_list

def save_to_excel(infected_code_list, output_file):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    worksheet.append(["File Path", "Decoded String", "Line Number", "Matched Pattern"])

    for file_path, decoded_string, line_number, pattern_name in infected_code_list:
        worksheet.append([file_path, decoded_string, line_number, pattern_name])

    workbook.save(output_file)

if __name__ == "__main__":
    # Replace "your_directory_path" with the path to the directory containing PHP files to scan.
    directory_path = "/home/w3care/Desktop/python-ai/all_infected_code/"
    output_excel_file = "infected_code_list.xlsx"

    infected_code_list = find_infected_code_in_php(directory_path)
    save_to_excel(infected_code_list, output_excel_file)

    print("Infected code list has been saved to:", output_excel_file)
