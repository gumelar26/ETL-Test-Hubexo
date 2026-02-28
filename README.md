
# BCI Interview Project

## Overview
This project contains an Apache Airflow DAG pipeline for geocoding addresses.

## Prerequisites
- Docker
- Docker Compose

## Setup & Run

1. **Build and start services:**
  ```bash
  docker-compose up -d
  ```

2. **Access Airflow WebUI:**
  - Navigate to `http://localhost:8080`
  - Default credentials: `admin` / `admin`

3. **Trigger DAG:**
  - The `geocode_pipeline` DAG processes address data using the geocoding utility

## Project Structure
```
src/
  ├── integrations/    # Geocoding utilities
  ├── transformers/    # Address transformation logic
  └── utils/          # File readers/writers
dags/                 # Airflow DAG definitions
data/                 # Input/output sample data
```

## ⚠️ Important Security Warning

**This container runs as ROOT (UID 0:0).**

- **Folder Permissions:** Files and folders created by the container will have root ownership
- **Host Access Issues:** You may encounter permission errors when accessing logs, data, or dags from your host system
- **Cleanup:** To delete container-generated folders, you may need elevated privileges
