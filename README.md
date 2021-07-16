# python 環境設定

1. 透過啟動虛擬環境的方式來跑python
- Windows10 -> cmd模式下，執行啟動`./venv/Script/activate.bat`，關閉的話則為`./venv/Script/deactivate.bat`
- MAC, Linux -> zsh, bash模式下，執行`source ./venv/bin/activate` 關閉的話則為`deactivate`

2. 執行`pip list`確認是否有在虛擬環境下看到安裝的套件，再請執行`pip install -r requirements.txt`進行local install

# python flask api 啟動

在虛擬環境模式下執行 python run.py

# python test 執行

在flask啟動後再執行 pytest run.py

# docker-compose 啟動服務和進行測試

1. 初次執行請先執行建置 docker-compose build

2. 建置完成後請執行 docker-compose up

3. 啟動完成後請執行 docker exec -i -t web bash 進入container

4. 執行 pytest test.py

# RESTFUL API CRUD 使用說明
可以使用 POST MAN 或http request方式測試 起始路徑為 /python_flask 起始資料夾為 /python_flask/file (裡面的/path/to/裡有檔案可以測試)
1. GET
-  http://localhost:5000/{檔案路徑} or http://localhost:5000/{資料夾路徑}
-  若為 http://localhost:5000/{資料夾路徑} 可夾帶params {"orderBy":"", "orderByDirection":"", "filterByName":""}
2. POST
-  http://localhost:5000/{檔案路徑}
-  query 格式為 json {"files":""} or {"files": [" "]} 
3. PATCH
-  http://localhost:5000/{檔案路徑}
-  query 格式為 json {"files":""} or {"files": [" "]} 
4. DELETE
-  http://localhost:5000/{檔案路徑}

