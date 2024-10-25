#!/usr/bin/python3
import sys
import re

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        match = re.match(r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
