import main
from game_data import data


def test_get_random_account():
    first_account = main.get_random_account()
    second_account = main.get_random_account()
    assert first_account != second_account


def test_get_formatted_description_returns_proper_format():
    expected = "Selena Gomez, a Musician and actress, from United States."
    test_data = {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    }
    assert main.get_formatted_description(test_data) == expected


def test_check_answer():
    assert main.check_answer("a", 100, 200) == False
    assert main.check_answer("a", 100, 100) == True
    assert main.check_answer("b", 100, 100) == True
    assert main.check_answer("a", 200, 100) == True
    assert main.check_answer("b", 100, 200) == True
    assert main.check_answer("b", 200, 100) == False


def test_start_game_with_correct_answer_continues_game(capfd, monkeypatch):
    inputs = ['A', 'A', 'A', 'B']
    data_copy = data.copy()
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.get_random_account", lambda: data_copy.pop(0))
    main.start_game()
    out, err = capfd.readouterr()
    assert "Compare A: Instagram, a Social media platform, from United States." in out
    assert "Against B: Cristiano Ronaldo, a Footballer, from Portugal." in out
    assert "Against B: Ariana Grande, a Musician and actress, from United States." in out
    assert "Against B: Dwayne Johnson, a Actor and professional wrestler, from United States." in out
    assert "Against B: Selena Gomez, a Musician and actress, from United States." in out
    assert "You're right! Current score: 3" in out
    assert "Sorry, that's wrong. Final score: 3" in out


def test_start_game_with_wrong_answer_ends_game(capfd, monkeypatch):
    inputs = ['B']
    data_copy = data.copy()
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.get_random_account", lambda: data_copy.pop(0))
    main.start_game()
    out, err = capfd.readouterr()
    assert "Compare A: Instagram, a Social media platform, from United States." in out
    assert "Against B: Cristiano Ronaldo, a Footballer, from Portugal." in out
    assert "Sorry, that's wrong. Final score: 0" in out
