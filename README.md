# python-tests

1) Unit-tests на 3 задания

[basic.py](https://github.com/mezhibo/python-tests/blob/e017f57162f673db3c0d41ac84e52ba5d4598aa2/basic.py)

[tests/test_basic.py](https://github.com/mezhibo/python-tests/blob/e017f57162f673db3c0d41ac84e52ba5d4598aa2/tests/test_basic.py)

2) Тесты для API Яндекс.Диска

[yandex_disk.py](https://github.com/mezhibo/python-tests/blob/e017f57162f673db3c0d41ac84e52ba5d4598aa2/yandex_disk.py)

[tests/test_yandex_disk.py](https://github.com/mezhibo/python-tests/blob/e017f57162f673db3c0d41ac84e52ba5d4598aa2/tests/test_yandex_disk.py)


Для запуска

```
pip install pytest requests
pytest -v
```

```
export YANDEX_TOKEN="ваш_токен"
pytest -v
```
