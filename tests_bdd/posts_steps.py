from pytest_bdd import given, when, then


@given("initial amount of post in Oxwall database", target_fixture="init_posts_result")
def initial_posts(app):
    return app.dashboard_page.posts


@given("I as a logged user", target_fixture="logged_user")
def logged_user(app, admin, logout):
    user = admin
    app.login(user.username, user.password)
    return user
    # app.logout()


@when("I add a new post with <text> in Dashboard page")
def create_post(app, text):
    app.dashboard_page.create_post(text)


@then("a new post block appears before old table of posts")
def wait_new_post(init_posts_result, app):
    app.dashboard_page.wait_new_post_appear(len(init_posts_result))


@then("this post block has this <text> and author as this user and time \"within 1 minute\"")
def verify_new_post(app, text, logged_user):
    new_post = app.dashboard_page.posts[0]
    assert new_post.text == text, f"Visible post text is not equal input text: {new_post.text} != {text}"
    assert new_post.user == logged_user, f"Visible user text is not logged user: {new_post.user} != {logged_user}"
    assert new_post.time == "within 1 minute", f"Post time is not 'within 1 minute: {new_post.time}'"
