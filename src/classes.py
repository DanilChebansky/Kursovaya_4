import requests
import json
from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс для работы с API"""
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, "area": 113, "currency": "RUR"}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Ищет вакансии по ключевому слову на 20 страницах сайта"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class Vacancy:
    """Класс для перевода полученных с сайта вакансий в вид списка словарей"""
    @classmethod
    def cast_to_object_list(cls, list_):
        vacan_list = []
        for vacanc in list_:
            new_vacanc = cls(vacanc)
            vacan_list.append(new_vacanc.__dict__())
        return vacan_list

    def __init__(self, vocabul):
        self.name = vocabul["name"]
        self.url = vocabul['apply_alternate_url']
        self.salary = vocabul["salary"]
        self.requirements = vocabul["snippet"]["requirement"]
        self.experience = vocabul["experience"]["name"]
        self.area = vocabul["area"]["name"]
        if vocabul["salary"] is None:
            self.salary = "Зарплата не указана"
            self.mid_salary = 0
        elif vocabul["salary"] is not None and vocabul["salary"]["from"] is None:
            self.min_salary = 0
            self.max_salary = vocabul["salary"]["to"]
            self.mid_salary = (int(self.min_salary) + int(self.max_salary)) / 2
        elif vocabul["salary"] is not None and vocabul["salary"]["to"] is None:
            self.min_salary = vocabul["salary"]["from"]
            self.max_salary = 0
            self.mid_salary = vocabul["salary"]["from"]
        else:
            self.min_salary = vocabul["salary"]["from"]
            self.max_salary = vocabul["salary"]["to"]
            self.mid_salary = (int(self.min_salary) + int(self.max_salary)) / 2

    def __dict__(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "requirements": self.requirements,
            "experience": self.experience,
            "area": self.area,
            "mid_salary": self.mid_salary
        }


class HeadJsonEditor(ABC):
    """Родительский класс для редактирования вакансий в JSON-файле"""
    @abstractmethod
    def vacancy_adder(self, vacancy):
        pass

    @abstractmethod
    def vacancy_deliter(self, vacancy):
        pass

    @abstractmethod
    def vacancy_reader(self):
        pass


class JsonEditor(HeadJsonEditor):
    """Класс для сохранения вакансий в JSON-файл"""
    def __init__(self, vacancies):
        with open("vacancies.json", "w", encoding="utf-8") as editing_file:
            json.dump(vacancies, editing_file)

    def vacancy_adder(self, vacancy):
        """Добавляет вакансии в JSON-файл"""
        new_vacancy_list = []
        with open("vacancies.json", "r+", encoding="utf-8") as appending_vacancy:
            for vacanc in json.load(appending_vacancy):
                new_vacancy_list.append(vacanc)
            new_vacancy_list.append(vacancy)
        with open("vacancies.json", "w", encoding="utf-8") as appending_vacancy:
            appending_vacancy.write(json.dumps(new_vacancy_list))

    def vacancy_reader(self):
        """Выводит вакансии из JSON-файла"""
        with open("vacancies.json", encoding="utf-8") as reading_vacancy:
            return json.load(reading_vacancy)

    def vacancy_deliter(self, vacancy):
        """Удаляет выбранные вакансии в JSON-файле"""
        new_vacancy_list = []
        with open("vacancies.json", "r+", encoding="utf-8") as deliting_vacancy:
            for vacanc in json.load(deliting_vacancy):
                if vacancy in vacanc["name"]:
                    continue
                else:
                    new_vacancy_list.append(vacanc)
        with open("vacancies.json", "w", encoding="utf-8") as appending_vacancy:
            appending_vacancy.write(json.dumps(new_vacancy_list))
