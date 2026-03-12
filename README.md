GeoPulse AI 🌍
Real-Time Global Ontology Intelligence Engine

GeoPulse AI is an AI-powered geopolitical intelligence platform that collects global information from multiple sources, processes it using Natural Language Processing, and generates structured intelligence insights through a knowledge graph and interactive dashboard.

The system analyzes news and global developments to detect events, evaluate risk levels, and visualize them through a modern intelligence dashboard.

🚀 Features
🌍 Global Event Map

Visualizes geopolitical events across the world using an interactive map.

📡 Live Intelligence Feed

Displays real-time global events detected from news sources.

🚨 Strategic Alerts

Highlights high-risk events with expandable details for deeper analysis.

📊 Risk Analytics

Analyzes geopolitical risk levels across different countries.

🔎 Event Detection

Uses NLP techniques to extract entities and detect event types from news articles.

🧠 Cross Verification Engine

Identifies similar events across different news sources to increase reliability.

🔗 Knowledge Graph Storage

Stores detected events and relationships inside a Neo4j graph database.

📺 Intelligence Ticker

Displays a scrolling news-style ticker similar to Bloomberg or CNN.

🧠 How It Works

The system processes data through several AI components:

News API
   ↓
Data Fetching
   ↓
NLP Processing
   ↓
Entity Extraction
   ↓
Event Detection
   ↓
Risk Scoring
   ↓
Knowledge Graph Storage
   ↓
FastAPI Backend
   ↓
Streamlit Intelligence Dashboard
🛠 Tech Stack
Backend

Python

FastAPI

Pandas

AI / NLP

spaCy

Sentence Transformers

Data Processing

Pandas

News APIs

Database

Neo4j Graph Database

Visualization

Streamlit

Plotly

📂 Project Structure
geopulse-ai
│
├── api
│   └── server.py
│
├── dashboard
│   └── app.py
│
├── data_fetcher
│   └── fetch_news.py
│
├── nlp_pipeline
│   └── entity_extraction.py
│
├── event_engine
│   ├── detect_events.py
│   └── verify_events.py
│
├── scoring
│   └── risk_score.py
│
├── graph_db
│   └── neo4j_store.py
│
├── main.py
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/geopulse-ai.git
cd geopulse-ai

Install dependencies:

pip install -r requirements.txt
▶️ Running the System
Step 1 — Run the Pipeline
python main.py

This will:

fetch news

detect events

calculate risk scores

generate events.csv

Step 2 — Start the API
uvicorn api.server:app --reload

API runs at:

http://127.0.0.1:8000
Step 3 — Launch Dashboard
streamlit run dashboard/app.py

The dashboard will open automatically in your browser.

📊 Dashboard Components

The intelligence dashboard includes:

Global Event Map

Live Intelligence Feed

Strategic Alert Panel

Risk Analytics Charts

Event Distribution

Intelligence News Ticker

🔮 Future Improvements

Planned upgrades include:

Global Risk Heatmap

AI-based Conflict Prediction

Automated Geopolitical Forecasting

Satellite and climate data integration

Real-time event streaming

Advanced knowledge graph exploration

🌎 Use Cases

GeoPulse AI can help:

Policy analysts

Researchers

Journalists

Intelligence analysts

Strategic planners

understand complex global developments through structured intelligence.

👨‍💻 Author

Shubham Raj,Kshitij Choudhary,Vishisht Magan

B.Tech CSE (AI & ML)
Manipal University Jaipur

Interests:

Artificial Intelligence

Machine Learning

Data Intelligence Systems

Geopolitical Analytics
