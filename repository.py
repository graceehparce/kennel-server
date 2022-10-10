RESOURCES = {
    "animals": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 4,
            "status": "Admitted"

        },
        {
            "id": 2,
            "name": "Eleanor",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            "status": "Admitted"
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            "status": "Admitted"

        }
    ],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        },
        {
            "id": 2,
            "name": "Rupert Parce"
        },
        {
            "id": 3,
            "name": "Jenna Kohles"
        },
        {
            "id": 4,
            "name": "Harry Potter"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        },
        {
            "id": 2,
            "name": "Gracie Parce"
        },
        {
            "id": 3,
            "name": "Tony Parce"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}


def all(resource):
    return resource
    pass


def retrieve(id, resource):
    requested_object = None

    for item in resource:

        if item["id"] == id:
            requested_object = item

    return requested_object
    pass


def create(resource, new_object):
    max_id = resource[-1]["id"]

    new_id = max_id + 1

    new_object["id"] = new_id

    resource.append(new_object)

    return new_object
    pass


def update(id, resource, updated_object):
    for index, item in enumerate(resource):
        if item["id"] == id:
            resource[index] = updated_object
            break
    pass


def delete(id, resource):
    item_index = -1

    for index, item in enumerate(resource):
        if item["id"] == id:
            item_index = index

    if item_index >= 0:
        resource.pop(item_index)

    pass
