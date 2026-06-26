import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    pristine_activities = copy.deepcopy(app_module.activities)

    # Arrange baseline state before each test.
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(pristine_activities))

    yield

    # Ensure test mutations are cleaned up for the next test.
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(pristine_activities))


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
