import requests
from Scrapers.base_scraper import Scraper


class HH_Scraper(Scraper):
    def __init__(self, url, profession):
        super().__init__(url, profession)
        self.__params = {
            'text': profession,
            'per_page': 100,
            'only_with_salary': True
        }
        response = requests.get(self.url, params=self.__params)
        self.data = response.json()["items"]


    def rub_vacancies(self, mode="1", town='1'):
        """Переберает вакансии с зп в рублях и дает выбрать действие с вакансией и город вакасии"""
        vacancies = []
        for i in range(len(self.data)):
            if self.data[i]['salary']['from']:
                if self.data[i]["salary"]["currency"] == "RUR":
                    if town == '1':
                        if mode == '1':
                            print(f'id: {self.data[i]["id"]}\n'
                            f'Проффесия: {self.data[i]["name"]}\n'
                            f'Зарплата: от {self.data[i]["salary"]["from"]} рублей\n'
                            f'Город: {self.data[i]["area"]["name"]}\n'
                            f'Требования: {self.data[i]["snippet"]["requirement"]}\n'
                            f'Ссылка: {self.data[i]["alternate_url"]}\n')
                        elif mode == '2':
                            vacancies.append(
                                    {
                                        "id": int(self.data[i]["id"]),
                                        "vacancy": self.data[i]["name"],
                                        "salary": self.data[i]["salary"]["from"],
                                        "town": self.data[i]["area"]["name"],
                                        "link": self.data[i]["alternate_url"]
                                    }
                                        )
                    elif town == '2':
                        if self.data[i]["area"]["name"] == "Москва":
                            if mode == '1':
                                print(f'id: {self.data[i]["id"]}\n'
                            f'Проффесия: {self.data[i]["name"]}\n'
                            f'Зарплата: от {self.data[i]["salary"]["from"]} рублей\n'
                            f'Город: {self.data[i]["area"]["name"]}\n'
                            f'Требования: {self.data[i]["snippet"]["requirement"]}\n'
                            f'Ссылка: {self.data[i]["alternate_url"]}\n')
                            elif mode == '2':
                                vacancies.append(
                                    {
                                        "id": int(self.data[i]["id"]),
                                        "vacancy": self.data[i]["name"],
                                        "salary": self.data[i]["salary"]["from"],
                                        "town": self.data[i]["area"]["name"],
                                        "link": self.data[i]["alternate_url"]
                                    }
                                        )

        if mode == '2':
            return vacancies
