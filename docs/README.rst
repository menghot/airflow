 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Documentation
#############

This directory contains documentation for the Apache Airflow project and other packages that are closely related to it ie. providers packages.  Documentation is built using `Sphinx <https://www.sphinx-doc.org/>`__.

Development documentation preview
==================================

Documentation from the development version is built and automatically published: `s.apache.org/airflow-docs <https://s.apache.org/airflow-docs>`_

Building documentation
======================

To generate a local version you can use `<../BREEZE.rst>`_.

The documentation build consists of verifying consistency of documentation and two steps:

* spell checking
* building documentation

You can only run one of the steps via ``--spellcheck-only`` or ``--docs-only``.

.. code-block:: bash

    breeze build-docs

or just to run spell-check

.. code-block:: bash

     breeze build-docs --spellcheck-only

or just to run documentation building

.. code-block:: bash

     breeze build-docs --docs-only

Also, you can only build one documentation via ``--package-filter``.

.. code-block:: bash

    breeze build-docs --package-filter <PACKAGE-NAME>

You can also use shorthand names as arguments instead of using the full names
for airflow providers. To find the short hand names, follow the instructions in :ref:`generating_short_form_names`.

You can also see all the available arguments via ``--help``.

.. code-block:: bash

    breeze build-docs --help

Running the Docs Locally
------------------------

Once you have built the documentation you can start the webserver in breeze environment and view the built documentation
at ``http://localhost:28080/docs/``

Alternatively, run the following command from the root directory.
You need to have Python installed to run the command:

.. code-block:: bash

    docs/start_doc_server.sh


Then, view your docs at ``localhost:8000``, if you are using a virtual machine e.g WSL2,
you need to find the WSL2 machine IP address and in your browser replace "0.0.0.0" with it
``http://n.n.n.n:8000``, where n.n.n.n will be the IP of the WSL2.

Troubleshooting
---------------

If you are creating ``example_dags`` directory, you need to create ``example_dags/__init__.py`` with Apache
license or copy another ``__init__.py`` file that contains the necessary license.

.. _generating_short_form_names:

Generating short form names for Providers
-----------------------------------------

Skip the ``apache-airflow-providers-`` from the usual provider full names.
Now with the remaining part, replace every ``dash("-")`` with a ``dot(".")``.

Example:
If the provider name is ``apache-airflow-providers-cncf-kubernetes``, it will be ``cncf.kubernetes``.

Note: For building docs for apache-airflow-providers index, use ``providers-index`` as the short hand operator.

Cross-referencing syntax
========================

Cross-references are generated by many semantic interpreted text roles.
Basically, you only need to write:

.. code-block:: rst

    :role:`target`

And a link will be
created to the item named *target* of the type indicated by *role*. The link's
text will be the same as *target*.

You may supply an explicit title and reference target, like in reST direct
hyperlinks:

.. code-block:: rst

    :role:`title <target>`

This will refer to *target*, but the link text will be *title*.

Here are practical examples:

.. code-block:: rst

    :class:`airflow.models.dag.DAG` - link to Python API reference documentation
    :doc:`/docs/operators` - link to other document
    :ref:`handle` - link to section in current or another document

    .. _handle:

    Section title
    ----------------------------------

Role ``:class:`` works well with references between packages. If you want to use other roles, it is a good idea to specify a package:

.. code-block:: rst

    :doc:`apache-airflow:installation/index`
    :ref:`apache-airflow-providers-google:write-logs-stackdriver`

If you still feel confused then you can view more possible roles for our documentation:

.. code-block:: bash

    ./list-roles.sh

For more information, see: `Cross-referencing syntax <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_ in Sphinx documentation

Support
=======

If you need help, write to `#documentation <https://apache-airflow.slack.com/archives/CJ1LVREHX>`__ channel on `Airflow's Slack <https://s.apache.org/airflow-slack>`__
