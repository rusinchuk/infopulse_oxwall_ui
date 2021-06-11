import pytest

input_data = ["Newly created post from Sergii"]

@pytest.mark.parametrize("input_text", input_data)
def test_post_create(app, login_user, input_text):
    old_number = len(app.posts())
    app.create_post(input_text)
    app.wait_new_post_appear(old_number)
    post_blocks = app.posts()
    assert input_text in post_blocks[0].text
