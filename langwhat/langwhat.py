class What:
    def __init__(self, query, is_zh: bool=False, api_base: str | None=None):
        # if api_base:
        #     openai.api_base = api_base
        self.query = query
        self.is_zh = is_zh

    def get_response(self) -> dict[str, str]:
        from utils import get_chains
        chain, chain_zh = get_chains()
        if self.is_zh:
            return chain_zh(self.query)
        return chain(self.query)


    def show_what(self):
        from rich.console import Console
        from rich.table import Table
        from rich.style import Style
        from rich.text import Text
        from utils import parse_chain_response
        might_be, description = parse_chain_response(self.get_response())

        console = Console()
        title = Text("LangWhat", style=Style(color="#268bd2", bold=True))
        table = Table(title=title, show_lines=False, style="dim")
        table.add_column("Query", style=Style(color="#b58900"))
        table.add_column("Might Be", style=Style(color="#d33682"), justify="middle")
        table.add_column("Description", style=Style(color="#859900"), justify="left")
        table.add_row(self.query, might_be, description)
        console.print(table)

