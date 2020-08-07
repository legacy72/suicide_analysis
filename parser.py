import vk_api
import requests
import bs4


LOGIN = ''  # paste your login here
PASSWORD = ''  # paste your password here


def vk_parse(file_name, owner_ids):
    vkp = VKParser(LOGIN, PASSWORD, file_name, owner_ids)
    vkp.parse()


class VKParser:
    def __init__(self, login, password, file_name, owner_ids=None):
        vk_session = self.authorization(login, password)
        self.tools = vk_api.VkTools(vk_session)
        self.file_name = file_name
        self.owner_ids = owner_ids

    @staticmethod
    def authorization(login, password):
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth(token_only=True)
        return vk_session

    def write_posts_from_club(self, owner_id):
        wall = self.tools.get_all(method='wall.get', max_count=100, values={'owner_id': owner_id})
        file = open(self.file_name, 'a')
        for w in wall['items']:
            if w['text']:
                file.write(w['text'] + '\n')
                file.write('-------------------------------\n')
        file.close()

    def parse(self):
        for owner_id in self.owner_ids:
            self.write_posts_from_club(owner_id)


class SiteParser:
    def __init__(self, site_url):
         self._site_url = site_url

    def get_content_from_page(self):
        content = requests.get(self._site_url)
        content.encoding = content.apparent_encoding
        return content.text

    def get_posts_from_page(self):
        soup = bs4.BeautifulSoup(self.get_content_from_page(), "html.parser")
        posts = soup.find_all('p', align="justify")

        return [post.text.strip() for post in posts if len(post.text) > 20]

    def write_posts_from_club(self):
        posts = self.get_posts_from_page()
        file = open('data/suicide_data2.txt', 'a')
        for post in posts:
            file.write(post + '\n')
            file.write('-------------------------------\n')
        file.close()


if __name__ == '__main__':
    sp = SiteParser('http://www.lossofsoul.com/DEATH/suicide/zapiski.htm')
    sp.write_posts_from_club()
