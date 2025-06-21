import os
import requests
import chainlit as cl
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, function_tool

# Load .env file
load_dotenv(find_dotenv())


gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set up the API provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the AI model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Configure the run
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# API call wrapped in a function tool
@function_tool
def get_crypto_prices():
    response = requests.get("https://api.coinlore.net/api/tickers/")
    coins = response.json()["data"][:5]
    return "\n\n".join([
    f'{coin["name"]} ({coin["symbol"]})\nRank: {coin["rank"]}\nPrice (USD): ${coin["price_usd"]}\nPrice (BTC): {coin["price_btc"]}\nMarket Cap: ${coin["market_cap_usd"]}'
    for coin in coins
])



# Create the agent
crypto_agent = Agent(
    name="CryptoDataAgent",
    instructions="Agar koi poochay crypto ka current rate to Coinlore API se nikaal kar batao.",
    tools=[get_crypto_prices]
)

@cl.on_chat_start
async def start():
    await cl.Message(content=" Welcome to CryptoDataAgent! Ask me about the latest crypto prices.").send()

# Handle user message
@cl.on_message
async def on_message(message: cl.Message):
    result = await Runner.run(crypto_agent, input=message.content, run_config=config)
    await cl.Message(content=result.final_output).send()




