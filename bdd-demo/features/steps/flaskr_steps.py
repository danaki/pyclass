from behave import given, when, then
from hamcrest import assert_that, equal_to, contains_string
from pprint import pprint
import sys

@given('flaskr is setup')
def flask_setup(context):
    assert context.client and context.db

@given('i login with "{username}" and "{password}"')
@when('i login with "{username}" and "{password}"')
def login(context, username, password):
    context.page = context.client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

    assert_that(context.page.status_code, equal_to(200))

@when('i logout')
def logout(context):
    context.page = context.client.get('/logout', follow_redirects=True)
    assert_that(context.page.status_code, equal_to(200))

@then('i should see the alert "{message}"')
def logged_in(context, message):
    assert_that(str(context.page.data), contains_string(message))

@when('i create a post with title "{title}" and body "{text}"')
def create_post(context, title, text):
    context.page = context.client.post('/add', data=dict(
        title=title,
        text=text
    ), follow_redirects=True)

    assert_that(context.page.status_code, equal_to(200))

@then('i should see created post with title "{title}"')
def post_created(context, title):
    assert_that(str(context.page.data), contains_string(title))
