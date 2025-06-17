# log_parser.py

def parse_log(filepath: str) -> list[dict]:
    parsed_entries = []

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            # Example format: "2023-01-01T10:00:00 Login from 192.168.1.10"
            parts = line.split(" ", 1)
            if len(parts) == 2:
                timestamp, event = parts
                parsed_entries.append({
                    "timestamp": timestamp,
                    "event": event
                })
            else:
                parsed_entries.append({
                    "timestamp": "unknown",
                    "event": line
                })

    return parsed_entries
