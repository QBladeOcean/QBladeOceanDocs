OYE Model
=========

In QBlade dynamic stall may be modeled in unsteady :doc:`../lifting_line/lifting_line` or :doc:`../bem/bem` simulations by using the dynamic stall model proposed by Oye :footcite:`Oye1991`. It should be noted that this model only captures the dynamics of separated flow. The additional attached flow dynamics due to airfoil wake memory effects are captured intrinsically by the :doc:`../lifting_line/lifting_line` model. In its implementation in QBlade the Oye dynamic stall model is only applied within the angle of attack range of -50° to 50°.


In Oye's work the dynamic stall is modeled with the help of a separation function :math:`f`. It is used to calculate the dynamic lift :math:`Cl_{dyn}` in the following way:

.. math::
	\begin{align}
	Cl_{dyn} = f \cdot Cl_{att} + (1-f) \cdot Cl_{sep}.
	\end{align}
	
Where :math:`Cl_{att}` is the fully attached inviscid lift contribution and :math:`Cl_{sep}` the fully separated lift contribution. 
To solve the equation above, it is applied to steady conditions. The result is:

.. math::
	\begin{align}
	Cl^{st} = f^{st} \cdot Cl_{att}^{st} + (1-f^{st}) \cdot Cl_{sep}^{st}.
	\end{align}

where the superscript :math:`st` refers to steady conditions. Comparing the equations above, :math:`Cl_{att} = Cl^{st}_{att}` and :math:`Cl_{sep} = Cl^{st}_{sep}`. :math:`Cl^{st}` is obtained by reading in static polar data and :math:`Cl_{att}^{st}` is obtained by extrapolating the linear part of the lift curve to the required angle of attack. 
Following Hansen :footcite:`Hansen2004b`, :math:`f^{st}` can be calculated in the following way:

.. math::
	\begin{align}
	f^{st} = \left(2\sqrt{\frac{Cl^{st}}{Cl_{att}^{st}}}\right)^2  . 
	\end{align}
	
The value of :math:`f^{st}` is limited to be between 0 and 1. Now :math:`f` is assumed to return to the static value :math:`f^{st}` as follows:

.. math::
	\begin{align}
	\frac{df}{dt} = \frac{f^{st} - f}{\tau}  .
	\end{align}

Integrating the equation above allows the determination  of the dynamic behavior of :math:`f(t)`:

.. math::
	\begin{align}
	f(t) = f^{st}(t) + \left(f(t-\Delta t) - f^{st}(t)\right)e^{\frac{-\Delta t}{\tau}} . 
	\end{align}
	
:math:`\tau` is a time constant, defined as:

.. math::
	\begin{align}
	\tau = \frac{A \frac{c}{2}}{V_{rel}} , 
	\end{align}
	
where :math:`A` is a parameter (typically around 8), :math:`c` is the airfoil chord and :math:`V_{rel}` the relative velocity at the airfoil section. After :math:`f` has been evaluated, :math:`Cl_{sep}` can be obtained from:

.. math::
	\begin{align}
	Cl_{sep} = \frac{Cl^{st}-f^{st}Cl_{att}}{1-f^{st}} .
	\end{align}
	
:math:`Cl_{att}` is gained by extrapolation of the linear lift curve. 

Now, all variables have been determined and the dynamic lift :math:`Cl_{dyn}` can be computed.


In QBlade, the Oye dynamic stall model also determines a dynamically changing drag coefficient :math:`Cd_{dyn}`.  After Bergami, the dynamic drag :math:`Cd_{dyn}` is evaluated as:

.. math::
	\begin{align}
	Cd_{dyn} = Cd^{st} + (Cd^{st}-Cd^{st}_0) (0.5(\sqrt{f^{st}}-\sqrt{f}))-0.25(f-f^{st}).
	\end{align}

In this equation :math:`Cd^{st}_{0}` is the drag at 0 degree angle of attack.
	
.. footbibliography::
