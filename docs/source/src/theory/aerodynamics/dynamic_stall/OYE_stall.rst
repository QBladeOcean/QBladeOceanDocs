OYE Model
=========

In QBlade, dynamic stall may be modeled in unsteady :doc:`../lifting_line/lifting_line` or :doc:`../bem/bem` simulations by using the dynamic stall model proposed by Oye :footcite:`Oye1991`. It should be noted that this model only captures the dynamics of separated flow. The additional attached-flow dynamics due to airfoil wake memory effects are captured intrinsically by the :doc:`../lifting_line/lifting_line` model. In its implementation in QBlade, the model contribution is smoothly faded out toward the static polar near ±50°.

In Oye's work, dynamic stall is modeled with the help of a separation function :math:`f`. It is used to calculate the dynamic lift :math:`Cl_{dyn}` as:

.. math::
    \begin{align}
    Cl_{dyn} = f \cdot Cl_{att} + (1-f) \cdot Cl_{sep}.
    \end{align}

Here, :math:`Cl_{att}` is the fully attached inviscid lift contribution and :math:`Cl_{sep}` is the fully separated lift contribution. Applying the same relation to steady conditions gives:

.. math::
    \begin{align}
    Cl^{st} = f^{st} \cdot Cl_{att}^{st} + (1-f^{st}) \cdot Cl_{sep}^{st}.
    \end{align}

The superscript :math:`st` refers to steady conditions. :math:`Cl^{st}` is obtained from the static polar data, while :math:`Cl_{att}^{st}` is obtained by extrapolating the linear part of the lift curve to the required angle of attack. Following Hansen :footcite:`Hansen2004b`, the steady separation function :math:`f^{st}` is calculated as:

.. math::
    \begin{align}
    f^{st} = \left(2\sqrt{\frac{Cl^{st}}{Cl_{att}^{st}}}-1\right)^2.
    \end{align}

The ratio :math:`Cl^{st}/Cl_{att}^{st}` is evaluated with its sign. For negative angles of attack, this ratio remains positive as long as :math:`Cl^{st}` and :math:`Cl_{att}^{st}` have the same sign. If :math:`Cl_{att}^{st}` is close to zero, :math:`f^{st}` is set to 1. The resulting value of :math:`f^{st}` is limited to the range :math:`0 \le f^{st} \le 1`.

The dynamic separation function :math:`f` is assumed to return to the static value :math:`f^{st}` according to:

.. math::
    \begin{align}
    \frac{df}{dt} = \frac{f^{st} - f}{\tau}.
    \end{align}

Integrating this equation yields:

.. math::
    \begin{align}
    f(t) = f^{st}(t) + \left(f(t-\Delta t) - f^{st}(t)\right)e^{-\Delta t/\tau}.
    \end{align}

The time constant :math:`\tau` is defined as:

.. math::
    \begin{align}
    \tau = \frac{A c}{2 V_{rel}},
    \end{align}

where :math:`A` is a model parameter, typically around 8, :math:`c` is the airfoil chord, and :math:`V_{rel}` is the relative velocity at the airfoil section.

After :math:`f` has been evaluated, :math:`Cl_{sep}` is obtained from:

.. math::
    \begin{align}
    Cl_{sep} = \frac{Cl^{st}-f^{st}Cl_{att}}{1-f^{st}}.
    \end{align}

For values of :math:`f^{st}` close to 1, this expression is regularized in the implementation to avoid division by a very small number. :math:`Cl_{att}` is obtained by extrapolating the linear lift curve. With these quantities known, :math:`Cl_{dyn}` can be computed.

In QBlade, the Oye dynamic stall model also determines a dynamically changing drag coefficient :math:`Cd_{dyn}`. Following Bergami, the dynamic drag is evaluated as:

.. math::
    \begin{align}
    Cd_{dyn} = Cd^{st} + \left(Cd^{st}-Cd^{st}_0\right) \left[0.5\left(\sqrt{f^{st}}-\sqrt{f}\right) - 0.25\left(f-f^{st}\right) \right].
    \end{align}

Here, :math:`Cd^{st}_{0}` is the drag coefficient at zero angle of attack.

.. footbibliography::