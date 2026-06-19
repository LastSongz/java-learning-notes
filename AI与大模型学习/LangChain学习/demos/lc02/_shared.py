import os
from pathlib import Path


def load_local_env() -> None:
    """Load .env from this demo directory if python-dotenv is installed."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    env_file = Path(__file__).with_name(".env")
    load_dotenv(env_file, override=True)


def build_llm(temperature: float = 0.2):
    """Create a Chat Model using LangChain's unified init_chat_model entry."""
    load_local_env()

    provider = os.getenv("LANGCHAIN_MODEL_PROVIDER", "deepseek")
    model = os.getenv("LANGCHAIN_MODEL", "deepseek-chat")

    provider_prefix = provider.upper().replace("-", "_")
    api_key = (
        os.getenv("LANGCHAIN_API_KEY")
        or os.getenv(f"{provider_prefix}_API_KEY")
        or os.getenv("DEEPSEEK_API_KEY")
    )
    base_url = (
        os.getenv("LANGCHAIN_BASE_URL")
        or os.getenv(f"{provider_prefix}_BASE_URL")
        or os.getenv("DEEPSEEK_BASE_URL")
    )

    if not api_key:
        raise RuntimeError(
            "Missing API key. Copy .env.example to .env and fill in your key."
        )

    try:
        from langchain.chat_models import init_chat_model
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependencies. Run: pip install -U langchain langchain-deepseek python-dotenv"
        ) from exc

    kwargs = {
        "model": model,
        "model_provider": provider,
        "api_key": api_key,
        "temperature": temperature,
    }
    if base_url:
        kwargs["base_url"] = base_url

    return init_chat_model(**kwargs)


def print_title(title: str) -> None:
    line = "=" * len(title)
    print(f"\n{title}\n{line}")
