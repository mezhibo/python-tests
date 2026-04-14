import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"


def get_headers(token: str) -> dict:
    return {"Authorization": f"OAuth {token}"}


def create_folder(token: str, path: str):
    return requests.put(
        BASE_URL,
        headers=get_headers(token),
        params={"path": path},
        timeout=10,
    )


def get_root_files(token: str):
    return requests.get(
        BASE_URL,
        headers=get_headers(token),
        params={"path": "disk:/"},
        timeout=10,
    )


def get_resource_info(token: str, path: str):
    return requests.get(
        BASE_URL,
        headers=get_headers(token),
        params={"path": path},
        timeout=10,
    )


def delete_resource(token: str, path: str):
    return requests.delete(
        BASE_URL,
        headers=get_headers(token),
        params={"path": path, "permanently": "true"},
        timeout=10,
    )
