import allure

from framework.resources.base_resource import BaseResource


class Photos(BaseResource):
    @allure.step
    def get_all_photos(self):
        return self.get(path=f'/photos')

    @allure.step
    def get_photo_by_id(self, photo_id: int):
        return self.get(path=f'/photo/{photo_id}')

    @allure.step
    def get_photos_by_album_id(self, post_id: int):
        params = {"albumId": post_id}
        return self.get(path=f'/photos', params=params)

    @allure.step
    def add_photo(self, photo: dict):
        return self.post(path=f'/photos', json_str=photo)

    @allure.step
    def update_photo(self, photo_id: int, photo: dict):
        return self.put(path=f'/photos/{photo_id}', json_str=photo)

    @allure.step
    def update_photo_partly(self, photo_id: int, photo: dict):
        return self.patch(path=f'/photos/{photo_id}', json_str=photo)

    @allure.step
    def delete_photo(self, photo_id: int):
        return self.delete(path=f'/photos/{photo_id}')
