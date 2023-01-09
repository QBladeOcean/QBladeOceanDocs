DLC Generator
*************

.. admonition:: QBlade-EE

   This feature is only available in the Enterprise Edition of QBlade.
   
QBlade-EE is equipped with a fully featured automatic DLC generator (see :numref:`fig-dlc_diag`), according to the following standards:

* **IEC 61400-1 Ed. 2**
* **IEC 61400-1 Ed. 3**
* **IEC 61400-2 Ed. 2**
* **IEC 61400-3-1 Ed. 1**
* **IEC 61400-3-2 Ed. 2**

Furthermore, the DLC generator allows to setup automatic evaluations of *Campbell Diagrams* and *Aeroelastic Operational (Power) Curves*.
After a DLC has been defined in the dialog, all individual loadcases can be automatically exported as ``.sim`` files, for an evaluation in the Command Line Interface (:ref:`CLI Overview`) or can be directly evaluated in the GUI via the :ref:`Multi-Threaded Batch Analysis` (see :numref:`fig-dlc_gen`).
   
.. _fig-dlc_diag:
.. figure:: dlc_diag.png
   :align: center
   :alt: The DLC Generator Dialog.

   The DLC Generator Dialog.
   
.. _fig-dlc_gen:
.. figure:: dlc_gen.png
   :align: center
   :alt: Generation of DLC Simulations from a DLC definition.

   Generation of DLC Simulations from a DLC definition.
   
Alternatively, DLC sets can be defined using an Excel spreadsheet.
   
