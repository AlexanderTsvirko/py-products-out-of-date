import datetime
from unittest import mock
from app.main import outdated_products
from typing import Any


# @pytest.fixture()
# def mocked_datetime():
#     with mock.patch("app.main.datetime") as mocked_date:
#         return mocked_date


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: Any) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 5)
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]) == ["duck"]
