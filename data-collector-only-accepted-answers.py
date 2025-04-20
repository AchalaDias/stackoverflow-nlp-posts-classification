import requests
import pandas as pd
import time

ACCESS_TOKEN = '<TOKEN>'
API_KEY = '<API-KEY>'

base_url = 'https://api.stackexchange.com/2.3/search/advanced'
params = {
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'nlp',
    'accepted': 'True',
    'site': 'stackoverflow',
    'key': API_KEY,
    'access_token': ACCESS_TOKEN,
    'filter': 'withbody',
    'pagesize': 100,
    'page': 1
}

data = []

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

    time.sleep(1.5)

df = pd.DataFrame(data)
df.to_csv('nlp_post_data_with_only_accepted_answers.csv', index=False)
print("Data saved to nlp_post_data_with_only_accepted_answers.csv")
