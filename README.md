# System Design
This system uses:
- Vector embeddings for semantic job matching
- k-NN similarity search
- A decoupled scraping pipeline
- A dedicated embedding + LLM service

See diagrams below for detailed flows.


## System Architecture

![High-level architecture](docs/architecture.png)

## Client Onboarding Flow

![Client onboarding sequence](docs/client_onboarding.png)

## Job Matching Pipeline

![Job ingestion and matching](docs/job_matching.png)


## Detailed Design Overview
![Detailed design overview](docs/detailed.png)