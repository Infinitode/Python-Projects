import re
from collections import Counter


def parse_log_line(line):
    """
    Parses a single log line assuming a standard format:
    YYYY-MM-DD HH:MM:SS [LEVEL] Message
    Example: 2026-03-31 10:15:30 [ERROR] Database connection failed
    """
    log_pattern = r"^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[([A-Z]+)\]\s+(.*)$"
    match = re.match(log_pattern, line.strip())
    if match:
        timestamp, level, message = match.groups()
        return {
            "timestamp": timestamp,
            "level": level.upper(),
            "message": message
        }
    return None


def analyze_logs(log_lines):
    """
    Analyzes a list of log lines, returning frequency stats and parsed entries.
    """
    level_counts = Counter()
    parsed_logs = []

    for line in log_lines:
        entry = parse_log_line(line)
        if entry:
            level_counts[entry["level"]] += 1
            parsed_logs.append(entry)

    return level_counts, parsed_logs


def generate_report(level_counts, parsed_logs, filter_level=None):
    """
    Generates a formatted text summary report.
    """
    report = []
    report.append("=== Log Analysis Report ===")
    report.append(f"Total Log Entries Parsed: {len(parsed_logs)}")
    report.append("\nLog Counts by Level:")
    for level, count in level_counts.items():
        report.append(f"  {level:<8}: {count}")

    if filter_level:
        filter_level = filter_level.upper()
        report.append(f"\n--- Entries Matching Level: '{filter_level}' ---")
        filtered = [entry for entry in parsed_logs if entry["level"] == filter_level]
        if filtered:
            for entry in filtered:
                report.append(f"[{entry['timestamp']}] {entry['message']}")
        else:
            report.append("No log entries match the specified filter level.")

    return "\n".join(report)


if __name__ == "__main__":
    print("=== Log File Parser & Analyzer ===")

    # Sample log data for demonstration
    sample_logs = [
        "2026-03-31 08:00:01 [INFO] Server initialization started",
        "2026-03-31 08:00:05 [INFO] Database connected successfully",
        "2026-03-31 08:12:30 [WARNING] High memory usage detected (82%)",
        "2026-03-31 08:15:45 [ERROR] Failed to fetch user profile for ID 402",
        "2026-03-31 08:20:10 [INFO] User 105 logged in",
        "2026-03-31 08:35:12 [ERROR] Database timeout occurred",
        "2026-03-31 08:40:00 [CRITICAL] Out of memory exception",
        "2026-03-31 08:45:22 [INFO] Server health check passed"
    ]

    print("\nParsing sample log data...")
    counts, logs = analyze_logs(sample_logs)

    # Generate complete summary report
    summary = generate_report(counts, logs)
    print("\n" + summary)

    # Generate filtered report for ERROR level
    error_summary = generate_report(counts, logs, filter_level="ERROR")
    print("\n" + error_summary)
