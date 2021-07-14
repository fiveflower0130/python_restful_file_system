import asyncio
import aiofiles
import os
from app import app
from flask import jsonify, request


def check_file_path(url):
    result = {}
    if os.path.exists(url):
        if os.path.isfile(url):
            result = {
                'type': 'file',
                'exist': True
            }
        if os.path.isdir(url):
            result = {
                'type': 'folder',
                'exist': True
            }
    return result


async def get_file_data(file_path):
    # data = []
    async with aiofiles.open(file_path, encoding='utf-8', mode='r') as f:
        contents = await f.read()
        # await for line in f:
        #     data.append(line.strip())
        # f.close()
    # await asyncio.sleep(1)
    return contents


async def get_folder_data(folder_path):
    data = os.listdir(folder_path)
    await asyncio.sleep(1)
    return data


@app.route('/')
def hello():
    try:
        resp = jsonify('hello')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/file/<path:localSystemFilePath>', methods=['GET'])
async def get_path(localSystemFilePath):
    try:
        _result = None
        resp = None
        _path = f'./file/{localSystemFilePath}'
        _path_info = check_file_path(_path)
        if _path_info['type'] == 'file':
            result = await get_file_data(_path)
        elif _path_info['type'] == 'folder':
            data = await get_folder_data(_path)
            result = {
                'isDirectory': True,
                'files': data
            }
        else:
            return not_found()
        await asyncio.sleep(1)
        resp = jsonify(result)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/file/<path:localSystemFilePath>', methods=['POST'])
def add_path(localSystemFilePath):
    try:
        _result = None
        _json = request.json
        _data = _json['files']
        if _data and request.method == 'POST':
            _path = f'./file/{localSystemFilePath}'
            _path_info = check_file_path(_path)

        else:
            message = {
                'status': 400,
                'message': 'No file data in request'
            }
            resp = jsonify(message)
            resp.status_code = 400
            return resp

    except Exception as e:
        print(e)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': 500,
        'message': 'server or network error: ',
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


if __name__ == "__main__":
    app.run()
