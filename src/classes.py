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
