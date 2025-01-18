
Campbell Graphs
###############

.. admonition:: QBlade-EE

   This feature is only available in the Enterprise Edition of QBlade.

Campbell Graphs provide a visualization of the interaction between a wind turbine's structural natural frequencies and the excitation frequencies caused by rotor harmonics and environmental conditions, such as wind speed. They are an essential tool for identifying potential resonance conditions that could impact turbine performance and durability.

Simulation Setup for Campbell Graphs
************************************

An efficient way to set up Campbell Graphs is using the Design Load Case Generator (see :ref:`Design Load Case Generation`). Choosing the *Steady Power Curve* standard allows for efficient setup of simulations across a range of wind speeds. Ensure the :ref:`Modal Analysis` feature is activated for each simulation. After generating the simulations from this DLC definition, they can be quickly evaluated using the :ref:`Multi-Threaded Batch Analysis` feature, and subsequently, a Campbell Graph can be generated.

.. _fig-modal5:
.. figure:: modal_4.png
   :align: center
   :scale: 35%
   :alt: Setup of *Steady Power Curve* simulations for modal analysis

   Setup of *Steady Power Curve* simulations for modal analysis

Turbine Settings
****************

To accurate capture aerodynamic damping the user should select the option **Aero. Loads: Aero. Panels**. When the aerodynamic loads are evaluated at the panels the aerodynamic gradients are also evaluated. This has no impact in time domain simulations with small timesteps, but largely affects the damping ratios obtained from a modal analysis. Furthermore, the user should enable the evaluation of **Geometric Stiffness** so that the modal analysis can accurately capture centrifugal stiffening and softening effects.

.. _fig-modal6:
.. figure:: modal_5.png
   :align: center
   :scale: 60%
   :alt: Turbine structural settings recommended for the modal analysis

   Turbine structural settings recommended for the modal analysis
   
Campbell Graph Generation
*************************

Campbell graphs can be generated from a set of simulations for which a :ref:`Modal Analysis` has been carried out. Generally, this set of simulations spans over a range of wind speeds or rotational speeds. Across this range, the modes are tracked using the Modal Assurance Criterion (MAC). The modal frequencies and damping ratios are then aggregated and visualized in the **Campbell Graph**. To generate a Campbell graph, first select a simulation. The set of simulations will consist of all simulations that share the same turbine object as the selected simulation. The *Modal Analysis Dock Window* in :numref:`fig-modal3` is used to generate the Campbell diagram.

.. _fig-modal3:
.. figure:: modal_1.png
   :align: center
   :scale: 35%
   :alt: The Modal Analysis Dock Window

   The Modal Analysis Dock Window
   
   
The user can choose to sort the simulation set based on rotational speed or wind speed (**Sort**). The value **d_f [Hz]** specifies the maximum allowable delta in frequency for the same mode between two adjacent operating points during the mode sorting process. **from Mode** selects the starting mode for generating the Campbell diagram, and **num Modes** specifies the number of different modes (starting from **from Mode**) for the Campbell diagram. Clicking on **Create Campbell Graph Data** then generates the mode shapes. An exemplary Campbell Graph is shown in :numref:`fig-modal4`.

.. _fig-modal4:
.. figure:: modal_3.png
   :align: center
   :scale: 35%
   :alt: Campbell Graph showing modal frequencies and damping ratios

   Campbell Graph showing modal frequencies and damping ratios
   

.. footbibliography::

