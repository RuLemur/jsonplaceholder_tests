import allure

from framework.resources.base_resource import BaseResource


class Comments(BaseResource):
    @allure.step
    def get_all_comments(self):
        return self.get(path=f'/comments')

    @allure.step
    def get_comment_by_id(self, comment_id: int):
        return self.get(path=f'/comment/{comment_id}')

    @allure.step
    def get_comments_by_post_id(self, post_id: int):
        params = {"postId": post_id}
        return self.get(path=f'/comments', params=params)

    @allure.step
    def get_comments_by_email(self, email: str):
        params = {"email": email}
        return self.get(path=f'/comments', params=params)

    @allure.step
    def add_comment(self, comment: dict):
        return self.post(path=f'/comments', json_str=comment)

    @allure.step
    def update_comment(self, comment_id: int, comment: dict):
        return self.put(path=f'/comments/{comment_id}', json_str=comment)

    @allure.step
    def update_comment_partly(self, comment_id: int, comment: dict):
        return self.patch(path=f'/comments/{comment_id}', json_str=comment)

    @allure.step
    def delete_comment(self, comment_id: int):
        return self.delete(path=f'/comments/{comment_id}')
