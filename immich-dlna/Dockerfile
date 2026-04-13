ARG BUILD_FROM=ghcr.io/hassio-addons/base:17.2.1
FROM ${BUILD_FROM}
ARG APP_GIT_URL=https://github.com/DevrajGajurel/ha-app-immich-dlna.git
ARG APP_GIT_REF=main

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apk add --no-cache python3 py3-pip git

RUN pip3 install --no-cache-dir "git+${APP_GIT_URL}@${APP_GIT_REF}"

COPY rootfs /
RUN chmod a+x /etc/services.d/immich-dlna/run
