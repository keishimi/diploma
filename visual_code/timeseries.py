import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os

def timeseries(filepath, output_dir="outputs/charts_ts"):
 
    try:
        df = pd.read_csv(filepath, parse_dates=['month'], dayfirst=True)
        os.makedirs(output_dir, exist_ok=True)

        columns_to_plot = ['Total_crimes', 'Serious', 'Huge_damage', '"Ecological"', 'Terrorism']

        # Matplotlib
        plt.figure(figsize=(12, 6))
        for col in columns_to_plot:
            plt.plot(df['month'], df[col], label=col)
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.title('Преступность в России: 2003 – 2020 годы (Matplotlib)')
        plt.legend()
        plt.savefig(os.path.join(output_dir, 'matplotlib_timeseries.png'))
        plt.close()

        # Seaborn
        plt.figure(figsize=(12, 6))
        for col in columns_to_plot:
            sns.lineplot(x='month', y=col, data=df, label=col)
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.title('Преступность в России: 2003 – 2020 годы (Seaborn)')
        plt.legend()
        plt.savefig(os.path.join(output_dir, 'seaborn_timeseries.png'))
        plt.close()

        # Plotly
        fig = go.Figure()
        for col in columns_to_plot:
            fig.add_trace(go.Scatter(x=df['month'], y=df[col], mode='lines+markers', name=col))
        fig.update_layout(title='Преступность в России: 2003 – 2020 годы(Plotly)', xaxis_title='Month', yaxis_title='Count')
        html_file = os.path.join(output_dir, "plotly_timeseries.html")
        fig.write_html(html_file)


    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {filepath} пустой.")

filepath = 'crime.csv'
timeseries(filepath)

