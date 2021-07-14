import asyncio
import aiofiles
import os
from app import app
from flask import jsonify, request


def check_file_path(url):
    result = None
    if os.path.exists(url):
        if os.path.isfile(url):
            result = 'file'
        if os.path.isdir(url):
            result = 'folder'
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
        result = None
        resp = None
        path = f'./file/{localSystemFilePath}'
        path_type = check_file_path(path)
        if path_type == 'file':
            result = await get_file_data(path)
        elif path_type == 'folder':
            data = await get_folder_data(path)
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
    _result = None
    _json = request.json
    _path = _json['localSystemFilePath']
    if _path and request.method == 'POST':
        _result = check_file_path(localSystemFilePath)
        if not _result:
            return jsonify()
        else:
            return jsonify()
    return jsonify({'data': 'result'})


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
