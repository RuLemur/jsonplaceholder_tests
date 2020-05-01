import allure

from framework.resources.base_resource import BaseResource


class Todos(BaseResource):
    @allure.step
    def get_all_todos(self):
        return self.get(path=f'/todos')

    @allure.step
    def get_todo_by_id(self, todo_id: int):
        return self.get(path=f'/todo/{todo_id}')

    @allure.step
    def get_todos_by_user_id(self, user_id: int):
        params = {"userId": user_id}
        return self.get(path=f'/todos', params=params)

    @allure.step
    def get_todos_by_status(self, status: bool):
        params = {"completed": str(status).lower()}
        return self.get(path=f'/todos', params=params)

    @allure.step
    def add_todo(self, todo: dict):
        return self.post(path=f'/todos', json_str=todo)

    @allure.step
    def update_todo(self, todo_id: int, todo: dict):
        return self.put(path=f'/todos/{todo_id}', json_str=todo)

    @allure.step
    def update_todo_partly(self, todo_id: int, todo: dict):
        return self.patch(path=f'/todos/{todo_id}', json_str=todo)

    @allure.step
    def delete_todo(self, todo_id: int):
        return self.delete(path=f'/todos/{todo_id}')
