Free Vortex Wake Settings
=========================

Wake Modelling
--------------

- **Wake Integration Type**: This sets the velocity integration method for the wake nodes during the free wake convection step. **EF**: A simple 1st Order Euler Forward integration. **PC**: A 2nd Order Predictor Corrector integration method. **PC2B**: A second Order Predictor Corrector Backwards integration scheme.
- **Wake Rollup**: This actives or deactivates the wake self-induction.
- **Include Trailing/Shed Vortices**: This sets if trailing (streamwise) or shed (spanwise) vortices are generated at the blades trailing edge during every timepstep. 
- **Wake Convection**: The user can choose here which free-stream velocity contributes to the total convection velocitzy of the wake nodes. **BL**: The convection velocity is the mean boundary layer velocity (as a function of height). **HH**: The convection velocity is the constant hub-height velocity. **LOC**: The convection velocity is evaluated locally at each wake node position.
- **Wake Relaxation Factor**: This factor can be used to *relax* the wake by blending out the starting vortex. The factor controls how long the wake is allowed to be after a given number of rotor revolutions or timesteps (depending on the **Count Wake Length In** setting). Such as a value of 0.5 allows for a wake length of 5 revolutions after the rotor has undergone 10 revolutions. A factor of 1 deactivaes the blending.
- **First Wake Row Length Factor**: This factor can be used to assign a shortened length to the newly created wake elements at the trailing edge so that the newly created shed vorticity is in closer proximity to the blade. A factor of 1 deactivates the shortening.
- **Max Num. Elements / Norm. Distance**: These two values are used to cut-off the wake after a fixed numbner of vortex elements has been created (Max. Num. Wake Elements) or after a vortex element has reached a distance (normalized by rotor diameter) from the hub that is larger than **Norm. Distance**.
- **Wake Reduction Factor**: This factor *filters* out wake elements that have a circulation smaller than the maximum circulation in the wake multiplied by this factor. In most cases this effectively removes shed vorticity that does not significantly affect the wake induction (see :numref:`fig-wakereduction`).

.. _fig-wakereduction:
.. figure:: wakereduction.png
    :align: center
    :alt: Visualization of the wake reduction approach.
    
    Visualization of the wake reduction approach.

- **Count Wake Length In**: This setting controls how the age of a vortex element is counted. Either as a number of rotor revolutions, or as a number of timesteps that have passed since the elemnt was created.
- *Particle Conversion after [Revolutions/Timesteps]**: (**Only QBlade-EE**) This setting controls when a vortex filament is converted into a vortex particle. If the vortex elemnt has reached an age (in timesteps or revolutions) equal to this value it is converted into a particle. 
- **Wake Zones N/1/2/3 in [Revolutions/Timesteps]**: This setting controls the *length* of the different wake zones. The length is either counted in rotor revolutions or in timesteps, depending on the setting (**Count Wake Length In**). Each wake zone has a successively coarser discretization (depending on the **Wake Zones Factor** settings) to reduce the total number of free wake elements and thereby to speed up the simulation.
- **Wake Zones 1/2/3 factor**: These (integer) factors control by how much the wake is coarsenend in between the different wake zones. A factor of 4 means that when transitioning from one zone to the next 4 wake elements are replaced by a single wake element to coarsen the wake resolution (see :numref:fig-wakezones`.png`).

.. _fig-wakezones:
.. figure:: wakezones.png
    :align: center
    :alt: Visualization of the wake zoning approach.
    
    Visualization of the wake zoning approach.

Vortex Modelling
----------------

- **Fixed Bound Core Radius (% Chord)**: This sets the fixed core radius of the bound blade vortices. Defined as a fraction of the local blade chord.
- **Initial Wake Core Radius (% Chord)**: This sets the intial core radius of the free vortices that are created at the blades trailing edge. Defined as a fraction of the local blade chord.
- **Turbulent Vortex Viscosity**: This value is used in the vortex core growth model, see :ref:`Vortex Core Desingularization`.
- **Include Vortex Stretching**: This option activates vortex stretching, see :ref:`Vortex Core Desingularization`.
- **Maximum Vortex Stretching Factor**: After the cummulative vortex strain rate has reached a value larger than this factor it is automatically removed from the wake.

Turbine Gamma Iteration Parameters
----------------------------------

- **Relaxation Factor**: This relaxation factor is used when the blade circulation is updated during the circulation iteration.
- **Max. Epsilon for Convergence**: The convergence criteria for the blade circulation.
- **Max. Number of Iterations**: The maximum number of blade circulation iterations that will be carried out.
