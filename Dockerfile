FROM ubuntu:16.10
MAINTAINER James Shaw <js102@zepler.net>

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    wget \
    apt-transport-https \
    && add-apt-repository http://dl.openfoam.org/ubuntu \
    && sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -" \
    && apt-get update && apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    make \
    rsync \
    openfoam4 \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r phd && \
    useradd -r -m -d /home/phd -s /sbin/nologin -g phd phd && \
    chown -R phd:phd /home/phd
RUN mkdir -p /home/phd/build && chown phd:phd /home/phd/build
USER phd

RUN git clone --branch master https://github.com/hertzsprung/make-common.git /home/phd/src/make-common \
    && git clone --branch master https://github.com/AtmosFOAM/AtmosFOAM-tools.git /home/phd/src/AtmosFOAM-tools \
    && git clone --branch master https://github.com/AtmosFOAM/AtmosFOAM.git /home/phd/src/AtmosFOAM \
    && git clone --branch master https://github.com/hertzsprung/AtmosTests.git /home/phd/src/AtmosTests

ENV MAKE_COMMON=/home/phd/src/make-common \
    ATMOSFOAM_TOOLS_SRC=/home/phd/src/AtmosFOAM-tools/src \
    ATMOSFOAM_SRC=/home/phd/src/AtmosFOAM/src

RUN echo ". /opt/openfoam4/etc/bashrc" >> /home/phd/.bashrc

RUN /bin/bash -c ". /opt/openfoam4/etc/bashrc && cd /home/phd/src/AtmosFOAM-tools && ./Allwmake"
RUN /bin/bash -c ". /opt/openfoam4/etc/bashrc && cd /home/phd/src/AtmosFOAM && ./Allwmake"


