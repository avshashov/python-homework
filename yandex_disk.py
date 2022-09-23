import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {"content-type": "application/json",
                "Authorization": f'OAuth {self.token}'}

    # def get_files_list(self):
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    #     headers = self.get_headers()
    #     response = requests.get(url=files_url, headers=headers)
    #     return response.json()

    def _get_upload_link(self, disk_space_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_space_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_space_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        return 'Success' if response.status_code == 201 else 'Error'


if __name__ == '__main__':
    path_to_file = 'test_file.txt'
    filename = 'test_file.txt'
    token = ' '
    up = YaUploader(token)
    result = up.upload(path_to_file, filename)
    print(result)
