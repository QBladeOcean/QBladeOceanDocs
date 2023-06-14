QBlade 2.0.6.2 beta
-------------------

 * added total morison force to output for substructure members in hydrodyn. time graphs
 * fixed some small issues with the openCl device selection when not in the GUI mode (CLI or SIL)
 * fixed normal calculation for .stl blade export at blade hub and tip end faces
 * added an optional export filter to rearrange/filter the export files that are generated
 * added a getCustomSimulationData function to the SIL interface
 * substructure constraint loads can now be added to the graphs by specifying the constraint with the identifier "CST"
 * added export filter feature to CLI
 * fixed issue where CLI was searching for a "wrong" binary file name

QBlade 2.0.6.1 beta
-------------------

 * fixed typos
 * in BEM/DMS analysis power is now always displayed as kW
 * fixed issue with turbine sorting for multi turbine simulations

QBlade 2.0.6.0 beta
-------------------

**Substructure**

 * added MOORLOADS to add buoyancy forces and loads to mooring lines
 * ADDMASS functionality was extended so that also diagonal inertia 3xIXX & offdiagonal 3xIXY (in local body coords) can be added to a structure
 * added RECTANGULAR members to the substructure definition, these members can use directional hydro coefficients for the local x and y directions
 * added a new and more consistent table format for MOORELEMENTS and CABLELEMENTS that uses only 6 instead of 7 entries
 * added substructure elements, constraints and spings/dampers to global mooring systems

**Control / SIL**

 * added the functionality to "wire" custom external library and controller data channels from the swap arrays to turbine actions
 * added interface for external controller libraries
 * added function SetExternalAction() to DLL interface to enable highly customized simulations / controllers
 * added visualization of hydrodynamic Morison forces
 * when simulating with the ROSCO controller the "PerfFileName" is now also serialized in the same way as the WPData file for the DTU controller

**Wave Generation**

 * added wave probes to the wave module
 * added constrained embedded wave feature to linear waves
 * added option to merge linear waves

**Misc**

 * turbines (and floater, mooring systems) can now be globally rotated
 * implemented the IAG dynamic stall model
 * added Cn and Ct graphs to polars and 360 polars
 * added feature to assign distributed damping properties for the blade, towers and struts
 * added feature to account for nacelle drag

**QBlade-EE**

 * added aerodynamic damping calculation and damped frequencies to modal analysis (QB-EE only)
 * implemented linearization of buoyancy for modal analysis (QB-EE only)
 * OpenCl: improved kernel performance by ~20%

Furthermore, a lot of features and fixes based on community feedback have been implemented in various modules and the overall stability and robustness has been improved.

QBlade 2.0.5.2 alpha
--------------------

 * public release of QBlade's Software in Loop (SIL) interface
 * project files now 100% compatible between EE and CE versions (dedicated EE format is omitted)
 * catching a possible crash that could occur when pressing the "Mode Animation" botton before the simulation has finished
 * fixed issue where an impulsive aerodynamic load was present at the first timestep due to an error in relative velocity initialization
 * fixed an issue in shared mooring systems
 * in substructure files TP_INTERFACE_POS_1 can now also be used instead of TP_INTERFACE_POS (which was omitting the _1 part)

QBlade 2.0.5.1 alpha
--------------------

 * LLFVW: bound circulation core size is now defined based on aerodynamic panel width instead of chord
 * fixed a small issue in wake coarsening where the redistribution of shed vorticity could lead to a small induction "jump"
 * default blade discretization type is now COSINE
 * improved evaluation of 360° polar parameters, such as slope, aoa_0, Cl_0 etc...
 * OYE and ATEFlap DS models are now limited to the range of +-50° AoA
 * fixed major issue in implementation of nonlinear p-y curves
 * from now on the version stringis part of the binary files to better distinguish them
 * improved custom data aquisition for python and matlab (SIL) interfaces

