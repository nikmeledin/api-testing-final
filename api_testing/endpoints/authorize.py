import requests
import allure
from api_testing.endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):

    @allure.step('Authorize and verify that the token is valid/active')
    def authorize_and_check_token(self, payload=None):
        if self.token is None:
            self.response = requests.post(f'{self.url}/authorize', json=payload)
            self.data = self.response.json()
            self.token = self.data['token']
            return self.token
        else:
            self.response = requests.get(f'{self.url}/{self.token}')
            if self.response.status_code != 200:
                self.response = requests.post(f'{self.url}/authorize', json=payload)
                self.token = self.response.json()['token']
                return self.token
            else:
                return self.response.json()['token']
