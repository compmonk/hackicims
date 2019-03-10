from collections import Counter

import pandas as pd

applications = pd.read_json("../../data/applications.json")
people = pd.read_json("../../data/people.json")
jobs = pd.read_json("../../data/jobs.json")

master = people.merge(right=applications, how='inner', left_on='id', right_on='personId').merge(right=jobs, how='inner',
                                                                                                left_on='jobId',
                                                                                                right_on='id')
cities = pd.DataFrame(columns=['cities'], data=map(lambda x: x['city'], map(dict, master['address'])))

visual = master[['title', 'status']].join(cities)
# print visual

status = Counter(visual['status'])

status = pd.DataFrame(data=status.values(), index=status.keys())
# print status

plot = status.plot.pie(figsize=(5, 5), subplots=True)

# print visual['cities'].unique(), len(visual['cities'].unique())
# print visual['title'].unique(), len(visual['title'].unique())

print visual.groupyBy('cities')
