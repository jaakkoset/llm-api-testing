# LLM API testing

[![GHA workflow badge](https://github.com/jaakkoset/llm-api-testing/workflows/CI/badge.svg)](https://github.com/jaakkoset/llm-api-testing/actions)
[![codecov](https://codecov.io/gh/jaakkoset/llm-api-testing/graph/badge.svg?token=0ml9x1ceqR)](https://codecov.io/gh/jaakkoset/llm-api-testing)

LLM API:en käytön harjoittelua.

## Asennus

 1. [Luo oma Gemini API key](https://ai.google.dev/gemini-api/docs/api-key)

 2. Luo juurikansioon .env-tiedosto ja määrittele sen sisällöksi

        GEMINI_API_KEY=<YOUR_API_KEY_HERE>

 3. Asenna Poetry

        poetry install

## Käyttö

Ohjelman ajaminen

    poetry run invoke start

Testien ajaminen

    poetry run invoke test

Pylint-testaus

    poetry run invoke lint
