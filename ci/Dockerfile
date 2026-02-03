# Single stage build for Jenkins with pre-installed plugins
# Use a recent LTS Jenkins version with JDK 21
FROM jenkins/jenkins:lts-jdk21

# Install additional system utilities needed for tests
# Using system level apt-get with explicit cache handling
USER root
RUN apt-get update && \
    apt-get install -y iputils-ping gzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER jenkins

# Copy plugins.txt
COPY plugins.txt /tmp/plugins.txt

# Install plugins using jenkins-plugin-cli
# This handles plugin dependencies automatically
RUN jenkins-plugin-cli --plugin-file /tmp/plugins.txt --verbose

# Set Jenkins configuration to skip setup wizard and disable UDP multicast
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Dhudson.DNSMultiCast.disabled=true"

# Health check to verify Jenkins is ready
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/api/json || exit 1

# Expose Jenkins port
EXPOSE 8080

# Expose Jenkins agent port
EXPOSE 50000
