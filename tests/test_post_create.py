import pytest
import json
import os.path
from conftest import PROJECT_DIR
from data.random_string import random_string2

file_name = os.path.join(PROJECT_DIR, "data", "post_positive_data.json")

with open(file_name, encoding="utf8") as f:
    input_data = json.load(f)

for _ in range(3):
    input_data.append(random_string2(cyr=True, spaces=True))

# @pytest.mark.parametrize("input_text", input_data)
# def test_post_create(app, login_user, input_text):
#     old_number = len(app.posts())
#     app.create_post(input_text)
#     app.wait_new_post_appear(old_number)
#     post_blocks = app.posts()
#     assert input_text in post_blocks[0].text


@pytest.mark.parametrize("input_text", input_data, ids=input_data)
def test_post_create2(app, login_user, input_text, db, delete_post):
    old_number = len(app.dashboard_page.posts)
    app.dashboard_page.create_post(input_text)
    app.dashboard_page.wait_new_post_appear(old_number)
    assert db.get_last_text_post() == input_text
    new_post = app.dashboard_page.posts[0]
    assert new_post.text == input_text
    assert new_post.user == login_user
    # assert new_post.user.real_name == login_user.real_name
    assert new_post.time == "within 1 minute"
