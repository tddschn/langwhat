from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from langchain.chains import LLMChain
    from langchain.prompts.few_shot import FewShotPromptTemplate

def get_chains() -> tuple['LLMChain', ...]:
    from langchain.prompts.few_shot import FewShotPromptTemplate
    from langchain.prompts.prompt import PromptTemplate
    from langchain.llms import OpenAIChat
    from langchain.chains import LLMChain

    langwhat_example_prompt = PromptTemplate(input_variables=["question", "answer"], template="Q: {question}\nA:{answer}")

    langwhat_examples = [
        {"question": "vJzDRsEKDa0",
        "answer": 
    """
    Might be:
    A YouTube video ID
    Description:
    The ID "vJzDRsEKDa0" is most likely a unique identifier for a specific video on YouTube.
    This alphanumeric code is automatically assigned to every video uploaded on the platform and is used to access the video directly or share it with other users.
    """}, {"question": "https://langchain.readthedocs.io/", "answer":
    """
    Might be:
    A website or online documentation
    Description:
    This website/document provides information about LangChain, a technology or platform that could be used for language processing or analysis.
    """   }
    ]

    langwhat_examples_zh = [
        {"question": "vJzDRsEKDa0",
        "answer": 
    """
    可能是:
    YouTube 视频 ID
    描述:
    “vJzDRsEKDa0”这个ID很可能是YouTube上特定视频的唯一标识符。
    每上传一个视频，该平台都会自动分配这个字母数字代码，并用于直接访问或与其他用户共享该视频。
    """}, {"question": "https://langchain.readthedocs.io/", "answer":
    """
    可能是:
    一个网站或在线文档
    描述:
    这个网站/文件提供有关LangChain的信息，它是一种可用于语言处理或分析的技术或平台。
    """   }
    ]

    langwhat_prompt = FewShotPromptTemplate(
        # example_selector=example_selector, 
        example_prompt=langwhat_example_prompt, 
        examples = langwhat_examples,
        suffix="Q: {input}\nA:", 
        input_variables=["input"]
    )
    langwhat_prompt_zh = FewShotPromptTemplate(
        # example_selector=example_selector, 
        example_prompt=langwhat_example_prompt, 
        examples = langwhat_examples_zh,
        suffix="Q: {input}\nA:", 
        input_variables=["input"]
    )

    llm = OpenAIChat() # type: ignore
    chain = LLMChain(llm=llm, prompt=langwhat_prompt)
    chain_zh = LLMChain(llm=llm, prompt=langwhat_prompt_zh)
    return chain, chain_zh

def save_prompts(langwhat_prompt: 'FewShotPromptTemplate', langwhat_prompt_zh: 'FewShotPromptTemplate'):
    from pathlib import Path

    base_dir = Path(__file__).parent
    for ext in ('.yaml', '.json'):
        for i, prompt in enumerate((langwhat_prompt, langwhat_prompt_zh)):
            if i == 0:
                prompt.save(base_dir / f'langwhat_prompt{ext}')
            else:
                prompt.save(base_dir / f'langwhat_prompt_zh{ext}')

def parse_chain_response(chain_response: dict[str, str]) -> tuple[str, str]:
    """Parse the response from the chain.

    Args:
        chain_response (dict[str, str]): The response from the chain.

    Returns:
        tuple[str, str]: The first element is the might be, the second element is the description.
    """
    ans_lines = chain_response['text'].strip().splitlines()
    might_be = ans_lines[1]
    description = '\n'.join(ans_lines[3:])
    description = description.replace(",", ",\r\n")
    description = description.replace("，", "，\r\n")
    description = description.replace("。", "。\r\n")
    return might_be, description