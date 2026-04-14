import os
import uuid

import pytest

from yandex_disk import create_folder, get_root_files, get_resource_info, delete_resource


@pytest.fixture
def token():
    token_value = os.getenv("YANDEX_TOKEN")
    if not token_value:
        pytest.skip("Не задана переменная окружения YANDEX_TOKEN")
    return token_value


@pytest.fixture
def folder_name():
    return f"test_folder_{uuid.uuid4().hex[:8]}"


def test_create_folder_status_code(token, folder_name):
    response = create_folder(token, folder_name)

    assert response.status_code == 201


def test_created_folder_appears_in_files_list(token, folder_name):
    create_response = create_folder(token, folder_name)
    assert create_response.status_code == 201

    files_response = get_root_files(token)
    assert files_response.status_code == 200

    items = files_response.json()["_embedded"]["items"]
    names = [item["name"] for item in items]

    assert folder_name in names

    delete_resource(token, folder_name)


def test_created_folder_can_be_requested_by_path(token, folder_name):
    create_response = create_folder(token, folder_name)
    assert create_response.status_code == 201

    info_response = get_resource_info(token, folder_name)
    assert info_response.status_code == 200
    assert info_response.json()["name"] == folder_name
    assert info_response.json()["type"] == "dir"

    delete_resource(token, folder_name)


@pytest.mark.parametrize(
    "bad_token",
    [
        "",
        "wrong_token",
        "123",
    ],
)
def test_create_folder_with_invalid_token_returns_401(bad_token, folder_name):
    response = create_folder(bad_token, folder_name)
    assert response.status_code == 401


def test_create_existing_folder_returns_409(token, folder_name):
    first_response = create_folder(token, folder_name)
    assert first_response.status_code == 201

    second_response = create_folder(token, folder_name)
    assert second_response.status_code == 409

    delete_resource(token, folder_name)


@pytest.mark.parametrize(
    "bad_path",
    [
        "",
        None,
    ],
)
def test_create_folder_with_invalid_path_returns_error(token, bad_path):
    response = create_folder(token, bad_path)
    assert response.status_code in (400, 409)
