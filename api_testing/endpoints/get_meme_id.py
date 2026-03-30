import requests
import allure
from api_testing.endpoints.base_endpoint import BaseEndpoint


class GetMemeID(BaseEndpoint):

    @allure.step('Get Meme ID')
    def get_meme_id(self, headers, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            return None
