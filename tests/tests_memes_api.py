import pytest
import data
from endpoints import delete_meme


### Тест авторизации
def test_authoriz(authoriz, payload):
    authoriz.authorize_and_check_token(payload)
    authoriz.check_status_code(expected_code=200)
    authoriz.check_not_null()

### Тест получения приветственной страницы
def test_get_welcome_page(get_base):
    get_base.get_welcome_page()
    get_base.check_status_code(expected_code=200)

### Тест получения всех мемов
def test_get_all_meme(get_all_meme, headers):
    get_all_meme.get_all_meme(headers)
    get_all_meme.check_status_code(expected_code=200)
    get_all_meme.check_not_null()

### Тест получения мема по ID
def test_get_meme_id(get_meme_id, headers, create_and_delete_meme):
    get_meme_id.get_meme_id(headers, create_and_delete_meme)
    get_meme_id.check_id(create_and_delete_meme)
    get_meme_id.check_status_code(expected_code=200)
    get_meme_id.check_not_null()

### ТЕст создания нового мема
def test_post_new_meme(post_new_meme, post_payload, headers, delete_meme):
    response = post_new_meme.post_new_meme(post_payload, headers)
    meme_id = response['id']
    post_new_meme.check_status_code(expected_code=200)
    post_new_meme.check_not_null()
    post_new_meme.check_payload(post_payload)
    delete_meme.delete_meme(headers, meme_id)

### Тест создания нового мема без обязательных полей
def test_post_new_meme_missing_required_fields(post_new_meme, headers, payload_no_required_fields):
    post_new_meme.post_new_meme(payload_no_required_fields, headers)
    post_new_meme.check_status_code(expected_code=400)

### Тест изменения мема
def test_put_meme(put_meme, headers, put_payload):
    meme_id = put_payload['id']
    put_meme.put_meme(put_payload, headers, meme_id)
    put_meme.check_status_code(expected_code=200)
    put_meme.check_not_null()
    put_meme.check_payload(put_payload)

### Тест удаления мема
def test_delete_meme(delete_meme, headers, post_new_meme, post_payload):
    meme_data = post_new_meme.post_new_meme(post_payload, headers)
    meme_id = meme_data['id']
    delete_meme.delete_meme(headers, meme_id)
    delete_meme.check_status_code(expected_code=200)

### Тест получения мемов без авторизации
def test_unauthorized_get(get_all_meme, invalid_headers):
    get_all_meme.get_all_meme(invalid_headers)
    get_all_meme.check_status_code(expected_code=401)

### Тест создания мема без авторизации
def test_unauthorized_post(post_new_meme, post_payload, invalid_headers):
    post_new_meme.post_new_meme(post_payload, invalid_headers)
    post_new_meme.check_status_code(expected_code=401)

### Тест изменения мема без авторизации
def test_unauthorized_put(put_meme, invalid_headers, put_payload):
    meme_id = put_payload['id']
    put_meme.put_meme(put_payload, invalid_headers, meme_id)
    put_meme.check_status_code(expected_code=401)

### тест удаления мема без авторизации
def test_unauthorized_delete(delete_meme, invalid_headers, create_and_delete_meme, headers):
    meme_id = create_and_delete_meme
    delete_meme.delete_meme(invalid_headers, meme_id)
    delete_meme.check_status_code(expected_code=401)

### Тест создания мема с невалидным телом
@pytest.mark.parametrize("test_scenario,invalid_payload", data.invalid_meme_scenarios)
def test_post_new_meme_invalid_payload(post_new_meme, headers, invalid_payload, test_scenario):
    post_new_meme.post_new_meme(invalid_payload, headers)
    post_new_meme.check_status_code(expected_code=400)

### Тест невалидной авторизации
@pytest.mark.parametrize("invalid_payload", data.invalid_payload)
def test_authoriz_neg(authoriz, invalid_payload):
    authoriz.authorize_and_check_token(invalid_payload)
    authoriz.check_status_code(expected_code=400)
    authoriz.check_not_null()

### Тест на получение мема с несуществующим ID
def test_get_invalid_id(get_meme_id, headers):
    get_meme_id.get_meme_id(headers, meme_id=100500)
    get_meme_id.check_status_code(expected_code=404)

### Тест на изменения мема с несуществующим ID
def test_put_meme_not_found(put_meme, headers, put_payload):
    put_meme.put_meme(put_payload, headers, meme_id=100500)
    put_meme.check_status_code(expected_code=404)

### Тест на изменение мема с невалидным телом
@pytest.mark.parametrize("invalid_payload", data.invalid_put_payloads)
def test_put_meme_invalid_payload(put_meme, headers, create_and_delete_meme, invalid_payload):
    put_meme.put_meme(invalid_payload, headers, create_and_delete_meme)
    put_meme.check_status_code(expected_code=400)

### Тест на удаления мема с несуществующим ID
def test_delete_meme_invalid_id(headers, delete_meme):
    delete_meme.delete_meme(headers, meme_id=100500)
    delete_meme.check_status_code(expected_code=404)

### Тест на проверку жизни токена
def test_check_token_life(authoriz, payload):
    authoriz.authorize_and_check_token(payload)
    authoriz.check_token_life(expected_code=200)
    authoriz.check_token_life_message(payload)

### Тест на проверку жизни устаревшего токена (невалидного)
def test_invalid_token_not_alive(authoriz):
    authoriz.check_token_life_by_token(token='qwertyuyuiuyiouio', expected_code=404)
