import pytest


def test_authoriz(authoriz, payload):
    authoriz.authorize_and_check_token(payload)
    authoriz.check_status_code(expected_code=200)
    authoriz.check_not_null()

def test_get_welcome_page(get_base):
    get_base.get_welcome_page()
    get_base.check_status_code(expected_code=200)

def test_get_all_meme(get_all_meme, headers):
    get_all_meme.get_all_meme(headers)
    get_all_meme.check_status_code(expected_code=200)
    get_all_meme.check_not_null()

def test_get_meme_id(get_meme_id, headers, create_meme, delete_meme):
    meme_id = create_meme
    get_meme_id.get_meme_id(headers, meme_id)
    get_meme_id.check_id(meme_id)
    get_meme_id.check_status_code(expected_code=200)
    get_meme_id.check_not_null()
    delete_meme.delete_meme(headers, meme_id)
    delete_meme.checking_if_the_meme_has_been_deleted(headers, meme_id)

def test_post_new_meme(post_new_meme, post_payload, headers, delete_meme):
    meme_data = post_new_meme.post_new_meme(post_payload, headers)
    meme_id = meme_data['id']
    post_new_meme.check_status_code(expected_code=200)
    post_new_meme.check_not_null()
    post_new_meme.check_payload(post_payload)
    delete_meme.delete_meme(headers, meme_id)
    delete_meme.checking_if_the_meme_has_been_deleted(headers, meme_id)

def test_post_new_meme_missing_required_fields(post_new_meme, headers, payload_no_required_fields):
    post_new_meme.post_new_meme(payload_no_required_fields, headers)
    post_new_meme.check_status_code(expected_code=400)

def test_put_meme(put_meme, headers, put_payload):
    meme_id = put_payload['id']
    put_meme.put_meme(put_payload, headers, meme_id)
    put_meme.check_status_code(expected_code=200)
    put_meme.check_not_null()
    put_meme.check_payload(put_payload)

def test_delete_meme(delete_meme, headers, create_meme):
    meme_id = create_meme
    delete_meme.delete_meme(headers, meme_id)
    delete_meme.check_status_code(expected_code=200)
    delete_meme.checking_if_the_meme_has_been_deleted(headers, meme_id)

def test_unauthorized_get(get_all_meme, invalid_headers):
    get_all_meme.get_all_meme(invalid_headers)
    get_all_meme.check_status_code(expected_code=401)

def test_unauthorized_post(post_new_meme, post_payload, invalid_headers):
    post_new_meme.post_new_meme(post_payload, invalid_headers)
    post_new_meme.check_status_code(expected_code=401)

def test_unauthorized_put(put_meme, invalid_headers, put_payload):
    meme_id = put_payload['id']
    put_meme.put_meme(put_payload, invalid_headers, meme_id)
    put_meme.check_status_code(expected_code=401)

def test_unauthorized_delete(delete_meme, invalid_headers, create_meme, headers):
    meme_id = create_meme
    delete_meme.delete_meme(invalid_headers, meme_id)
    delete_meme.check_status_code(expected_code=401)
    delete_meme.delete_meme(headers, meme_id)

@pytest.mark.parametrize("test_scenario,invalid_payload", [
    ("missing_text", {
        "url": "https://brobible.com/wp-content/uploads/2025/12/funniest-meme-2026-is-coming.jpg",
        "tags": ["test"],
        "info": {}
    }),
    ("missing_url", {
        "text": "Sample text",
        "tags": ["test"],
        "info": {}
    }),
    ("missing_tags", {
        "text": "Sample text",
        "url": "https://i.pinimg.com/736x/c1/fb/20/c1fb20e5dcc1b2883b600cb6b4a9f72a.jpg",
        "info": {}
    }),
    ("missing_info", {
        "text": "Sample text",
        "url": "https://example.com/meme.jpg",
        "tags": ["test"]
    }),
    ("tags_as_string", {
        "text": "Sample text",
        "url": "https://i.pinimg.com/736x/b7/de/f0/b7def07ff211ffd30822f52b20451363.jpg",
        "tags": "not_a_list",
        "info": {}
    }),
    ("info_as_list", {
        "text": "Sample text",
        "url": "https://i.pinimg.com/736x/a9/e5/a2/a9e5a2d5aaa1f28338356244a195a0b2.jpg",
        "tags": ["test"],
        "info": ["not_an_object"]
    }),
    ("text_as_number", {
        "text": 123,
        "url": "https://i.pinimg.com/736x/63/bc/46/63bc46d981d842da09a7be778db76c49.jpg",
        "tags": ["test"],
        "info": {}
    }),
    ("url_as_number", {
        "text": "Sample text",
        "url": 123,
        "tags": ["test"],
        "info": {}
    }),
])
def test_post_new_meme_invalid_payload(post_new_meme, headers, invalid_payload, test_scenario):
    post_new_meme.post_new_meme(invalid_payload, headers)
    post_new_meme.check_status_code(expected_code=400)
