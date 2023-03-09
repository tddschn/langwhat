from codecs import getdecoder


class LangWhat:
    def __init__(
        self,
        query,
        is_zh: bool = False,
        sydney: bool = False,
        bing_cookie_json_path: str | None = None,
        api_base: str | None = None,
    ):
        # if api_base:
        #     openai.api_base = api_base
        self.query = query
        self.is_zh = is_zh
        self.sydney = sydney
        if self.sydney and bing_cookie_json_path is None:
            raise Exception("Bing cookie json path not provided")
        self.cookie_path = bing_cookie_json_path
        self.references: str | None = None

    def get_response_openai(self):
        from langwhat.utils import get_llm_chain

        chain = get_llm_chain(is_zh=self.is_zh)
        response = chain(self.query)
        from .utils import parse_chain_response

        self.might_be, self.description = parse_chain_response(response)

    async def get_response_sydney(self):
        from langwhat.utils import get_edgegpt_answer, split_edgegpt_answer

        assert self.cookie_path is not None
        edgegpt_answer = await get_edgegpt_answer(
            cookie_path=self.cookie_path, query=self.query, is_zh=self.is_zh
        )
        references, self.might_be, self.description = split_edgegpt_answer(
            edgegpt_answer
        )
        if references:
            self.references = references

    async def show(self):
        from rich.console import Console
        from rich.table import Table
        from rich.style import Style
        from rich.text import Text

        if self.sydney:
            await self.get_response_sydney()
        else:
            self.get_response_openai()

        console = Console()
        title = Text(
            "LangWhat [https://github.com/tddschn/langwhat]",
            style=Style(color="#268bd2", bold=True),
        )
        table = Table(title=title, show_lines=False, style="dim")  # type: ignore
        table.add_column("Query", style=Style(color="#b58900"))
        table.add_column("Might Be", style=Style(color="#d33682"), justify="middle")  # type: ignore
        table.add_column("Description", style=Style(color="#859900"), justify="left")
        table.add_row(self.query, self.might_be, self.description)
        console.print(table)

        if self.references:
            console.print("References:")
            console.print(self.references)
