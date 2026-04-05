import requests
import allure


class BaseEndpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    response = None
    data = None
    token = None
    id = None
    body_without_id = None

    @allure.step('Get a welcome page')
    def get_welcome_page(self, welcome_text = "Hi there! That's a simple API We are tracking memes here."):
        self.response = requests.get(self.url)
        text = self.response.text
        if '<!--' in text:
            text = text.split('<!--')[0]
        cleaned = text.replace('<br>', '')
        cleaned = ' '.join(cleaned.split())
        assert cleaned == welcome_text

    @allure.step('Check that the HTTP status code')
    def check_status_code(self, expected_code):
        assert self.response.status_code == expected_code

    @allure.step('Check that the ID is valid')
    def check_id(self, meme_id):
        assert self.response.json()['id'] == meme_id

    @allure.step('Check that the answer is not empty')
    def check_not_null(self):
        if self.response.status_code == 200:
            self.data = self.response.json()
            assert len(self.data) > 0

    @allure.step('Check valid payload')
    def check_payload(self, put_payload):
        assert self.data['url'] == put_payload['url']
        assert self.data['text'] == put_payload['text']
        assert self.data['tags'] == put_payload['tags']
        assert self.data['info'] == put_payload['info']
