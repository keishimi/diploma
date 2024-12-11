import os
from visual_code.matplotlib_vis import create_and_save_matplotlib_charts
from visual_code.seaborn_vis import create_and_save_seaborn_charts
from visual_code.plotly_vis import create_and_save_plotly_charts
from visual_code.timeseries import timeseries

def main():
    print("Выберите модуль для сохранения графиков:")
    print("1. Matplotlib")
    print("2. Seaborn")
    print("3. Plotly")
    print("4. Timeseries")
    
    
    choice = input("Введите номер выбранного модуля (1/2/3/4): ")
    
    if choice == '1':
        create_and_save_matplotlib_charts()
        print("График Matplotlib успешно создан и сохранен!")
    elif choice == '2':
        create_and_save_seaborn_charts()
        print("График Seaborn успешно создан и сохранен!")
    elif choice == '3':
        create_and_save_plotly_charts()
        print("График Plotly успешно создан и сохранен!")
    elif choice == '4':
        timeseries()
        print("График Timeseries успешно создан и сохранен!")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")

if __name__ == "__main__":
    main()
