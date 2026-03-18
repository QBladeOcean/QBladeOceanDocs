QFoil Airfoil Analysis Code
===========================

Introduction
------------

QFoil is a modified derivative of XFoil 6.99 with a focus on improved numerical robustness and more realistic viscous/post-stall behavior for wind-energy airfoil analysis. It is is released under the GNU General Public License (GPL), and its binaries are integrated into QBlade's airfoil analysis workflow. The source code for QFoil is included with QBlade's release and can also be downloaded from QBlade webpage: `QFoil Download <https://qblade.org/assets/Qfoil_0.9_minimal_src.zip>`_

This page documents the QFoil-specific changes relative to XFoil 6.99.

Summary of Main Changes
-----------------------

Main changes at a glance
~~~~~~~~~~~~~~~~~~~~~~~~

Compared to XFoil 6.99, QFoil 0.9 introduces the following key changes:

* modified viscous solver relaxation and iteration step limits for robustness
* RFoil-style wake dissipation adjustment in the boundary-layer system
* new wake correction parameter ``GWAKE`` (default ``0.40``) and CLI command ``GW``
* dynamic (shape-factor-dependent) shear-lag coefficient in the BL closure
* modified drag extrapolation logic in ``CDCALC`` with wake correction + fallback
* forced re-initialization strategy for ALFA sweeps (inviscid reset + suction clamping)
* minor turbulent BL correlation constant retuning
* increased internal array limits to support up to 600 surface panels

Expected impact on results and workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compared to stock XFoil 6.99, QFoil is expected to behave differently in the following ways:

* **Different stall and post-stall trends** due to dynamic shear-lag and wake dissipation changes
* **Different drag prediction** due to the modified wake-based drag correction and fallback logic
* **More robust viscous convergence** in difficult operating points (tighter Newton step control)
* **Additional tuning knob** for users via ``GWAKE``
* **Reduced carry over effects** during ALFA sweeps (fresh BL initialization for every angle)
* **Higher resolution analysis** permitted by expanded surface panel and wake node limits

.. warning::

   QFoil is not numerically equivalent to XFoil or ECN-RFoil. Polar results should be re-validated for any workflow that was previously calibrated against stock XFoil or a specific RFoil branch.

Relationship to XFoil and RFoil
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QFoil is not a port of ECN-RFoil. It remains structurally an XFoil-derived codebase, but introduces targeted modifications inspired by RFoil-family ideas, especially in:

* turbulent shear-lag closure behavior
* wake dissipation treatment
* post-stall drag correction behavior

For the original XFoil framework and viscous–inviscid coupling background, see Drela's XFoil reference and the XFoil software page :footcite:`drela1989xfoil,drelayoungren_xfoil_site`. For early RFoil boundary-layer/post-stall modifications, see Van Rooij :footcite:`vanrooij1996rfoil`. For drag-correction work on thick airfoils in XFoil-like methods, see Ramanujam et al. :footcite:`ramanujam2016drag`.

Origin of the main modeling ideas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The diff indicates a clear provenance path for the main model-level changes:

* **XFoil base formulation**: Drela's original XFoil framework and viscous–inviscid
  coupling formulation :footcite:`drela1989xfoil,drelayoungren_xfoil_site`
* **RFoil-style BL/post-stall improvements**: boundary-layer and post-stall
  modifications for improved stall behavior :footcite:`vanrooij1996rfoil`
* **Shape-factor-dependent shear-lag practice (wind-energy RFoil usage)**:
  commonly attributed in later wind-energy airfoil methodology discussions to the
  RFoil line and reported in Hansen's thesis context :footcite:`hansen2017airfoil`
* **Improved drag prediction in XFoil-like tools**: drag-correction work for thick
  airfoils :footcite:`ramanujam2016drag`

QFoil: Modifications to XFOIL 6.99
----------------------------------

The modifications implemented in QFoil draw heavily from the physical models proposed in the literature for RFOIL to provide enhanced stall and post-stall predictions. The detailed changes relative to XFOIL 6.99 are outlined below.

1. Dynamic Shear-Lag Model
~~~~~~~~~~~~~~~~~~~~~~~~~~

In standard XFOIL, the shear-lag coefficient (``SCC``) is maintained as a constant. QFoil replaces this with a shape-factor-dependent formulation, resulting in the prediction of delayed and smoother stall onset.

