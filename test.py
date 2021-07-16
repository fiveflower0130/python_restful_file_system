import requests
import unittest
import pytest


def test_get_path():
    url = 'http://127.0.0.1:5000/file/path/to/'
    resp = requests.get(url)
    assert resp.status_code == 200


def test_error_get_path():
    url = 'http://127.0.0.1:5000/file/path/to/to'
    resp = requests.get(url)
    assert resp.status_code == 404
    
def test_get_path_orderBy_lastModified():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"orderBy":"lastModified"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200

def test_get_path_orderBy_size():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"orderBy":"size"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200

def test_get_path_orderBy_fileName():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"orderBy":"fileName"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200

def test_get_path_orderByDirection_ascending():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"orderByDirection":"Ascending"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200

def test_get_path_orderByDirection_descending():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"orderByDirection":"Descending"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200

def test_get_path_orderBy_filterByName():
    url = 'http://127.0.0.1:5000/file/path/to/'
    test_params = {"filterByName":"test"}
    resp = requests.get(url, params=test_params)
    assert resp.status_code == 200
    
def test_get_file():
    url = 'http://127.0.0.1:5000/file/path/to/test.txt'
    resp = requests.get(url)
    assert resp.status_code == 200


def test_error_get_file():
    url = 'http://127.0.0.1:5000/file/path/to/test5.txt'
    resp = requests.get(url)
    assert resp.status_code == 404


def test_post_file():
    url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
    info = {"files": ["111111"]}
    resp = requests.post(url, json=info, headers={
                         'Content-Type': 'application/json'})
    assert resp.status_code == 200

def test_post_file_error():
    url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
    info = {"files": ["333333"]}
    resp = requests.post(url, json=info, headers={
                         'Content-Type': 'application/json'})
    assert resp.status_code == 400


def test_patch_file():
    url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
    info = {"files": ["22222", "3333333"]}
    resp = requests.patch(url=url, json=info)
    assert resp.status_code == 200

def test_patch_file_error():
    url = 'http://127.0.0.1:5000/file/path/to/test2.txt'
    info = {"files": ["22222", "3333333"]}
    resp = requests.patch(url=url, json=info)
    assert resp.status_code == 404

def test_delete_file():
    url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
    resp = requests.delete(url)
    data = resp.json()
    print("data: ", data)
    assert resp.status_code == 200

def test_delete_file_error():
    url = 'http://127.0.0.1:5000/file/path/to/test2.txt'
    resp = requests.delete(url)
    data = resp.json()
    print("data: ", data)
    assert resp.status_code == 404

# class RestCalls():
#     def get_requests(path, methos):
#         base_url = 'http://127.0.0.1:5000/file/'
#         url= base_url + path
#         try:
#             r = requests.get(url)
#             return r
#         except requests.exceptions.Timeout as errt:
#             print (errt)
#             raise
#         except requests.exceptions.HTTPError as errh:
#             print (errh)
#             raise
#         except requests.exceptions.ConnectionError as errc:
#             print (errc)
#             raise
#         except requests.exceptions.RequestException as err:
#             print (err)
#             raise

# class TestLibFunction(unittest.TestCase):
    
#     def test_get_path(self):
#         url = 'http://127.0.0.1:5000/file/path/to/'
#         resp = requests.get(url)
#         self.assertEqual(200,resp.status_code)
    
#     def test_error_get_path(self):
#         url = 'http://127.0.0.1:5000/file/path/to/to'
#         resp = requests.get(url)
#         self.assertEqual(404,resp.status_code)
        
#     def test_get_file(self):
#         url = 'http://127.0.0.1:5000/file/path/to/test.txt'
#         resp = requests.get(url)
#         self.assertEqual(200,resp.status_code)
    
#     def test_error_get_file(self):
#         url = 'http://127.0.0.1:5000/file/path/to/test5.txt'
#         resp = requests.get(url)
#         self.assertEqual(404,resp.status_code)
        
#     def test_post_file(self):
#         url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
#         info = {"files":["111111"]}
#         resp = requests.post(url, json=info, headers={'Content-Type': 'application/json'})
#         self.assertEqual(200,resp.status_code)
    
#     def test_delete_file(self):
#         url = 'http://127.0.0.1:5000/file/path/to/test1.txt'
#         resp = requests.delete(url)
#         data = resp.json()
#         print("data: ",data)
#         self.assertEqual(200,resp.status_code)
#     # def test_exception(self):
#     #     self.assertRaises(requests.exceptions.Timeout,RestCalls.get_requests,'http://localhost:28989')

# if __name__ == '__main__':
#     unittest.main()
        
# base_url = 'http://127.0.0.1:5000/file/'


# async def count():
#     for i in [1, 2, 3, 4, 5]:
#         print(i)
#         await asyncio.sleep(1)


# async def test_get_path(path):
#     endpoint = base_url+path
#     print(f'Getting start with {endpoint}')

#     async with ClientSession() as session:
#         async with session.get(endpoint) as response:
#             response = await response.json()
#             print(response)


# async def main():
#     await asyncio.gather(count(), test_get_path('path/to/'), test_get_path('path/to/README.md'))
#     # resp = requests.get(endpoint)
#     # data = resp.json()
#     # print(data)

# asyncio.run(main())
# print('Finished!')
