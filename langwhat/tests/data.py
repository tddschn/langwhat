edgegpt_answer_mary = """
[1]: https://en.wikipedia.org/wiki/Mary_Ball_Washington "Mary Ball Washington - Wikipedia"
[2]: https://www.mountvernon.org/library/digitalhistory/digital-encyclopedia/article/mary-ball-washington/ "Mary Ball Washington · George Washington's Mount Vernon"
[3]: https://washingtonindependent.com/mary-ball-washington/ "Mary Ball Washington: Who Was George Washington's Mother?"
[4]: https://www.geni.com/people/Mary-Washington/6000000007409105599 "Mary Washington (Ball) (1708 - 1789) - Genealogy - geni family tree"

Might be:
The mother of George Washington
Description:
Mary Ball Washington was born in 1708 in Virginia. She married Augustine Washington in 1730 and had six children, including George Washington, who became the first president of the United States[^1^][1] [^2^][2]. She died in 1789 at age 80[^1^][1].

What would you like to know more about Mary Ball Washington?
"""

edgegpt_answer_OPENAI_API_KEY_FILE = '''
Might be:
An environment variable or a file name
Description:
The OPENAI_API_KEY_FILE could be either an environment variable that stores the path to a file containing the OpenAI API key, or the name of the file itself. The OpenAI API key is a secret token that allows access to the OpenAI services and products.
'''
edgegpt_test_query_with_answer = {
    'mary ball washington', edgegpt_answer_mary,
    'OPENAI_API_KEY_FILE', edgegpt_answer_OPENAI_API_KEY_FILE,
}
