from pathlib import Path

XDG_CONFIG_DIR = Path.home() / '.config'
KEY_FILE = Path(XDG_CONFIG_DIR) / "langwhat" / "api_key.txt"


def get_api_key() -> str:
    """
    Retrieves API key from the file located in the user's home
    directory, or prompts the user to input it if it does not exist.

    :return: String API key for OpenAI API requests.
    """
    if not KEY_FILE.exists():
        from getpass import getpass
        api_key = getpass(prompt="Please enter your API secret key")
        KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
        KEY_FILE.write_text(api_key)
    else:
        api_key = KEY_FILE.read_text().strip()
    return api_key