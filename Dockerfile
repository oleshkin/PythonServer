# syntax=docker/dockerfile:1
# Pulling the latest python img.
FROM python:latest

# Use /usr/src/app as our workdir.
WORKDIR /usr/src/app

# Copy our server.py file to 'usr/src/app/server.py'.
COPY server.py ./

# Install a dependency.
RUN pip install sshkeyboard

# Container is listening on poart 65432.
EXPOSE 65432

# Run the command
CMD  ["python", "./server.py"]