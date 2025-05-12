import dash
from dash import dcc, html, dash_table
import plotly.express as px

def create_dashboard(df):
    app = dash.Dash(__name__)
    
    # Color anomalies differently
    df['status'] = df['anomaly_flag'].apply(lambda x: 'anomalous' if x == -1 else 'normal')
    
    # Create a time-series scatter plot to visualize activity scores
    fig = px.scatter(df, x='timestamp', y='activity_score', color='status',
                     title="Cloud/CASB Activity Risk Trends",
                     labels={"activity_score": "Risk Score", "timestamp": "Time"})
    
    app.layout = html.Div(children=[
        html.H1("Cloud & CASB Insider Risk Dashboard"),
        dash_table.DataTable(
            id='log-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])
    
    return app

if __name__ == '__main__':
    from cloud_data_generator import generate_casb_logs
    from behavioral_analysis import analyze_behavior
    import pandas as pd
    df = generate_casb_logs(20)
    df, _ = analyze_behavior(df)
    app = create_dashboard(df)
    app.run_server(debug=True)
