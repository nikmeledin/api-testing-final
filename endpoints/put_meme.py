import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint):

    @allure.step('Put Meme')
    def put_meme(self, put_payload, headers, meme_id):
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=put_payload, headers=headers)
        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            return None
