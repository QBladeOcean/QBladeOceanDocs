Design Load Cases Overview
**************************

.. admonition:: QBlade-EE

   This feature is only available in the Enterprise Edition of QBlade.
   
For the certification of a wind turbine it is often required to assess the wind turbine lifetime and structural integrity by means of simulations. These simulations are referred to as Design Load Cases (DLC's). Depending on the IEC standard, after which the turbine is to be certified, an individual DLC typically is a simulation timeseries between 10 and 60 min length. To be representative of the whole turbine life-cycle a full certification requires several hundrets to thousands of DLC's to be evaluated. Each DLC is unique in its boundary condition (wind & waves) and operational state (normal power production, shut-down, fault, etc...). While each individual DLC can be setup manually with ease in QBlade's user interface, generating several hundret DLC's manually is not desireable. 

QBlade-EE is equipped with a fully featured automatic DLC generator (see :numref:`fig-dlc_diag`), according to the following standards:

* **IEC 61400-1 Ed. 2**
* **IEC 61400-1 Ed. 3**
* **IEC 61400-2 Ed. 2**
* **IEC 61400-3-1 Ed. 1**
* **IEC 61400-3-2 Ed. 2**

There two different ways how DLC's can be generated in QBlade with a high degree of automation. After all DLC simulations have been defined in QBlade all simulations are typically exported as Simulation Definition Files (:ref:`Simulation Definition ASCII File`) and then evaluated in parallel in the Command Line Interface (:ref:`CLI Overview`).
 
DLC Object Generation (in GUI)
******************************

This feature allows to generate a DLC object, which contains the definitions of all simulation timeseries for a specific DLC number from a specific IEC standard. After a DLC object has been generated, all simulations belonging to the DLC object can either be auto-generated as *Simulation Definition Objects* within QBlade or be exported as *Simulation Definition ASCII Files*.



Template
--------
The automatic DLC generator can generate DLC's after a user selected standard. In the Template subsection of the dialog the user may choose the DLC, the IEC standard and a name for the DLC object.

Turbine Data
------------
In this section the turbine object, for which the DLC's should be generated, and the *Turbine Class* and *Turbulence Class* can be chosen.

DLC Parameter Range
-------------------

The user can choose the range and increments of windspeeds, inflow angles and turbine initial conditions that are required for the DLC definition. Depending on the DLC number that has been chosen some fields are automatically dactivated if they are not required.

Wind Model
----------

In this section the user can choose the wind model for the setup of the DLC. Typically all values are filled out automatically, according to the chosen IEC standard and the DLC number.

Turbulent Grid Parameters
-------------------------

The turbulent wind fields that are required for some DLC's are generated automatically by TurbSim and imported into QBlade if required. The spatial and temporal discretization, the wind field dimensions and the reference height can be chosen in this section.

Environmental Vars
------------------

The site specific environmental variables can be defined by the user.

General Sim Settings 
--------------------

Here the user needs to define the duration of the simulation (typically 600s with some added time to remove initial transients) and the timestep of the simulation. 

Rotational Speed Setting
------------------------

In this section the user can choose how the ramp-up phase should be handled (see :ref:`Rotational Speed Settings`).

Simulation Event(Fault) Settings
--------------------------------

If a specific event (such as shut-down, start-up, emergency brake, gid loss, etc.) should be included in the simulation the event definition file can be added to the simulation. SImulation events, and how they are defined, are detailed here: :ref:`Turbine Behavior`.

Structural Sim Settings
-----------------------

These settings concern the structural simulation of the wind turbine and are detailed here: :ref:`Structural Simulation Settings`.

Modal Analysis Settings
-----------------------

A modal analysis can be performed at the end of each DLC, if activated here. As an example, this feature can be used to automatically generate **Campbell** diagrams.

Stored Sim Data
---------------

In this section the user can choose from which timestep and what kind of data should be stored for each generated simulation. Typically the initial transient time is discarded from each DLC run.
   
.. _fig-dlc_diag:
.. figure:: dlc_diag.png
   :align: center
   :alt: The DLC Generator Dialog.

   The DLC Generator Dialog.
   
Exporting DLC Definitions
*************************

After a *DLC Definition Object* has been defined through the dialog, all individual simulations can be automatically exported as ``.sim`` files, for an evaluation in the Command Line Interface (:ref:`CLI Overview`) or can be directly be generated and later evaluated in the GUI via the :ref:`Multi-Threaded Batch Analysis`. To export the DLC object into .sim files press: " Export .sim Files from this DLC Definition". To generate Simulation Objects within QBlade press "Create SImulations from this DLC Definition". (see :numref:`fig-dlc_gen`).
   
.. _fig-dlc_gen:
.. figure:: dlc_gen.png
   :align: center
   :alt: Generation of DLC Simulations from a DLC definition.

   Generation of DLC Simulations from a DLC definition.
   
DLC Generation via Spreadsheets
*******************************

Alternatively, to using the GUI based dialog, DLC's may also be generated, based on a spreadsheet software. This gives the user full controll over each aspect of the DLC definition and is especially usefull in the DLC generation for offshore wind turbines where wind and wave distributions, their misalignement and sea currents need to be combined in often unique ways. 

The general methodology, when generating DLC's via a spreadsheet, is to define simulation definition (.sim), wind (.inp) and wave (.lwa) template files and only to define and modify the variable parameters in a spreadsheet. When the spreadsheet is finished and all entries are defined it is possible to either import all defined simulation into QBlade as *Simulation Definition Objects* or to automatically generate *Simulation Definition ACII Files* from the spreadsheet.

The definition of a single simulation requires 33 entries (columns) in a spreadsheet. The different entries are explained in detail in the following. If an entry should not be defined please insert *none* into the respective column. Only spreadsheet lines with 33 columns are identified during import.

1 **Name** : Each timeseries should have a unique name assigned.

2 **Simulation Length** : The length of the timeseries in [s].

3 **Master Simulation** : The path to a simulation definition template. A relative path based on the spreadsheet location can be used. This needs to be a *Simulation Definition ASCII File* with all associated files (.trb, plr, .bla, etc.). In this template all fixed varuiables that are not defined in one of the spreadsheet columns can be set.

4 **Events** : The (absolute or relative) path to an event definition file. If no event should be simulation insert the word *none*.  

5 **Windspeed** : The windspeed in [m/s].

6 **Horizontal Inflow Angle** : The horizontal inflow angle in [°].

7 **Vertical Inflow Angle** : The vertical inflow angle in [°].

8 **Shear Exponent** : The shear exponent of the power law wind profile.

9 **Turbulence Seed** : The seed that is used by TurbSim for the turbulent windfield generation (if a TurbSim template is defined).

10 **Hub Height Input File** : The (absolute or relative) path of a hub-height wind input file.

11 **TurbSim Template** : The (absolute or relative) path of the TurbSim input file (.inp) that will be used as a template for the generation of turbulent wind fields. Depending on the user entries in columns 4-9 the respective values in the template are overwritten.

12 **Water Depth** : The water depth in [m]. If an onshore turbine is simulated use the value 0.

13 **Significant Height (Hs)** : The significant wave height in [m].

14 **Significant Wave Period (Tp)** : The significant wave period in [s].

15 **Wave Misalignement** : The misalignement between wind and waves in [°]. The wave direction is calculated so that the wave is misaligned from the wind by the user specified value as a positive rotation around the global z-axis.

15 **Wave Seed** : The seed that is used by the wave generator during the generation of wave timeseries from wave spectra.

16 **Wave Template** : The (absolute or relative) path to a :ref:`Wave Definition ASCII File` that is used as a template for the wave generation. Depending on the user entries in column 13-15 the respective values in the template are overwritten.

17 **Near Surface Current Velocity** : The velocity of the near surface current in [m/s], see :ref:`Currents`.

18 **Near Surface Current Direction** : The direction of the near surface current in [°], see :ref:`Currents`.

19 **Near Surface Current Depth** : The depth of the near surface current in [m], see :ref:`Currents`.

20 **Sub Surface Current Velocity** : The velocity of the sub surface current in [m/s], see :ref:`Currents`.

21 **Sub Surface Current Direction** : The direction of the sub surface current in [°], see :ref:`Currents`.

22 **Sub Surface Current Exponent** : The exponent of the sub surface current velocity profile, see :ref:`Currents`.

23 **Near Shore Current** : The velocity of the near shore current in [m/s], see :ref:`Currents`.

24 **Near Shore Current Direction** : The direction of the near shore current in [°], see :ref:`Currents`.

25 **Intial Rotor Yaw** : The intial rotor yaw of the turbine at the beginning of the simulation, in [°]

26 **Intial Rotor Azimuth** : The intial rotor azimuthal angle of the turbine at the beginning of the simulation, in [°]

27 **Intial Rotor Pitch** : The intial collective rotor pitch angle at the beginning of the simulation, in [°]

28 **Initial FLoater X Position** : The initial position of the floating wind turbine in X-direction, in [m]

29 **Initial FLoater Y Position** : The initial position of the floating wind turbine in Y-direction, in [m]

30 **Initial FLoater Z Position** : The initial position of the floating wind turbine in Z-direction, in [m]

31 **Initial FLoater X Rotation** : The initial rotation of the floating wind turbine around X, in [°]

32 **Initial FLoater Y Rotation** : The initial rotation of the floating wind turbine around Y, in [°]

33 **Initial FLoater Z Rotation** : The initial rotation of the floating wind turbine around Z, in [°]