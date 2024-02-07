FROM debian:latest

RUN apt-get update && apt-get install -y \
lsb-release wget procps

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


CMD ["/bin/bash"]
