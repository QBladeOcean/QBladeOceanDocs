Seabed
======

The Seabed Interaction Model defines how cable and mooring elements interact with the seafloor. This model implements the MoorDyn seabed contact formulation :footcite:`housner2022seabed` based on the saturated damping friction model, with the addition of a numerical impulse cap to guarantee time-domain stability in the physics engine.

It calculates normal restorative forces based on element penetration, alongside a velocity-regularized directional friction model that evaluates axial and transverse sliding drag independently.


Normal Contact (Soil Penetration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The normal seabed contact force on a line node is calculated using a linear spring-damper formulation based on absolute soil properties. For a flat seabed, the force is evaluated as:

.. math::
   F_n = [(z_b - x_z)k_b - v_zc_b]dl

Where :math:`z_b` is the depth to the seabed, :math:`r_3` is the vertical position of the node, :math:`k_b` is the seabed stiffness, :math:`v_3` is the vertical velocity, :math:`c_b` is the seabed damping, and :math:`dl` is the line segment length.

Because our solver evaluates volumetric elements, this continuous distributed load is converted into equivalent nodal forces using a static lever rule based on the element's burial geometry:

* **Partially Submerged (Triangle Wedge):** Force is shifted toward the buried node, with the center of pressure located at :math:`1/3` of the submerged length.
* **Fully Submerged (Trapezoid):** Load is distributed asymmetrically based on the centroid of the trapezoidal penetration profile.


Directional Tangential Friction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To circumvent numerical instabilities caused by standard Coulomb friction discontinuous flips, the model relies on a saturated damping friction formulation. 

The node's in-plane velocity along the seabed (:math:`v`) is broken up into axial (:math:`v_A`) and transverse (:math:`v_T`) components:

.. math::
   v_A = (v \cdot \hat{q})\hat{q}

.. math::
   v_T = v - v_A

Where :math:`\hat{q}` is the axial unit vector of the cable element.

The continuous tangential force evaluates a static ramp below the arbitrary ramp-up velocity threshold (:math:`v_c`), and saturates to the kinetic limit above it. For example, the transverse component evaluates as:

.. math::
   -F_{f_T} = \begin{cases} F_{k_T} & \text{if } |v_T| \ge v_c \\ (\mu_{s_T} c_v) v_T & \text{if } |v_T| < v_c \end{cases}

Where the arbitrary damping term :math:`c_v` represents the slope :math:`F_n / v_c`. This allows the use of distinct static and kinetic friction coefficients for both the axial and transverse directions.

**Numerical Impulse Safety Cap:** To improve solver robustness beyond standard analytical formulations, the evaluated friction magnitude is mathematically capped by the stopping impulse: :math:`F_{stop} = (m \cdot v) / dt`. This strictly guarantees that the applied tangential force cannot artificially flip the node's velocity direction within a single integration time step, eliminating numerical high-frequency chatter.

Parameters
^^^^^^^^^^

.. _seabed-stiffness:

Seabed Stiffness
----------------
Defines the linear foundation stiffness of the seabed (:math:`k_b`). When a cable element penetrates the seabed (defined by :math:`z < -m\_waterDepth`), a normal restorative force is applied based on the penetration volume.

* **Unit:** Pa/m

.. _seabed-damping:

Seabed Damping
--------------

Defines the physical viscous damping constant of the seabed soil (:math:`c_b`). This treats the seabed as a uniform medium that exerts a resistive pressure against the element's vertical penetration velocity.

* **Unit:** Pa·s/m

.. _seabed-fric-coeff-axial:

Axial Friction Coefficient
--------------------------

The kinetic Coulomb friction coefficient (:math:`\mu_{k_A}`) used to calculate drag along the longitudinal axis of the cable. Sliding a cable along its own trench typically yields lower friction.

* **Unit:** Dimensionless

.. _seabed-fric-coeff-transverse:

Transverse Friction Coefficient
-------------------------------

The kinetic Coulomb friction coefficient (:math:`\mu_{k_T}`) used to calculate drag perpendicular to the cable axis. Dragging a line sideways generally displaces more soil, yielding higher friction.

* **Unit:** Dimensionless

.. _seabed-stat-dyn-fric-scale:

Seabed Static/Kinetic Friction Scale
------------------------------------

A multiplier applied to the kinetic friction coefficients to define the static breakout friction coefficients (:math:`\mu_s = \mu_k \times \text{Scale}`). If set to 1.0, static and kinetic friction are identical.

* **Unit:** Dimensionless

.. _seabed-fric-vel:

Seabed Friction Break Velocity
------------------------------
Defines the critical arbitrary ramp-up velocity (:math:`v_c`) threshold where the friction model transitions from static creeping to fully saturated kinetic sliding. This velocity threshold should be as close to zero as possible.

* **Unit:** m/s
* **Note:** To port a MoorDyn ``FricDamp`` (CV) value, use :math:`v_c = 1.0 / \text{FricDamp}`.

.. footbibliography::
