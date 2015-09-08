# Dockerfile


FROM celery:3.1.18

WORKDIR /opt/service

COPY . /opt/service

CMD ["celery", "worker", "-l", "info", "-A", "business.tasks", "-n", "business.%h"]


# EOF
