#!/usr/bin/python3
import sys

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")
        except (IndexError, ValueError):
            continue

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
