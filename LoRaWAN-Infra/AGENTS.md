# AGENTS.md

## Structure

The root files define and document the deployment: `docker-compose.yml` orchestrates the services, `Makefile` provides helper commands, `Caddyfile` configures the reverse proxy, and `.env.example` documents the required environment variables.
The `configuration/` directory contains ChirpStack, Gateway Bridge, Mosquitto, and PostgreSQL configuration files for the supported regions and integrations.
The `uplink-collector/` directory contains the MQTT-to-PostgreSQL collector application, its Dockerfile, and Python dependencies.

## Stack

This directory contains a Docker Compose stack for LoRaWAN experiments:

- **ChirpStack**: LoRaWAN network server.
- **Gateway Bridge**: Semtech UDP and Basic Station gateway integrations.
- **REST API**: ChirpStack REST interface.
- **PostgreSQL**: application database.
- **Redis**: ChirpStack cache and session backend.
- **Mosquitto**: MQTT broker.
- **Uplink Collector**: MQTT-to-PostgreSQL uplink processor.
- **Grafana**: metrics and dashboard visualization.
- **Caddy**: HTTP/HTTPS reverse proxy.