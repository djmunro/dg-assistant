test: test-backend test-assistant

test-backend:
	uv run --package backend pytest

backend-up:
	docker compose -f packages/backend/docker-compose.yaml up

backend-down:
	docker compose -f packages/backend/docker-compose.yaml down

test-assistant:
	uv run --package assistant pytest
