Free Vortex Wake Settings
=========================

Wake Modelling
--------------

- **Wake Integration Type**: This sets the velocity integration method for the wake nodes during the free wake convection step. **EF**: A simple 1st Order Euler Forward integration. **PC**: A 2nd Order Predictor Corrector integration method. **PC2B**: A second Order Predictor Corrector Backwards integration scheme.
- **Wake Rollup**: This actives or deactivates the wake self-induction.
- **Include Trailing/Shed Vortices**: This sets if trailing (streamwise) or shed (spanwise) vortices are generated at the blades trailing edge during every timepstep. 
- **Wake Convection**: The user can choose here which free-stream velocity contributes to the total convection velocitzy of the wake nodes. **BL**: The convection velocity is the mean boundary layer velocity (as a function of height). **HH**: The convection velocity is the constant hub-height velocity. **LOC**: The convection velocity is evaluated locally at each wake node position.
- **Wake Relaxation Factor**:
- **First Wake Row Length Factor**:
- **Max Num. Elements / Norm. Distance**:
- **Wake Reduction Facto**:
- **Count Wake Length In**:
- *Particle Conversion after [Revolutions/Timesteps]**: (**Only QBlade-EE**) 
- **Wake Zones N/1/2/3 in [Revolutions/Timesteps]**:
- **Wake Zones 1/2/3 factor**:

Vortex Modelling
----------------

- **Fixed Bound Core Radius (% Chord)**: This sets the fixed core radius of the bound blade vortices. Defined as a fraction of the local blade chord.
- **Initial Wake Core Radius (% Chord)**: This sets the intial core radius of the free vortices that are created at the blades trailing edge. Defined as a fraction of the local blade chord.
- **Turbulent Vortex Viscosity**: 
- **Include Vortex Stretching**: The user has the option
- **Maximum Vortex Stretching Factor**:

Turbine Gamma Iteration Parameters
----------------------------------

- **Relaxation Factor**: This relaxation factor is used when the blade circulation is updated during the circulation iteration.
- **Max. Epsilon for Convergence**: The convergence criteria for the blade circulation.
- **Max. Number of Iterations**: The maximum number of blade circulation iterations that will be carried out.
