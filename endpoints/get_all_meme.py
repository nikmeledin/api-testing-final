import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):

    @allure.step('Get all meme')
    def get_all_meme(self, headers):
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            return None
