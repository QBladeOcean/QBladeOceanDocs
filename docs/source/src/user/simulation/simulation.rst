Simulation Module Overview
==========================

Simulation Definition Dialog
============================

Simulation Export
=================

Simulation objects can be exported into the text based ``.sim`` format. When a simulation object is exported into the ``.sim`` format, the associated turbine ``.trb`` file is automatically generated and exported. See an exemplary ``.sim`` file below:

.. code-block:: console

	----------------------------------------QBlade Simulation Definition File------------------------------------------
	Generated with : QBlade IH v2.0.2_alpha windows
	Archive Format: 310003
	Time : 17:22:16
	Date : 29.06.2022

	----------------------------------------Object Name-----------------------------------------------------------------
	IEA_15MW_TURB-UBEM222                    OBJECTNAME         - the name of the simulation object

	----------------------------------------Simulation Type-------------------------------------------------------------
	0                                        ISOFFSHORE         - use a number: 0 = onshore; 1 = offshore

	----------------------------------------Turbine Parameters---------------------------------------------------------
	multiple turbines can be added by adding multiple definitions encapsulated with TURB_X and END_TURB_X, where X must start at 1

	TURB_1
	    IEA_15MW_ASE_UBEM/IEA_15MW_ASE_UBEM.trb TURBFILE           - the turbine definition file that is used for this simulation
	    IEA_15MW_ASE_UBEM                    TURBNAME           - the (unique) name of the turbine in the simulation (results will appear under this name)
	    0.00                                 INITIAL_YAW        - the initial turbine yaw in [deg]
	    0.00                                 INITIAL_PITCH      - the initial collective blade pitch in [deg]
	    0.00                                 INITIAL_AZIMUTH    - the initial azimuthal rotor angle in [deg]
	    1                                    STRSUBSTEP         - the number of structural substeps per timestep (usually 1)
	    20                                   RELAXSTEPS         - the number of initial static structural relaxation steps
	    0                                    PRESCRIBETYPE      - rotor RPM prescribe type (0 = ramp-up; 1 = whole sim; 2 = no RPM prescibed) 
	    2.000                                RPMPRESCRIBED      - the prescribed rotor RPM [-]
	    0                                    TINTEGRATOR        - the time integrator for the structural sim (0 = HHT; 1 = linEuler; 2 = projEuler; 3 = Euler)
	    10                                   STRITERATIONS      - number of iterations for the time integration (used when integrator is HHT or Euler)
	    1                                    MODNEWTONITER      - use the modified newton iteration?
	    0.00                                 GLOBPOS_X          - the global x-position of the turbine [m]
	    0.00                                 GLOBPOS_Y          - the global y-position of the turbine [m]
	    0.00                                 GLOBPOS_Z          - the global z-position of the turbine [m]
						 EVENTFILE          - the file containing fault event definitions (leave blank if unused)
						 LOADINGFILE        - the loading file name (leave blank if unused)
						 SIMFILE            - the simulation file name (leave blank if unused)
						 MOTIONFILE         - the prescribed motion file name (leave blank if unused)
	END_TURB_1

	----------------------------------------Simulation Settings-------------------------------------------------------
	0.050000                                 TIMESTEP           - the timestep size in [s]
	1600                                     NUMTIMESTEPS       - the number of timesteps
	10.000                                   RAMPUP             - the rampup time for the structural model
	0.000                                    ADDDAMP            - the initial time with additional damping
	100.000                                  ADDDAMPFACTOR      - for the additional damping time this factor is used to increase the damping of all components
	0.000                                    WAKEINTERACTION    - in case of multi-turbine simulation the wake interaction start at? [s]

	----------------------------------------Wind Input-----------------------------------------------------------------
	1                                        WNDTYPE            - use a number: 0 = steady; 1 = windfield; 2 = hubheight
	Windfield.bts                            WNDNAME            - filename of the turbsim input file or hubheight file (with extension), leave blank if unused
	1                                        STITCHINGTYPE      - the windfield stitching type; 0 = periodic; 1 = mirror
	0                                        WINDAUTOSHIFT      - the windfield shifting automatically based on rotor diameter; 0 = false; 1 = true
	11.00                                    SHIFTTIME          - the windfield is shifted by this time if shift type = 1
	10.00                                    MEANINF            - the mean inflow velocity, overridden if a windfield or hubheight file is use
	0.00                                     HORANGLE           - the horizontal inflow angle
	0.00                                     VERTANGLE          - the vertical inflow angle
	0                                        PROFILETYPE        - the type of wind profile used (0 = Power Law; 1 = Logarithmic)
	0.200                                    SHEAREXP           - the shear exponent if using a power law profile, if a windfield is used these values are used to calculate the mean wake convection velocities
	0.010                                    ROUGHLENGTH        - the roughness length if using a log profile, if a windfield is used these values are used to calculate the mean wake convection velocities
	0.00                                     DIRSHEAR           - a value for the directional shear in deg/m
	150.00                                   REFHEIGHT          - the reference height, used to contruct the BL profile

	----------------------------------------Ocean Depth, Waves and Currents------------------------------------------- 
	the following parameters only need to be set if ISOFFSHORE = 1
	1.00                                     WATERDEPTH         - the water depth
						 WAVEFILE           - the path to the wave file, leave blank if unused
	0                                        WAVESTRETCHING     - the type of wavestretching, 0 = vertical, 1 = wheeler, 2 = extrapolation, 3 = none
	20000.00                                 SEABEDSTIFF        - the vertical seabed stiffness [N/m^3]
	0.50                                     SEABEDDAMP         - a damping factor for the vertical seabed stiffness evaluation, between 0 and 1 [-]
	0.00                                     SEABEDSHEAR        - a factor for the evaluation of shear forces (friction), between 0 and 1 [-]
	0.00                                     SURF_CURR_U        - near surface current velocity [m/s]
	0.00                                     SURF_CURR_DIR      - near surface current direction [deg]
	30.00                                    SURF_CURR_DEPTH    - near surface current depth [m]
	0.00                                     SUB_CURR_U         - sub surface current velocity [m/s]
	0.00                                     SUB_CURR_DIR       - sub surface current direction [deg]
	0.14                                     SUB_CURR_EXP       - sub surface current exponent
	0.00                                     SHORE_CURR_U       - near shore (constant) current velocity [m/s]
	0.00                                     SHORE_CURR_DIR     - near shore (constant) current direction [deg]

	----------------------------------------Global Mooring System------------------------------------------------------
						 MOORINGSYSTEM      - the path to the global mooring system file, leave blank if unused

	----------------------------------------Environmental Parameters---------------------------------------------------
	1.22500                                  DENSITYAIR         - the air density
	0.000016468                              VISCOSITYAIR       - the air kinematic viscosity
	997.00000                                DENSITYWATER       - the water density
	0.000001307                              VISCOSITYWATER     - the water kinematic viscosity
	9.806650000                              GRAVITY            - the gravity constant

	----------------------------------------Output Parameters----------------------------------------------------------
	0                                        STOREREPLAY        - store a replay of the simulation: 0 = off, 1 = on (warning, large memory will be required)
	20.000                                   STOREFROM          - the simulation stores data from this point in time, in [s]
	1                                        STOREAERO          - should the aerodynamic data be stored (0 = OFF; 1 = ON)
	1                                        STOREBLADE         - should the local aerodynamic blade data be stored (0 = OFF; 1 = ON)
	1                                        STORESTRUCT        - should the structural data be stored (0 = OFF; 1 = ON)
	0                                        STOREHYDRO         - should the controller data be stored (0 = OFF; 1 = ON)
	0                                        STORECONTROLLER    - should the controller data be stored (0 = OFF; 1 = ON)
	----------------------------------------Modal Analysis Parameters--------------------------------------------------
	0                                        CALCMODAL          - perform a modal analysis after the simulation has completed (only for single turbine simulations)
	0.00000                                  MINFREQ            - store Eigenvalues, starting with this frequency
	0.00000                                  DELTAFREQ          - omit Eigenvalues that are closer spaced than this value
