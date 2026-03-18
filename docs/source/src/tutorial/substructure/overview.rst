Guide to the QBlade Substructure Module
=======================================

.. note::
   The substructure file defines the physical and hydrodynamic foundation of your wind turbine. This guide outlines the core concepts, topology, and physics approaches required to successfully model complex onshore and offshore structures in QBlade. For all details and keywords see the section :ref:`Substructure Modelling` in QBlade's user guide!

What Can You Do with the Substructure Module?
---------------------------------------------

The substructure file extends far beyond basic tubular towers. You can use it to model:

* **Floating Offshore Wind Turbines (FOWTs):** Complete with pontoons, heave plates, columns, and comprehensive hydrodynamic forces.
* **Mooring Systems:** Flexible, buoyant cables that keep your floater stationed, including seabed contact and friction.
* **Lattice Towers:** Complex, multi-member onshore or offshore jacket structures with high degrees of freedom.
* **Multi-Rotor Assemblies:** Connecting multiple wind turbine rotors to a single, shared foundation.
* **Soil Dynamics:** Modeling how bottom-fixed foundations interact with the seabed using non-linear springs (p-y curves) with elastic perfectly-plastic hysteresis.

The Building Blocks
-------------------

Creating the physical geometry of your substructure relies on a strict triad: Joints, Elements, and Members (see :ref:`Substructure Topology`). You define these using space-separated data tables in your text file.


* **Joints (SUBJOINTS):** These are the structural nodes in 3D space (x, y, z). Everything connects to these points. If ``ISFLOATING`` is true, the origin (0,0,0) is at Mean Sea Level (MSL). If false, the origin is at the seabed. For more details, see :ref:`Substructure Joints`.
* **Elements (SUBELEMENTS, SUBELEMENTSRIGID, etc.):** Think of these as your material blueprints. They define the cross-section (cylindrical or rectangular), dimensions, mass distribution, and whether the part is rigid or flexible. **Crucial Note:** Every element needs a unique ID across *all* element tables. Read more in :ref:`Substructure Elements`.
* **Members (SUBMEMBERS):** These are the physical struts. A member connects Joint A to Joint B using a specific Element blueprint. Here, you also define member-specific properties like flooding (flooded area), marine growth, and structural discretization. See :ref:`Substructure Members` for formatting.

Making Connections
------------------

Your substructure geometry must be anchored to the turbine, the environment, and itself.

* **The Transition Piece (TP_INTERFACE_POS):** This is the master reference and connection point. It dictates where your substructure physically bolts onto the bottom of the wind turbine tower, the torquetube, or directly to the rotor nacelle assembly (RNA). Learn more in :ref:`The Transition Piece`.
* **Constraints (SUBCONSTRAINTS):** Use this table to dictate joint behavior. You can rigidly lock joints together, attach them to the Transition Piece, or fix them to the seabed. This table is also used to insert non-linear springs or dampers between joints to create compliant, flexible connections. See :ref:`Substructure Constraints`.

Mass & Buoyancy: Two Approaches
-------------------------------

QBlade gives you two distinct ways to handle the physical properties of your substructure (see :ref:`Modeling Options for an Offshore Substructure`). You can utilize one exclusively or mix them depending on your analysis goals.

