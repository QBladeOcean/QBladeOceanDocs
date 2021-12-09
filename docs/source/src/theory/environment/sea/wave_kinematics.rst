Wave Kinematics
================

The velocity and acceleration profile over the water depth may be derived from the velocity potentials (finite and infinite depth). For simplicity, the distinction between
uni- and multi-directional wave fields is neglected in this section. In the case of a uni-directional wave field, the first summation term becomes redundant. In the case of infinite
depth (for most waves of interest this represents a depth greater than 100m), the velocity profiles are defined by:

.. math::
   \begin{align}
   V_x = \sum_{i}^{N_i}\sum_{j}^{N_j} A_{ij}\omega_i cos(\Theta_j)E_m(z)sin(k_i X_j - \omega_i t+\epsilon_{ij},
   \end{align}

.. math::
   \begin{align}
   V_y = \sum_{i}^{N_i}\sum_{j}^{N_j} A_{ij}\omega_i sin(\Theta_j)E_m(z)sin(k_i X_j - \omega_i t+\epsilon_{ij},
   \end{align}

.. math::
   \begin{align}
   V_z = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i E_m(z)cos(k_i X_j - \omega_i t+\epsilon_{ij}.
   \end{align}

Hence, the acceleration may be derived:

.. math::
   \begin{align}
   a_x = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i^2 cos(\Theta_j)E_m(z)cos(k_i X_j - \omega_i t+\epsilon_{ij},
   \end{align}

.. math::
   \begin{align}
   a_y = \sum_{i}^{N_i}\sum_{j}^{N_j} -A_{ij}\omega_i^2 sin(\Theta_j)E_m(z)cos(k_i X_j - \omega_i t+\epsilon_{ij},
   \end{align}

.. math::
   \begin{align}
   a_z = \sum_{i}^{N_i}\sum_{j}^{N_j} A_{ij}\omega_i^2 E_m(z)sin(k_i X_j - \omega_i t+\epsilon_{ij}.
   \end{align}

:math:`E_m` is a scaling factor that depending on the case is defined as:

.. math::
   \begin{align}
   E_m(z) = \frac{cosh(k_i(z+h))}{sinh(k_ih)}
   \end{align}

for finite depth and

.. math::
   \begin{align}
   E_m(z) = e^{k_iz}
   \end{align}

for infinite depth.


.. footbibliography::
