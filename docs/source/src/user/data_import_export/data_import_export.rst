Object Hierarchy and Data Structure
====================================
   
In the back-end of QBlade all simulation objects and all data is organized in a specific hierarchy, representing the 'building blocks' of a completer aero-servo-hydro-elastic wind turbine simulation.
The data structure and object hierarchy of QBlade is shown in the following figure. 
  
 
.. _fig-data_struct:
.. figure:: data_struct.png
   :align: center
   :alt: Overview of QBlades data structure

   Overview of QBlades data structure.
   
One important thing to note is that when a data object is deleted from QBlades database all objects associated with it, that are below in the object hierarchy, are automatically removed from the database.
As an example: If a polar object is deleted all associated rotor blades are deleted and thus all associated simulations as well!
   
Project Serialization
=====================
   
Object Import and Export
========================