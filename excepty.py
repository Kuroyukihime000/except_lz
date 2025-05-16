import pandas as pd
import pandas.api.types as ptypes


class DataFrameStructureError(Exception):
    pass


class Dataframe:
    def __init__(self, filename):
        self.filename = filename
    def lol(self):
        try:
            self.df = pd.read_csv(filename)
            #print(self.df)
        except FileNotFoundError:
            print('Возникла следующая ошибка : [Errno 2] No such file or directory: "var8.csv')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка : Датафрейм пуст')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Структура датафрейма не соответсвует')
            raise SystemExit()
        try:
            self.column_list = self.df.columns.to_list()
            self.df_original = pd.read_csv('var8_original.csv')
            self.column_main = self.df_original.columns.to_list()
            if self.column_list != self.column_main:
                raise DataFrameStructureError('Возникла ошибка : структура файла не верная, ожидалось [Участники гражданского оборота,Тип операции,Сумма операции,Вид расчета,Место оплаты,Терминал оплаты,Дата оплаты,Время оплаты,Результат операции,Cash-back,Сумма cash-back]')
        except DataFrameStructureError:
            print('Please, remake your columns, we were waiting for', self.column_main, ', but you given', self.column_list)
        expected_types = {
            'Участники гражданского оборота': str,
            'Тип операции': str,
            'Сумма операции': float,
            'Вид расчета': str,
            'Место оплаты': str,
            'Терминал оплаты': str,
            'Дата оплаты': str,
            'Время оплаты': str,
            'Результат операции': str,
            'Cash-back': str,
            'Сумма cash-back': float
        }

        try:
            for column, expected_type in expected_types.items():
                if column in self.df.columns:
                    if not self.df[column].apply(lambda x: isinstance(x, expected_type)).all():
                        raise ValueError(f"Ошибка! В столбце '{column}' обнаружены значения, не соответствующие типу {expected_type.__name__}.")
        except ValueError as e:
            print(e)
            raise SystemExit()

