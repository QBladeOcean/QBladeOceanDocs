Currents
=========

Three different types of time constant currents may be defined in QBlade. An overview of the available types of currents is given below. Further details can be found in :footcite:t:`Bladed`.

* **Near-Surface Currents**: The velocity profile of a near-surface current varies linearly with depth from a specified velocity at the sea surface to zero at the reference depth, which is defined by the user.

|

* **Sub-Surface Currents**: The sub-surface current velocity follows a power law profile. The implementation in QBlade is of the following form:

.. math::
   \begin{align}
   u_{cs}(z) = \left[\left(\frac{z+h}{h}\right)^\alpha \right]u_{s0}(z=0)
   \end{align}

where,

- :math:`u_{cs}(z=0)` is the velocity at the sea surface,
- :math:`\alpha` is the power law exponent (default value is :math:`\alpha = 0.14`),
- :math:`h` is the water depth,
- :math:`z`` is   :math:`0 \geq z \geq-h`.

|

* **Near-Shore Currents**: The near-shore current is defined as a uniform velocity profile independent of the depth

Any combination of these types of currents (together with waves) may be included within a QBlade simulation. In all cases, the velocities at each evaluation
point are calculated as a superposition of all contributions from waves and currents. A complete hydroelastic representation of the turbine also requires
the consideration of fluid-structure interaction. This topic is covered in Sections :ref:`Linear Potential Flow Theory` and :ref:`Morison Equation`.

.. footbibliography::
