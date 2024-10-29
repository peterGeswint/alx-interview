#!/usr/bin/python3
import sys
import re

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regex pattern to validate and extract data from lines in the correct format
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

try:
    for line in sys.stdin:
        # Match the line against the expected pattern
        match = pattern.match(line)
        if match:
            # Extract the status code and file size
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            
            # Update total file size
            total_file_size += file_size

            # Update status code count if it's one of the tracked codes
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")
except KeyboardInterrupt:
    pass
finally:
    # Print final stats on program exit or interruption
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
