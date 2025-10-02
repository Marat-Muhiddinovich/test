import pytest # type: ignore
from api.users_api import UsersAPI
from api.users_api import UserSearchAPI
from api.users_api import UserFilterAPI
from api.users_api import LimitSkipFilterUsersAPI
from api.users_api import UserSortAPI
from api.users_api import UserGetByIDAPI
from api.users_api import GetUserPostsAPI
from api.users_api import AddUserAPI
from api.new_user import new_user

# get all users test
@pytest.mark.api
def test_get_all_users(api_context):
    users_api = UsersAPI(api_context)
    response = users_api.get_all_users()
    assert response.status == 200 
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0
    assert "total" in data
    print(f"Total users: {data['total']}")

# search users test
@pytest.mark.api
def test_search_users(api_context):
    users_api = UserSearchAPI(api_context)
    query = "Emil"
    response = users_api.search_users(query)
    assert response.status == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0
    for user in data["users"]:
        assert query in user["firstName"] or query in user["lastName"]

    print(f"Found {len(data['users'])} users matching query '{query}'")

# search users no results test
@pytest.mark.api
def test_search_users_no_results(api_context):
    users_api = UserSearchAPI(api_context)
    query = "NonExistentName"
    response = users_api.search_users(query)
    assert response.status == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) == 0
    print(f"No users found matching query '{query}' as expected")

# filter users test
@pytest.mark.api
def test_filter_users(api_context):
    users_api = UserFilterAPI(api_context)
    key="hair"
    value="Red"
    type="circle"
    response = users_api.filter_users(key, value, type)
    assert response.status == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0
    for user in data["users"]:
        assert "hair" in user
        assert user["hair"]["color"].lower() == value.lower()

    print(f"Found {len(data['users'])} users with {key} color '{value}', type '{type}'")

@pytest.mark.api
def test_limit_skip_filter_users(api_context):
    users_api = LimitSkipFilterUsersAPI(api_context)
    limit=5
    skip=2
    response = users_api.limit_skip_filter_users(limit, skip)
    assert response.status == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) == limit
    print(data)
    for user in data["users"]:
        assert "firstName" in user
        assert "lastName" in user
        assert "age" in user

    print(f"Retrieved {len(data['users'])} users with limit {limit} and skip {skip}")

# sort users test
@pytest.mark.api
def test_sort_users(api_context):
    users_api = UserSortAPI(api_context)
    sort_by="firstName"
    response = users_api.sort_users(sort_by)
    assert response.status == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0

    print(f"Retrieved {len(data['users'])} users sorted by '{sort_by}' in ascending order")
    first_names = [user["firstName"] for user in data["users"]]
    assert first_names == sorted(first_names), "Users are not sorted correctly by firstName"
    print("Users are sorted correctly by firstName")
    print(first_names)

# get user by ID test
@pytest.mark.api
def test_get_user_by_id(api_context):
    users_api = UserGetByIDAPI(api_context)
    user_id=6
    response = users_api.get_user_by_id(user_id)
    assert response.status == 200
    data = response.json()
    assert "carts" in data
    assert isinstance(data["carts"], list)
    assert len(data["carts"]) > 0
    assert user_id == data["carts"][0]["userId"]
    print(f"user with ID {user_id}: {data}")

#get user posts by ID test
@pytest.mark.api
def test_get_user_posts(api_context):
    users_api = GetUserPostsAPI(api_context)
    user_id=5
    response = users_api.get_user_posts(user_id)
    assert response.status == 200
    data = response.json()
    assert "posts" in data
    assert isinstance(data["posts"], list)
    assert len(data["posts"]) > 0
    for post in data["posts"]:
        assert post["userId"] == user_id
    print(f"user with ID {user_id} posts: {data}")

@pytest.mark.api
def test_add_user(api_context):
    users_api = AddUserAPI(api_context)
    add_user = new_user
    response = users_api.add_user(add_user)
    assert response.status == 200 or response.status == 201
    data = response.json()
    assert "id" in data
    assert data["firstName"] == add_user["firstName"]
    assert data["lastName"] == add_user["lastName"]
    assert data["age"] == add_user["age"]
    print(f"Added new user with ID {data['id']}: {data}")
    