FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends blender fonts-dejavu-core ca-certificates libegl1 libgl1-mesa-dri xvfb && rm -rf /var/lib/apt/lists/*
WORKDIR /work
CMD ["blender", "-b"]
