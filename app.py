import streamlit as st
import pandas as pd

from analyzer import (
    load_logs,
    get_summary,
    detect_suspicious_ips,
    detect_brute_force,
    get_failed_by_ip,
    get_activity_by_hour,
)


st.set_page_config(
    page_title="Security Log Analyzer",
    page_icon="🛡️",
    layout="wide",
)


st.title("🛡️ Security Log Analyzer Dashboard")

st.write(
    "Analyze authentication logs and detect suspicious "
    "security activity."
)


uploaded_file = st.file_uploader(
    "Upload security log CSV",
    type=["csv"],
)


if uploaded_file is not None:
    df = load_logs(uploaded_file)

else:
    df = load_logs("sample_logs.csv")


summary = get_summary(df)


st.subheader("📊 Security Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    summary["total_events"],
)

col2.metric(
    "Successful Logins",
    summary["successful_logins"],
)

col3.metric(
    "Failed Logins",
    summary["failed_logins"],
)

col4.metric(
    "Unique IP Addresses",
    summary["unique_ips"],
)


st.divider()


st.subheader("🚨 Brute Force Detection")

brute_force = detect_brute_force(df)

if not brute_force.empty:

    st.error(
        f"{len(brute_force)} possible brute-force "
        "attack(s) detected."
    )

    st.dataframe(
        brute_force,
        use_container_width=True,
    )

else:

    st.success(
        "No brute-force activity detected."
    )


st.divider()


st.subheader("⚠️ Suspicious IP Addresses")

suspicious_ips = detect_suspicious_ips(df)

if not suspicious_ips.empty:

    st.dataframe(
        suspicious_ips,
        use_container_width=True,
    )

else:

    st.success(
        "No suspicious IP addresses detected."
    )


st.divider()


st.subheader("📈 Failed Login Attempts by IP")

failed_by_ip = get_failed_by_ip(df)

if not failed_by_ip.empty:

    st.bar_chart(
        failed_by_ip
    )


st.divider()


st.subheader("🕒 Security Events by Hour")

activity = get_activity_by_hour(df)

st.line_chart(
    activity.set_index("hour")
)


st.divider()


st.subheader("📋 Raw Security Logs")

status_filter = st.selectbox(
    "Filter by login status",
    [
        "ALL",
        "SUCCESS",
        "FAILED",
    ],
)


filtered_df = df.copy()

if status_filter != "ALL":

    filtered_df = df[
        df["status"] == status_filter
    ]


st.dataframe(
    filtered_df,
    use_container_width=True,
)


st.divider()


st.caption(
    "Security Log Analyzer | "
    "Educational Cybersecurity Portfolio Project"
)