* **Implementation:** The shear lag coefficient employs a tanh-based formulation depending on the local boundary-layer shape factor :math:`H_k`:
  
  .. math::
      
      K_c = 4.65 - 0.95 \tanh(0.5(H_k - 3.5))

* **Jacobian Integration:** To preserve Newton solver robustness near stall, the analytical derivative of the shear-lag coefficient with respect to the shape factor :math:`H_k` has been explicitly added to the solver's Jacobian matrix terms (``SCC_HKA`` and ``Z_HKA``).
* **Origin:** This formulation relies on the dynamic shear lag theories initially explored by van Rooij (1996) :footcite:`vanrooij1996rfoil` and later formulated and adapted by Hansen (2017) :footcite:`hansen2017airfoil`.

2. Modified Wake Dissipation Length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To facilitate faster wake relaxation and reduce numerical sensitivity to wake length in post-stall conditions, the equilibrium dissipation length in the wake region has been significantly modified.

* **Implementation:** The dissipation length formulation (``ALD``) in the wake region (``ITYP = 3``) is divided by 4 (``ALD = DLCON / 4.0``). This effectively quadruples the equilibrium shear stress in the wake.
* **Origin:** This specific correction to handle massively separated flows was proposed and validated by Ramanujam et al. (2016) :footcite:`ramanujam2016drag`.

3. Solver Iteration Limits and Relaxation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QFoil enforces tighter constraints on the Newton solver updates to prevent divergence when exploring unphysical states during highly separated flows:

* **Under-relaxation factor:** ``RLX`` reduced from ``1.0`` to ``0.7``.
* **Maximum Lift Coefficient Limits:** The maximum allowable :math:`C_L` change per iteration (``DCLMAX``, ``DCLMIN``) is restricted from ``±0.5`` to ``±0.15``.
* **Kinematic Shape Factor bounds:** Bounds ``DHI`` and ``DLO`` were tightened from ``(1.5, -0.5)`` to ``(1.0, -0.4)``.
* **Turbulent HS Correlation parameters:** ``HSMIN`` was adjusted from ``1.500`` to ``1.505``, and ``DHSINF`` was increased from ``0.015`` to ``0.04``.

4. Alpha Step Initialization and Clamping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To significantly improve robustness during continuous ALFA sweeps, QFoil alters the initialization logic for the boundary layer edge velocities (``UEDG``) across angle steps:

* **Forced Inviscid Initialization:** QFoil bypasses wake memory and resets the boundary layer initialization to the purely inviscid velocity distribution (``UINV``) at the beginning of every ALFA step.
* **Suction Peak Clamping:** If an unphysically massive suction peak is detected (:math:`U_{inv} > 2.0`), it is automatically clamped to ``2.0`` to provide a safe "separated" starting guess for the Newton solver.
* **Amplification Reset:** The amplification factor (``CTAU``) is reset to the default attached value (``0.01``) for each ALFA step.

5. Wake-Corrected Drag Extrapolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QFoil modifies XFOIL's standard Squire-Young wake extrapolation routine to prevent unphysical drag excursions near stall:

* **Correction Factor:** A new tunable parameter, ``GWAKE`` (default ``0.40``), dictates a correction to the wake momentum thickness before computing drag. The correction applies strictly when the wake edge velocity ratio satisfies :math:`U_{e,\text{wake}} / U_\infty \le 1.0`.
* **Deep Stall Fallback:** If the edge velocity ratio exceeds 1.0, signaling deep stall or an untrustworthy wake, QFoil falls back to the original unmodified XFOIL drag formulation to guarantee robustness.

6. Increased Panel and Coordinate Limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To accommodate higher-resolution airfoil representations, the internal memory limits defined in ``XFOIL.INC`` have been expanded.

* **Expanded Node Capacity:** The master internal array size parameter (``IQX``) was increased from its default to ``1400``. This safely allows for up to 600 surface panels while retaining ample overhead for high-resolution wake discretizations (up to ~600 wake nodes) without overflowing the solver arrays.
* **Coordinate Buffer Expansion:** The maximum buffer size for polar storage coordinates (``NAX``) was increased to ``1200`` to prevent truncation errors when loading dense airfoil coordinate sets.


.. footbibliography::

