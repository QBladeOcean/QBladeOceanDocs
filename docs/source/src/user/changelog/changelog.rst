QBlade 2.0.7 beta
-----------------

**Structural Dynamics**

 * Added Timoshenko Beams
 * Added Timoshenko FPM 6x6 Beams
 * Added Anisotropic damping model
 * Added nonlinear stiffness model for mooring lines (to model polyester and nylon ropes)
 * Added calculation of blade mass inertia matrix to *Struct Model info* * Added strain to structural sensor outputs
 * Added strain to structural sensor outputs
 * Added function to automatically export 6x6 blade structural property tables from windIO yaml files
 * Added NLDATA<X> tables to define nonlinear distributions (stress/strain, displacement/force, etc...) 
 * Removed first force value for y=0 from nonlinear spring/damper tables
 * Distributed blade added masses now included in blade COG and inertia calculations in *Struct Model info*
 * Structural blade and strut beams are now always placed at the user defined elastic center
 * The reference position of the local section coordinate system is now the pitch axis
 * Constraints are now defined in the coordinate system of Joint1ID, except for constraints to the fixed ground
 * Improved modal analysis and Campbell diagram functionality (QB-EE only)
 * Can now visualize real, imag, mag, and phase values after a modal analysis (QB-EE only)
 * Fixed evaluation of global rotation displacement for reversed rotors
 * Changed: now NACCM, NACINER and HUBINER can be directly specified within one line (6 entries for inertia, 3 for CM position)
 * Old keywords NACCMX, NACCMZ, NACYINER are still accepted, but should be replaced eventually
 * Fixed issue where external loading data was not assigned for substructure joints
 * Fixed issue where external loading was not correctly assigned when a substructure only was simulated
 
**Aerodynamics**

 * Added Dynamic Wake Meandering (DWM) model (mash up between Fast.Farm and HAWC2Farm models)
 * Added axial, tangential, and radial aerodynamic force to *Structural Time Graphs*
 * Added adaptive relaxation to speed up gamma bound fixed point iteration
 * Added *Aerodynamic Strut Graph* type to visualize distribution of aerodynamic variables over struts (VAWT only)
 * Finished first working version of WindIO YAML import for airfoil, polars, and blades
 * Fixed vortex line core growth model, now correctly working with time offset
 * Fixed UBEM to work properly for reversed rotors
 * Fixed issue with the reprojection of the moment coefficient before applying NC, attached flow, or DS corrections
 * Fixed behavior of the tower shadow model in certain conditions

**Hydrodynamics**

 * Added functionality for one-sided Morison drag for improved low-frequency excitation predictions
 * Added functionality to assign frequency-filtered axial drag coefficients for improved low-frequency excitation predictions
 * Added NBODY>1 feature of WAMIT to substructure definitions for multiple interacting hydro bodies
 * Added tangential cable drag coefficient, as optional column in HYDROMEMBERCOEFF tables
 * Added options to deactivate individual QTF DOF's (DIFF_INACTIVE_DOF, SUM_INACTIVE_DOF)
 * Changed the sign for the definition of the misalignement between wind and waves, when specified via a DLC table
 * Fixed issue in the mooring system where buoyancy wasn't accounted for
 * Fixed issue with turbine global position and water depth for offshore bottom-fixed turbines
 * Fixed issue with read-in functions for RAD and EXC potflow files (incompatible with Windcrete dataset)
 
**Wave Generation**

 * Added nonlinear streamfunction waves and constrained streamfunction waves
 * Added functionality to paste streamfunction waves over constrained newWaes
 * Added display variable at instantaneous sea level (ISL)
 * Changed regular linear waves to now start with a phase shift of 90°
 * Changed random number generation to be consistent across different platforms, e.g. Unix/Windows, using Mersenne Twister engine
 
**Wind Generation**

 * Added Mann turbulence generator
 * Added Mann generator option to create an "added turbulence" windfield for DWM model
 * Added option to create and export windfields from simulations
 * Improved behavior of WindFieldGenerator to better conform to IEC standards
 * Changed random number generation to be consistent across different platforms, e.g. Unix/Windows, using Mersenne Twister engine

**Control Systems**

 * Updated DTU controller to employ original source code and location of the wpData file(s)
 * Changed CpCtCq file of ROSCO controller to be defined relative to the controller library
 * Fixed issue regarding an incompatibility with older ROSCO controller versions

**General Improvements**

 * Improved computational speed for QBlade-CE (~2-3x)
 * Improved stability and numerous bug fixes
 * Finished import/export functionality for wind farm layouts (QB-EE only)
 * In DLC definition files a cell (or entry) beginning with a hashtag (#) is ignored now (QB-EE only)
 * Added new interpolation functions HERMITE, C2 splines and Akima (for structural properties and blade geometry)
 * Added functionality to specify the constrained DoF's between struts and blades and struts and the torquetube (VAWT)
 * Added visualization of IEA reference coordinate systems to QSimulation module
 * Polar Cl and Cn slopes are now obtained via linear regression
 * Added libxlnt to read data directly from excel documents
 * Added functionality so that "submerged" rotors in an "offshore" simulation get the water velocity, density, and viscosity as inputs for "aerodynamic" load calculations, this enables combined wind-hydro turbine simulations
 * Fixed issue in the DLL interface where advanceStructure() and AdvanceAero() were called in the wrong order
 * Fixed issue in cut-plane import/export related to timesteps when QSim had "store from time" enabled
 * Fixed issue where STORE_SIM was not recognized during ASCII simulation import

QBlade 2.0.6.3 beta
-------------------

 * fixed issue where for certains node/member arrangements a substructure could be over-constrained
 * fixed issue where for a substructure only turbine definition NaN inertia values were shown in model overview
 * fixed automatic scene scaling for displaced substructure-only configurations
 * orientations of subjoints and the transition piece can now also be defined by means of consecutive Euler rotations
 * optimizations of OpenCl particle kernels (QBlade-EE)
 * fixed crash of modal analysis of substructure-only configurations (QBlade-EE)
 * fixed issue where the multi-turbine (.mta) ASCII import could crash if some files were missing (QBlade-EE)

QBlade 2.0.6.2 beta
-------------------

 * added total Morison force to output for substructure members in hydrodynamic time graphs
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

QBlade 2.0.6 beta
-----------------

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

QBlade 2.0.5 alpha
------------------

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

QBlade 2.0.4 alpha
------------------

 * This is the first public release of QBlade CE. Be aware that this is an alpha release which will be revisioned after the first user feedback arrives and incompatibilities and errors are fixed.