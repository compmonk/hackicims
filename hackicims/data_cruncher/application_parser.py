from collections import Counter

import pandas as pd

applications = pd.read_json("../../data/applications.json")
print Counter(applications['status'])
