# Single stage build for Jenkins with pre-installed plugins
FROM jenkins/jenkins:lts-jdk17

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
