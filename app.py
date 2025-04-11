import dash
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Generate sample data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
values = np.random.normal(100, 15, len(dates))
df = pd.DataFrame({
    'Date': dates,
    'Value': values,
    'Category': np.random.choice(['A', 'B', 'C'], len(dates))
})

# Create visualizations
line_fig = px.line(df, x='Date', y='Value', title='Time Series Analysis')
box_fig = px.box(df, x='Category', y='Value', title='Distribution by Category')
scatter_fig = px.scatter(df, x='Date', y='Value', color='Category', 
                        title='Scatter Plot with Categories')

# Define the layout
app.layout = html.Div([
    html.H1('Interactive Data Visualization Dashboard',
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
    
    html.Div([
        html.Div([
            dcc.Graph(figure=line_fig)
        ], style={'width': '100%', 'marginBottom': 20}),
        
        html.Div([
            html.Div([
                dcc.Graph(figure=box_fig)
            ], style={'width': '48%', 'display': 'inline-block'}),
            
            html.Div([
                dcc.Graph(figure=scatter_fig)
            ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '4%'})
        ])
    ], style={'padding': '20px'})
], style={'backgroundColor': '#f7f9fc'})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8000, debug=True)
