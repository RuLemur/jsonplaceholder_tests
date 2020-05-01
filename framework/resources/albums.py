import allure

from framework.resources.base_resource import BaseResource


class Albums(BaseResource):
    @allure.step
    def get_all_albums(self):
        return self.get(path=f'/albums')

    @allure.step
    def get_album_by_id(self, album_id: int):
        return self.get(path=f'/albums/{album_id}')

    @allure.step
    def get_album_photos(self, album_id: int):
        return self.get(path=f'/albums/{album_id}/photos')

    @allure.step
    def get_albums_by_user_id(self, user_id: int):
        params = {"userId": user_id}
        return self.get(path=f'/albums', params=params)

    @allure.step
    def add_album(self, album: dict):
        return self.post(path=f'/albums', json_str=album)

    @allure.step
    def update_album(self, album_id: int, album: dict):
        return self.put(path=f'/albums/{album_id}', json_str=album)

    @allure.step
    def update_album_partly(self, album_id: int, album: dict):
        return self.patch(path=f'/albums/{album_id}', json_str=album)

    @allure.step
    def delete_album(self, album_id: int):
        return self.delete(path=f'/albums/{album_id}')
