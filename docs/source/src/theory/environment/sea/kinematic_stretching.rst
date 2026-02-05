Kinematic Stretching
====================

In QBlade, linear (Airy) wave theory is used to compute wave kinematics (velocity, acceleration) and dynamic pressure as a function of depth. In its standard form, linear theory is formulated with respect to the mean (still) water level, and the kinematics are typically evaluated for points at and below mean sea level (MSL), i.e. :math:`z \le 0` (with :math:`z` positive upwards).

For many offshore structures (columns, braces, heave plates), hydrodynamic loads are strongly influenced by the *near-surface* region. In a wave crest, parts of the structure may be located between MSL and the instantaneous free surface. To evaluate kinematics consistently in this region (and to avoid unrealistic growth of linear-theory kinematics above MSL), various stretching and extrapolation approaches have been proposed :footcite:t:`DNV_RP205`, :footcite:t:`orcinaStr`.

In the following, the stretching options implemented in QBlade are described briefly. In all cases, the instantaneous free-surface elevation is denoted by :math:`\zeta(x,y,t)` (positive upwards), and the water depth is :math:`h>0`. For further details and recommendations, see :footcite:t:`DNV_RP205` and :footcite:t:`orcinaStr`.

General concept
---------------
In linear wave theory, many kinematic expressions contain a depth-dependent factor (e.g. the familiar hyperbolic decay terms). Conceptually, stretching and extrapolation methods modify how this depth dependence is evaluated in the near-surface region by replacing the physical depth coordinate :math:`z` with an effective coordinate :math:`z_\mathrm{eval}` (or by extrapolating kinematics directly). This enables evaluation up to the instantaneous free surface while maintaining a bounded and numerically robust formulation.

In QBlade, kinematics and Morison-type loads are only applied to points that are *wetted*. By default, the wetting condition is checked against the local instantaneous free surface elevation, i.e. a point is considered dry if :math:`z > \zeta(x,y,t)`. This behaviour can be changed using the :code:`STATICSUBMERGENCE` keyword (see :ref:`Miscellaneous Substructure Parameters`) , which evaluates the wetting condition with respect to mean sea level (MSL) instead.

Vertical Stretching
-------------------
Vertical stretching assumes that all points above MSL experience the same kinematics as at MSL. In other words, kinematics are evaluated at

.. math::

    z_\mathrm{eval} = \min(z, 0).

This is a simple and robust engineering approximation. However, it introduces an inherent crest–trough asymmetry: in wave crests, points between MSL and :math:`\zeta` are evaluated using MSL kinematics (no additional vertical decay), while in troughs the wetted region is truncated and kinematics are only evaluated below MSL. In Morison/strip-theory models, this near-surface treatment can noticeably affect low-frequency response because the periodically wetted zone often contributes strongly to viscous loading.

Optional blending to Wheeler (``VERTWEIGHT``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
QBlade provides an optional blending parameter ``VERTWEIGHT`` (hereafter :math:`\alpha`) to continuously transition from pure vertical stretching to Wheeler stretching. This can be used for sensitivity studies (and, if required, calibration) of near-surface model-form uncertainty.

- :math:`\alpha = 1.0`: pure vertical stretching (maximum asymmetry)
- :math:`\alpha = 0.0`: Wheeler stretching
- intermediate values blend linearly (default: 1.0)

The blended evaluation coordinate is

.. math::

    z_\mathrm{vert} = \min(z,0), \qquad
    z_\mathrm{whe}  = (z-\zeta)\frac{h}{h+\zeta}, \qquad
    z_\mathrm{eval} = \mathrm{\alpha}\,z_\mathrm{vert} + (1-\mathrm{\alpha})\,z_\mathrm{whe}.

Wheeler Stretching
------------------
Wheeler stretching modifies the effective depth coordinate such that kinematics are “stretched” (or “contracted”) to the instantaneous free surface. This is achieved by replacing :math:`z` with

.. math::

    z_\mathrm{eval} = (z-\zeta)\frac{h}{h+\zeta}.

Wheeler stretching can be interpreted as mapping the instantaneous fluid domain :math:`-h \le z \le \zeta` to the fixed linear-theory domain :math:`-h \le z_\mathrm{eval} \le 0`. Compared to vertical stretching, this tends to produce a more continuous crest–trough behaviour in the near-surface region.

Extrapolation Stretching
------------------------
Extrapolation stretching evaluates kinematics above MSL by linearly extrapolating the *first-order* kinematics from MSL using their vertical gradient at MSL. Conceptually:

- for :math:`z \le 0`, kinematics are evaluated directly from linear theory,
- for :math:`z > 0`, kinematics are approximated by :math:`u(z) \approx u(0) + z\,(\partial u/\partial z)\vert_{z=0}`.

Below MSL, kinematics are left unchanged. Extrapolation is commonly used as a pragmatic extension that preserves local slope information at the surface and remains numerically stable for moderate crest elevations :footcite:t:`DNV_RP205`.


.. footbibliography::
