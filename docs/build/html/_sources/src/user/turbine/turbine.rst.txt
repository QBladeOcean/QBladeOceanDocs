Turbine Definition Dialog
=========================

A new wind turbine is defined within the dialog shown below. A turbine object can either be defined with or without a structural model definition. If the turbine object is defined without a structural model it is assumed as rigid, and only aerodynamic forces are evaluated during a simulation. The only operational modes for a turbine object without a structural model are constant or prescribed operational speed. If a structural model is added to a turbine object an aeroelastic simulation can be performed. The simulation results then include gravitational, inertia, centrifugal, gyroscopic and aerodynamic forces. For turbine objects with structural model definitions full supervisory turbine controllers may be added to the turbine definition. If a turbine object also contains a definition of a floating or bottom fixed substructure also hydrodynamic forces are evaluated during the simulation.

.. _fig-turbine-dialog1:
.. figure:: turbine_dialog1.png
    :align: center
    :alt: The turbine definition dialog, part 1.
    
    The turbine definition dialog, part 1.
    
.. _fig-turbine-dialog2:
.. figure:: turbine_dialog2.png
    :align: center
    :alt: The turbine definition dialog, Unsteady BEM settings.
    
    The turbine definition dialog, Unsteady BEM settings.
    
.. _fig-turbine-dialog3:
.. figure:: turbine_dialog3.png
    :align: center
    :alt: The turbine definition dialog, part 3.
    
    The turbine definition dialog, Free Vortex Wake Settings.
    
.. _fig-turbine-dialog4:
.. figure:: turbine_dialog4.png
    :align: center
    :alt: The turbine definition dialog, part 4.
    
    The turbine definition dialog, part 4.
    
The parameters that need to be filled in are now discussed below.

Turbine Name and Rotor
----------------------

- **Turbine Name**: A unique name needs to be assigned to the turbine object.
- **Blade Design**: Choose the aerodynamic blade design that will be used for this turbine object.
- **Turbine Type**: Switch between a HAWT or a VAWT turbine design.
- **Number of Blades**: Sets the numvber of blades for this rotor. This overrides the number of blades that is specified in the *Blade Design*. If the turbine is equipped with a structural model the number of blades is defined in the structural model main input file and this value is not used.
- **Up- or Downwind**: Choose an up- or downwind rotor configuration (only used for HAWT turbine definitions).
- **Rotor Rotation**: Sets the rotor rotation to standard (clockwise) or reversed (counterclockwise).

Turbine Version Info
--------------------

- **Version Info**: Adds an info string to this turbine object that can be used to annotate changes to the model or revisions of the turbine design.


Turbine Geometry
----------------

If no structural model is defined for this turbine object the turbine geometry is defined here. If a structural model is defined the geometry is defined within the structural model files.
    
- **Rotor Overhang**: Sets the rotor overhang of the turbine object (see :numref:`fig-turbine-geometry`)
- **Tower Height**: Definition of the tower height.
- **Tower Top/Bottom Radius**: Defined the tower top and bottom radius. A linear interpolation is applied for all tower stations in between.
- **Rotor Shaft Tilt Angle**: Sets the rotor shaft tilt angle (see :numref:`fig-turbine-geometry`).
- **Rotor Cone Angle**: Sets the rotor cone angle (see :numref:`fig-turbine-geometry`).


.. _fig-turbine-geometry:
.. figure:: turbine_geometry.png
    :align: center
    :alt: Definition of turbine geometry parameters.
    
    Definition of turbine geometry parameters.
    
Aerodynamic Discretization
--------------------------

- **Blade Panels**: Here the user can specifiy the number of blade panels and the type of spacing. A **Linear** spacing distribues the panels evenly over the blade length. A **Cosine** spacing results in a finer discretization near the blade ends (root and tip) and a slighly coarser discretization near the blade center. The option **Table** uses the aerodynamic blade definition table as a temnplate for the aerodynamic discretization, thus the user can use this option for a fully customized blade discretization.

Aerodynamic Models
------------------

- **Dynamic Stall**: The user can activate the use of a dynamic stall model. The options are: **Off**: No dynamic stall model is used. **OYE**: The OYE dynamic stall model is used, see :ref:`OYE Dynamic Stall Model`. **ATEF**: The ATEFlap unsteady aerodynamics model is used, see :ref:`ATEFlap Dynamic Stall Model`.
- **2 Point L/D Eval**: This actives the two point lift and drag evaluation model, proposed by :footcite:t:`wes-2021-163`. The advantage of this two point evaluation is that lift and drag predictions for dihedral or conned wind turbine rotor are improved and the airfoil **pitch rate** is explicitly being taken into account by evaluating the angle of attack at the three-quarter chord point and then applying the aerodynamic coefficients at the quarter-chord point.
- **Himmelskamp Effect**: The correction for the *Himmelskamp* effect can be activated here, see :ref:`Himmelskamp Effect`.
- **Tower Shadow**: The *Tower Shadow Effect* can be avtivated, see :ref:`Tower Influence`.
- **Tower Drag Coeff.**: Sets the drag coefficient that is used to model the *Tower Shadow Effect*.
    
Wake Type
---------

Here the user can choose between the **Free Vortex Wake** or the **Unsteady BEM** aerodynamic model. The **Unsteady BEM** model can only be used with **HAWT** turbine defintions.
See :ref:`Free Vortex Wake Settings` and :ref:`Unsteady BEM Settings`.


.. footbibliography::
