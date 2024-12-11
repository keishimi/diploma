import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

def create_and_save_seaborn_charts(filepath, output="outputs/seaborn_charts"):

    try:
        os.makedirs(output)
        df = pd.read_csv(filepath)
        required_cols = ['Survived', 'Sex', 'Age','Fare']
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Отсутствуют столбцы: {missing_cols}")
        
        # круговая диаграмма 
        plt.figure(figsize=(6, 6))
        survived_counts = df['Survived'].value_counts()
        plt.pie(survived_counts, labels=['Погибли', 'Выжили'], autopct='%1.1f%%', startangle=90) 
        plt.title('Выживаемость')
        plt.axis('equal') 
        plt.savefig(os.path.join(output, 'pie_chart_survival.png'))
        plt.close()
        
        # столбчатая диаграмма 
        plt.figure(figsize=(6, 6))
        sns.countplot(x='Sex', data=df, palette='pastel')
        plt.title('Распределение по полу')
        plt.savefig(os.path.join(output, 'bar_chart_sex.png'))
        plt.close()
        
        # точечная диаграмма
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='Age', y='Fare', data=df, alpha=0.7) 
        plt.title('Возраст и стоимость билета')
        plt.savefig(os.path.join(output, 'scatter_age_survival.png'))
        plt.close()

        print(f"Графики сохранены в '{output}'")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {filepath} пустой.")

filepath = 'titanic.csv' 
create_and_save_seaborn_charts(filepath)
    

