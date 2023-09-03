from abc import ABC, abstractmethod
import json
class Scraper(ABC):
    @abstractmethod
    def __init__(self, url, profession):
        """Иницилизируется по ссылке и проффессии"""
        self.url = url
        self.profession = profession
        self.data = []

    def __str__(self):
        return self.url

    def __repr__(self):
        return json.dumps(self.data, indent=2, ensure_ascii=False)

    def best_vacancy(self, vacancy):
        """Перебирает все вакансии и выводит самую высокооплачиваемую"""
        best_vacancy = None
        salary = 0
        for i in range(len(vacancy)):
            if salary < vacancy[i]["salary"]:
                salary = vacancy[i]["salary"]
                best_vacancy = vacancy[i]
            i += 1
        print(f'id: {best_vacancy["id"]}\n'
                    f'Проффесия: {best_vacancy["vacancy"]}\n'
                    f'Зарплата: от {best_vacancy["salary"]} рублей\n'
                    f'Город: {best_vacancy["town"]}\n'
                    f'Ссылка: {best_vacancy["link"]}\n')
