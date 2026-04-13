ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM ${BUILD_FROM}
ARG APP_GIT_URL=https://github.com/DevrajGajurel/ha-app-immich-dlna.git
ARG APP_GIT_REF=main
# Bump when you need to invalidate Docker layer cache on build hosts (e.g. after PEP 668 / install fixes).
ARG APP_BUILD_VERSION=0.1.11

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apk add --no-cache python3 py3-pip git

# PEP 668: system Python is externally managed — install only inside a venv (never pip3 onto system).
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && echo "Installing immich-dlna for build ${APP_BUILD_VERSION}" \
    && /opt/venv/bin/pip install --no-cache-dir "git+${APP_GIT_URL}@${APP_GIT_REF}"

ENV PATH="/opt/venv/bin:${PATH}"

COPY rootfs /
RUN chmod a+x /etc/services.d/immich-dlna/run
