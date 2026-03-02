# SentinelFlow AI

> Production-ready microservice architecture for AI-powered sentiment
> analysis\
> Built with Spring Boot (Java 21) and FastAPI (Python)

------------------------------------------------------------------------

## Overview

SentinelFlow AI is a clean, scalable microservice platform for real-time
sentiment analysis.

The system is split into two independent services:

-   **API Gateway (Spring Boot / Java 21)**
-   **AI Inference Service (FastAPI / Python 3.12)**

This separation enables independent scaling, easier maintenance, and
model flexibility.

------------------------------------------------------------------------

## Architecture

    Client
       ↓
    Spring Boot API Gateway (Java 21)
       ↓ HTTP
    FastAPI AI Service (Python)
       ↓
    HuggingFace Transformer Model

### Responsibilities

**API Gateway** - Request validation - Routing - Business logic layer -
External exposure

**AI Service** - Model loading - Inference - Prediction responses -
Stateless processing

------------------------------------------------------------------------

## AI Model

-   distilbert-base-uncased-finetuned-sst-2-english
-   Powered by HuggingFace Transformers
-   Cached pipeline for performance
-   Stateless inference design

------------------------------------------------------------------------

## Project Structure

    sentinelflow-ai/
    │
    ├── docker-compose.yml
    │
    ├── ai-model-service/
    │   ├── app.py
    │   ├── model.py
    │   ├── requirements.txt
    │   └── Dockerfile
    │
    ├── api-gateway/
    │   ├── build.gradle.kts
    │   ├── settings.gradle.kts
    │   └── src/main/java/com/sentinelflow/
    │       ├── SentinelFlowApplication.java
    │       └── controller/SentimentController.java
    │
    └── README.md

------------------------------------------------------------------------

## Run with Docker

``` bash
docker compose up --build
```

### Services

  Service       Port   Description
  ------------- ------ ----------------------
  API Gateway   8080   Public REST API
  AI Service    5000   ML inference service

------------------------------------------------------------------------

## Example Request

``` bash
curl -X POST http://localhost:8080/api/analyze -H "Content-Type: application/json" -d '{"text":"This product is amazing!"}'
```

### Example Response

``` json
{
  "label": "POSITIVE",
  "score": 0.9997
}
```

------------------------------------------------------------------------

## Technology Stack

-   Java 21
-   Spring Boot 3 (WebFlux)
-   Python 3.12
-   FastAPI
-   HuggingFace Transformers
-   Docker
-   Docker Compose

------------------------------------------------------------------------

## Design Principles

-   Microservice separation of concerns
-   Stateless AI inference
-   Independent service scaling
-   Container-first deployment
-   Cloud-native architecture ready

------------------------------------------------------------------------

## Future Enhancements

-   Redis caching layer
-   Kafka event streaming
-   JWT authentication
-   GPU acceleration support
-   Kubernetes deployment manifests
-   Observability (Prometheus / Grafana)

------------------------------------------------------------------------

## License

MIT License
