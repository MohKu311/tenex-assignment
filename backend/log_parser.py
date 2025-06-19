# log_parser.py

def parse_log(filepath: str) -> list[dict]:
    parsed_entries = []

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            parts = line.split(",")
            if len(parts) < 8:
                # Malformed entry
                parsed_entries.append({
                    "timestamp": parts[0] if len(parts) > 0 else "unknown",
                    "event": line,
                    "anomaly": True  # malformed lines = suspicious
                })
                continue

            # Unpack known format
            timestamp, src_ip, dest_ip, url, action, status, agent, threat_type = parts[:8]

            is_anomaly = (action.upper() == "BLOCK") or (threat_type.strip() != "-")

            parsed_entries.append({
                "timestamp": timestamp,
                "source_ip": src_ip,
                "destination_ip": dest_ip,
                "url": url,
                "action": action,
                "status_code": status,
                "user_agent": agent,
                "threat_type": threat_type,
                "anomaly": is_anomaly
            })

    return parsed_entries
