FROM python:3.10-slim as prod

# Set virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONBUFFERED=1

# OS dependency
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*


# Program dependency
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./script /app/
RUN chmod +x *.sh
COPY . /app/

ENTRYPOINT ["./entrypoint.sh"]
CMD ["./start.sh", "server"]
