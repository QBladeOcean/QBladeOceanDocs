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
