import re
import datetime
import argparse

timestamp_pattern = re.compile(r"(\d{4}-\d{2}-\d{2}-\d{2}:\d{2}:\d{2}\.\d{6})")

def filter_logs(log_file_path, regex_str):
    # Compile the regular expression for better performance
    pattern = re.compile(regex_str)
    
    prev_timestamp = None
    
    # Open the file and process line by line
    with open(log_file_path, "r") as file:
        for line in file:
            if pattern.search(line):
                # Extract timestamp from the line
                match = timestamp_pattern.search(line)
                if match:
                    curr_timestamp = datetime.datetime.strptime(match.group(1), '%Y-%m-%d-%H:%M:%S.%f')
                    if prev_timestamp:
                        time_diff = (curr_timestamp - prev_timestamp).total_seconds() * 1000
                        print(f"{line.strip()} | Time Difference: {time_diff:.2f} ms")
                    else:
                        print(line.strip())
                    prev_timestamp = curr_timestamp

def main():
    parser = argparse.ArgumentParser(description="get params")
    parser.add_argument('-f', '--file', type=str, required=True, help='log file path')
    parser.add_argument('-r', '--regex', type=str, required=True, help='regex pattern')
    args = parser.parse_args()

    filter_logs(args.file, args.regex)
    # print(matching_lines)

if __name__ == "__main__":
    main()
