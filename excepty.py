import pandas as pd


class DataFrameStructureError(Exception):
    pass


class TypeError(Exception):
    pass


class Dataframe:
    def __init__(self, filename):
        self.filename = filename
    def lol(self):
        try:
            self.df = pd.read_csv(self.filename)
        except FileNotFoundError:
            print('Возникла следующая ошибка: Отсутствует файл: ', self.filename)
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка: Пустой файл')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Возникла следующая ошибка: Не соответствие колонок')
            raise SystemExit()
        try:
            self.column_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv('var8_original.csv')
            self.column_main = self.df_original.columns.to_list()
            if self.column_from_file != self.column_main:
                raise DataFrameStructureError('Возникла следующая ошибка: Названия столбцов не совпадают: \n' \
            'Ожидаемые: ', self.column_main,
            '\nПолученные: ', self.column_from_file)
        except DataFrameStructureError as e:
            print(e)
            raise SystemExit()
        try:
            self.file_types = self.df.dtypes
            self.file_types = str(self.file_types)
            self.main_types = self.df_original.dtypes
            self.main_types = str(self.main_types)
            if self.file_types != self.main_types:
                raise TypeError('Неверные типы данных')
            else:
                print('Чтение файла завершено успешно')
        except TypeError:
            print('Возникла следующая ошибка: Несовпадение типов данных с ожидаемыми: \n' \
            'Ожидалось: ', self.main_types,
            '\nПолучено: ', self.file_types)