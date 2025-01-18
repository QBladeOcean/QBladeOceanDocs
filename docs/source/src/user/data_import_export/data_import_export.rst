Object Hierarchy and Data Structure
====================================
   
In QBlade's back-end, all simulation objects and data are organized into a hierarchical structure, representing the "building blocks" of a complete aero-servo-hydro-elastic wind turbine simulation. This hierarchy is depicted in the following figure:
  
 
.. _fig-data_struct:
.. figure:: data_struct.png
   :align: center
   :alt: Overview of QBlades data structure

   Overview of QBlades data structure.

Hierarchy Details
-----------------

- **Automatic Deletion**: When a data object is deleted from QBlade's database, all associated objects lower in the hierarchy are automatically removed.  
  - For example: Deleting a *Polar* object results in the deletion of all associated rotor blades and, consequently, any related simulations.

Project Serialization
=====================
QBlade supports the serialization of all data and objects into a binary QBlade Project File (`.qpr`) format. This memory-efficient binary format facilitates easy sharing and saving of projects and simulation results.

Archive Versioning
------------------

- **Archive Format Versioning**: Each `.qpr` file includes an **Archive Format Version Number**, ensuring compatibility.  
  - A `.qpr` file can only be opened in QBlade releases with an equal or higher archive version number than that of the saved file to ensure that all features stored in the :code:`qpr` file can be interpreted correctly..

Data Objects Import and Export
==============================

In QBlade, various data objects collectively form the foundation of an aero-servo-hydro-elastic simulation. These objects and their respective file types are outlined below (see :numref:`fig-data_struct`):

**Data Object Types**
---------------------

- **Simulation Definition**: Specifies boundary conditions, discretization, simulation duration, and additional parameters.  
  File type: ``.sim``
  
- **Turbine Definition**: Describes the aero-servo-hydro-elastic model of the turbine.  
  File type: ``.trb``
  
- **Blade Definition**: Contains the aerodynamic configuration of the rotor blade.  
  File type: ``.bld``
  
- **Polar**: Stores airfoil performance coefficients.  
  File type: ``.plr``
  
- **Airfoil**: Defines the outer contour of the airfoil.  
  File type: ``.afl``
  
- **Windfield**: Includes time-resolved inflow data.  
  File types: ``.bts``, ``.hht``, ``.inp``
  
- **Wavefield**: Represents time-resolved sea state information.  
  File type: ``.lwa``

Object Creation and Editing
---------------------------

QBlade allows users to easily create and edit data objects via custom GUI dialogs. These objects can also be:

- **Exported**: Objects can be exported to an ASCII format for external editing or customization.
- **Imported**: Objects created or edited externally in ASCII can be seamlessly imported back into QBlade.

This feature, combined with the :ref:`Software in Loop Interface (SIL)`, enables users to create custom optimization or variable space exploration scripts. These scripts can target any aspect of the simulation model, including airfoil shapes, aerodynamic coefficients, structural parameters, hydrodynamic properties, and control settings.