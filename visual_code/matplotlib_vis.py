import matplotlib.pyplot as plt
import pandas as pd
import os

def create_and_save_matplotlib_charts(filepath, output="outputs/matplotlib_charts"):
    
    try:
        os.makedirs(output, exist_ok=True)
        df = pd.read_csv(filepath)
        required_cols = ['Survived', 'Sex', 'Age', 'Fare']
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            raise ValueError(f"В CSV-файле отсутствуют следующие столбцы: {missing_cols}")

        # круговая диаграмма 
        survived_counts = df['Survived'].value_counts()
        labels = ['Погибли', 'Выжили']
        sizes = [survived_counts[0], survived_counts[1]]
        plt.figure(figsize=(7, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Процент выживших и погибших пассажиров')
        plt.savefig(os.path.join(output, 'pie_chart_survival.png'))
        plt.close() 

        # столбчатая диаграмма 
        sex_counts = df['Sex'].value_counts()
        plt.figure(figsize=(7, 7))
        plt.bar(sex_counts.index, sex_counts.values)
        plt.xlabel('Пол')
        plt.ylabel('Количество')
        plt.title('Распределение по полу')
        plt.savefig(os.path.join(output, 'bar_chart_sex.png'))
        plt.close()

        # точечная диаграмма 
        plt.figure(figsize=(8, 6))
        plt.scatter(df['Age'], df['Fare'], alpha=0.5) 
        plt.xlabel('Возраст')
        plt.ylabel('Стоимость')
        plt.title('Возраст и стоимость билета')
        plt.savefig(os.path.join(output, 'scatter_age_survival.png'))
        plt.close()

        print(f"Графики успешно сохранены в папку '{output}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {filepath} пустой.")

filepath = 'titanic.csv' 
create_and_save_matplotlib_charts(filepath)

