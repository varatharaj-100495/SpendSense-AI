from app.ai.providers.gemini_provider import GeminiProvider

provider = GeminiProvider()

response = provider.generate(
    "Say hello in one sentence."
)

print(response)