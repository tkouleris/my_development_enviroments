#FROM mcr.microsoft.com/dotnet/core/aspnet:3.0
FROM microsoft/dotnet:aspnetcore-runtime

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh | sh

RUN nvm install 4.4.7

RUN npm install -g npm

# Add a non-root user to prevent files being created with root permissions on host machine.
ENV USER=developer
ENV UID=1000
ENV GID=1000

RUN addgroup --gid "$GID" "$USER" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/developer" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

USER developer

ENV HOME /home/developer/app

WORKDIR /home/developer/app

ENTRYPOINT ["tail", "-f", "/dev/null"]