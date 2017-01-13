# Dockerfile


FROM celery:3.1.18

WORKDIR /opt/service

COPY . /opt/service

CMD ["celery", "worker", "--loglevel=info", "--app=business.tasks", "--hostname=business.%h"]


# EOF
