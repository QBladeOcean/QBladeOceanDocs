Kinematic Stretching
====================

Linear wave theory only provides information about the water kinematics at and below mean sea level (MSL). If the velocity or 
acceleration within points above MSL is of interest (i.e. in a wave crest), extrapolation or stretching methods become 
necessary :footcite:t:`DNV_RP205`. 

In the literature, several wave stretching methods have been introduced :footcite:t:`DNV_RP205`, :footcite:t:`orcinaStr`, :footcite:t:`Frydom`.
Their general approach is to model the respective scaling factor :math:`E(z)` (introduced in :ref:`Wave Kinematics`) for points above MSL :math:`(z > 0)` 
by stretching or extrapolating its values. In the following, the three methods that have been implemented into QBlade are introduced briefly. 
For further information the reader is referred to :footcite:t:`DNV_RP205`, :footcite:t:`orcinaStr`, :footcite:t:`Frydom`.

Vertical Stretching
-------------------
This method assumes that all points above MSL equal the kinematic conditions at MSL :math:`(E(z) = 0).` :math:`E` below MSL is left unchanged

Extrapolation Stretching
------------------------
This method extrapolates :math:`E(z)` above MSL linearly by  using its gradient along the z-axis. Again, :math:`E(z)` below MSL is left unchanged.

Wheeler Stretching
------------------
This method modifies :math:`E(z)` so it always is stretched (or contracted) to the instantaneous wave elevation (:math:`z = \zeta`). This is done by replacing 
z with a scaling factor :math:`z'` that  modifies :math:`z` linearly so the following statement is always valid :math:`h < z' < 0`, where :math:`h` Is the water depth.


.. footbibliography::
