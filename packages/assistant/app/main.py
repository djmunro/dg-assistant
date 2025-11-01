import asyncio
from dataclasses import dataclass

import httpx
from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext

load_dotenv()


@dataclass
class MyDeps:
    http_client: httpx.Client


agent = Agent(
    model="anthropic:claude-sonnet-4-0",
    system_prompt="You are a helpful disc golf assistant. Be concise and opinionated.",
)


@agent.tool
async def get_discs(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get("http://localhost:8000/api/v1/discs")
    response.raise_for_status()
    return f"Here are the discs: {response.json()}"


async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps(client)
        # prompt = "I currently throw a innova TL3. But I want to try other disc manufacturers. What discs are similar to the TL3? Can you include the flight numbers so I can compare them?"
        prompt = "Can you list all the discs? and total count?"
        result = await agent.run(
            prompt,
            deps=deps,
        )
        print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
