import requests
import allure
from endpoints.base_endpoint import BaseEndpoint
import data


class Authorize(BaseEndpoint):

    @allure.step('Authorize and verify that the token is valid/active')
    def authorize_and_check_token(self, payload):
        if self.token is None:
            self.response = requests.post(f'{self.url}/authorize', json=payload)
            if self.response.status_code == 200:
                self.data = self.response.json()
                self.token = self.data['token']
                return self.token
            else:
                self.data = None
                return None
        else:
            self.response = requests.get(f'{self.url}/{self.token}')
            if self.response.status_code != 200:
                self.response = requests.post(f'{self.url}/authorize/{self.token}', json=payload)
                if self.response.status_code == 200:
                    self.token = self.response.json()['token']
                    return self.token
                else:
                    self.data = None
                    return None
            else:
                return self.response.json()['token']

    @allure.step('')
    def check_token_life(self, expected_code):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        assert self.response.status_code == expected_code
        return self.response.text

    @allure.step('Verify token alive message')
    def check_token_life_message(self, payload):
        assert self.response.text == f"Token is alive. Username is {payload['name']}"

    @allure.step('Check token validity with provided token')
    def check_token_life_by_token(self, token, expected_code):
        self.response = requests.get(f'{self.url}/authorize/{token}')
        assert self.response.status_code == expected_code
