import logging

from src.base_classes import Manager

logger_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


class DBManager(Manager):

    def __init__(self):
        '''получает список всех компаний и количество вакансий у каждой компании'''
        pass

    def __str__(self):
        '''получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию'''
        pass

    def __call__(self, *args, **kwds):
        '''получает среднюю зарплату по вакансиям'''
        pass

    def get_companies_and_vacancies_count():
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'''
        pass

    def get_all_vacancies():
        pass

    def get_avg_salary():
        pass

    def get_vacancies_with_higher_salary():
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python'''
        pass
