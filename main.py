import logging

import requests as re


logger_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main():
    logger_main.info("Get started main")
    triger = True

    # Входные данные
    api_src = "https://api.hh.ru/vacancies"
    # Куда сохранить список вакансий, полученных из апи
    save_to_file = "data/vacancies_hh.json"
    # Куда сохранить список отсортированных и отфильтрованных вакансий
    save_to_file_sort = "data/selected_vacancies_hh.json"

    pattern = re.compile(r"[.,?]")

    while triger:

        user_choice = re.sub(
            pattern,
            "",
            (
                input(
                    "Привет! Добро пожаловать в программу подбора вакансий\n"
                    + """Выберите необходимый пункт меню:
    1. Запросить список вакансий по ключевому слову
    2. Выйти

    Введите номер варианта: """
                )
            ),
        ).lower()

        if user_choice == "1":
            logger_main.info("")

            to_filtring = re.sub(
                    pattern,
                    "",
                    (
                        input(
                            """             Если желаете отфильтровать по типу занятости, то
                введите параметр в точности:
                - Частичная занятость
                - Проектная работа
                - Полная занятость
                - Вахта
                - Гибрид
                - Удалённо
                - Разъездной
                - На месте работодателя
                или нажмите продолжть:\n"""
                        )
                    ),
                )
            logger_main.info(f"{to_filtring}")
            print("\nВозвращаюсь в главное меню\n")

        elif user_choice == "2":
            print("До следующей встречи)")
            triger = False
        else:
            print("Хм, кажется такого варианта у меня пока нет(")

    logger_main.info("End main")


if __name__ == "__main__":
    main()
