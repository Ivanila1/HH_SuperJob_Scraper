from Scrapers.hh_scraper import HH_Scraper
from Scrapers.superjob_scraper import SuperJob_Scraper
from Upload_to_file.upload_to_json import JSON_Loader

hh_url = 'https://api.hh.ru/vacancies'
superjob_url = 'https://api.superjob.ru/2.0/vacancies/'

def user_interface():
    """Пользовательский интерфейс в консоли"""
    while True:
        user_vacancy = input("Введите название вакансии:\n0 - Выход\nВвод: ")
        if user_vacancy == "0":
            break
        hh = HH_Scraper(hh_url, user_vacancy)
        sj = SuperJob_Scraper(superjob_url, user_vacancy)
        user_action = input('Выберите действие:\n1 - Вывести вакансии в консоль\n2 - Загрузить вакансии в json файл\n3 - Вывести 2 самые высокооплачиваемые вакансии в консоль\n0 - Выход\nВвод: ')
        if user_action == "0":
            break
        user_town = input('Выбери область поиска:\n1 - Вся Россия\n2 - Москва\nВвод: ')

        if user_town == '1':
            if user_action == '1':
                '''Выводит все вакансии'''
                hh.rub_vacancies()
                sj.rub_vacancies()
            elif user_action == '2':
                """Добавляет все вакансии в json файл"""
                filename = input('Введите название файла: ')
                filename = filename + '.json'
                load = JSON_Loader(filename)
                load.write(hh.rub_vacancies("2"))
                print(f'Ваш файл: {filename}')
            elif user_action == '3':
                """Выводит 2 самых высокооплачиваемых среди всех"""
                hh_vacancies = hh.rub_vacancies("2")
                hh.best_vacancy(hh_vacancies)
                sj_vacancies = sj.rub_vacancies("2")
                sj.best_vacancy(sj_vacancies)

        elif user_town == '2':
            if user_action == '1':
                '''Выводит все Московские вакансии'''
                hh.rub_vacancies("1", "2")
                sj.rub_vacancies("1", "2")
            elif user_action == '2':
                """Добавляет все Московские вакансии в json файл"""
                filename = input('Введите название файла: ')
                filename = filename+'.json'
                load = JSON_Loader(filename)
                load.write(hh.rub_vacancies("2", "2"))
            elif user_action == '3':
                """Выводит 2 самых высокооплачиваемых среди Московских"""
                hh_vacancies = hh.rub_vacancies("2", "2")
                hh.best_vacancy(hh_vacancies)
                sj_vacancies = sj.rub_vacancies("2", "2")
                sj.best_vacancy(sj_vacancies)
