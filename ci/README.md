# Docker-based Jenkins CI Infrastructure

This directory contains Docker configuration for building and running Jenkins instances for testing the jenkinsapi library.

## Quick Start: Local Development

### Build the Docker image locally

```bash
cd ci/
docker build -t jenkinsapi-jenkins:local .
```

### Run Jenkins with docker-compose

```bash
cd ci/
docker-compose up -d
```

Jenkins will be available at `http://localhost:8080` once it's ready. The health check will monitor its status.

```bash
# View logs
docker-compose logs -f jenkins

# Stop Jenkins
docker-compose down

# Clean up volumes
docker-compose down -v
```

## Testing with Docker

Run tests using the locally built Docker image:

```bash
# From repository root
JENKINS_DOCKER_IMAGE=jenkinsapi-jenkins:local pytest -sv jenkinsapi_tests/systests/
```

### Environment Variables

- `JENKINS_DOCKER_IMAGE`: Docker image to use (e.g., `jenkinsapi-jenkins:local`)
- `SKIP_DOCKER`: Set to `1` to skip Docker and use the war file instead
- `JENKINS_URL`: Set to use an existing Jenkins instance instead of starting a new one

## Testing with War File Fallback

To verify the fallback to war file installation still works:

```bash
# From repository root
SKIP_DOCKER=1 pytest -sv jenkinsapi_tests/systests/
```

## GitHub Container Registry

The Jenkins image is automatically built and published to GitHub Container Registry (GHCR) on:
- Weekly schedule (Sunday 2 AM UTC)
- Manual trigger via workflow dispatch
- When ci/ directory changes

### Using the published image

```bash
# Pull the latest image
docker pull ghcr.io/pycontribs/jenkinsapi-jenkins:latest

# Run tests with published image
JENKINS_DOCKER_IMAGE=ghcr.io/pycontribs/jenkinsapi-jenkins:latest pytest -sv jenkinsapi_tests/systests/
```

### Image Tags

The workflow publishes multiple tags for flexibility:

- `latest` - Latest weekly build
- `weekly` - Alias for latest weekly
- `weekly-YYYY-MM-DD` - Dated weekly build
- `YYYY-MM-DD` - Build date only

## Files

- **Dockerfile** - Multi-stage build with pre-installed plugins
- **plugins.txt** - List of Jenkins plugins to install
- **docker-compose.yml** - Local development configuration

## Troubleshooting

### Jenkins takes a long time to start

Jenkins initialization may take 30-60 seconds on first run. The health check is configured with appropriate timeouts. Check logs:

```bash
docker-compose logs jenkins
```

### Port already in use

If port 8080 is already in use, modify the port mapping in docker-compose.yml:

```yaml
ports:
  - "8081:8080"  # Use 8081 instead
```

Then access Jenkins at `http://localhost:8081`

### Image build fails

Ensure you have:
- Docker installed and running
- At least 4GB available disk space
- Network connectivity to download plugins

## Architecture

The Dockerfile uses a multi-stage build for efficiency:

1. **Builder stage**: Installs all plugins using `jenkins-plugin-cli`
2. **Final stage**: Copies pre-installed plugins from builder

This approach:
- Eliminates runtime plugin installation delays
- Ensures consistent plugin versions
- Reduces image size by ~200MB vs installing at runtime

## Next Steps

See the main README.rst for:
- Running the full test suite
- How the docker launcher integrates with CI
- Performance comparisons with war file approach
