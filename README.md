# cloud casb insider risk analyzer

This tool simulates the analysis of cloud access and casb logs to detect potential insider threats.
It generates synthetic logs, performs behavioral analytics to identify anomalies, visualizes risk trends,
and produces automated mitigation recommendations.

## Key Features
- Simulated cloud/SaaS log integration
- Behavioral analysis using rule-based/ML techniques
- Interactive risk visualization dashboard
- Automated mitigation suggestion generation

## Usage
1. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python src/main.py
```

## Repository Structure
```
cloud-casb-insider-risk-analyzer/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── simulated_casb_logs.csv
└── src/
    ├── main.py
    ├── cloud_data_generator.py
    ├── behavioral_analysis.py
    ├── dashboard.py
    └── mitigation_suggestions.py
```
requirements.txt: List dependencies (e.g., Flask, dash, pandas, scikit-learn, plotly, requests).

Example:
Flask==2.2.2
dash==2.9.0
pandas==1.5.3
plotly==5.13.1
scikit-learn==1.2.2
requests==2.28.2
