FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app/
WORKDIR $APP_HOME

COPY Pipfile.lock* Pipfile $APP_HOME

# Install production dependencies.
RUN pip install pipenv
RUN if [ ! -f "Pipfile.lock" ]; then \
    echo -e "Pipfile.lock not found. Generating...\n" && \
    pipenv lock; \
    fi
RUN pipenv sync

# Copy the rest of project files
COPY . $APP_HOME

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]