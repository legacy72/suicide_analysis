import json

from prepare_text import TextPreparation


class ComposeData:
    def __init__(self, mapping, file_write):
        self._mapping = mapping
        self._file_write = file_write

    def get_data_from_file(self):
        data_and_type_mapping = {}
        for file_name, type in self._mapping.items():
            with open(file_name) as file:
                data_and_type_mapping[type] = file.read()
        return data_and_type_mapping

    def write_data_to_file(self, data):
        with open(self._file_write, 'w',  encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)

    def get_data(self):
        training_data = {}

        data_and_type_mapping = self.get_data_from_file()
        for type, data_text in data_and_type_mapping.items():
            data_list = data_text.split('-------------------------------')
            training_data[type] = []
            for step, data in enumerate(data_list):
                if step % 1000 == 0:
                    print(f'STEP: {step}')
                if not data.strip():
                    continue
                tp = TextPreparation(data)
                prepared_data = tp.prepare_text()
                dict = {
                    'text': prepared_data,
                }
                training_data[type].append(dict)
        return training_data

    def fill_training_data(self):
        data = self.get_data()
        self.write_data_to_file(data)


if __name__ == '__main__':
    mapping = {
        'data/suicide_data.txt': 'suicide',
        'data/suicide_data2.txt': 'suicide',
        'data/normal_data.txt': 'normal',
    }
    file_write = 'data/training_data.json'

    cd = ComposeData(mapping, file_write)
    cd.fill_training_data()
