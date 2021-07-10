from pathlib import Path
import re
from collections import OrderedDict
import pandas as pd


folder = Path('./scripts')
cool_counts = OrderedDict()
scripts = list(folder.glob('*.txt'))
scripts = sorted(scripts)
for script in scripts:
    cool_counts[script.stem] = 0
    with open(script, 'r') as file:
        for line in file:
            cool_counts[script.stem] += len(line.lower().split('cool')) - 1

df = pd.DataFrame({'episode': cool_counts.keys(), 'count': cool_counts.values()})
df.to_csv('cool_counts.csv', index=False)            