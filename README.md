# Возможности
Клиент может отправлять на сервер запросы:
+ Регистрация
+ Посадка нового дерева
+ Рубка уже имеющегося дерева

# Инструкция по сборке
### Генерация файлов из `user.proto`
```
python3 -m grpc_tools.protoc -I. —python_out=. —grpc_python_out=. user.proto
```
### Запуск тестов
```
python3 -m pytest -v test.py
```
### Запуск сервера и клиента
```
python3 server.py
```
```
python3 client.py
```
