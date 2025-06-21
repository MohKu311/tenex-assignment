# log_parser.py

from ml.ml_inference import predict_threat_and_action

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

            # If action or threat_type is missing/blank, predict using ML
            if action.strip() == "" or threat_type.strip() == "":
                inferred_threat, inferred_action = predict_threat_and_action({
                    "source_ip": src_ip,
                    "dest_ip": dest_ip,
                    "url": url,
                    "status_code": status,
                    "user_agent": agent
                })
                action = inferred_action
                threat_type = inferred_threat

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
