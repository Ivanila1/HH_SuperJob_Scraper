import requests
from Scrapers.base_scraper import Scraper
import os

class SuperJob_Scraper(Scraper):
    def __init__(self, url, profession):
        super().__init__(url, profession)
        superjob_code = os.getenv('SUPERJOB_CODE')
        self._params = {"keywords": [[1, profession]],
                        "count": 100,
                        }
        self.headers = {'X-Api-App-Id': superjob_code}
        response = requests.get(self.url, headers=self.headers, params=self._params)
        self.data = response.json()['objects']

    def rub_vacancies(self, mode="1", town='1'):
        """Переберает вакансии с зп в рублях и дает выбрать действие с вакансией и город вакасии"""
        vacancies = []
        for i in range(len(self.data)):
            if self.data[i]["currency"] == "rub":
                if self.data[i]["payment_from"] > 0:
                    if town == '1':
                        if mode == '1':
                            print(f'id: {self.data[i]["id"]}\n'
                        f'Проффесия: {self.data[i]["profession"]}\n'
                        f'Зарплата: от {self.data[i]["payment_from"]} рублей\n'
                        f'Город: {self.data[i]["town"]["title"]}\n'
                        f'Ссылка: {self.data[i]["link"]}\n')

                        elif mode == '2':
                            vacancies.append(
                                    {
                                        "id": int(self.data[i]["id"]),
                                        "vacancy": self.data[i]["profession"],
                                        "salary": self.data[i]["payment_from"],
                                        "town": self.data[i]["town"]["title"],
                                        "link": self.data[i]["link"]
                                    }
                                        )
                    elif town == '2':
                        if self.data[i]["town"]["title"] == "Москва":
                            if mode == '1':
                                print(f'id: {self.data[i]["id"]}\n'
                        f'Проффесия: {self.data[i]["profession"]}\n'
                        f'Зарплата: от {self.data[i]["payment_from"]} рублей\n'
                        f'Город: {self.data[i]["town"]["title"]}\n'
                        f'Ссылка: {self.data[i]["link"]}\n')

                            elif mode == '2':
                                vacancies.append(
                                    {
                                        "id": int(self.data[i]["id"]),
                                        "vacancy": self.data[i]["profession"],
                                        "salary": self.data[i]["payment_from"],
                                        "town": self.data[i]["town"]["title"],
                                        "link": self.data[i]["link"]
                                    }
                                        )

        if mode == '2':
            return vacancies
