from scheduler import scheduler
import numpy as np
import pandas as pd

schedule = scheduler()
print(schedule)
df = pd.DataFrame(schedule)
df.to_csv('data.csv', index=False, header=False)
