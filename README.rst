Jenkinsapi
==========

.. image:: https://badge.fury.io/py/jenkinsapi.png
    :target: http://badge.fury.io/py/jenkinsapi

Installation
------------

.. code-block:: bash

    pip install jenkinsapi

Important Links
---------------
* `Documentation <http://pycontribs.github.io/jenkinsapi/>`__
* `Source Code <https://github.com/pycontribs/jenkinsapi>`_
* `Support and bug-reports <https://github.com/pycontribs/jenkinsapi/issues?direction=desc&sort=comments&state=open>`_
* `Releases <https://pypi.org/project/jenkinsapi/#history>`_


About this library
-------------------

Jenkins is the market leading continuous integration system.

Jenkins (and its predecessor Hudson) are useful projects for automating common development tasks (e.g. unit-testing, production batches) - but they are somewhat Java-centric.

Jenkinsapi makes scripting Jenkins tasks a breeze by wrapping the REST api into familiar python objects.

Here is a list of some of the most commonly used functionality

* Add, remove, and query Jenkins jobs
* Control pipeline execution
    * Query the results of a completed build
    * Block until jobs are complete or run jobs asyncronously
    * Get objects representing the latest builds of a job
* Artifact management
    * Search for artifacts by simple criteria
    * Install artifacts to custom-specified directory structures
* Search for builds by source code revision
* Create, destroy, and monitor
    * Build nodes (Webstart and SSH slaves)
    * Views (including nested views using NestedViews Jenkins plugin)
    * Credentials (username/password and ssh key)
* Authentication support for username and password
* Manage jenkins and plugin installation

Full library capabilities are outlined in the `Documentation <http://pycontribs.github.io/jenkinsapi/>`__

Get details of jobs running on Jenkins server
---------------------------------------------

.. code-block:: python

    """Get job details of each job that is running on the Jenkins instance"""
    def get_job_details():
        # Refer Example #1 for definition of function 'get_server_instance'
        server = get_server_instance()
        for job_name, job_instance in server.get_jobs():
            print 'Job Name:%s' % (job_instance.name)
            print 'Job Description:%s' % (job_instance.get_description())
            print 'Is Job running:%s' % (job_instance.is_running())
            print 'Is Job enabled:%s' % (job_instance.is_enabled())

Disable/Enable a Jenkins Job
----------------------------

.. code-block:: python

    def disable_job():
        """Disable a Jenkins job"""
        # Refer Example #1 for definition of function 'get_server_instance'
        server = get_server_instance()
        job_name = 'nightly-build-job'
        if (server.has_job(job_name)):
            job_instance = server.get_job(job_name)
            job_instance.disable()
            print 'Name:%s,Is Job Enabled ?:%s' % (job_name,job_instance.is_enabled())

Use the call ``job_instance.enable()`` to enable a Jenkins Job.


Known issues
------------
* Job deletion operations fail unless Cross-Site scripting protection is disabled.

For other issues, please refer to the `support URL <https://github.com/pycontribs/jenkinsapi/issues?direction=desc&sort=comments&state=open>`_

Development
-----------

### Quick Start

1. Create and activate a virtual environment

.. code-block:: bash

    uv sync

2. Run tests

.. code-block:: bash

    uv run pytest -sv

### Using Docker for Testing (Recommended)

Jenkins can be started in Docker for testing, which is significantly faster than downloading and installing Jenkins.

**Requirements:**
- Docker installed and running

**Local Testing with Docker:**

.. code-block:: bash

    # Build the Docker image locally
    cd ci/
    docker build -t jenkinsapi-jenkins:local .

    # Run tests with Docker
    JENKINS_DOCKER_IMAGE=jenkinsapi-jenkins:local pytest -sv jenkinsapi_tests/systests/

**Using Pre-built Image from GitHub Container Registry:**

.. code-block:: bash

    # Tests will automatically pull the image if available
    pytest -sv jenkinsapi_tests/systests/

**Using War File (Fallback):**

If Docker is not available or you want to use the traditional approach:

.. code-block:: bash

    # Make sure Java is installed first
    SKIP_DOCKER=1 pytest -sv jenkinsapi_tests/systests/

For more detailed Docker setup and development instructions, see `ci/README.md <ci/README.md>`_

Python versions
---------------

The project has been tested against Python versions:

* 3.9 - 3.14

Jenkins versions
----------------

Project tested on both stable (LTS) and latest Jenkins versions.

Project Contributors
--------------------

* Aleksey Maksimov (ctpeko3a@gmail.com)
* Salim Fadhley (sal@stodge.org)
* Ramon van Alteren (ramon@vanalteren.nl)
* Ruslan Lutsenko (ruslan.lutcenko@gmail.com)
* Cleber J Santos (cleber@simplesconsultoria.com.br)
* William Zhang (jollychang@douban.com)
* Victor Garcia (bravejolie@gmail.com)
* Bradley Harris (bradley@ninelb.com)
* Kyle Rockman (kyle.rockman@mac.com)
* Sascha Peilicke (saschpe@gmx.de)
* David Johansen (david@makewhat.is)
* Misha Behersky (bmwant@gmail.com)
* Clinton Steiner (clintonsteiner@gmail.com)

Please do not contact these contributors directly for support questions! Use the GitHub tracker instead.
