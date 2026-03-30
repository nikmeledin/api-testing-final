import requests
import allure
from api_testing.endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):

    @allure.step('Deleting a Meme')
    def delete_meme(self, headers, meme_id):
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)

    @allure.step('Check that the meme is deleted')
    def checking_if_the_meme_has_been_deleted(self, headers, meme_id):
        get_response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        assert get_response.status_code == 404