Approach A: Explicit (Distributed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Mass:** Calculated automatically based on the length, cross-section, and material density of your individual ``SUBMEMBERS`` (see :ref:`Substructure Mass and Inertia`).
* **Buoyancy:** Calculated dynamically by the solver based on exactly how much of each member is submerged underwater at any given time step, accounting for local wave elevations (see :ref:`Substructure Buoyancy`). 
* *Tip:* You can use ``ADVANCEDBUOYANCY`` to increase the geometric resolution of partially submerged cylinders.

Approach B: Lumped (Simplified Matrix)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Mass:** You provide a single 6x6 mass and rotational inertia matrix (``SUB_MASS``) applied at a specific Center of Gravity point (``REF_COG_POS``). *Ensure your individual members are assigned near-zero mass to avoid double-counting.*
* **Buoyancy:** You define a linearized 6x6 hydrostatic stiffness matrix (``SUB_HYDROSTIFFNESS``) applied at a hydrodynamic reference point. 
* See :ref:`Lumped Mass, Inertia and Hydrodynamic Forces` for matrix formatting.

Hydrodynamics for Offshore Modelling
------------------------------------

For marine structures, QBlade evaluates wave kinematics and fluid forces using two primary hydrodynamic models (see :ref:`Hydrodynamic Modeling of a Substructure`). 

1. Morison Equation (Strip Theory)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **What it is:** Calculates viscous drag, added mass, and Froude-Krylov forces locally along slender cylinders or rectangular beams.
* **How to do it:** Define normal and axial coefficients using ``HYDROMEMBERCOEFF`` or ``HYDROJOINTCOEFF`` tables, then assign these IDs to your ``SUBMEMBERS``.
* **Best for:** Mooring lines, lattice/jacket structures, slender columns, and capturing viscous drag on floaters. Advanced features like MacCamy-Fuchs correction and High-Pass Filtered Morison Drag are available for fine-tuning. Full details in :ref:`Morison Equation (Strip Theory) Modelling`.

2. Linear Potential Flow Theory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **What it is:** Utilizes pre-calculated hydrodynamic databases from external Boundary Element Method (BEM) software like WAMIT, NEMOH, or ANSYS AQWA.
* **How to do it:** Point QBlade to your external files (e.g., ``.1`` for radiation, ``.3`` for excitation, ``.hst`` for stiffness) using keywords like ``POT_RAD_FILE`` and apply them to a single reference point (``REF_HYDRO_POS``).
* **Best for:** Large, bulky floaters (semi-submersibles, spar buoys) where wave radiation and diffraction are dominant and structural flexibility is secondary. Detailed setup is found in :ref:`Linear Potential Flow Modelling`.

.. tip::
   **The Industry Standard Hybrid:** The most common approach for FOWTs is to use Linear Potential Flow for the primary radiation/diffraction wave loads, while utilizing Morison Equation coefficients on explicit members purely to capture viscous drag (which potential flow inherently ignores).

5. Moorings & Soil Dynamics
---------------------------

* **Moorings (MOORMEMBERS & MOORELEMENTS):** Define flexible cables connecting your floater to the seabed. You define mass per length, axial stiffness (which can be non-linear via ``NLDATA`` tables), and hydrodynamic drag. QBlade handles seabed contact and friction automatically based on the ``SEABEDDISC`` parameter. Reference :ref:`Mooring Elements`.

* **Soil Modeling (NLSPRINGDAMPERS):** For bottom-fixed structures, the seabed yields under load. You can input force-displacement pairs (p-y curves) to create non-linear springs that mimic realistic soil resistance, complete with elastic perfectly-plastic hysteresis when ultimate soil resistance is reached. See :ref:`Nonlinear Spring and Damper Constraints` and :ref:`Soil Modeling with P-Y Curves`.

Quick Start Checklist for New Users
-----------------------------------

1. **Start Simple:** Build your geometry first using rigid elements (``SUBELEMENTSRIGID``). Ensure your topology looks correct in the QBlade visualizer before introducing complex physics or flexibility.
2. **Define the TP:** Place your ``TP_INTERFACE_POS`` and securely connect your upper substructure joints to it via the ``SUBCONSTRAINTS`` table.
3. **Choose your Mass Strategy:** Decide between a lumped 6x6 mass matrix or explicitly modeled member mass. Lumped is generally easier to debug for floating platforms.
4. **Add Hydrodynamics:** For floaters, import your WAMIT/NEMOH files. *Crucial:* Set ``STATICBUOYANCY`` to ``true`` if your potential flow file already accounts for dynamic wave elevations to prevent double-counting forces!
5. **Anchor It:** Add your mooring lines (``MOORMEMBERS``) if floating, or rigidly fix your bottom joints to the ground (``SUBCONSTRAINTS``) if onshore/bottom-fixed.
6. **Add Sensors:** To measure the tension in a mooring line or the internal load on a joint, add a sensor keyword (e.g., ``MOO_1_0.0`` for Mooring 1 at its anchor point, or ``CST_1`` for constraint 1) at the bottom of your file. (See :ref:`Sensor Locations and Definitions`).
