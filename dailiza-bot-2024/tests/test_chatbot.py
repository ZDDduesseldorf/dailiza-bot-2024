import pytest
from dailizabot.main import dailiza_answer


def test_dailiza_answer():
    user_input = "Wie geht es dir denn so?"
    expected_responses = [
        "Danke. Mir geht es gut und dir?",
        "Sehr gut, danke. Und wie läuft's bei dir?",
        "Ich kann nicht klagen. Was ist mit dir?"
    ]

    response = dailiza_answer(user_input)
    assert response in expected_responses, f"Unexpected response: {response}"
