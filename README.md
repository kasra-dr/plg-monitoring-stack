# Modern Monitoring Stack with Prometheus, Loki, and Grafana (PLG)

This project deploys a complete, containerized observability stack using Docker Compose. It's designed to collect, store, and visualize both **metrics** and **logs** from a sample application and the host system itself.

This setup provides a powerful, real-world monitoring solution, putting key **SRE** principles into practice.

---

## Architecture

The stack consists of several key components working together:

* **Prometheus:** Scrapes and stores time-series metrics.
* **Grafana:** The visualization layer for creating dashboards for both metrics and logs.
* **Loki:** Aggregates and stores logs.
* **Promtail:** The log agent that ships logs from containers to Loki.
* **Node Exporter:** Exposes host-level metrics (CPU, RAM, Disk, etc.) for Prometheus.
* **Sample Flask App:** A simple web application that exposes its own metrics for Prometheus to scrape.

All services are orchestrated via a single `docker-compose.yml` file.

---

## Technologies Used

* **Orchestration:** Docker Compose
* **Metrics:** Prometheus
* **Logging:** Grafana Loki & Promtail
* **Visualization:** Grafana
* **Sample Application:** Python (Flask)

---

## How to Run

1.  Ensure you have Docker and Docker Compose installed.
2.  Clone this repository.
3.  Navigate to the project directory and run the stack:
    ```bash
    docker-compose up -d
    ```
4.  Access the services:
    * **Grafana:** `http://localhost:3000` (user: `admin`, pass: `admin`)
    * **Prometheus:** `http://localhost:9090`

---
