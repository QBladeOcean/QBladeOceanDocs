Blade Element Momentum Method
=============================

In QBlade the aerodynamic forces acting on a rotor can be modeled either using a steady Blade Element Momentum (BEM) or a with a more advanced, time resolved
unsteady BEM (UBEM) that is enhanced by several correctional models. The theory interlinks the Momentum Theory (MT) and the Blade Element Theory (BET) and it was
first introduced by :footcite:t:`Glauert1935`. Despite its simplicity, the BEM method allows for an accurate representation of the aerodynamic loads that act on
the rotor of a wind turbine as long as critical assumptions are not violated.

Momentum Theory
----------------
Under the assumptions of a steady, incompressible and axissymmetric inflow of an inviscid fluid the MT may be applied. Thereby, the rotor is assumed as an actuator
disk that causes a uniform pressure drop over the rotor area while the velocitiy through the disk is assumed to beheave continously.
In the most simplified apllicaton of the momentum theory (1D), the pressure drop is imposed onto the model, the velocity through the rotor disk does not contain a rotational
component and the pressures far up- and downstream of the rotor are equal to the ambient pressure. These assumptions allow to capture the rotor performance
(power and thrust) and the velocity in the rotor plane by applying the conservation of mass and the conservation of momentum laws (see :footcite:t:`Branlard2017`).
The introduction of the induction factor :math:`a` allows to express the velocity in the rotor plane as function of the incoming velocity :math:`u_{0}`:

.. math::
.. 	\begin{align}
	u = (1-a)u_\infty .
	\end{align}


The rotor performance coefficients for power and thrust may also be expressed as a function of the axial induction factor :math:`a`:

.. math::
	\begin{align}
	C_T = 4a(1-a),
	\end{align}

.. math::
	\begin{align}
	C_P = 4a(1-a)^2.
	\end{align}

.. figure:: MT.png
   :scale: 75 %
   :align: center
   :alt: MT_1D

   1D momentum theory, pressure and velocity evolution.


Blade Element Theory
--------------------
The blade element theory (BET) allows to compute the loads acting on a rotor based on the geometric and aerodynamic properties of individual blade sections at a certain
radius of the blade. Thereby, a blade is divided into a discrete number of radially distributed sections. The loads on a singular section may be determined
individually below the assumption that flow only has a component in chordwise direction and that the aerodynamic characteristics of 2-dimensional lift, drag and moment coefficients are applicable.

.. figure:: 2d_af.png
   :scale: 60 %
   :align: center
   :alt: Forces on a 2D airfoil

   2D forces on an airfoil.

Classical Blade Element Momentum Theory
----------------------------------------
The blade element momentum theory interlinks the 1D momentum theory with the blade element momentum theory. For practical reasons, the stream tube theory is
applied to radially distributed annular rings that match the discretization of the blade elements. Since both theories allow to express
the rotor loads (power and thrust) within an annular segment in dependence of the induction factors :math:`a` and :math:`a'`, a system of equations can be iterated with
the induction factors serving as the iterative quantities until a convergence threshold is reached.

Corrections
-----------
Due to the two-dimensional nature of the BEM theory, three dimensional effects, cannot be accounted for by the classical BEM. This leads to large deviations of
the computed data compared with measured turbine data, especially under the influence of stall. Additionally, the assumption of the actuator disk (infitnite blade number) eradicates
the tip loss in theory. To improve the accuracy of the BEM results, two correctional methods are implemented into QBlade:

- Prandtl Tip Loss Factor (see :footcite:t:`Glauert1935`);
- 3D Correction (see :footcite:t:`Snel1992`);



Unsteady Blade Element Momentum Theory
---------------------------------------
The classical BEM theory provides good estimates of the annual energy production but is incapable of taking unsteady phenomena like the atmospheric boundary layer, turbulence or the tower influence into account. These unsteady phenomena make the position of each blade at a certain time necessary. Hence, non-rotating coordinate systems are placed at the bottom of the tower and the nacelle.
Furthermore, a coordinate system is attached to the rotating shaft and each blade. The instantaneous velocity seen by each blade can now be determined and be accounted for in the calculation of
the flow angle (:footcite:t:`Tavares2013`).
Since the clasical BEM is only valid for an equilibrium state and provides induced velocities corresponding to this specific state, a dynamic inflow model is used to introduce a lag with which the
wake settles to a new equilibrium state (see :footcite:t:`Glauert1935` or :footcite:t:`Henriksen2012`).

Polar Grid
----------
The polar-grid has been developed by (:footcite:t:`Madsen2020`) to consider for azimuthal variations of the axial induction caused by the azimuthal dependence of blade loadings. Within the approach, the annular rings of the MT are divided
into stationary azimuthal subelements. Each point on the azimuthal grid is associated with a local induction factor, based on the local instantaneous velocity. The latter is approximated by the induced
velocity of the neighboring two blades and weighted by their azimuthal distance (:footcite:t:`BdL2022`).

.. figure:: polargrid.png
   :scale: 60 %
   :align: center
   :alt: Polar grid

   Classical BEM approach (left) and polar grid with azimuthal sub elements (right), taken from :footcite:t:`Madsen2020`)



.. footbibliography::
