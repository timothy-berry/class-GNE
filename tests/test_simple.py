import os


def test_gh_actions():
    running_in_gh = os.getenv("GITHUB_ACTIONS")
    assert running_in_gh


def test_env_var():
    my_env = os.getenv("ENVIRONMENT", "local")
    assert my_env == "gh_actions"
