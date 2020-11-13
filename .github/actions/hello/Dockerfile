# Container image that runs your code
FROM python:3

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY hello.py /hello.py

#Make entrypoint.sh exacutable
RUN chmod +x /entrypoint.sh
RUN chmod +x /hello.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
