import allure

from framework.resources.base_resource import BaseResource


class Users(BaseResource):
    @allure.step
    def get_all_users(self):
        return self.get(path=f'/users')

    @allure.step
    def get_user_by_id(self, user_id: int):
        return self.get(path=f'/user/{user_id}')

    def _get_user_by_param(self, param: str, value: str):
        params = {param: value}
        return self.get(path=f'/users', params=params)

    @allure.step
    def get_users_by_name(self, name: str):
        return self._get_user_by_param("name", name)

    @allure.step
    def get_users_by_username(self, username: str):
        return self._get_user_by_param("username", username)

    @allure.step
    def get_users_by_email(self, email: str):
        return self._get_user_by_param("email", email)

    @allure.step
    def get_users_by_phone(self, name: str):
        params = {"name": name}
        return self.get(path=f'/users', params=params)

    @allure.step
    def get_users_by_website(self, website: str):
        return self._get_user_by_param("website", website)

    @allure.step
    def get_user_albums(self, user_id: int):
        return self.get(path=f'/posts/{user_id}/albums')

    @allure.step
    def get_user_todos(self, user_id: int):
        return self.get(path=f'/posts/{user_id}/todos')

    @allure.step
    def get_user_posts(self, user_id: int):
        return self.get(path=f'/posts/{user_id}/posts')

    @allure.step
    def add_user(self, user: dict):
        return self.post(path=f'/users', json_str=user)

    @allure.step
    def update_user(self, user_id: int, user: dict):
        return self.put(path=f'/users/{user_id}', json_str=user)

    @allure.step
    def update_user_partly(self, user_id: int, user: dict):
        return self.patch(path=f'/users/{user_id}', json_str=user)

    @allure.step
    def delete_user(self, user_id: int):
        return self.delete(path=f'/users/{user_id}')
