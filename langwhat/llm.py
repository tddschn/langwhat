from langchain.llms.base import LLM


class EdgeLLM(LLM):
    bing_cookie_path: str

    @property
    def _llm_type(self) -> str:
        return "edge"

    def _call(self, prompt: str, stop: list[str] | None = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        from EdgeGPT import Chatbot
        import asyncio

        # import nest_asyncio

        # nest_asyncio.apply()

        bot = Chatbot(cookiePath=self.bing_cookie_path)
        r = asyncio.run(bot.ask(prompt))
        answer = r["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
        return answer
