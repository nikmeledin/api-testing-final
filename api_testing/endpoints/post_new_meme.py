import requests
import allure
from api_testing.endpoints.base_endpoint import BaseEndpoint


class PostNewMeme(BaseEndpoint):

    @allure.step('Post New Meme')
    def post_new_meme(self, post_payload, headers):
        self.response = requests.post(f'{self.url}/meme', json=post_payload,headers=headers)
        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            return None
