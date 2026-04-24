Gormont-Berg Model
==================

For the simulation of dynamic stall on VAWTs, especially at low tip speed ratios where the angle of attack variations can become very large, QBlade includes Berg's :footcite:`osti_6279384` modification of Gormont's :footcite:`gormontstall` dynamic stall model.

The model is based on the stall-hysteresis formulation originally introduced by Gormont. In this approach, the instantaneous blade-element angle of attack is modified into a rate-dependent reference angle of attack. This reference angle is then used to evaluate the static polar data. A positive angle-of-attack rate reduces the reference angle and therefore delays stall, while a negative angle-of-attack rate increases the reference angle and promotes stall recovery or deeper separated-flow conditions.

In QBlade, the Gormont-Berg model is implemented as a reference-angle correction applied to the static airfoil polar data. The additional attached-flow dynamics due to airfoil wake memory effects are not explicitly modeled by this dynamic stall correction. In unsteady lifting-line simulations, these attached-flow effects are captured intrinsically by the wake dynamics. The model contribution is smoothly faded out toward the static polar outside the specified dynamic-stall angle-of-attack range.

Reference Angle Formulation
---------------------------

The model defines separate reference angles for lift and for moment/drag. The lift reference angle is given by:

.. math::
    \begin{align}
    \alpha_{ref,L}
    =
    \alpha
    -
    K_1 Y_L
    \sqrt{\left|T_u \dot{\alpha}_g\right|}
    \operatorname{sign}\left(\dot{\alpha}_g\right),
    \end{align}

where :math:`\alpha` is the current angle of attack, :math:`\dot{\alpha}_g` is the geometric angle-of-attack rate, :math:`T_u` is the half-chord time constant,

.. math::
    \begin{align}
    T_u = \frac{c}{2 V_{rel}},
    \end{align}

and :math:`Y_L` is the lift stall-delay function.

The reference angle used for the moment and drag coefficients is calculated analogously:

.. math::
    \begin{align}
    \alpha_{ref,M}
    =
    \alpha
    -
    K_1 Y_M
    \sqrt{\left|T_u \dot{\alpha}_g\right|}
    \operatorname{sign}\left(\dot{\alpha}_g\right).
    \end{align}

Here, :math:`Y_M` is the moment stall-delay function. In QBlade, the same reference angle :math:`\alpha_{ref,M}` is used for both moment and drag. This follows the assumption used in Gormont's formulation that drag rise occurs with the same delay as moment stall, since both are associated with the separated-flow movement of the aerodynamic center.

The empirical factor :math:`K_1` accounts for the different behavior between increasing and decreasing angle of attack:

.. math::
    \begin{align}
    K_1 =
    \begin{cases}
    1.0, & \dot{\alpha}_g \ge 0, \\
    0.5, & \dot{\alpha}_g < 0.
    \end{cases}
    \end{align}

The smaller value during decreasing angle of attack reduces the tendency of the model to predict premature stall on the downstroke.

Stall Delay Functions
---------------------

In QBlade, simplified thickness-dependent stall-delay functions are used:

.. math::
    \begin{align}
    Y_L = 1.4 - 6.0\left(0.06-\frac{t}{c}\right),
    \end{align}

and

.. math::
    \begin{align}
    Y_M = 1.0 - 2.5\left(0.06-\frac{t}{c}\right),
    \end{align}

where :math:`t/c` is the relative airfoil thickness. The original Gormont formulation also contains Mach-number-dependent and compound stall-delay functions. These additional dependencies are not used in the simplified QBlade implementation, which is mainly intended for low-Mach-number wind-turbine applications.

Dynamic Lift Coefficient
------------------------

The dynamic lift coefficient is obtained by evaluating the static lift coefficient at the lift reference angle :math:`\alpha_{ref,L}` and using the corresponding effective lift-curve slope:

.. math::
    \begin{align}
    Cl_{GB}
    =
    \frac{Cl^{st}\left(\alpha_{ref,L}\right)}
    {\alpha_{ref,L}-\alpha_0}
    \left(\alpha-\alpha_0\right),
    \end{align}

where :math:`\alpha_0` is the zero-lift angle of attack. If :math:`\alpha_{ref,L}` is very close to :math:`\alpha_0`, the static lift coefficient is used directly to avoid division by a very small number.

Dynamic Drag and Moment Coefficients
------------------------------------

The drag and pitching-moment coefficients are evaluated directly from the static polar at the moment/drag reference angle:

.. math::
    \begin{align}
    Cd_{GB} = Cd^{st}\left(\alpha_{ref,M}\right),
    \end{align}

.. math::
    \begin{align}
    Cm_{GB} = Cm^{st}\left(\alpha_{ref,M}\right).
    \end{align}

For the pitch-axis moment coefficient, QBlade uses the corresponding pitch-axis moment coefficient evaluated at the same reference angle:

.. math::
    \begin{align}
    Cm_{pitch,GB} = Cm_{pitch}^{st}\left(\alpha_{ref,M}\right).
    \end{align}

Berg Correction
---------------

The original Gormont model was developed for helicopter rotor applications. For VAWT simulations, particularly at low tip speed ratios, the angle-of-attack excursions can become very large. Berg's modification reduces the dynamic-stall correction at large angles of attack by blending the Gormont-corrected coefficients back toward the static polar.

For the positive angle-of-attack side, the upper blending limit is defined as:

.. math::
    \begin{align}
    \alpha_{end}^{+}
    =
    \alpha_0
    +
    A_m\left(\alpha_{Cl,max}-\alpha_0\right),
    \end{align}

where :math:`A_m` is the Berg correction factor and :math:`\alpha_{Cl,max}` is the angle of attack at maximum static lift.

For the negative angle-of-attack side, the corresponding limit is:

.. math::
    \begin{align}
    \alpha_{end}^{-}
    =
    \alpha_0
    +
    A_m\left(\alpha_{Cl,min}-\alpha_0\right),
    \end{align}

where :math:`\alpha_{Cl,min}` is the angle of attack at minimum static lift.

The blending factor :math:`\gamma` is then calculated as:

.. math::
    \begin{align}
    \gamma =
    \frac{\alpha_{end}^{+}-\alpha}
    {\alpha_{end}^{+}-\alpha_{Cl,max}}
    \end{align}

on the positive side, and as:

.. math::
    \begin{align}
    \gamma =
    \frac{\alpha_{end}^{-}-\alpha}
    {\alpha_{end}^{-}-\alpha_{Cl,min}}
    \end{align}

on the negative side. The value of :math:`\gamma` is limited to the range :math:`0 \le \gamma \le 1`.

The final dynamic coefficients are then obtained by blending between the static polar and the Gormont-corrected values:

.. math::
    \begin{align}
    Cl_{dyn}
    =
    Cl^{st}
    +
    \gamma\left(Cl_{GB}-Cl^{st}\right),
    \end{align}

.. math::
    \begin{align}
    Cd_{dyn}
    =
    Cd^{st}
    +
    \gamma\left(Cd_{GB}-Cd^{st}\right),
    \end{align}

.. math::
    \begin{align}
    Cm_{dyn}
    =
    Cm^{st}
    +
    \gamma\left(Cm_{GB}-Cm^{st}\right).
    \end{align}

The same blending is applied to the pitch-axis moment coefficient.

Finally, QBlade applies an additional smooth fade-out toward the static polar near :math:`\pm 50^\circ`, the prescribed dynamic-stall angle-of-attack limit for the Gormont-Berg model. This avoids discontinuities when the model is used in simulations with very large angle-of-attack excursions.

.. footbibliography::