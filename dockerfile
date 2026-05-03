FROM alpine:latest

RUN apk add --no-cache \
    gcc musl-dev cmake make

WORKDIR /app

CMD ["gcc","--version"]