from streamlit.testing.v1 import AppTest


def test_run() -> None:
    at = AppTest.from_file("infrahub_agent/frontend.py")
    at.run()

    assert not at.exception


def test_run_risk() -> None:
    at = AppTest.from_file("infrahub_agent/frontend.py")
    at.run()
    assert at.info[0].value == "Please accept the risk"

    at.radio(key="accept_risk").set_value("Yes").run()
    assert at.info[0].value == "Please add your API keys to continue."
    assert not at.exception


def test_run_all_infos() -> None:
    at = AppTest.from_file("infrahub_agent/frontend.py")
    at.run()
    at.radio(key="accept_risk").set_value("Yes")
    at.text_input(key="infrahub_url").input("https://localhost:8000")
    at.text_input(key="infrahub_key").input("my key")
    at.text_input(key="openai_api_key").input("my api")
    at.run()

    assert not len(at.info)
    assert len(at.chat_input) == 1
    assert not at.exception
