import logging

import requests as re

from src.base_classes import Manager

logger_db_manager = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_db_manager.addHandler(file_handler)
logger_db_manager.setLevel(logging.INFO)


class DBManager(Manager):
    
    url: str

    def __init__(self, url):
        ''''''
        self.__url = url
        self.__params = {"text": "", "page": 1, "per_page": 10}
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__vacancies = []

    def __str__(self):
        ''''''
        pass

    def __call__(self, *args, **kwds):
        ''''''
        pass

    def get_companies_and_vacancies_count(self, vacancies: list = []):
        '''получает список всех вакансий с указанием названия компании, названия вакансии
        и зарплаты и ссылки на вакансию'''
        pass

    def get_all_vacancies(self):
        '''получает среднюю зарплату по вакансиям'''
        pass

    def get_avg_salary(self):
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'''
        salary_all = 0
        for i, value in enumerate(self.__vacancies):
            salary_all += f"{i + 1}. {value["name"]} {value["salary"]["from"]}\n"

    def get_vacancies_with_higher_salary(self, search_word: str = ""):
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова'''
        self.__params['text'] = search_word
        while self.__params.get("page") != 20:
            vacancies = []
            try:
                response = re.get(self.__url, headers=self.__headers, params=self.__params)
                if response.status_code == 200:
                    vacancies = response.json()["items"]

            except re.exceptions.ConnectionError:
                vacancies = []
                raise ConnectionError("Connection Error. Please check your network connection.")

            except re.exceptions.HTTPError:
                vacancies = []
                raise ValueError("HTTP Error. Please check the URL.")

            finally:
                logger_db_manager.info(f"Attempt to access API completed, returned:\n{vacancies[:50]}")

            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
            
            self.__drop_salary_null()
            
        return self.__vacancies

    def __drop_salary_null(self):
        for i, value in enumerate(self.__vacancies):
                try:
                    if value["salary"]["from"]:
                        value["salary"]["from"] = 0
                except TypeError:
                    if value["salary"]:
                        value["salary"] = {"from" : 0}
        return self.__vacancies

    def __making_a_convenient_list(self):
        result = []
        for vacanci in self.__vacancies:
            result.append(
                {
                "id" : vacanci["id"],
                "name" : vacanci["id"],
                "link" : vacanci["id"],
                "hirer" : vacanci["id"],
                "salary" : vacanci["id"],
                "requirements" : vacanci["id"],
                }
            )
