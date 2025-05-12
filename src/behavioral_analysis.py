import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def analyze_behavior(df):
    """
    Applies a basic behavioral analysis:
      - Flag unusual activity patterns (e.g., repeated downloads or a failed login followed by file access).
      - Use IsolationForest as a simple anomaly detector.
    """
    # Convert timestamp column if not already a datetime type
    if not np.issubdtype(df['timestamp'].dtype, np.datetime64):
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Create a simplified numeric feature: assign a numeric score to each activity type
    score_map = {'login': 10, 'config-change': 20, 'file-download': 40, 'file-access': 30}
    df['activity_score'] = df['activity'].map(score_map)
    
    # Use IsolationForest on the numeric feature to detect anomalies
    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly_flag'] = model.fit_predict(df[['activity_score']])
    
    # Simplistic risk summary: count anomalies per user
    risk_summary = df[df['anomaly_flag'] == -1].groupby('user').size().to_dict()
    
    return df, risk_summary

if __name__ == '__main__':
    import pandas as pd
    from cloud_data_generator import generate_casb_logs
    df_sample = generate_casb_logs(20)
    analyzed, summary = analyze_behavior(df_sample)
    print(analyzed[['event_id', 'user', 'activity', 'activity_score', 'anomaly_flag']])
    print("Risk Summary:", summary)
