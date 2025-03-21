"""
About this library
==================

Jenkins is the market leading continuous integration system, originally created
by Kohsuke Kawaguchi. This API makes Jenkins even easier to use by providing an
easy to use conventional python interface.

Jenkins (and It's predecessor Hudson) are fantastic projects - but they are
somewhat Java-centric. Thankfully the designers have provided an excellent and
complete REST interface. This library wraps up that interface as more
conventional python objects in order to make most Jenkins oriented
tasks simpler.

This library can help you:

 * Query the test-results of a completed build
 * Get a objects representing the latest builds of a job
 * Search for artifacts by simple criteria
 * Block until jobs are complete
 * Install artifacts to custom-specified directory structures
 * username/password auth support for jenkins instances with auth turned on
 * Ability to search for builds by subversion revision
 * Ability to add/remove/query jenkins slaves

Installing JenkinsAPI
=====================

pip install jenkinsapi

Project Authors
===============

 * Salim Fadhley (sal@stodge.org)
 * Ramon van Alteren (ramon@vanalteren.nl)
 * Ruslan Lutsenko (ruslan.lutcenko@gmail.com)
 * Aleksey Maksimov
 * Clinton Steiner

Current code lives on github: https://github.com/pycontribs/jenkinsapi

"""

from importlib.metadata import version

from jenkinsapi import (
    # Modules
    command_line,
    utils,
    # Files
    api,
    artifact,
    build,
    config,
    constants,
    custom_exceptions,
    fingerprint,
    executors,
    executor,
    jenkins,
    jenkinsbase,
    job,
    node,
    result_set,
    result,
    view,
)

__all__ = [
    "command_line",
    "utils",
    "api",
    "artifact",
    "build",
    "config",
    "constants",
    "custom_exceptions",
    "executors",
    "executor",
    "fingerprint",
    "jenkins",
    "jenkinsbase",
    "job",
    "node",
    "result_set",
    "result",
    "view",
]
__docformat__ = "epytext"
__version__ = version("jenkinsapi")
