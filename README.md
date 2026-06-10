# tavern-ai 🍺

AI-powered D&D 5e SRD assistant. Ask questions about rules, spells, and monsters.
Built with LangChain, LangGraph, AWS Bedrock, and Qdrant.

## Stack

- **LLM:** AWS Bedrock (Claude Haiku)
- **Embeddings:** AWS Bedrock (Titan Embeddings V2)
- **Vector DB:** Qdrant Cloud (hybrid search)
- **Orchestration:** LangGraph
- **Observability:** Langfuse
- **Backend:** FastAPI
- **Deploy:** AWS App Runner

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- AWS account with Bedrock access (eu-west-1)
- [Qdrant Cloud](https://cloud.qdrant.io) account
- [Langfuse Cloud](https://cloud.langfuse.com) account

## Local setup

**1. Clone and install dependencies:**

```bash
git clone https://github.com/YOUR_USERNAME/tavern-ai.git
cd tavern-ai
uv sync
uv sync --group dev
```

**2. Configure environment:**

```bash
cp .env.example .env
```

Fill in `.env` with your credentials:

| Variable                  | Description                       |
| ------------------------- | --------------------------------- |
| `AWS_REGION`              | AWS region (default: `eu-west-1`) |
| `AWS_ACCESS_KEY_ID`       | AWS IAM access key                |
| `AWS_SECRET_ACCESS_KEY`   | AWS IAM secret key                |
| `BEDROCK_LLM_MODEL`       | Bedrock LLM model ID              |
| `BEDROCK_EMBEDDING_MODEL` | Bedrock embedding model ID        |
| `QDRANT_URL`              | Qdrant Cloud cluster URL          |
| `QDRANT_API_KEY`          | Qdrant Cloud API key              |
| `QDRANT_COLLECTION_NAME`  | Qdrant collection name            |
| `LANGFUSE_PUBLIC_KEY`     | Langfuse public key               |
| `LANGFUSE_SECRET_KEY`     | Langfuse secret key               |
| `S3_BUCKET_NAME`          | S3 bucket with SRD documents      |

**3. Install pre-commit hooks:**

```bash
uv run pre-commit install
```

## AWS Setup

Required services:

- **S3** — bucket for SRD source documents
- **Bedrock** — model access for Claude Haiku + Titan Embeddings V2
- **DynamoDB** — table for chat history (`tavern-ai-sessions`)
- **ECR** — container registry (`tavern-ai`)
- **App Runner** — managed container deployment

IAM permissions required: see `docs/iam-policy.md` _(coming soon)_

## Deployment

Push to `main` triggers automatic deployment via GitHub Actions:
lint → build Docker image → push to ECR → deploy to App Runner

Required GitHub Actions secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `APP_RUNNER_SERVICE_ARN`

## Development

```bash
# Run locally
uv run uvicorn api.main:app --reload

# Lint
uv run ruff check .

# Format
uv run ruff format .
```
