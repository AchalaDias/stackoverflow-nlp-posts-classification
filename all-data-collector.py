import requests
import pandas as pd
import time

# Replace with your actual access token and key
ACCESS_TOKEN = '<TOKEN>'
API_KEY = '<API-KEY>'

base_url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'nlp',
    'site': 'stackoverflow',
    'access_token': ACCESS_TOKEN,
    'key': API_KEY,
    'filter': 'withbody',
    'pagesize': 100,  # max allowed per request
    'page': 1
}

# Storage list
data = []

# Collect up to 10,000 results (max 100 per page)
for page in range(1, 101):
    print(f"Fetching page {page}...")
    params['page'] = page
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code)
        break

    items = response.json().get('items', [])
    if not items:
        break

    for item in items:
        title = item.get('title')
        body = item.get('body')
        tags = ', '.join(item.get('tags', []))
        accepted_answer_id = item.get('accepted_answer_id')
        view_count = item.get('view_count')
        creation_date = item.get('creation_date')

        # Fetch accepted answer content
        accepted_answer_body = ''
        if accepted_answer_id:
            answer_url = f"https://api.stackexchange.com/2.3/answers/{accepted_answer_id}"
            answer_params = {
                'site': 'stackoverflow',
                'access_token': ACCESS_TOKEN,
                'key': API_KEY,
                'filter': 'withbody'
            }
            ans_response = requests.get(answer_url, params=answer_params)
            if ans_response.status_code == 200:
                answers = ans_response.json().get('items', [])
                if answers:
                    accepted_answer_body = answers[0].get('body')

        data.append({
            'Title': title,
            'Description': body,
            'Tags': tags,
            'Accepted_Answer': accepted_answer_body,
            'View_Count': view_count,
            'Creation_Date': creation_date
        })

    time.sleep(1.5)  # Avoid hitting rate limits

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('./data/04.csv', index=False)
