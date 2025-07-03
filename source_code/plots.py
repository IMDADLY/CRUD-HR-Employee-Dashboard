import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.strip(df, x="lifeExp", hover_name='country')
fig.show()
