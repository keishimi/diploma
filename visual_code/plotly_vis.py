
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

def create_and_save_plotly_charts(filepath, output="outputs/plotly_charts.html"):

    try:
        df = pd.read_csv(filepath)
        required_cols = ['Survived', 'Sex', 'Age', 'Fare']
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Отсутствуют столбцы: {missing_cols}")

        #  фигура с подграфиками
        fig = make_subplots(rows=1, cols=3, subplot_titles=('Выживаемость', 'Распределение по полу', 'Возраст и стоимость билета'),
                            specs=[[{"type": "pie"}, {"type": "bar"}, {"type": "scatter"}]])
        # круговая диаграмма
        survived_counts = df['Survived'].value_counts()
        fig.add_trace(go.Pie(labels=['Погибли', 'Выжили'], values=survived_counts,
                             marker=dict(colors=px.colors.sequential.RdBu )), row=1, col=1)
        # столбчатая диаграмма
        sex_counts = df['Sex'].value_counts()
        fig.add_trace(go.Bar(x=sex_counts.index, y=sex_counts.values,
                             marker=dict(color=px.colors.qualitative.Set1)), row=1, col=2)

        # точечная диаграмма 
        fig.add_trace(go.Scatter(x=df['Age'], y=df['Fare'], mode='markers',
                                 marker=dict(color=df['Survived'], colorscale=px.colors.qualitative.Set2)), row=1, col=3)

        # HTML-файл
        fig.update_layout(title='Статистические данные', title_x=0.5, height=500, template='plotly_white')
        fig.write_html(output)
        print(f"Графики сохранены в '{output}'")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {filepath} пустой.")

filepath = 'titanic.csv' 
create_and_save_plotly_charts(filepath)    
