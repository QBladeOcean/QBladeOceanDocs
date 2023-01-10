Soil
====

In both onshore and fixed bottom offshore installations, a wind turbine is fixed in position through a suitable foundation.
A variety of foundations are available depending on the site conditions, material choices, desired interaction and dynamics.
A generalized model is implemented within QBlade in order to be able to simulate accurately not only pile foundations but also other 
foundations of interest.
This model makes use of a distributed spring model with nonlinear spring coefficients as illustrated in :numref:`fig-Soil-Im1`. 
The spring coefficients are specified with linear segments which represent the restoring force as a function of displacement, 
these are commonly referred to as p-y curves :footcite:`SalgadoBook`.
For simplicity, the springs shown in this figure provide a restoring force in a single direction,
however the model allows specification of nonlinear restoring forces in all translational and rotational degrees of freedom.

.. _fig-Soil-Im1:
.. figure:: Soiled.png
	:align: center
	:scale: 80%
	:alt: SI
	
	P-y curves for specification of nonlinear spring coefficients. The dynamics of the foundation in this case shall be captured with four lateral springs.

This generalized approach furthermore allows the structure of the foundation to be discretely treated, capturing the full structural dynamics of the foundation. 
This influences greatly the natural frequencies of the structure.

.. footbibliography::
