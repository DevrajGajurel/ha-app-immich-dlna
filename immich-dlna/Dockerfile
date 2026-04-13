ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM ${BUILD_FROM}
ARG APP_GIT_URL=https://github.com/DevrajGajurel/ha-app-immich-dlna.git
ARG APP_GIT_REF=main
ARG APP_BUILD_VERSION=0.1.10

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apk add --no-cache python3 py3-pip git

# PEP 668: system Python is externally managed; install into a venv (not --break-system-packages).
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

RUN pip install --upgrade pip

RUN echo "Installing immich-dlna source for build version ${APP_BUILD_VERSION}" \
    && pip install --no-cache-dir "git+${APP_GIT_URL}@${APP_GIT_REF}"

COPY rootfs /
RUN chmod a+x /etc/services.d/immich-dlna/run
