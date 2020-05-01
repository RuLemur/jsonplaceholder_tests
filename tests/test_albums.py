import allure
import pytest
from requests import codes

from framework.check import validate_response, ObjectType, \
    check_response_object_count, check_response_code, \
    validate_created_response, check_that_two_response_equals, \
    check_that_value_in_request_was_changed
from framework.helper import generate_album, generate_str


@allure.suite('Test Albums')
class TestAlbums:

    @allure.title('Positive. Response Get all albums is valid')
    def test_get_all_albums(self, api_client):
        response = api_client.albums.get_all_albums()
        validate_response(response, ObjectType.ALBUM)

    @allure.title('Positive. Check count in response get all albums')
    def test_count_get_all_albums(self, api_client):
        response = api_client.albums.get_all_albums()
        check_response_object_count(response, 100)

    @allure.title('Positive. Check count in response get album id')
    def test_count_get_album_by_id(self, api_client):
        response = api_client.albums.get_album_by_id(1)
        check_response_object_count(response, 1)

    @allure.title('Positive. Check valid response in get album id')
    def test_get_album_by_id(self, api_client):
        response = api_client.albums.get_all_albums()
        validate_response(response, ObjectType.ALBUM)

    @allure.title('Positive. Get not-existing album by id')
    def test_get_not_existing_album_by_id(self, api_client):
        response = api_client.albums.get_album_by_id(101)
        check_response_code(response, codes.not_found)

    @pytest.mark.parametrize("album_id,result",
                             [(0, codes.not_found),
                              (-4, codes.not_found),
                              ("aa", codes.not_found)])  # incorrect error
    @allure.title('Negative. Get album with incorrect id')
    def test_album_with_incorrect_id(self, api_client, album_id, result):
        response = api_client.albums.get_album_by_id(album_id)
        check_response_code(response, result)

    @pytest.mark.skip('We want get 404 error here')
    @allure.title('Positive. Get not-existing album by user_id')
    def test_get_not_existing_album_by_user_id(self, api_client):
        response = api_client.albums.get_albums_by_user_id(11)
        check_response_code(response, codes.not_found)

    @pytest.mark.parametrize("user_id,result",
                             [(0, codes.not_found),
                              (-4, codes.not_found),
                              ("aa", codes.not_found)])  # incorrect error
    @allure.title('Negative. Get album with incorrect user id')
    def test_album_with_incorrect_user_id(self, api_client, user_id, result):
        response = api_client.albums.get_album_by_id(user_id)
        check_response_code(response, result)

    @allure.title('Positive. Add new album')
    def test_add_new_album(self, api_client):
        new_album = generate_album(4)
        response = api_client.albums.add_album(new_album)
        validate_created_response(response, ObjectType.ALBUM)

    @allure.title('Positive. Update full album')
    def test_update_full_album(self, api_client):
        new_album = generate_album(11)
        response = api_client.albums.update_album(1, new_album)
        new_album["id"] = 1
        check_that_two_response_equals(response, new_album)

    @allure.title('Positive. Update half album')
    def test_update_album_partly(self, api_client):
        new_title = generate_str()
        response = api_client.albums.update_album_partly(1,
                                                         {"title": new_title})
        check_that_value_in_request_was_changed(response, "title", new_title)

    @allure.title('Positive. Delete album')
    def test_delete_album(self, api_client):
        response = api_client.albums.delete_album(1)
        check_response_code(response, codes.ok)

    @pytest.mark.skip('We want get 404 error here')
    @allure.title('Positive. Delete album')
    def test_delete_not_existing_album(self, api_client):
        response = api_client.albums.delete_album(101)
        check_response_code(response, codes.not_found)
