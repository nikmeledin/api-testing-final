payload = {"name": "Jason Statham"}

invalid_payload = [
    {},
    {"name": None},
    {"name": 123},
    {"name": True}
]


invalid_headers = {"Authorization": "invalid_token"}


post_payload = {
    "text": "Возьми телефон, детка",
    "url": "https://i.ytimg.com/vi/lPr9iVqmAng/sddefault.jpg",
    "tags": ["Toxis, телефон, детка"],
    "info": {}
}


payload_no_required_fields = {
        "tags": ["Test, qwe"],
        "info": {}
}


invalid_meme_scenarios = [
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
]


put_valid_sample = {
    "text": "Some text",
    "url": "https://i.pinimg.com/736x/63/bc/46/63bc46d981d842da09a7be778db76c49.jpg",
    "tags": ["tag1", "tag2"],
    "info": {}
}


invalid_put_payloads = [
    {**put_valid_sample, "text": None},
    {**put_valid_sample, "text": 123},
    {**put_valid_sample, "url": "not_a_url"},
    {**put_valid_sample, "tags": "not_a_list"},
    {**put_valid_sample, "info": "not_an_object"},
    {**put_valid_sample, "text": ""},
    {},
    {**put_valid_sample, "extra_field": "something"},
    {**put_valid_sample, "tags": [1, 2, 3]},
]
