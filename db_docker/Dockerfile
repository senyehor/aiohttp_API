FROM postgres:15

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=iot_devices_tracker

COPY ./sample_data.sql /docker-entrypoint-initdb.d/init.sql

# Expose the default PostgreSQL port
EXPOSE 5432