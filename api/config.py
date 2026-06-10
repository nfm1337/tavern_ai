from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    aws_region: str = "eu-west-1"
    aws_access_key_id: str | None = None
    aws_secret_access_key: str | None = None

    bedrock_llm_model: str = "anthropic.claude-haiku-4-5"
    bedrock_embedding_model: str = "amazon.titan-embed-text-v2:0"

    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection_name: str = "tavern-ai-srd"

    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_host: str = "https://cloud.langfuse.com"

    s3_bucket_name: str = "tavern-ai-srd-docs"
    s3_srd_prefix: str = "srd/"

    dynamodb_table_name: str = "tavern-ai-sessions"

    app_env: str = "dev"
    app_port: int = 8000


settings = Settings()
