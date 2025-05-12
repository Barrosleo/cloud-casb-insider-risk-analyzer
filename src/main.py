from cloud_data_generator import generate_casb_logs
from behavioral_analysis import analyze_behavior
from dashboard import create_dashboard
from mitigation_suggestions import generate_mitigation_suggestions
import os

def main():
    # Ensure required directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # Step 1: Generate synthetic CASB logs and save to CSV
    logs_df = generate_casb_logs(250)
    logs_df.to_csv("data/simulated_casb_logs.csv", index=False)
    print("Simulated CASB logs generated.")
    
    # Step 2: Perform behavioral analysis to flag suspicious events
    analyzed_df, risk_summary = analyze_behavior(logs_df)
    print("Behavioral analysis complete. Risk summary:", risk_summary)
    
    # Step 3: Launch dashboard to visualize risk trends (runs on local web server)
    app = create_dashboard(analyzed_df)
    # Optionally, you could run the dashboard in a separate thread/process
    app.run_server(debug=True)
    
    # Step 4: Generate automated mitigation suggestions based on risk analysis
    suggestions = generate_mitigation_suggestions(risk_summary)
    print("Mitigation suggestions:", suggestions)

if __name__ == '__main__':
    main()
