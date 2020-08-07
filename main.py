from parser import vk_parse


if __name__ == '__main__':
    # suicide
    owner_ids = [-41708431, -160049741, -112451604, -118904273, -132718463, -165953887, -109151422]
    file_name = 'data/suicide_data.txt'
    vk_parse(file_name, owner_ids)

    # normal
    owner_ids = [-71729358]
    file_name = 'data/normal_data.txt'

    vk_parse(file_name, owner_ids)
