FROM mcr.microsoft.com/dotnet/core/sdk:3.0

# Add a non-root user to prevent files being created with root permissions on host machine.
ENV USER=developer
ENV UID=1000
ENV GID=1000

RUN addgroup --gid "$GID" "$USER" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/developer" \
#    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

USER developer

ENV HOME /home/developer/app

WORKDIR /home/developer/app

EXPOSE 5000

ENTRYPOINT ["tail", "-f", "/dev/null"]