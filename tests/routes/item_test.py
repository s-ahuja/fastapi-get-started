import pytest
from main_test import client


@pytest.fixture(scope="module")
def create_item(request):
    return dict(id=request.param, title=f"Foo Bar_{request.param}", description=f"The Foo Barters_{request.param}")


@pytest.mark.dependency()
@pytest.mark.parametrize("create_item", [1, 2, 3], indirect=["create_item"])
def test_create_item(create_item):
    response = client.post("/item/", json=create_item, )
    actual_output = response.json()
    assert response.status_code == 201
    assert actual_output == create_item


@pytest.mark.parametrize("create_item, expected_count", [(1, 3), (2, 3), (3, 3)], indirect=["create_item"])
def test_get_all_items(create_item, expected_count):
    response = client.get("/items/")
    actual_output = response.json()
    assert response.status_code == 200
    assert expected_count == 3
    create_item.pop('id')
    assert create_item in actual_output


@pytest.mark.parametrize("create_item, expected_status_code, expected_message",
                         [(1, 200, None),
                          (0, 404, {'detail': 'Item with id 0 not found'})],
                         indirect=["create_item"], ids=["valid_id", "exception_id"])
def test_get_item(create_item, expected_status_code, expected_message):
    item_id = create_item['id']
    response = client.get(f"/item/{item_id}")
    assert response.status_code == expected_status_code
    if expected_message:
        assert response.json() == expected_message
    else:
        assert response.json() == create_item


@pytest.mark.parametrize("create_item, expected_status_code, expected_message",
                         [(1, 202, None),
                          (0, 404, {'detail': 'Item with id 0 not found'})],
                         indirect=["create_item"], ids=["valid_id", "exception_id"])
def test_put_item(create_item, expected_status_code, expected_message):
    create_item.update({"title": "Foo Bar Updated", "description": "The Foo Barters updated"})
    item_id = create_item['id']
    response = client.put(f"/item/{item_id}", json=create_item)
    assert response.status_code == expected_status_code
    if expected_message:
        assert response.json() == expected_message
    else:
        assert response.json() == create_item


@pytest.mark.parametrize("create_item, expected_status_code, expected_message",
                         [(1, 202, {'detail': 'Item with id 1 deleted successfully'}),
                          (0, 404, {'detail': 'Item with id 0 not found'})],
                         indirect=["create_item"], ids=["valid_id", "exception_id"])
def test_delete_item(create_item, expected_status_code, expected_message):
    id = create_item['id']
    response = client.delete(f"/item/{id}")
    assert response.status_code == expected_status_code
    assert response.json() == expected_message
