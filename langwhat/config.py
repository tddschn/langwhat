from pathlib import Path

XDG_CONFIG_DIR = Path.home() / '.config'
OPENAI_API_KEY_FILE = Path(XDG_CONFIG_DIR) / "langwhat" / "api_key.txt"
EDGEGPT_COOKIE_FILE = Path(XDG_CONFIG_DIR) / "langwhat" / "cookie_file_path.txt"


def get_api_key() -> str:
    """
    Retrieves API key from the file located in the user's home
    directory, or prompts the user to input it if it does not exist.

    :return: String API key for OpenAI API requests.
    """
    if not OPENAI_API_KEY_FILE.exists():
        print('Instructions to get your API key:')
        print('https://platform.openai.com/account/api-keys')
        from getpass import getpass

        api_key = getpass(prompt="Please enter your API secret key: ")
        OPENAI_API_KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
        OPENAI_API_KEY_FILE.write_text(api_key)
    else:
        api_key = OPENAI_API_KEY_FILE.read_text().strip()
    return api_key


def get_cookies_file() -> str:
    """
    Retrieves cookie file from the file located in the user's home
    directory, or prompts the user to input it if it does not exist.

    :return: String cookie file for Bing API requests.
    """
    if not EDGEGPT_COOKIE_FILE.exists():
        print('Instructions to get your cookie file:')
        print('https://github.com/acheong08/EdgeGPT')
        from getpass import getpass

        cookie_file = getpass(
            prompt="Please enter the path to your bing.com cookie file: "
        )
        EDGEGPT_COOKIE_FILE.parent.mkdir(parents=True, exist_ok=True)
        EDGEGPT_COOKIE_FILE.write_text(cookie_file)
    else:
        cookie_file = EDGEGPT_COOKIE_FILE.read_text().strip()
    return cookie_file
