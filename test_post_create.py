import pytest

input_data = ["Newly created post from Sergii", "One more comment"]

@pytest.mark.parametrize("input_text", input_data)
def test_post_create(app, login_user, input_text):
    old_number = len(app.posts())
    app.create_post(input_text)
    app.wait_new_post_appear(old_number)
    post_blocks = app.posts()
    assert input_text in post_blocks[0].text


@pytest.mark.parametrize("input_text", input_data)
def test_post_create2(app, login_user, input_text):
    old_number = len(app.dashboard_page.posts)
    app.dashboard_page.create_post(input_text)
    app.dashboard_page.wait_new_post_appear(old_number)
    new_post = app.dashboard_page.posts[0]
    assert new_post.text == input_text
    assert new_post.user == login_user
    # assert new_post.user.real_name == login_user.real_name
    assert new_post.time == "within 1 minute"


