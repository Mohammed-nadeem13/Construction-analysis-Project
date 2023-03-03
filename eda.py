import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(r"C:\Users\nadee\Documents\Project Construction analysis\data set1.csv")
df.dtypes
df.info

from pandas_profiling import ProfileReport
profile = ProfileReport(pd.read_csv(r"C:\Users\nadee\Documents\Project Construction analysis\data set1.csv"))
profile.to_file("output.html")


import sweetviz as sv
sweet_report = sv.analyze(pd.read_csv(r"C:\Users\nadee\Documents\Project Construction analysis\data set1.csv"))
sweet_report.show_html('sweet_report.html')

