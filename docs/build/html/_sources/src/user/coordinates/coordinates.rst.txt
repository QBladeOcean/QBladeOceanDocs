Global Coordinate System
========================

The fixed global coordinate system in QBlade is defined as shown in :numref:`fig-globalcoord`. The x-axis points in the downwind direction and the z-axis points vertically upwards. The y-axis is oriented to form a right handed coordinate system. If a sensor name in one of QBlades graphs is annotated by **_g**, such as **X_g** it is referring to the global coordinate system. Whenever a coordinate system is displayed in QBlade the following color-code is used: x-axis indicated in **RED**, y-axis indicated in **GREEN** and z-axis indicated in **BLUE**. This color code also applies to all local coordinate systems.

.. _fig-globalcoord:
.. figure:: globalcoord.png
    :align: center
    :alt: Visualization of the global coordinate system.
    
    Visualization of the global coordinate system.
    
Local Body Coordinate Systems
=============================

Some simulation results are output into local body coordinate systems, such as the local blade coordinate systems or the local tower coordinate system. In general, the local coordinate systems are denoted by **_g** in the variable name, such as **X_g**.

.. _fig-localcoord:
.. figure:: localcoord.png
    :align: center
    :alt: Visualization of the local blade and tower coordinate systems.
    
    Visualization of the local blade and tower coordinate systems.

Local Blade Coordinate System
-----------------------------

For the rotor blades and struts the x-axis is oriented normal to the chord, pointing towards the suction side, the y-axis is oriented in the chord wise direction, pointing towards the trailing edge and the z-axis points along the principal beam direction to form a right handed coordinate system. If the rotor is constructed to rotate in the reverse direction the y-axis is pointing towards the leading edge instead.

Local Tower Coordinate System
-----------------------------

For the tower the local x-axis is oriented along the global x-axis, the local y-axis is pointing towards the global y-axis and the tower z-axis points along the principal beam direction.

Local Sensor Coordinate Systems
===============================

Additional turbine load sensors are written out in the following coordinate systems: Blade CS, Coned CS, Nacelle CS, Hub CS, Shaft CS. These coordinate systems are defined inline with convention used in the FAST users Guide :footcite:`FASTUG`. An overview is given in :numref:`fig-localcoord2`.

.. _fig-localcoord2:
.. figure:: localcoord2.png
    :align: center
    :alt: Visualization of the Blade, Coned, Nacelle, Hub and Shaft CS.
    
    Visualization of the Blade, Coned, Nacelle, Hub and Shaft CS.

.. footbibliography::
