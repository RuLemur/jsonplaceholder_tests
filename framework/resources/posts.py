import allure

from framework.resources.base_resource import BaseResource


class Posts(BaseResource):
    @allure.step
    def get_all_posts(self):
        return self.get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self.get(path=f'/posts/{post_id}')

    @allure.step
    def get_post_comments(self, post_id: int):
        return self.get(path=f'/posts/{post_id}/comments')

    @allure.step
    def get_posts_by_user_id(self, user_id: int):
        params = {"userId": user_id}
        return self.get(path=f'/posts', params=params)

    @allure.step
    def add_post(self, post: dict):
        return self.post(path=f'/posts', json_str=post)

    @allure.step
    def update_post(self, post_id: int, post: dict):
        return self.put(path=f'/posts/{post_id}', json_str=post)

    @allure.step
    def update_post_partly(self, post_id: int, post: dict):
        return self.patch(path=f'/posts/{post_id}', json_str=post)

    @allure.step
    def delete_post(self, post_id: int):
        return self.delete(path=f'/posts/{post_id}')
