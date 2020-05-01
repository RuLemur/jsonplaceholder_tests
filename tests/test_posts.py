import allure
import pytest
from requests import codes

from framework.check import validate_response, ObjectType, \
    check_response_object_count, check_response_code, \
    validate_created_response, check_that_two_response_equals, \
    check_that_value_in_request_was_changed
from framework.helper import generate_post, generate_str


@allure.suite('Test Posts')
class TestPosts:

    @allure.title('Positive. Response Get all posts is valid')
    def test_get_all_posts(self, api_client):
        response = api_client.posts.get_all_posts()
        validate_response(response, ObjectType.POST)

    @allure.title('Positive. Check count in response get all posts')
    def test_count_get_all_posts(self, api_client):
        response = api_client.posts.get_all_posts()
        check_response_object_count(response, 100)

    @allure.title('Positive. Check count in response get post id')
    def test_count_get_post_by_id(self, api_client):
        response = api_client.posts.get_post_by_id(1)
        check_response_object_count(response, 1)

    @allure.title('Positive. Check valid response in get post id')
    def test_get_post_by_id(self, api_client):
        response = api_client.posts.get_post_by_id(1)
        validate_response(response, ObjectType.POST)

    @allure.title('Positive. Get comments for post')
    def test_get_comments_by_post_id(self, api_client):
        response = api_client.posts.get_post_comments(1)
        validate_response(response, ObjectType.COMMENT)

    @allure.title('Positive. Get not-existing post by id')
    def test_get_not_existing_post_by_id(self, api_client):
        response = api_client.posts.get_post_by_id(101)
        check_response_code(response, codes.not_found)

    @pytest.mark.parametrize("post_id,result",
                             [(0, codes.not_found),
                              (-4, codes.not_found),
                              ("aa", codes.not_found)])  # incorrect error
    @allure.title('Negative. Get post with incorrect id')
    def test_post_with_incorrect_id(self, api_client, post_id, result):
        response = api_client.posts.get_post_by_id(post_id)
        check_response_code(response, result)

    @pytest.mark.skip('We want get 404 error here')
    @allure.title('Positive. Get not-existing post by user_id')
    def test_get_not_existing_post_by_user_id(self, api_client):
        response = api_client.posts.get_posts_by_user_id(11)
        check_response_code(response, codes.not_found)

    @pytest.mark.parametrize("user_id,result",
                             [(0, codes.not_found),
                              (-4, codes.not_found),
                              ("aa", codes.not_found)])  # incorrect error
    @allure.title('Negative. Get post with incorrect user id')
    def test_post_with_incorrect_user_id(self, api_client, user_id, result):
        response = api_client.posts.get_post_by_id(user_id)
        check_response_code(response, result)

    @allure.title('Positive. Add new post')
    def test_add_new_post(self, api_client):
        new_post = generate_post(4)
        response = api_client.posts.add_post(new_post)
        validate_created_response(response, ObjectType.POST)

    @allure.title('Positive. Update full post')
    def test_update_full_post(self, api_client):
        new_post = generate_post(11)
        response = api_client.posts.update_post(1, new_post)
        new_post["id"] = 1
        check_that_two_response_equals(response, new_post)

    @allure.title('Positive. Update half post')
    def test_update_post_partly(self, api_client):
        new_title = generate_str()
        response = api_client.posts.update_post_partly(1, {"title": new_title})
        check_that_value_in_request_was_changed(response, "title", new_title)

    @allure.title('Positive. Delete post')
    def test_delete_post(self, api_client):
        response = api_client.posts.delete_post(1)
        check_response_code(response, codes.ok)

    @pytest.mark.skip('We want get 404 error here')
    @allure.title('Positive. Delete post')
    def test_delete_not_existing_post(self, api_client):
        response = api_client.posts.delete_post(101)
        check_response_code(response, codes.not_found)
