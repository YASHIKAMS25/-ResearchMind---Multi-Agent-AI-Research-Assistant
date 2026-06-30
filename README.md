🔬 ResearchMind - Multi-Agent AI Research Assistant

ResearchMind is a Multi-Agent AI Research System built using LangChain, Google Gemini, and Streamlit. Instead of relying on a single AI model, it uses multiple specialized AI agents that collaborate to search the web, extract information, generate a research report, and review the final output.

The project demonstrates how autonomous AI agents can work together to perform complex research tasks with minimal human intervention.

🚀 Features
🔍 Search Agent
Searches the web for recent and reliable information.
Collects relevant sources related to the research topic.
📄 Reader Agent
Selects the most relevant URL.
Scrapes and extracts detailed information from the webpage.
✍️ Writer Agent
Generates a professional research report.
Organizes the report into Introduction, Key Findings, Conclusion, and Sources.
🧐 Critic Agent
Reviews the generated report.
Provides a quality score, strengths, improvement suggestions, and overall verdict.
🎨 Modern Streamlit Interface
Beautiful responsive UI.
Live pipeline progress.
Expandable raw agent outputs.
Download final report as Markdown.
🏗️ Architecture
                 User
                   │
                   ▼
          Enter Research Topic
                   │
                   ▼
          🔍 Search Agent
                   │
                   ▼
          📄 Reader Agent
                   │
                   ▼
          ✍️ Writer Chain
                   │
                   ▼
          🧐 Critic Chain
                   │
                   ▼
        Final Research Report
🛠️ Tech Stack
Python
LangChain
Google Gemini 2.5 Flash
Streamlit
BeautifulSoup
Requests
dotenv
📂 Project Structure
researchmind/
│
├── app.py                 # Streamlit UI
├── main.py                # CLI research pipeline
├── agents.py              # AI Agents and Chains
├── tools.py               # Web search & scraping tools
├── requirements.txt
├── .env
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/researchmind.git

cd researchmind
2. Create Virtual Environment
Windows
python -m venv .venv

.venv\Scripts\activate
Linux / Mac
python3 -m venv .venv

source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Create .env
GOOGLE_API_KEY=YOUR_API_KEY
5. Run the Application
Streamlit UI
streamlit run app.py
Command Line Version
python main.py
🔄 Workflow
Step 1 — Search Agent
Searches the internet.
Finds reliable and recent information.
Returns search results.

↓

Step 2 — Reader Agent
Picks the best search result.
Scrapes detailed webpage content.
Extracts useful information.

↓

Step 3 — Writer Chain
Combines search results and scraped content.
Writes a complete research report.

↓

Step 4 — Critic Chain
Evaluates the report.
Gives:
Score
Strengths
Improvements
Final Verdict
📖 Example
Input
Topic:
Future of Quantum Computing
Output
Introduction

...

Key Findings

1.
2.
3.

Conclusion

...

Sources

https://...
https://...

Then the critic generates:

Score: 9/10

Strengths
- Well structured
- Accurate
- Clear explanations

Areas to Improve
- Add more recent statistics
- Include industry comparison

Verdict
High-quality research report.
📸 UI Preview

Add your application screenshot here.

README.md
images/
   └── app.png

Then include:

![ResearchMind UI](images/app.png)
📌 Future Improvements
PDF report export
Citation generation
Multi-source comparison
Vector database integration
Memory-enabled agents
Human-in-the-loop editing
Parallel agent execution using LangGraph
Research history dashboard
🎯 Learning Outcomes

This project demonstrates:

Building AI Agents with LangChain
Tool Calling
Prompt Engineering
Multi-Agent Workflows
Web Search Integration
Web Scraping
LLM Chains
Streamlit UI Development
AI Report Generation
Autonomous AI Pipelines
