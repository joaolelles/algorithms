import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('message', 4) == 'ega_ssem'
    assert encrypt_message('message', 3) == 'sem_egas'
    assert encrypt_message('message', -1) == 'egassem'
    assert encrypt_message('message', 9) == 'egassem'
    with pytest.raises(TypeError):
        encrypt_message('message', 1.2)
    with pytest.raises(TypeError):
        encrypt_message(True, 1)
