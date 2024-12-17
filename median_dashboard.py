import pandas as pd
import numpy as np
import altair as alt

data = pd.read_csv('bank-full.csv', delimiter = ';')

chart = alt.Chart(data).mark_point().encode( x='age', y='age' ) 
chart.show()
