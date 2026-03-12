import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(
    page_title="GeoPulse AI",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("🌍 GeoPulse AI Intelligence Dashboard")
st.markdown("Real-Time Global Event Intelligence")

# ----------------------------
# Fetch Data From FastAPI
# ----------------------------

try:
    response = requests.get("http://127.0.0.1:8000/events")
    data = response.json()
    df = pd.DataFrame(data)

except:
    st.error("⚠ Could not connect to GeoPulse API. Showing demo data.")

    data = {
        "Country": ["China", "Russia", "USA", "India", "Iran"],
        "Event": [
            "Military Activity",
            "Economic Sanction",
            "Political Event",
            "Technology Policy",
            "Military Drill"
        ],
        "News": [
            "China deploys naval ships in the South China Sea amid rising regional tensions.",
            "Western countries announce new economic sanctions targeting Russian oil exports.",
            "Political debate intensifies in the United States over new foreign policy reforms.",
            "India introduces a new national policy for regulating artificial intelligence technologies.",
            "Iran conducts a large-scale military drill near the Persian Gulf."
        ],
        "Risk": [0.9, 0.7, 0.6, 0.5, 0.8]
    }

    df = pd.DataFrame(data)

# ----------------------------
# Country Coordinates (Map Fix)
# ----------------------------

country_coords = {
    "China": (35.8, 104.1),
    "Russia": (61.5, 105.3),
    "USA": (37.1, -95.7),
    "India": (20.6, 78.9),
    "Iran": (32.4, 53.7),
    "United Kingdom": (55.3, -3.4),
    "France": (46.2, 2.2),
    "Germany": (51.2, 10.4),
    "Japan": (36.2, 138.2),
    "Ukraine": (48.3, 31.1)
}

df["Latitude"] = df["Country"].map(lambda x: country_coords.get(x, (0,0))[0])
df["Longitude"] = df["Country"].map(lambda x: country_coords.get(x, (0,0))[1])

# ----------------------------
# Risk Priority Classification
# ----------------------------

def classify_risk(score):
    if score >= 0.8:
        return "HIGH"
    elif score >= 0.6:
        return "MEDIUM"
    else:
        return "LOW"

df["Priority"] = df["Risk"].apply(classify_risk)

df = df.sort_values(by="Risk", ascending=False)

# ----------------------------
# Intelligence Ticker
# ----------------------------

ticker_items = []

for _, row in df.head(10).iterrows():

    if row["Risk"] > 0.8:
        icon = "🔴"
    elif row["Risk"] > 0.6:
        icon = "🟠"
    else:
        icon = "🟢"

    ticker_items.append(f"{icon} {row['Country']} - {row['Event']}")

ticker_text = "  |  ".join(ticker_items)

st.markdown(
    f"""
    <div style="
        width:100%;
        overflow:hidden;
        white-space:nowrap;
        border-top:1px solid #333;
        border-bottom:1px solid #333;
        padding:8px;
        background:#0e1117;
        color:white;
        font-size:16px;
    ">
        <marquee behavior="scroll" direction="left" scrollamount="6">
            {ticker_text}
        </marquee>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Risk Filter
# ----------------------------

min_risk = st.slider("Minimum Risk Level", 0.0, 1.0, 0.4)
df = df[df["Risk"] >= min_risk]

# ----------------------------
# Layout
# ----------------------------

col1, col2 = st.columns([2, 1])

# ----------------------------
# Global Event Map
# ----------------------------

with col1:

    st.subheader("Global Event Map")

    fig = px.scatter_geo(
        df,
        lat="Latitude",
        lon="Longitude",
        color="Risk",
        hover_name="Country",
        hover_data=["Event","Risk"],
        size="Risk",
        projection="natural earth",
        title="Global Risk Distribution"
    )

    st.plotly_chart(fig, width="stretch")

# ----------------------------
# Scrollable Intelligence Feed
# ----------------------------

with col2:

    st.subheader("Live Intelligence Feed")

    feed_html = ""

    for _, row in df.iterrows():

        if row["Risk"] > 0.8:
            color = "🔴"
        elif row["Risk"] > 0.6:
            color = "🟠"
        else:
            color = "🟢"

        feed_html += f"""
        <div style="margin-bottom:12px;">
        <b>{color} {row['Event']}</b><br>
        Country: {row['Country']}<br>
        Priority: <b>{row['Priority']}</b><br>
        Risk Score: {row['Risk']}
        </div>
        """

    st.markdown(
        f"""
        <div style="
        height:420px;
        overflow-y:scroll;
        border:1px solid #333;
        border-radius:10px;
        padding:10px;">
        {feed_html}
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Strategic Alerts
# ----------------------------

st.subheader("🚨 Strategic Alerts (High Priority)")

high_priority = df[df["Priority"] == "HIGH"]

if high_priority.empty:
    st.info("No high priority alerts detected.")

else:

    for _, row in high_priority.iterrows():

        with st.expander(f"🔴 {row['Event']} - {row['Country']}"):

            st.write("**Risk Level:**", row["Risk"])
            st.write("**Priority:**", row["Priority"])

            st.markdown("### News Details")
            st.write(row["News"])

# ----------------------------
# Risk Analytics
# ----------------------------

st.subheader("Risk Analytics")

fig2 = px.bar(
    df,
    x="Country",
    y="Risk",
    color="Event",
    title="Risk Score by Country"
)

st.plotly_chart(fig2, width="stretch")

# ----------------------------
# Event Distribution
# ----------------------------

st.subheader("Event Distribution")

fig3 = px.pie(
    df,
    names="Event",
    title="Event Category Distribution"
)

st.plotly_chart(fig3, width="stretch")