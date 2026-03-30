import pytest
from api_testing.endpoints.base_endpoint import BaseEndpoint
from api_testing.endpoints.authorize import Authorize
from api_testing.endpoints.delete_meme import DeleteMeme
from api_testing.endpoints.get_all_meme import GetAllMeme
from api_testing.endpoints.get_meme_id import GetMemeID
from api_testing.endpoints.post_new_meme import PostNewMeme
from api_testing.endpoints.put_meme import PutMeme


@pytest.fixture
def payload():
    return {"name": "Jason Statham"}

@pytest.fixture
def post_payload():
    return {
    "text": "Возьми телефон, детка",
    "url": "https://i.ytimg.com/vi/lPr9iVqmAng/sddefault.jpg",
    "tags": ["Toxis, телефон, детка"],
    "info": {}
}

@pytest.fixture
def put_payload(post_new_meme, post_payload, headers, delete_meme):
    meme_id = post_new_meme.post_new_meme(post_payload, headers)['id']
    yield {
    "id": meme_id,
    "text": "test",
    "url": "https://i.ytimg.com/vi/lPr9iVqmAng/sddefault.jpg",
    "tags": ["Toxis, телефон, детка"],
    "info": {}
}
    delete_meme.delete_meme(headers, meme_id)

@pytest.fixture
def payload_no_required_fields():
    return {
        "tags": ["Test, qwe"],
        "info": {}
    }

@pytest.fixture
def invalid_headers():
    return {"Authorization": "invalid_token"}

@pytest.fixture
def headers(authoriz, payload):
    authoriz.authorize_and_check_token(payload)
    return {"Authorization": authoriz.token}

@pytest.fixture
def authoriz(payload):
    return Authorize()

@pytest.fixture
def get_base():
    return BaseEndpoint()

@pytest.fixture
def get_all_meme():
    return GetAllMeme()

@pytest.fixture
def get_meme_id():
    return GetMemeID()

@pytest.fixture
def post_new_meme():
    return PostNewMeme()

@pytest.fixture
def put_meme():
    return PutMeme()

@pytest.fixture
def delete_meme():
    return DeleteMeme()

@pytest.fixture
def create_meme(post_new_meme, headers, post_payload):
    meme_id = post_new_meme.post_new_meme(post_payload, headers)['id']
    return meme_id
