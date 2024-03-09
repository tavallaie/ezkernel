================
 ezkernel
================

ezkernel is a Python library for managing Jupyter kernels. With ezkernel, you can easily add, remove, and rename Jupyter kernels directly from the command line.

Installation
============

To install ezkernel, simply run this command in your terminal:

.. code-block:: bash

    pip install ezkernel

Features
========

- Add new Jupyter kernels
- Remove existing Jupyter kernels
- Rename Jupyter kernels

Usage
=====

Adding a Kernel
---------------

To add a new Jupyter kernel, use the following command:

.. code-block:: bash

    ezkernel add <kernel-name> --display-name "Display Name"

Removing a Kernel
-----------------

To remove an existing Jupyter kernel, use:

.. code-block:: bash

    ezkernel remove <kernel-name>

Renaming a Kernel
-----------------

To rename an existing Jupyter kernel, use:

.. code-block:: bash

    ezkernel rename <old-kernel-name> <new-kernel-name>

Contributing
============

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

License
=======

`MIT <https://choosealicense.com/licenses/mit/>`_
