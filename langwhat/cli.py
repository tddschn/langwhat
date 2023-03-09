#!/usr/bin/env python3

import argparse
from os import environ as env


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("what", help="what is it")
    # parser.add_argument(
    #     "--openai-key", dest="openai_key", type=str, default="", help="OpenAI api key"
    # )
    # parser.add_argument(
    #     '--bing-cookie-json', dest='bing_cookie_json', type=str, default='', help='Bing cookie json'
    # )
    # args to change api_base
    # parser.add_argument(
    #     "--api_base",
    #     dest="api_base",
    #     type=str,
    #     help="specify base url other than the OpenAI's official API address",
    # )
    parser.add_argument(
        "-z", "--zh", dest="zh", action="store_true", help="If use Mandarin to answer"
    )

    args = parser.parse_args()
    from langwhat.langwhat import What

    # OPENAI_API_KEY = args.openai_key or env.get("OPENAI_API_KEY")
    # BING_COOKIE_JSON = args.bing_cookie_json or env.get("BING_COOKIE_JSON") or env.get("COOKIE_FILE")
    OPENAI_API_KEY = env.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise Exception("OpenAI API key not provided, please google how to obtain it")

    # what = What(args.what, is_en=args.en, api_base=args.api_base)
    what = What(args.what, is_zh=args.zh, api_base=None)
    what.show_what()


if __name__ == "__main__":
    main()