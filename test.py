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

