import pandas as pd
import random
import datetime

def generate_casb_logs(num_records=100):
    sources = ['cloud', 'casb']
    users = ['alice', 'bob', 'charlie', 'dave']
    activities = {
        'cloud': ['login', 'config-change'],
        'casb': ['file-download', 'file-access']
    }
    details = {
        'login': ['successful', 'failed'],
        'config-change': ['permission_update', 'settings_update'],
        'file-download': ['confidential_report.pdf', 'large_dataset.zip', 'classified_strategy.docx'],
        'file-access': ['employee_data.xlsx', 'public_info.docx']
    }
    
    logs = []
    for i in range(num_records):
        src = random.choice(sources)
        activity = random.choice(activities[src])
        log = {
            "event_id": i + 1,
            "timestamp": datetime.datetime.now().isoformat(),
            "source": src,
            "user": random.choice(users),
            "activity": activity,
            "detail": random.choice(details[activity])
        }
        logs.append(log)
    return pd.DataFrame(logs)

if __name__ == '__main__':
    df = generate_casb_logs(10)
    print(df.head())