QBlade 2.0.5.0 alpha
--------------------

 * added blade force in X_c and X_b coordinate systems to the standard outputs
 * added functionality to the assignement of nonlinear springs and dampers for substructures
 * overhauled read-in functionality for WAMIT diffraction and excitation files
 * directionality for 2nd order difference loads now taken into account
 * arbitrary orientations can now be assigned to substructure nodes, substructure node coordinate systems can now be displayed
 * added option to read-in WAMIT .8 files
 * added correct Reynolds number to steady BEM outputs
 * fixed issue where TSR string was set to zero after creating a bladeLoading definition
 * fixed bug that corrupted project files after a polar was edited with "Edit Current Polar Points" and then discarded
 * added optional generator efficiency
 * fixed initial camera view angles for QTurbine and QSimulation modules
 * renamed StrModel variables for aerodynamic and generator power and torque
 * improved import/export functionality of velocity cut-plane definitions
 * fixed broken link to forum
 * added controller SWAP array to getCustomData() function of the DLL interface

QBlade 2.0.4.9 alpha
--------------------

 * added CPmin variable to results of the XFoil polar analysis, corrected evaluation of friction drag coefficient from XFoil
 * bugfix: overhauled interface with Xfoil binary which is now working with absolute instead of relative path names
 * bugfix: fixed a crash that occurred when a TDMS object was deleted in the GUI
 * added blade root forces to default sensors
 * added FAST binary format to the avaliable export formats for simulation timeseries
 * fixed issue where when using hubheight inflow files the horizontal inflow angle was not read in properly
 * changed the sign in the definition of the horizontal inflow angle to be in line with the most common convention
 * bugfix: prevent UBEM crashes that occurred at inflow velocity of zero
 * tower bodies, torquetube bodies & strut bodies can now have buoyancy & addedmass & dynamic pressure coefficients assigned to model hydrokinetic turbines. model hydrokinetic turbines as onshore turbines with changed air density
 
QBlade 2.0.4.8 alpha
--------------------

 * chord can now be optimized idependent of twist
 * optimize PROP dialog now hidden during HAWT blade design
 * displaced water volume added to hydrodynamic variables
 * when a simulation is diverging the last 3 timesteps are removed from the data to prevent NaN in data
 * added yaw event to turbine events

QBlade 2.0.4.7 alpha
--------------------

 * default sensors added for tower top and nacelle (velocity, acceleration, deflection)
 * fixed issue in DS models that could occur when "bad quality" polar data (such as with negative slope) was used
 * removed structural time integrator selection from SimulationCreatorDialog, HHT is now default
 * fixed issue where the tower drag coefficient was not read from the structural data table
 * fixed issue with the tower shadow model, the position of tower shadow is now the instantaneous position of floating turbine
 * added info for RNA and Tower COG to turbine design module, inertia info displayed now around the global COG
 * when importing TurbSim .inp files the TurbSim console output is now displayed
 * added delete by selection for turbine objects
 * graph data can now be directly copied to clipboard
 * several small gui improvements

QBlade 2.0.4.6 alpha
--------------------

 * fixed error where the current yaw angle read from the structural model had the wrong sign
 * fixed error when during import of linear waves from a time series the mean heading angle was read in radians and not degrees
 * added yaw angle to structural outputs
 * added ROSCO 2.4.1 controller library

QBlade 2.0.4.5 alpha
--------------------

 * Implemented various checks to prevent users from defining overconstrained nodes during substructure generation that could cause divergence in the structural solver; checking SUBELEMENTSRIGID and SUBCONSTRAINT data tables

QBlade 2.0.4.4 alpha
--------------------

 * Bugfix in steady state BEM for HAWT's

QBlade 2.0.4.3 alpha
--------------------

 * Fixed an issue in the classical steady state BEM iteration that appeared at large (above optimum) TSR's.

QBlade 2.0.4.2 alpha
--------------------

 * There were issues with the OpenCL.dll under Windows, this dll has been replaced with a more compatible version that should detect OpenCL for most users

QBlade 2.0.4.1 alpha
--------------------

 * Fixed issue with virtual camber transformation, where values were not read from dialog
 * Improved behavior of FoilTable when Foil selection is changed

QBlade 2.0.4.0 alpha
--------------------

 * This is the first public release of QBlade CE. Be aware that this is an alpha release which will be revisioned after the first user feedback arrives and incompatibilities and errors are fixed.