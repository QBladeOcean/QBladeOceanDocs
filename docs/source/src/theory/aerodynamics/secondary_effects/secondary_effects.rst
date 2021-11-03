Tower Influence
===============

.. _fig-towershadow:
.. figure:: towershadow.PNG
    :align: center
    :alt: towershadow

    Visualization of the tower shadow model; showing velocity magnitude.

A tower shadow model, based on the work of Bak (:footcite:t:`Moriarty2005`) is implemented in QBlade. This model is based on a superposition of the analytical solution for potential flow around a cylinder and a model for the downwind wake behind a cylinder, based on a tower drag coefficient. 
The tower shadow model only affects velocity components that are normal to the tower centerline; the z-component of the velocity, parallel to the tower centerline, remains unaffected. 
The tower shadow model is only used when the z-component of the evaluation point is smaller or equal to the tower height. 
An application of the tower model, including a comparison to CFD simulations and experimental data is found in the work of :footcite:t:`Klein2018`.


Ground Effect
=============

Ground effects can be modelled with the :doc:`../lifting_line/lifting_line` method by mirroring all vortex elements, bound and free, at the ground plane (:footcite:t:`Leishman2000`). 
A mirror image (see Figure \ref{fig:ground}) of all bound and free vortices is created at every time step using the ground as a symmetry plane. 
Such a treatment doubles the number of times that the Biot-Savart equation is calculated and thereby doubles the computational time needed for the evaluation of the convection step. 

.. _fig-groundeffect:
.. figure:: ground.PNG
    :align: center
    :alt: groundeffect

    Modeling of ground effect through mirroring of the wake.

Himmelskamp Effect
==================

The maximum lift coefficient of profiles on a rotating rotor blade is significantly higher than the maximum lift coefficient of the same profile measured on a stationary rotor. The centrifugal force accelerates the boundary layer radially. 
This results in a thinner boundary layer in which stall is delayed. At the same time, air flowing radially, in a rotating reference system, generates a Coriolis force opposite to the rotational direction of the rotor. 
This force is opposing the rise in pressure of the profile's suction side and delays the stall. 
This effect, called stall delay or Himmelskamp effect, can be taken into account by modifying the two dimensional polar data. 
For the affected profiles the stalled region will shift to higher angles of attack. With a viscous-inviscid interaction method, Snel investigated the flow around a rotating rotor blade 
and developed a semi-empirical formula to correct 2D polar data (:footcite:t:`SnelH.HouwinkR.andPiers1993`). 
According to Snel, only the lift but not the drag coefficient, needs to be modified. The Himmelskamp effect, can be modeled in QBlade using Snel's correction:
	
.. math::	
	\begin{align}
	Cl_{3D} = Cl_{2D}+\frac{3.1\lambda^2}{1+\lambda^2}g\left(\frac{c}{r}\right)^2\left(\frac{\partial Cl}{\partial\alpha}(\alpha-\alpha_0)-Cl_{2D}\right).
	\end{align}

Where :math:`g` is a blending factor: :math:`g=1` for :math:`0<\alpha<30`; :math:`g=0.5(1+\cos(6\alpha-180))` for :math:`30<\alpha<60` and :math:`g=0` for :math:`60<\alpha<360`.
If this correction is activated for a simulation it is applied on the unmodified, tabulated 2D airfoil data at every timestep.


.. footbibliography::