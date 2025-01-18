Floating and Node-Locked License Files
======================================

Commercial licenses of **QBlade Enterprise Edition** are implemented through license files. There are two types of license files: floating and node-locked.

Floating License Files
----------------------

Floating license files necessitate an active internet connection to validate the license. This validation occurs via an HTTPS request to a licensing service provider. Each floating license is allocated a certain number of seats. Within these constraints, any number of QBlade-EE instances can run concurrently on a single machine for each available seat. However, once all allocated seats are in use, no additional QBlade instances can be initiated on new machines until a seat becomes available by terminating all QBlade instances on a machine previously using a seat.

For continuous operation of QBlade-EE, periodic license validation checks require an uninterrupted internet connection.

Debugging Floating License Activation Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instances where QBlade-EE, once activated, crashes leading to a non-release of a license seat, thereby occupying a license unjustly, can arise. In such a case the :ref:`Command Line Interface (CLI)` can be used to manually free the license seat or require additional information. The following functionality exists:

:code:`QBladeEE -cli GET_MACHINES`
 Through the **GET_MACHINES** argument, the application can list all currently activated machines for this floating license.
 
:code:`QBladeEE -cli DEACTIVATE:MACHINE_ID`
 Supports deactivation of the machine that is identified by **MACHINE_ID**, with a special case for deactivating all machines activated through this license (**DEACTIVATE:ALL**). **Note:** Deactivation results in a failed license validation upon the next check for the deactivated machine, potentially disrupting ongoing simulations.

:code:`QBladeEE -cli LICENSE_DEBUG`
  Activates a debug mode providing detailed insights into the license activation and troubleshooting process.
  
Resolving OpenSSL Issues on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On certain Windows machines, the SIL (dll) version of QBlade-EE may encounter issues with initializing the OpenSSL libraries. These problems typically arise when the system cannot locate the necessary OpenSSL libraries in the QBlade directory. To fix this, you can add the QBlade directory to the system's PATH variable with the following steps:

#. **Open the Start Search Bar**: Type "System Environment Variables" and select "Edit the system environment variables" from the search results.

#. **System Properties Window**: In the System Properties window, click the "Environment Variables" button near the bottom of the Advanced tab.

#. **Edit the PATH Variable**: In the Environment Variables window, scroll to find the 'Path' variable under the 'System variables' section and select it. Then click 'Edit...'.

#. **Add QBlade Directory**: In the Edit Environment Variable window, click 'New' and paste the full path to the QBlade directory where the OpenSSL libraries (libssl-1_1-x64.dll and libcrypto-1_1-x64.dll) are located.

#. **Save and Exit**: Click 'OK' to close each window, ensuring your changes are saved.

After completing these steps, restart Windows to allow the changes to take effect. This should resolve the issue with initializing the OpenSSL libraries in QBlade's SIL interface. 

If the issue persists, particularly when loading the QBlade SIL interface library from Python, you can try the following additional step:

#. Copy the OpenSSL-related libraries (libssl-1_1-x64.dll and libcrypto-1_1-x64.dll) directly into the Python installation folder, placing them alongside the Python executable.

This workaround has proven effective in several cases and is likely related to machine-specific environment configurations. These configurations may involve conflicting or missing OpenSSL libraries within the Python environment, which prevent the proper initialization of the QBlade SIL interface.

Node-Locked License Files
-------------------------

Unlike floating licenses, node-locked licenses are tied to a specific hardware ID, eliminating the need for an internet connection. This license is uniquely issued for and restricted to the designated machine. Although node-locked licenses support offline operation, they lack the flexibility of floating licenses and are unsuitable for cloud computing or transferring between machines.

Node-locked licenses are ideally suited for standalone installations in secure or isolated environments where internet connectivity is a concern, or for users who prefer a simple, one-time licensing process without the need for ongoing management. They are also beneficial for organizations that prioritize software security and license control, as they provide a straightforward approach to licensing without the complexities of network-based checks or validations.

By choosing a node-locked license, organizations can ensure a robust and secure licensing mechanism that aligns with their specific operational needs and constraints, albeit with the understanding that such licenses offer less operational flexibility compared to their floating counterparts.