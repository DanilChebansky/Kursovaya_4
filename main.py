from src.classes import HH
from src.classes import Vacancy
from src.classes import JsonEditor
from src.functions import user_interaction


# Словарь для ручного внесения вакансии в JSON-файл
vacancy_dict = {
    "name": "Test Name",
    "apply_alternate_url": "Test Url",
    "salary": {"from": 20, "to": 30},
    "snippet": {"requirement": "Test Requirements"},
    "experience": {"name": "Test Experience"},
    "area": {"name": "Test Area"},
    }

search_query = input("Введите поисковый запрос: ")
# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()

# Получение вакансий с hh.ru в формате JSON
hh_api.load_vacancies(search_query)
hh_vacancies = hh_api.vacancies

# Сохранение информации о вакансиях в файл
json_saver = JsonEditor(hh_vacancies)
json_saver.vacancy_adder(vacancy_dict)
json_saver.vacancy_deliter("Test Name")

# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

# Вывод топ-рейтинга вакансий по зарплате
user_interaction(vacancies_list)
