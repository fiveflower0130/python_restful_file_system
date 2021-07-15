import asyncio
from typing import List
import aiofiles
import os
from app import app
from flask import jsonify, request


def check_file_path(url):
    result = {}
    if os.path.exists(url):
        if os.path.isfile(url):
            result = {'type': 'file', 'exist': True}
        if os.path.isdir(url):
            result = {'type': 'folder', 'exist': True}
    else:
        file_name = url.rsplit('.', 1)[1].lower()
        if file_name:
            result = {'type': 'file', 'exist': False}
    return result


async def get_file_data(file_path):
    # data = []
    async with aiofiles.open(file_path, encoding='utf-8', mode='r') as f:
        contents = await f.read()
        # await for line in f:
        #     data.append(line.strip())
        # f.close()
    await asyncio.sleep(1)
    return contents


async def get_folder_data(folder_path):
    data = os.listdir(folder_path)
    await asyncio.sleep(1)
    return data


async def add_file(file_path, file_data):
    async with aiofiles.open(file_path, encoding='utf-8', mode='w') as file:
        if isinstance(file_data, List):
            await file.write('\n'.join(file_data))
        else:
            await file.write(file_data)
    await asyncio.sleep(1)
    return True if os.path.exists(file_path) else False


async def update_file(file_path, file_data):
    before_len = None
    async with aiofiles.open(file_path, encoding='utf-8', mode='r') as file:
        contents = await file.read()
        lines = contents.split('\n')
        before_len = len(lines)
        file.close()

    async with aiofiles.open(file_path, encoding='utf-8', mode='w') as sortedbooks:
        if isinstance(file_data, List) and len(file_data) > 0:
            lines.extend(file_data)
        else:
            if len(file_data) > 0:
                lines.append(file_data)
        await sortedbooks.write('\n'.join(lines))
        await sortedbooks.close()

    async with aiofiles.open(file_path, encoding='utf-8', mode='r') as file:
        contents = await file.read()
        update_lines = contents.split('\n')
    await asyncio.sleep(1)

    return True if len(update_lines) >= before_len else False


async def drop_file(file_path):
    os.remove(file_path)
    await asyncio.sleep(1)
    return False if os.path.exists(file_path) else True


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
        if _path_info['type'] == 'file' and _path_info['exist'] == True:
            _result = await get_file_data(_path)
        elif _path_info['type'] == 'folder' and _path_info['exist'] == True:
            data = await get_folder_data(_path)
            _result = {
                'isDirectory': True,
                'files': data
            }
        else:
            return not_found()
        resp = jsonify(_result)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/file/<path:localSystemFilePath>', methods=['POST'])
async def create_file(localSystemFilePath):
    try:
        _result = None
        _json = request.json
        _data = _json['files']
        _path = f'./file/{localSystemFilePath}'
        _path_info = check_file_path(_path)
        if _path_info['type'] == 'file' and _path_info['exist'] == False:
            _result = await add_file(_path, _data)
            if _result == True:
                message = {'status': 200,
                           'message': f'Create {_path} success!!'}
                resp = jsonify(message)
                resp.status_code = 200
                return resp
            else:
                message = {
                    'status': 400, 'message': f'{_path} create fail, please check file data!'}
        else:
            message = {'status': 400, 'message': f'{_path} has been exist!'}
        resp = jsonify(message)
        resp.status_code = 400
        return resp

    except Exception as e:
        print(e)


@app.route('/file/<path:localSystemFilePath>', methods=['PATCH'])
async def edit_file(localSystemFilePath):
    try:
        _result = None
        _json = request.json
        _data = _json['files']
        _path = f'./file/{localSystemFilePath}'
        _path_info = check_file_path(_path)
        if _path_info['type'] == 'file' and _path_info['exist'] == True:
            _result = await update_file(_path, _data)
            if _result == True:
                message = {'status': 200,
                           'message': f'Update {_path} success!!'}
                resp = jsonify(message)
                resp.status_code = 200
                return resp
            else:
                message = {
                    'status': 400, 'message': f'{_path} update fail, please check file data!'}
                resp = jsonify(message)
                resp.status_code = 400
                return resp
        else:
            return not_found()

    except Exception as e:
        print(e)


@app.route('/file/<path:localSystemFilePath>', methods=['DELETE'])
async def delete_file(localSystemFilePath):
    try:
        _result = None
        _path = f'./file/{localSystemFilePath}'
        _path_info = check_file_path(_path)
        if _path_info['type'] == 'file' and _path_info['exist'] == True:
            _result = await drop_file(_path)
            print('delete result: ', _result)
            if _result == True:
                message = {'status': 200,
                           'message': f'Delete file {_path} success!!'}
                resp = jsonify(message)
                resp.status_code = 200
                return resp
        else:
            return not_found()

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
