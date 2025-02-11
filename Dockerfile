FROM apache/airflow:2.7.1-python3.9

# Copy the requirements file into the container
COPY requirements.txt /opt/airflow/

# Switch to root user to install system dependencies
USER root
RUN apt-get update && apt-get install -y gcc python3-dev

# Switch back to airflow user
USER airflow

# First, remove the incompatible package
RUN pip uninstall -y apache-airflow-providers-openlineage || true

# Install Airflow dependencies
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Ensure the correct version of apache-airflow-providers-openlineage
RUN pip install --no-cache-dir "apache-airflow-providers-openlineage>=1.8.0"
