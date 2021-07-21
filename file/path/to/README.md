# python 環境設定

1. 透過啟動虛擬環境的方式來跑python
-  cmd模式下，執行啟動`./venv/Script/activate.bat`，關閉的話則為`./venv/Script/deactivate.bat`
- gitbash模式下，執行`source ./venv/Script/activate` 關閉的話則為`source ./venv/Script/deactivate`

2. 執行`pip list`確認是否有在虛擬環境下看到安裝的套件，若無請執行`pip install --no-index --find-links=./resource -r requirements.txt`進行local install