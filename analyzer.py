import pandas as pd


BRUTE_FORCE_THRESHOLD = 5


def load_logs(file):
    df = pd.read_csv(file)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def get_summary(df):
    total_events = len(df)

    successful_logins = len(
        df[df["status"] == "SUCCESS"]
    )

    failed_logins = len(
        df[df["status"] == "FAILED"]
    )

    unique_ips = df["ip_address"].nunique()

    return {
        "total_events": total_events,
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "unique_ips": unique_ips,
    }


def detect_suspicious_ips(df):
    failed = df[df["status"] == "FAILED"]

    failed_counts = (
        failed.groupby("ip_address")
        .size()
        .reset_index(name="failed_attempts")
    )

    failed_counts["severity"] = failed_counts[
        "failed_attempts"
    ].apply(calculate_severity)

    suspicious = failed_counts[
        failed_counts["failed_attempts"] >= 3
    ]

    return suspicious.sort_values(
        by="failed_attempts",
        ascending=False,
    )


def calculate_severity(count):
    if count >= 10:
        return "CRITICAL"

    elif count >= 7:
        return "HIGH"

    elif count >= 5:
        return "MEDIUM"

    elif count >= 3:
        return "LOW"

    return "INFO"


def detect_brute_force(df):
    failed = df[df["status"] == "FAILED"]

    attempts = (
        failed.groupby(["ip_address", "username"])
        .size()
        .reset_index(name="failed_attempts")
    )

    attacks = attempts[
        attempts["failed_attempts"]
        >= BRUTE_FORCE_THRESHOLD
    ].copy()

    if not attacks.empty:
        attacks["alert"] = "Possible Brute Force Attack"

    return attacks


def get_failed_by_ip(df):
    failed = df[df["status"] == "FAILED"]

    return (
        failed.groupby("ip_address")
        .size()
        .sort_values(ascending=False)
    )


def get_activity_by_hour(df):
    copy_df = df.copy()

    copy_df["hour"] = copy_df["timestamp"].dt.hour

    return (
        copy_df.groupby("hour")
        .size()
        .reset_index(name="events")
    )