import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):

    @allure.step('Deleting a Meme')
    def delete_meme(self, headers, meme_id):
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)

