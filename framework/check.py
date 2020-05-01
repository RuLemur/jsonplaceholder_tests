import allure
from deepdiff import DeepDiff
from hamcrest import assert_that, equal_to
from requests import codes
from framework.validator import validate_json, ObjectType


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code:'
                f' {response.status_code}. Url: {response.url}')


@allure.step
def check_response_object_count(response, count):
    _response_general_check(response)
    if type(response.json()) is dict:
        response_len = 1
    else:
        response_len = len(response.json())
    assert_that(response_len, equal_to(count),
                'Wrong number of objects came back')


@allure.step
def check_response_code(response, code):
    _response_general_check(response, code)


@allure.step
def validate_response(response, object_type: ObjectType):
    _response_general_check(response)
    assert_that(validate_json(response.json(), object_type),
                f'{object_type.value} response doesn\'t valid')


@allure.step
def validate_created_response(response, object_type: ObjectType):
    _response_general_check(response, codes.created)
    assert_that(validate_json(response.json(), object_type),
                f'{object_type.value} response doesn\'t valid')


@allure.step
def check_that_two_response_equals(response, before_json):
    _response_general_check(response)
    diff = DeepDiff(before_json, response.json(), ignore_order=True)
    assert_that(diff == {}, f'Response is not equals. \nDifference: {diff}')


@allure.step
def check_that_value_in_request_was_changed(response, title, new_value):
    _response_general_check(response)
    assert_that(response.json()[title] == new_value,
                'value has not been changed')
