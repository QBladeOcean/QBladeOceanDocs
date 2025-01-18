Wave Kinematics
================

The velocity and acceleration profile over the water depth may be derived from the velocity potentials (finite and infinite depth). For simplicity, the distinction between
uni- and multi-directional wave fields is neglected in this section. In the case of a uni-directional wave field, the first summation term becomes redundant. In the case of infinite
depth (for most waves of interest this represents a depth greater than 100m), the velocity profiles are defined by:

.. math::
   \begin{align}
   V_x = \sum_{i}^{N_i}\sum_{j}^{N_j} A_{ij}\omega_i cos(\Theta_j)E_c(z)sin(k_i X_j - \omega_i t+\epsilon_{ij}),
   \end{align}

.. math::
   \begin{align}
   V_y = \sum_{i}^{N_i}\sum_{j}^{N_j} A_{ij}\omega_i sin(\Theta_j)E_c(z)sin(k_i X_j - \omega_i t+\epsilon_{ij}),
   \end{align}

.. math::
   \begin{align}
   V_z = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i E_s(z)cos(k_i X_j - \omega_i t+\epsilon_{ij}).
   \end{align}

Hence, the acceleration may be derived:

.. math::
   \begin{align}
   a_x = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i^2 cos(\Theta_j)E_c(z)cos(k_i X_j - \omega_i t+\epsilon_{ij}),
   \end{align}

.. math::
   \begin{align}
   a_y = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i^2 sin(\Theta_j)E_c(z)cos(k_i X_j - \omega_i t+\epsilon_{ij}),
   \end{align}

.. math::
   \begin{align}
   a_z = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i^2 E_s(z)sin(k_i X_j - \omega_i t+\epsilon_{ij}).
   \end{align}

:math:`E_c` and :math:`E_s` are depth scaling factors that depending on the case are defined as:

.. math::
   \begin{align}
   E_c(z) = \frac{cosh(k_i(z+h))}{sinh(k_ih)}
   \end{align}
.. math::
   \begin{align}
   E_s(z) = \frac{sinh(k_i(z+h))}{sinh(k_ih)}
   \end{align}

for finite depth and:

.. math::
   \begin{align}
   E(z) = e^{k_iz}
   \end{align}

for infinite depth.


.. footbibliography::
