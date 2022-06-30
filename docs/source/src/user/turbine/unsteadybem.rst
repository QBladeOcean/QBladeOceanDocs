Unsteady BEM Settings
=====================
The theory of the unsteady polar BEM is briefly described in :ref:`Polar Grid`.

Unsteady BEM Parameters
-----------------------

- **Azimuthal Polar Grid Discretization**: The polar grid is discretized into the chosen number of azimuthal sections. A value of 1 is equal to the BEM without a polar grid.
- **Include Tip Loss**: This activates the classical BEM tip loss correction to account for a finite number of blades, see :footcite:t:`Glauert1935`. 
- **Convergence Acceleration Time**: The time lag constants in the unsteady BEM implementation are increased by a factor of 20 during the time span entered by the user. This enables a much faster convergence of the unsteady BEM towards a steady operational point.

.. footbibliography::
