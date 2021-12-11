OYE Dynamic Stall Model
=======================

In QBlade dynamic stall may be modeled in unsteady :doc:`../lifting_line/lifting_line` or :doc:`../bem/bem` simulations by using the dynamic stall model proposed by Oye :footcite:`Oye1991`. In Oye's work dynamic stall is modele via a separation function :math:`f`, by calculating the dynamic lift :math:`Cl_{dyn}` as:

.. math::
	\begin{align}
	Cl_{dyn} = f  Cl_{att} + (1-f)  Cl_{sep} . 
	\end{align}
	
Where :math:`Cl_{att}` is the fully attached inviscid lift contribution and Cl_{sep} the fully separated lift contribution. To solve the equation above is is applied to static consitions, such that:

.. math::
	\begin{align}
	Cl^{st} = f^{st}  Cl_{att}^{st}  + (1-f^{st} )  Cl_{sep}^{st}  . 
	\end{align}

Where the superscript :math:`st` refers to static conditions. By definition :math:`Cl_{att} = Cl^{st}_{att}` and :math:`Cl_{sep} = Cl^{st}_{sep}`. :math:`Cl^{st}` is obtained by reading in static polar data and :math:`Cl_{att}^{st}` is obtained by extrapolating the linear part of the lift curve to the required angle of attack. Hansen :footcite:`Hansen2004b` suggests to evaluate :math:`f^{st}` as:

.. math::
	\begin{align}
	f^{st} = \left(2\sqrt{\frac{Cl^{st}}{Cl_{att}^{st}}}\right)^2  . 
	\end{align}
	
The value of :math:`f^{st}` is limited to be between 0 and 1. Now :math:`f` is assumed to return to the static value :math:`f^{st}` after:

.. math::
	\begin{align}
	f(t) = f^{st}(t) + f(t-\Delta t) - f^{st}(t)e^{\frac{-\Delta t}{\tau}} . 
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
	
:math:`Cl_{att}` is gained by extrapolation of the linear lift curve, so now the dynamic lift :math:`Cl_{dyn}` can be computed.
After Bergami the dynamic drag :math:`Cd_{dyn}` is evaluated as:

.. math::
	\begin{align}
	Cd_{dyn} = Cd^{st} +  (Cd^{st}-Cd^{st}_0) (0.5(\sqrt{f^{st}}-\sqrt{f}))-0.25(f-f^{st}).
	\end{align}

In this equation :math:`Cd^{st}_{0}` is the drag and 0 degree angle of attack.
	
.. footbibliography::
