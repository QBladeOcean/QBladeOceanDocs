.. QBlade Documentation documentation master file, created by
   sphinx-quickstart on Thu Jul 15 12:34:20 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


`...back to QBlade.org website <https://qblade.org>`_


====================
QBlade Documentation
====================

QBlade :footcite:p:`Marten19` is a state of the art multi-physics code, covering the complete range of aspects required for the aero-servo-hydro-elastic simulation of horizontal, or vertical axis wind turbines. 
QBlade is being developed since 2010 at the Technical University of Berlin, and is realized as a modular implementation of highly efficient multi-fidelity aerodynamic, structural dynamic and hydrodynamic solvers in a modern, object oriented C++ framework.  

QBlade leverages the current computer architecture by thoroughly utilizing CPU (via OpenMP) and GPU (via OpenCL) parallelization techniques for a high numerical performance. 
QBlade is a platform independent software, and can be deployed on workstations or clusters running Windows, Unix or MacOS based operating systems. 
The software is equipped with an intuitive graphical user interface that aids the user during the whole wind turbine design process. 
All turbine and simulation details are readily available to be accessed and modified in a logical well-structured and tested interface. 
Simulation results are presented in dynamic graphs that give insight into every simulation detail. 
Simulations and turbine designs are fully rendered in real time to aid with the comprehension and evaluation of our complex multi-physics models. 
QBlade enabled the serialization of the complete model data, setup and results into project files to enable simple sharing and collaboration of complex simulation and turbine design projects. 
The Community Edition (CE) of QBlade is freely available to everyone under the open-source GNU GPLv2 license.

QBlade uses a highly optimized and thoroughly validated Lifting Line Free Vortex Wake Method for its aerodynamic calculations. 
Instead of approximating the wake aerodynamics with a steady-state momentum balance (BEM), the rotor wake is explicitly modeled through Lagrangian vortex elements. 
This results in a more accurate and detailed spatial and temporal representation (see :footcite:t:`Marten2020`) of the rotor induction, when compared to BEM approaches, and fully resolves the velocity distribution behind the rotor. 
This allows to assess wind turbine wake interaction, accurately accounts for the aerodynamics of oscillating floating wind turbine structures and explicitly resolves unsteady vertical axis wind turbine wake dynamics (see :footcite:t:`Balduzzi2017b`). 
As an alternative with lower computational demand the aerodynamics of horizontal-axis wind turbines can be simulated using an unsteady polar-BEM implementation (see :footcite:t:`polarBEM`).

The structural dynamics in QBlade are modeled in a true multi-body formulation. The sub components of the multi-body model are made up of rigid- or flexible nonlinear Euler beam elements in a corotational formulation. 
For floating offshore simulations QBlade integrates cable elements in the absolute nodal coordinate formulation (ANCF) which meet the requirements to effectively model the nonlinear dynamics of complex mooring systems.
Both bottom-fixed and floating offshore wind turbine systems can be modeled in QBlade. 

The hydrodynamic loads on the wind turbine’s substructure are calculated either via the potential flow theory, the Morison equation based strip theory or a user defined combination of the two. 
The integrated potential flow approach also includes the higher order slow drift forces obtained from quadratic transfer functions. QBlade integrates with potential flow data from common software such as the WAMIT, NEMOH or similar toolboxes.

.. _fig-turbines:
.. figure:: images/turbines.jpg
    :align: center
    :alt: Turbines

    Different wind turbine types modelled with QBlade.

.. toctree::
   :maxdepth: 4
   :caption: QBlade Docs

   src/theory/index_th
   src/user/index_ue
   src/validation/index_val
   src/license/index_license

.. footbibliography::
