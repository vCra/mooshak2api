from mooshak2api import user


def test_no_admin_default():
    u = user.User("test", "test", contest="Test")

    assert u.admin is False
