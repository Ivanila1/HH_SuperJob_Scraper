import json

class JSON_Loader:
    def __init__(self, filename):
        """Инициализация класса JSON_Loader"""
        self.filename = filename

    def write(self, vacancy):
        """Метод для записи файла"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json_list = json.dumps(vacancy, indent=2, ensure_ascii=False)
            file.write(f'{json_list}')
