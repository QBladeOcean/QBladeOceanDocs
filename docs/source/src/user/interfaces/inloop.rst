Software in Loop (SIL) Overview
*******************************
   
The Software in Loop interface in QBlade provides an easy way of controlling the whole simulation loop of a wind turbine and enable cosimulation within other software frameworks or scripting languages, such as Python or Matlab. To enable this functionality QBlade is compiled as a Dynamic Link Library (.dll, Windows) or as a Shared Object (.so, Unix) and the relevant functionality is exported into an interface.

Through the different functions that are exported the user can explicitly import QBlade projects (.qpr) or Simulation Definition Files (.sim) and then progress the simulation incrementally in time by calling the :code:`advanceTurbineSimulation()` function. At every timestep it is possible to inquire any variable of the simulation and control various aspects of the simulation in response, such as changing the inflow conditions, changing the position and orientation of the turbine or controlling the various control actuators (pitch, yaw, generator torque) of the wind turbine. A possible application for the SIL interface is a cosimulation, where the turbine floater can be modeled within a specialized software that is coupled with QBlade through force/position intercommunication. Instead of modeling the floater, the cosimulation could also model the drivetrain, controller or generator in a more sophisticated way. Another application is controller development, where the controller can run in a scripting language (such as Simulink), receiving custom signals from the simulation and controlling the turbine actuators in response. When running a multi-turbine simulation within the SIL interface the user may control each simulated turbine individually, enabling the modeling of global wind park controllers.

In general, the high level overview of the SIL interface and the simulation loop, when running the SIL in an external language, looks as follows:

.. code-block:: console

	loadLibrary()    
	createInstance()
	loadProject() 
	initializeSimulation()

	#start of the simulation loop
	
	for i in range(end):

		...do something...
		advanceTurbineSimulation()
		
	#end of the simulation loop

	storeProject()
	closeInstance()
	
Quick Start with the SIL Interface in Python
************************************************

To test the SIL interface in Python you can simply start the python script :code:`sampleScript.py`, which you find in the folder :code:`\PythonInterface` of the QBlade directory. This script imports the QBlade library, loads a turbine and simulation definition by from a QBlade project file (.qpr) and then runs a simulation loop for 500 timesteps while printing out some results and finally saving the finished simulation as a new project file. This samples are just meant as a quick demo on how to interface with QBlade in Python and does not serve any other particular purpose. Adapt as needed. 

Python Examples:
	:ref:`Python Example: Running the QBlade Library`.
	:ref:`Python Example: Definition of the QBladeLibrary Class`. 
	
Matlab Examples:
	:ref:`Matlab Example: Running the QBlade Library`.
	:ref:`Matlab Example: Definition of the QBladeLibrary Class`.
	
Interface Function Definitions
******************************

.. code-block:: c
	:linenos:
	:caption: : QBladeLibInclude.h

	#all variables and return values are c data types

	void setLibraryPath(char *str);
	
	void createInstance(int clDevice, int groupSize);
	void loadProject(char *str);
	void loadSimDefinition(char *str);
	void initializeSimulation();
	void runFullSimulation();
	
	void advanceController_at_num(double *vars, int num);
	bool advanceTurbineSimulation();
	
	void storeProject(char *str);
	void exportResults(int type, char *filepath, char* filename, char *filter);
	void closeInstance();
	void setLogFile(char *str);
	
	void loadTurbulentWindBinary(char *str);
	void addTurbulentWind(double windspeed, double refheight, double hubheight, double dimensions, int gridPoints, double length, double dT, char *turbulenceClass, char *turbulenceType, int seed, double vertInf, double horInf, bool removeFiles);
	
	void setPowerLawWind(double windspeed, double horAngle, double vertAngle, double shearExponent, double referenceHeight);
	void setDebugInfo(bool isDebug);
	void setUseOpenCl(bool isOpenCl);
	void setAutoClearTemp(bool enabled);

	void setGranularDebug(bool dStr, bool dSim, bool dTurb, bool dCont, bool dSer);
	void setTimestepSize(double timestep);
	void setRPMPrescribeType_at_num(int type, int num);
	void setRPM_at_num(double rpm, int num);
	void setRampupTime(double time);
	void setInitialConditions_at_num(double yaw, double pitch, double azimuth, double rpm, int num);
	void setTurbinePosition_at_num(double x, double y, double z, double rotx, double roty, double rotz, int num);
	void setControlVars_at_num(double *vars, int num);
	void setExternalAction(char *action, char *id, double val, double pos, char *dir, bool isLocal, int num);
	void setMooringStiffness(double EA, double neutralStrain, int cabID, int num);

	void getWindspeed(double posx, double posy, double posz, double *velocity);
	void getWindspeedArray(double *posx, double *posy, double *posz, double *velx, double *vely, double *velz, int arraySize);
	void getTowerBottomLoads_at_num(double *loads, int num);
	void getTurbineOperation_at_num(double *vars, int num);
	double getCustomData_at_num(char *str, double pos, int num);
	double getCustomSimulationTimeData(char *str);


Interface Function Documentation
********************************

In the following, the functionality that is exported from the QBlade dll or shared object is described and the function arguments and return types are given. All functions with the appendix **_at_num** affect the turbine specified by the argument **num** - this has only an effect for multi turbine simulations.

:code:`void setLibraryPath(char *atr)`
	This function sets the location of the QBlade dll or shared object so that the QBlade instance knows about its location. **This function must be called first** so that the QBlade instance knows about the location of associated binaries (XFoil, TurbSim) and possibly license files.

:code:`void createInstance(int clDevice = 0, int groupSize = 32)`
	This function creates a new instance of QBlade. The OpenCL device and the OpenCL group-size can both be specified in the arguments. **Calling this function is mandatory!** 
	
:code:`void loadProject(char *str)`
	This function loads a simulation definition from a QBlade project (.qpr) into the QBlade instance. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths. If the QBlade project contains one or more simulation definitions, the first simulation definition of the project file (in alphabetic order) is loaded into the SIL interface.

:code:`void loadSimDefinition(char *str)`
	This function loads a simulation definition (.sim) file into the QBlade instance. The (.sim) files are ASCII files and any aspect of the simulation can be changed by modifying or preprocessing (.sim) files. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.

:code:`void initializeSimulation()`
	This function initializes the simulation, e.g. the simulation is reset and structural ramp-up is carried out.
	
:code:`void runFullSimulation()`
	This function runs all timesteps for all turbines of the simulation as defined in the simulation object. This is equivalent to pressing the *Start Simulation* button in QBlade`s GUI. This function needs to be called after :code:`void initializeSimulation()`. When calling this function it is not possible to *interact* with the simulation before it is finished. To interact with the simulation you need to create your own simulation loop and call the functions :code:`void advanceController_at_num()` and :code:`void advanceTurbineSimulation()` at every timestep.

:code:`void advanceController_at_num(double *vars, int num = 0)`
	This function advances the controller shared library that is assigned to the selected turbine (argument *num*). When calling this function the controller outputs (gen. torque, blade pitch, etc.) are automatically applied to the turbine (no need to call :code:`void setControlVars_at_num(double *vars, int num = 0)`). The controller outputs are also returned in the *vars* array, and can be processed further:
	
	* vars[0] = generator torque [Nm]
	* vars[1] = yaw angle [deg]
	* vars[2] = pitch BLD_1 [deg]
	* vars[3] = pitch BLD_2 [deg]
	* vars[4] = pitch BLD_3 [deg]

:code:`bool advanceTurbineSimulation()`
	This function advances the turbine simulation for all turbines by one (time) step. Returns *true* if the step was successful.

:code:`void storeProject(char *str)`
	This functions stores a project file. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.
	
:code:`void exportResults(int type, char *filepath, char* filename, char *filter)`
	This function saves the results of the current simulation to a file in the chosen format
	
	* type: specifies the export format: 0: QBlade ASCII; 1: HAWC2 ASCII; 2: HAWC2 BINARY; 3: OpenFAST BINARY
	* filepath: sets the folder in which the export file(s) will be stored
	* filename: sets the name of the export file, do not add an extension. The extension will be added automatically, based on the chosen export format type
	* filter: allows to point to a global result filter file (see :ref:`Global Export Filter`), specify full fill path and extension
	
:code:`void setLogFile(char *str)`
	This functions sets the path to a log file that will be created to store the debug output. This is helpful when accessing the SIL interface from a tool that does not display standard output.

:code:`void closeInstance()`
	This function closes the instance of QBlade and frees the memory.
	
:code:`void loadTurbulentWindBinary(char *str)`
	This function allows to load a turbulent windfield that is stored in binary format. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.
	
:code:`void addTurbulentWind(double windspeed, double refheight, double hubheight, double dimensions, int gridPoints,double length, double dT, char *turbulenceClass, char *turbulenceType, int seed, double vertInf, double horInf, bool removeFiles = false)`	
	This function allows to define and add a turbulent windfield (using TurbSim) to the simulation. If a turbulent windfield is used the function :code:`setPowerLawWind()` has no effect. It uses the following parameters:
	
	* windspeed: the mean windspeed at the reference height [m/s]
	* refheight: the reference height [m]
	* hubheight: the hubheight, more specifically the height of the windfield center [m]
	* dimensions: the y- and z- dimensions of the windfield in meters [m]
	* length: the simulated length of the windfield in seconds [s]
	* dT: the temporal resolution of the windfield [s]
	* turbulenceClass: the turbulence class, can be "A", "B" or "C"
	* turbulenceType: the turbulence type, can be "NTM", "ETM", "xEWM1" or "xEWM50" - where x is the turbine class (1,2 or 3)
	* seed: the random seed for the turbulent windfield
	* vertInf: vertical inflow angle in degrees [deg]
	* horInf: horizontal inflow angle in degrees [deg]

:code:`void setPowerLawWind(double windspeed, double horAngle, double vertAngle, double shearExponent, double referenceHeight)`
	This function can be called before or at any time after the simulation has been initialized with :code:`initializeSimulation()` to statically or dynamically change the inflow conditions. It defines a power law wind profile (https://en.wikipedia.org/wiki/Wind_profile_power_law) and its inflow direction. The arguments for this function are:
	
	* windspeed: constant windspeed in m/s [m/s]
	* horAngle: the horizontal inflow angle in degrees [deg]
	* vertAngle: the vertical inflow angle in degrees [deg]
	* shearExponent: this is the exponent for the power law boundary layer profile, if this is set to 0 the windspeed is constant with height [-]
	* referenceHeight: this is the height at which the velocity in the boundary layer is the defined windspeed, usually set to the hubheight [m]
	* exemplary call: addTurbulentWind(12,115,115,220,20,60,0.1,"A","NTM",1000000,0,0);

:code:`void setDebugInfo(bool isDebug)`
	This function enables the debug output if set to true.
	
:code:`void setGranularDebug(bool dStr, bool dSim, bool dTurb, bool dCont, bool dSer)`
	This function enables a granular debug output.
	
	* dStr: enable structural model debug info
	* dSim: enable simulation debug info
	* dTurb: enable turbine debug info
	* dCont: enable controller debug info
	* dSer: enable serializer debug info

:code:`void setTimestepSize(double timestep)`
	This function can be used to set the timestep size (in [s]) if the user wants to change this value from the project or simulation definition file. It needs to be called before :code:`initializeSimulation()`.

:code:`void setRPMPrescribeType_at_num(int type, int num = 0)`
	This function can be used to change the rpm prescribe type. It needs to be called before :code:`initializeSimulation()`.
	
	* 0 - RPM prescribed during ramp-up only
	* 1 - RPM prescribed for the whole simulation
	* 3 - no prescribed RPM

:code:`void setRPM_at_num(double rpm, int num = 0)`
	This function can be used to change the prescribed rpm for a turbine.
	
	* The parameter **rpm** sets the rotational rate.
	* The parameter **num** specifies the turbine instance for which the rpm is set.

:code:`void setRampupTime(double time)`
	This function can be used to change the ramp-up time from the value specified in the project or simulation file, call before :code:`initializeSimulation()`.

:code:`void setInitialConditions_at_num(double yaw, double pitch, double azimuth, double rpm, int num = 0)`
	This function may be used to set the turbine initial yaw [deg], collective pitch [deg], azimuthal angle [deg] and initial rotSpeed [rpm] to a value different than specified in the QBlade project or simulation input file. It needs to be called before :code:`initializeSimulation()`.

:code:`void setTurbinePosition_at_num(double x, double y, double z, double rotx, double roty, double rotz, int num = 0)`
	This function sets the turbine tower bottom x, y and z position [m], and xrot, yrot zrot rotation [deg]. It can be called before :code:`initializeSimulation()` if the turbine position should be offset initially or during the simulation loop if it should be changed dynamically, for example during cosimulation with a hydrodynamics software that models the floater.

:code:`void setControlVars_at_num(double *vars, int num = 0)`
	This function applies the control actions to the selected turbine (argument *num*) for torque, pitch and yaw angle. If it is called after the function :code:`advanceController()` the control actions from the controller are overwritten (in this way the control actions can also be modified). The following data needs to be passed in the array *vars*.
	
	* vars[0] = generator torque [Nm];
	* vars[1] = yaw angle [deg];
	* vars[2] = pitch BLD_1 [deg];
	* vars[3] = pitch BLD_2 [deg];
	* vars[4] = pitch BLD_3 [deg];

:code:`void setExternalAction(char *action, char *id, double val, double pos, char *dir, bool isLocal, int num)`
	This is a general purpose function that can be used to apply an external action to the simulated turbine. 
	
	The action can be of different types, defined by the parameter **action**. All of these actions are not accumulated and are reset at every timestep, or in other words if, for example, a constant mass should be assigned to the turbine it needs to be assigned with this function at every timestep or it will automatically be reset to zero. The different types are:
	
	* ADDMASS: adds mass to a location, in [kg]
	* ADDFORCE: adds a force to a location, in [N]
	* ADDTORQUE: adds a torque to a location, in [Nm]
	* SETLENGTH: sets the delta Length of a cable, in [m]
	* SETAFC: sets the state of an AFC element [-]
	* SETTORQUE: sets the generator torque, in [Nm]
	* SETYAW: sets the yaw angle, in [rad]
	* SETPITCH: sets the pitch angle for BLD_X, in [rad]
	* SETBRAKE: sets the brake modulation [0-1]
	
	Some actions are applied to a certain location ID, indicated by the parameter **id**, the different locations are:
	
	* CAB_<X>: applies the action to the guycable with ID <X>. Actions on cables are: SETLENGTH, ADDMASS, ADDFORCE
	* MOO_<X>: applies the action to the mooring line with ID <X>. Actions on moorings are: SETLENGTH, ADDMASS, ADDFORCE
	* TRQ: applies the action to the torquetube. Actions on the torquetube are: ADDFORCE, ADDTORQUE, ADDMASS
	* BLD_<X>: applies the action to blade <X>. Actions on the blades are: ADDFORCE, ADDTORQUE, ADDMASS
	* STR_<X>_<Y>: applies the action to strut <X> of blade <Y>. Actions on the struts are: ADDFORCE, ADDTORQUE, ADDMASS
	* AFC_<X>_<Y>: applies the action to AFC <X> of blade <Y>. Actions on the AFC elements are: SETAFC
	* SUB_<X>: applies the action to the substructure element with ID <X>. Actions on the substructure elements are: ADDFORCE, ADDTORQUE, ADDMASS
	* JNT_<X>: applies the action to the substructure joint with ID <X>. Actions on the substructure joints are: ADDFORCE, ADDTORQUE, ADDMASS
	* HUB: applies the action to the free LSS hub node. Actions on the hub node are: ADDFORCE, ADDTORQUE, ADDMASS
	* HUBFIXED: applies the action to the fixed non-rotating hub node. Actions on the hub node are: DDFORCE, ADDTORQUE, ADDMASS
	
	The remaining parameters are used to further define the action that is applied, their coordinate systems, etc.
	
	* The parameter **val** specifies the mass [kg], torque [Nm], force [N], delta length [m] or AFC state [-]. 
	* The parameter **pos** sets the normalized position [0-1] at which the mass, force or torque is applied. Only has an effect on elements, not on nodes.
	* The parameter **dir** specifies the direction along which the force or torque is applied, options are "X", "Y", "Z".
	* The parameter **isLocal** specifies sets whether the direction is defined in global or local (element or node) coordinates.
	* The parameter **num** specifies the turbine instance to which the action is applied, if num is set to -1, the action is performed on the global mooring system.

:code:`void setMooringStiffness(double EA, double neutralStrain, int cabID, int num)`
	This function can be used to dynamically adjust the stiffness (EA value) and neutral strain of a mooring line. In this way a nonlinear stiffness-strain relationship can be implemented.
	
	* The parameter **EA**: the longitudinal stiffness value [N/m]
	* The parameter **neutralStrain**: adjusts the cable's rest length to be force-free at this strain, based on the initial length in the MOORMEMBERS table.
	* The parameter **cabID**: the cable id
	* The parameter **num**: the turbine instance for which the mooring line properties are changed, use -1 to apply this to a cable from the global mooringSystem

:code:`void getWindspeed(double x, double y, double z, double *velocity)`
	This function can be called to get the current windspeed at the chosen position (x,y,z), returns the windspeed vector in the *double pointer* velocity.
	
	* velocity[0] = x-component [m/s];
	* velocity[1] = y-component [m/s];
	* velocity[2] = z-component [m/s];
	
:code:`void getWindspeedArray(double *posx, double *posy, double *posz, double *velx, double *vely, double *velz, int arraySize)`
	This function can be called to get the current windspeed for an array of positions
	
	* posx = double array of position x-components;
	* posy = double array of position y-components;
	* posz = double array of position z-components;
	* velx = double array of velocity x-components evaluated at the pos array;
	* vely = double array of velocity y-components evaluated at the pos array;
	* velz = double array of velocity z-components evaluated at the pos array;
	* arraySize = the size of the pos and velocity arrays;

:code:`void getTowerBottomLoads_at_num(double *loads, int num)`
	This function can be used to obtain the loads at the bottom of the tower. The main purpose of this is to be used in conjunction with the :code:`setTurbinePosition_at_num()` function for force/position cosimilation with a hydrodynamics solver that is modeling the floater.

:code:`void getTurbineOperation_at_num(double *vars, int num = 0)`
	This function returns useful turbine operational parameters from the selected turbine (argument *num*). Typically, this data is used to feed the logic of a supervisory wind turbine controller. The data is returned in the array *vars* which has the following content:
	
	* vars[0] = rotational speed [rad/s]
	* vars[1] = power [W]
	* vars[2] = Abs HH wind velocity [m/s]
	* vars[3] = yaw angle [deg]
	* vars[4] = pitch BLD_1 [deg]
	* vars[5] = pitch BLD_2 [deg]
	* vars[6] = pitch BLD_3 [deg]
	* vars[7] = oop blade root bending moment BLD_1 [Nm]
	* vars[8] = oop blade root bending moment BLD_2 [Nm]
	* vars[9] = oop blade root bending moment BLD_3 [Nm]
	* vars[10] = ip blade root bending moment BLD_1 [Nm]
	* vars[11] = ip blade root bending moment BLD_2 [Nm]
	* vars[12] = ip blade root bending moment BLD_3 [Nm]
	* vars[13] = tor blade root bending moment BLD_1 [Nm]
	* vars[14] = tor blade root bending moment BLD_2 [Nm]
	* vars[15] = tor blade root bending moment BLD_3 [Nm]
	* vars[16] = oop tip deflection BLD_1 [m]
	* vars[17] = oop tip deflection BLD_2 [m]
	* vars[18] = oop tip deflection BLD_3 [m]
	* vars[19] = ip tip deflection BLD_1 [m]
	* vars[20] = ip tip deflection BLD_2 [m]
	* vars[21] = ip tip deflection BLD_3 [m]
	* vars[22] = tower top acceleration in global X [m/s^2]
	* vars[23] = tower top acceleration in global Y [m/s^2]
	* vars[24] = tower top acceleration in global Z [m/s^2]
	* vars[25] = tower top fore aft acceleration [m/s^2]
	* vars[26] = tower top side side acceleration [m/s^2]
	* vars[27] = tower top X position [m]
	* vars[28] = tower top Y position [m]
	* vars[29] = tower bottom force along global X [Nm]
	* vars[30] = tower bottom force along global Y [Nm]
	* vars[31] = tower bottom force along global Z [Nm]
	* vars[32] = tower bottom bending moment along global X [Nm]
	* vars[33] = tower bottom bending moment along global Y [Nm]
	* vars[34] = tower bottom bending moment along global Z [Nm]
	* vars[35] = current time [s]
	* vars[36] = azimuthal position of the LSS [deg]
	* vars[37] = azimuthal position of the HSS [deg]
	* vars[38] = HSS torque [Nm]
	* vars[39] = wind speed at hub height [m/s]
	* vars[40] = HH wind velocity x [m/s]
	* vars[41] = HH wind velocity y [m/s]
	* vars[42] = HH wind velocity z [m/s]

:code:`double getCustomData_at_num(char *str, double pos = 0, int num = 0)`
	This function can be used to access the current value from an arbitrary turbine simulation variable in QBlade. Specify the data name as is would appear in any QBlade graph as a *char pointer*. If you are requesting an aerodynamic 'at section' variable, for instance 'Angle of Attack at 0.25c (at section) BLD_1 [deg]' you can specify the normalized position along the blade length using the 'pos' variable. As an example, to get the AoA at 85% blade length from turbine 0, you would call the function the following way: :code:`getCustomData_at_num("Angle of Attack at 0.25c (at section) BLD_1 [deg]", 0.85,0)`. Choosing num == -1 allows to extract any values that are stored in the *Simulation Time Graph* (such as for the global mooring system).
	
:code:`double getCustomSimulationTimeData(char *str)`
	This function can be used to access the current value from an arbitrary *simulation time graph* variable in QBlade. 
	
:code:`void setAutoClearTemp(bool enabled)`
	This function allows to disable the automatic deletion of the TEMP folder, in which temporary controller libraries are files are stored. This automatic deletion can be problematic in case of multi-instanced SIL libraries, hence thhis function can deactivate it.


Python Example: Running the QBlade Library
******************************************
The following code example (*sampleScript.py*) is an example for a light weight Python script that utilizes the QBlade SIL interface. There are many ways to improve this, e.g. the library could be loaded into multiple separate processes for parallelization and sophisticated algorithms could be implemented instead of using a standard controller. This exemplary script only uses a small amount of the functionality that is exported by the QBlade library for purely illustrative purposes. 

In this Python example script the directory *dll_directory* is searched for shared library files. If a shared library file is found, the library is loaded by creating an object *QBLIB*, by calling the *QBladeLibrary* function that handles the library import. After the object *QBLIB* has been created any function of the QBlade library can be accessed by calling :code:`QBLIB.function_XYZ()`. All lines of code that are needed to load the QBlade library into python are highlighted in the example below.

After the QBlade library has been loaded a simulation object is imported and a simulation is started over 500 timesteps. During the simulation loop different data is obtained from the turbine simulation. The turbine controller that is defined in the simulation object is advanced and its signals are passed to the turbine actuators. After the simulation loop has finished the simulation is stored into a project file, for later inspection, and the library is unloaded from python.


.. code-block:: python
	:linenos:
	:caption: : sampleScript.py
	
	import os
	import sys
	from ctypes import *
	from QBladeLibrary import QBladeLibrary
	
	# Define the directory where the QBlade library is located
	dll_directory = "../"
	
	# On Windows systems, we update the PATH environment variable to include the QBlade directory. 
	# This ensures that the required SSL libraries (e.g., libssl and libcrypto) are properly located and loaded.
	# If experiencing issues with this DLL in a Windows Python environment see:
	# https://docs.qblade.org/src/license/license_files.html#resolving-openssl-issues-on-windows
	if os.name == 'nt':  # 'nt' indicates Windows
		os.environ["PATH"] = os.path.abspath(dll_directory) + ";" + os.environ.get("PATH", "")
	
	# Search the directory below for library files matching the pattern QBlade*.dll or QBlade*.so
	dll_files = [f for f in os.listdir(dll_directory) if 'QBlade' in f and ('.dll' in f or '.so' in f)]
	
	# Check if any matching files are found
	if not dll_files:
		print('No matching QBlade*.dll or QBlade*.so files found in the specified directory:',os.path.abspath(dll_directory))
		sys.exit(1)  # Exit the script with a non-zero status to indicate an error
	
	# Use the first matching file
	dll_file_path = os.path.join(dll_directory, dll_files[0])
	
	# Display the selected shared library file
	print(f'Using shared library file: {dll_file_path}')
	
	# Create an object of the class 'QBladeLibrary' that contains the API
	QBLADE = QBladeLibrary(dll_file_path)    
	
	# Creation of a QBlade instance from the library
	QBLADE.createInstance(1,32)
	
	# Loading a project or sim-file, in this case the DTU_10MW_Demo project or simulation definition file
	#QBLADE.loadSimDefinition(b"./DTU_10MW_Demo.sim") #uncomment this line to load a simulation definition file
	QBLADE.loadProject(b"./NREL_5MW_Sample.qpr") 
	
	# Initializing the sim and ramp-up phase, call before starting the simulation loop
	QBLADE.initializeSimulation()
	
	# We will run the simulation for 500 steps before storing the results
	number_of_timesteps = 500
	
	# Start of the simulation loop
	for i in range(number_of_timesteps):
	
		#advance the simulation
		success = QBLADE.advanceTurbineSimulation() 
		
		# Check if the simulation step was successful
		if not success:  # If success is False, exit the loop
			print(f"Simulation failed at timestep {i}. Exiting loop.")
			break
		
		# Assign the c-type double array 'loads' with length [6], initialized with zeros
		loads = (c_double * 6)(0,0,0,0,0,0) 
		# Retrieve the tower loads and store the in the array 'loads' by calling the function getTowerBottomLoads_at_num()
		QBLADE.getTowerBottomLoads_at_num(loads,0)
		
		# Uncomment the next line to try changing the position of the turbine dynamically
		#QBLADE.setTurbinePosition_at_num(-0.2*i,0,0,0,i*0.1,i*0.1,0) 
		
		# Example how to extract a variable by name from the simulation, call as often as needed with different variable names, extracting rpm and time in the lines below
		rpm = QBLADE.getCustomData_at_num(b"Rotational Speed [rpm]",0,0) 
		time = QBLADE.getCustomData_at_num(b"Time [s]",0,0) #example how to extract the variable 'Time' by name from the simulation
		AoA = QBLADE.getCustomData_at_num(b"Angle of Attack at 0.25c (at section) BLD_1 [deg]",0.85,0) #example how to extract the variable 'Angle of Attack' by name at 85% blade length from the simulation 
		
		# Example how to extract a 3 length double array with the x,y,z windspeed components at a global position of x=-50,Y=0,Z=100m from the simulation
		windspeed = (c_double * 3)(0,0,0) 
		QBLADE.getWindspeed(-50,0,100,windspeed)
		
		# Assign the c-type double array 'ctr_vars' with length [5], initialized with zeros
		ctr_vars = (c_double * 5)(0); 
		# Advance the turbine controller and store the controller signals in the array 'ctr_vars'
		QBLADE.advanceController_at_num(ctr_vars,0)
		
		# Pass the controller signals in 'ctr_vars' to the turbine by calling setControlVars_at_num(ctr_vars,0) 
		QBLADE.setControlVars_at_num(ctr_vars,0) 
		
		# Print out a few of the recorded data, in this case torque, tower bottom force along z (weight force) and rpm
		print("Time:","{:3.2f}".format(time),"   Windspeed:","{:2.2f}".format(windspeed[0]),"  Torque:","{:1.4e}".format(ctr_vars[0]),"    RPM:","{:2.2f}".format(rpm),"   Pitch:","{:2.2f}".format(ctr_vars[2]),"   AoA at 85%:","{:2.2f}".format(AoA))
	
	# The simulation loop ends here after all 'number_of_timesteps have been evaluated
		
	# Storing the finished simulation in a project as NREL_5MW_Sample_completed, you can open this file to view the results of the simulation inside QBlade's GUI
	QBLADE.storeProject(b"./NREL_5MW_Sample_completed.qpr")
	
	# Storing the simulation results in QBlade ASCII format in the file NREL_5MW_Sample_results.txt
	QBLADE.exportResults(0,b"./",b"NREL_5MW_Sample_results",b"")
	
	# Unloading the qblade library
	QBLADE.unload() 
	
	
	
Python Example: Definition of the QBladeLibrary Class
*****************************************************

The script *QBladeLibrary.py* defines the class *QBladeLibrary* and loads the shared object. This script is just a suggestion on how to interface with the QBlade Library in Python and certainly there are more efficient ways of how to do this.

.. code-block:: python
	:linenos:
	:caption: : QBladeLibrary.py

	from ctypes import *
	from typing import Dict, Any
	
	class QBladeLibrary:
		def __init__(self, shared_lib_path: str):
			"""Initialize and load the QBlade shared library."""
			self.lib_path = shared_lib_path
			self.lib = None
	
			# Define all functions with argument types and return types
			self.functions: Dict[str, Dict[str, Any]] = {
				"createInstance": {"argtypes": [c_int, c_int], "restype": c_void_p},
				"closeInstance": {"argtypes": None, "restype": c_void_p},
				"loadProject": {"argtypes": [c_char_p], "restype": c_void_p},
				"loadSimDefinition": {"argtypes": [c_char_p], "restype": c_void_p},
				"setOmpNumThreads": {"argtypes": [c_int], "restype": c_void_p},
				"getCustomData_at_num": {"argtypes": [c_char_p, c_double, c_int], "restype": c_double},
				"getCustomSimulationTimeData": {"argtypes": [c_char_p], "restype": c_double},
				"getWindspeed": {"argtypes": [c_double, c_double, c_double, POINTER(c_double * 3)], "restype": c_void_p},
				"getWindspeedArray": {"argtypes": [POINTER(c_double), POINTER(c_double), POINTER(c_double),POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int],"restype": c_void_p,},
				"storeProject": {"argtypes": [c_char_p], "restype": c_void_p},
				"exportResults": {"argtypes": [c_int, c_char_p, c_char_p, c_char_p], "restype": c_void_p},
				"setLibraryPath": {"argtypes": [c_char_p], "restype": c_void_p},
				"setLogFile": {"argtypes": [c_char_p], "restype": c_void_p},
				"addTurbulentWind": {"argtypes": [c_double, c_double, c_double, c_double, c_int, c_double,c_double, c_char_p, c_char_p, c_int, c_double, c_double, c_bool,],"restype": c_void_p,},
				"setExternalAction": {"argtypes": [c_char_p, c_char_p, c_double, c_double, c_char_p, c_bool, c_int],"restype": c_void_p,},
				"setMooringStiffness": {"argtypes": [c_double, c_double, c_int, c_int], "restype": c_void_p},
				"loadTurbulentWindBinary": {"argtypes": [c_char_p], "restype": c_void_p},
				"setTimestepSize": {"argtypes": [c_double], "restype": c_void_p},
				"setInitialConditions_at_num": {"argtypes": [c_double, c_double, c_double, c_double, c_int],"restype": c_void_p,},
				"setRPMPrescribeType_at_num": {"argtypes": [c_int, c_int], "restype": c_void_p},
				"setRPM_at_num": {"argtypes": [c_double, c_int], "restype": c_void_p},
				"setRampupTime": {"argtypes": [c_double], "restype": c_void_p},
				"setTurbinePosition_at_num": {"argtypes": [c_double, c_double, c_double, c_double, c_double, c_double, c_int],"restype": c_void_p,},
				"getTowerBottomLoads_at_num": {"argtypes": [POINTER(c_double * 6), c_int], "restype": c_void_p},
				"initializeSimulation": {"argtypes": None, "restype": c_void_p},
				"advanceTurbineSimulation": {"argtypes": None, "restype": c_bool},
				"advanceController_at_num": {"argtypes": [POINTER(c_double * 5), c_int], "restype": c_void_p},
				"setDebugInfo": {"argtypes": [c_bool], "restype": c_void_p},
				"setUseOpenCl": {"argtypes": [c_bool], "restype": c_void_p},
				"setGranularDebug": {"argtypes": [c_bool, c_bool, c_bool, c_bool, c_bool], "restype": c_void_p},
				"setControlVars_at_num": {"argtypes": [POINTER(c_double * 5), c_int], "restype": c_void_p},
				"getTurbineOperation_at_num": {"argtypes": [POINTER(c_double * 41), c_int], "restype": c_void_p},
				"setPowerLawWind": {"argtypes": [c_double, c_double, c_double, c_double, c_double], "restype": c_void_p},
				"runFullSimulation": {"argtypes": None, "restype": c_void_p},
				"setAutoClearTemp": {"argtypes": [c_bool], "restype": c_void_p},
			}
			
			# Automatically load the library
			self.load_library()
	
		def load_library(self):
			"""Load the shared library and dynamically bind all functions."""
			try:
				self.lib = CDLL(self.lib_path)
				print(f"Successfully loaded library from: {self.lib_path}")
			except Exception as e:
				raise RuntimeError(f"Could not load the library at {self.lib_path}: {e}")
	
			# Bind functions dynamically
			for func_name, config in self.functions.items():
				try:
					func = getattr(self.lib, func_name)
					func.argtypes = config.get("argtypes")
					func.restype = config.get("restype")
					setattr(self, func_name, func)  # Bind the function to the instance
				except AttributeError as e:
					raise RuntimeError(f"Failed to bind function '{func_name}': {e}")
	
			# Call setLibraryPath after the library is loaded
			try:
				self.setLibraryPath(self.lib_path.encode('utf-8'))
				print(f"Library path set to: {self.lib_path}")
			except Exception as e:
				raise RuntimeError(f"Failed to set library path: {e}")
	
		def unload(self):
			
			# Close the QBlade instance if it exists
			try:
				self.closeInstance()
				print("QBlade instance closed.")
			except Exception as e:
				print(f"Warning: Failed to close QBlade instance: {e}")
			
			# Clean up resources and unload the library
			if self.lib:
				del self.lib
				self.lib = None
				print("Library unloaded successfully.")
				
				
				

Matlab Example: Running the QBlade Library
******************************************

This is an example for using the QBlade library within Matlab. It reproduces the Python example above. An object of the class QBladeLibrary, that contains the library interface is created and a simple simulation loop is started.

.. code-block:: matlab
	:linenos:
	:caption: : sampleScript.m
	
	%%
	clear all
	close all 
	clc
	
	% Search the directory below for library files matching the pattern QBlade*.dll or QBlade*.so
	libSearchDirectory = '../';
	sharedLibFiles = dir(fullfile(libSearchDirectory, '*QBlade*'));
	sharedLibFiles = sharedLibFiles(contains({sharedLibFiles.name}, {'.dll', '.so'}));
	
	if isempty(sharedLibFiles)
		fprintf('No matching QBlade*.dll files or QBlade*.so found in the specified directory.');
		return;
	end
		
	% Use the first matching dll file and print out its name
	sharedLibFilePath = fullfile(libSearchDirectory, sharedLibFiles(1).name);
	fprintf('Using DLL file: %s\n', sharedLibFilePath);
	
	% Create an object of the class 'QBladeLibrary' that contains the API
	QBLADE = QBladeLibrary(sharedLibFilePath);
	
	QBLADE.createInstance(1,32);
	
	% Since matlab is unable to display the console output from the library, we
	% store the output in a log file
	QBLADE.setLogFile(fullfile('.', 'LogFile.txt'))
	
	QBLADE.loadProject('NREL_5MW_Sample.qpr')
	
	QBLADE.initializeSimulation()
	
	number_of_timesteps = 500; 
	
	f = waitbar(0,'Initializing Simulation') ;
	
	for i = 1:1:number_of_timesteps
		
		% Advance the simulation
		success = QBLADE.advanceTurbineSimulation();
		
		% Check if the simulation step was successful
		if ~success
			fprintf('Simulation failed at timestep %d. Exiting loop.\n', i);
			break; % Exit the loop
		end
		
		% Assign the c-type double array 'loads' with length [6], initialized with zeros
		loads = libpointer('doublePtr',zeros(6,1));
		% Retrieve the tower loads and store them in the array 'loads' by calling the function getTowerBottomLoads_at_num()
		QBLADE.getTowerBottomLoads_at_num(loads,0);
		% De-referencing the 'loads' pointer and accessing its first value
		loads.Value(1);
		
		% Uncomment the next line to try changing the position of the turbine dynamically
		%QBLADE.setTurbinePosition_at_num(-0.2*i,0,0,0,i*0.1,i*0.1,0)
		
		% Example how to extract a variable by name from the simulation, call as often as needed with different variable names, extracting rpm and time in the lines below
		rpm = QBLADE.getCustomData_at_num('Rotational Speed [rpm]',0,0);
		t = QBLADE.getCustomData_at_num('Time [s]',0,0);  %example how to extract the variable 'Time' by name from the simulation
		AoA = QBLADE.getCustomData_at_num('Angle of Attack at 0.25c (at section) BLD_1 [deg]',0.85,0); %example how to extract the variable 'Angle of Attack' by name at 85% blade length from the simulation 
		
		% Example how to extract a 3 length double array with the x,y,z windspeed components at a global position of x=-50,Y=0,Z=100m from the simulation
		windspeed = libpointer('doublePtr',zeros(3,1)); 
		QBLADE.getWindspeed(-50,0,100,windspeed);
		
		% Assign the c-type double array 'ctr_vars' with length [5], initialized with zeros
		ctr_vars = libpointer('doublePtr',zeros(5,1));
		% Advance the turbine controller and store the controller signals in the array 'ctr_vars'
		QBLADE.advanceController_at_num(ctr_vars,0)
		
		% Pass the controller signals in 'ctr_vars' to the turbine by calling setControlVars_at_num(ctr_vars,0) 
		QBLADE.setControlVars_at_num(ctr_vars,0)
		
		fprintf('Time: %3.2f	Windspeed: %2.2f    Torque: %1.4e	RPM: %2.2f	Pitch: %2.2f    AoA at 85%%: %2.2f\n',t,windspeed.Value(1),ctr_vars.Value(1),rpm,ctr_vars.Value(3),AoA);
		
		waitbar(i/number_of_timesteps,f,'QBlade Simulation Running')
	
	end
	
	close(f)
	
	% Storing the finished simulation in a project as NREL_5MW_Sample_completed, you can open this file to view the results of the simulation inside QBlade's GUI
	QBLADE.storeProject('./NREL_5MW_Sample_completed.qpr')
	
	% Storing the simulation results in QBlade ASCII format in the file NREL_5MW_Sample_results.txt
	QBLADE.exportResults(0,'./','NREL_5MW_Sample_Results','')
	
	% Closing the instance of the shared library, if this fail it can lead to unexpected behavior
	QBLADE.closeInstance()
	
	% Unloading the shared library
	QBLADE.unload()
	
	
	

Matlab Example: Definition of the QBladeLibrary Class
*****************************************************
This code shows how the class *QBladeLibrary* is defined in the Matlab environment. To load the library, a header file *QBladeLibInclude.h* is required that contains the C-type  :ref:`Interface Function Definitions` of the QBlade shared object.

.. code-block:: matlab
	:linenos:
	:caption: : QBladeLibrary.m
	
	classdef QBladeLibrary
		properties
			lib % DLL handle
		end
		
		methods
			% Constructor
			function obj = QBladeLibrary(dllPath)
				% Validate DLL path
				if ~isfile(dllPath)
					error('QBladeLibrary:InvalidPath', 'The specified DLL path does not exist: %s', dllPath);
				end
				
				% Check if the library is already loaded
				if libisloaded('QBLIB')
					disp('Library "QBLIB" is already loaded. Unloading it first...');
					unloadlibrary('QBLIB');
				end
				
				% Attempt to load the library
				try
					obj.lib = loadlibrary(dllPath, 'QBladeLibInclude.h', 'alias', 'QBLIB');
					calllib('QBLIB', 'setLibraryPath', dllPath);
					disp('Library loaded and path set successfully.');
				catch ME
					error('QBladeLibrary:LoadError', 'Failed to load library: %s\n%s', dllPath, ME.message);
				end
			end
			
			% Destructor
			function unload(obj)
				% Unload Library
				if libisloaded('QBLIB') % Check if the library is loaded
					try
						% Unload the library
						unloadlibrary('QBLIB');
						disp('Library unloaded successfully.');
					catch ME
						warning('Error during library unloading: %s', ME.message);
					end
				else
					disp('Library is not loaded. No action taken.');
				end
			end
			
			% Function to call library function
			function createInstance(obj,clDevice,groupSize)
				calllib('QBLIB', 'createInstance', clDevice, groupSize);
			end
			
			function loadProject(obj,str)
				calllib('QBLIB', 'loadProject', str);
			end
			
			function loadSimDefinition(obj,str)
				calllib('QBLIB', 'loadSimDefinition', str);
			end
			
			function setOmpNumThreads(obj,num)
				calllib('QBLIB', 'setOmpNumThreads', num);
			end
			
			function initializeSimulation(obj)
				calllib('QBLIB', 'initializeSimulation');
			end
			
			function runFullSimulation(obj)
				calllib('QBLIB', 'runFullSimulation');
			end
			
			function advanceController_at_num(obj,vars,num)
				calllib('QBLIB', 'advanceController_at_num', vars, num);
			end
			
			function success = advanceTurbineSimulation(obj)
				success = calllib('QBLIB', 'advanceTurbineSimulation');
			end
			
			function storeProject(obj,str)
				calllib('QBLIB', 'storeProject',str);
			end
			
			function exportResults(obj, type, filepath, filename, filter)
				calllib('QBLIB', 'exportResults',type, filepath, filename, filter);
			end
			
			function closeInstance(obj)
				calllib('QBLIB', 'closeInstance');
			end
			
			function setLogFile(obj,str)
				calllib('QBLIB', 'setLogFile',str);
			end
			
			function loadTurbulentWindBinary(obj,str)
				calllib('QBLIB', 'loadTurbulentWindBinary', str);
			end
			
			function addTurbulentWind(obj,windspeed, refheight, hubheight, dimensions, gridPoints, length, dT, turbulenceClass, turbulenceType, seed, vertInf, horInf, removeFiles)
				calllib('QBLIB', 'addTurbulentWind', windspeed, refheight, hubheight, dimensions, gridPoints, length, dT, turbulenceClass, turbulenceType, seed, vertInf, horInf, removeFiles);
			end
			
			function setPowerLawWind(obj,windspeed,horAngle,vertAngle,shearExponent,referenceHeight)
				calllib('QBLIB', 'setPowerLawWind',windspeed,horAngle,vertAngle,shearExponent,referenceHeight);
			end
			
			function setDebugInfo(obj,isDebug)
				calllib('QBLIB', 'setDebugInfo', isDebug);
			end
			
			function setUseOpenCl(obj,isOpenCl)
				calllib('QBLIB', 'setUseOpenCl', isOpenCl);
			end
			
			function setGranularDebug(obj,dStr,dSim,dTurb,dCont,dSer)
				calllib('QBLIB', 'setGranularDebug',dStr,dSim,dTurb,dCont,dSer);
			end
			
			function setTimestepSize(obj,timestep)
				calllib('QBLIB', 'setTimestepSize', timestep);
			end
			
			function setRPMPrescribeType_at_num(obj,type,num)
				calllib('QBLIB', 'setRPMPrescribeType_at_num',type,num);
			end
			
			function setRPM_at_num(obj,rpm,num)
				calllib('QBLIB', 'setRPM_at_num',rpm,num);
			end
			
			function setRampupTime(obj,time)
				calllib('QBLIB', 'setRampupTime',time);
			end
			
			function setInitialConditions_at_num(obj,yaw,pitch,azimuth,rpm,num)
				calllib('QBLIB', 'setInitialConditions_at_num',yaw,pitch,azimuth,rpm,num);
			end
			
			function setTurbinePosition_at_num(obj,x,y,z,xrot,yrot,zrot,num)
				calllib('QBLIB', 'setTurbinePosition_at_num',x,y,z,xrot,yrot,zrot,num);
			end
			
			function setControlVars_at_num(obj,vars,num)
				calllib('QBLIB', 'setControlVars_at_num',vars,num);
			end
			
			function setExternalAction(obj,action,id,val,pos,dir,isLocal,num)
				calllib('QBLIB', 'setExternalAction',action,id,val,pos,dir,isLocal,num);
			end
			
			function setMooringStiffness(obj,EA,id,num)
				calllib('QBLIB', 'setMooringStiffness',EA,neutralStrain,id,num);
			end
			
			function getWindspeed(obj,x,y,z,velocity)
				calllib('QBLIB', 'getWindspeed',x,y,z,velocity);
			end
			
			function getWindspeedArray(obj,posx,posy,posz,velx,vely,velz,arraySize)
				calllib('QBLIB', 'getWindspeedArray',posx,posy,posz,velx,vely,velz,arraySize);
			end
			
			function getTowerBottomLoads_at_num(obj,loads,num)
				calllib('QBLIB', 'getTowerBottomLoads_at_num',loads,num);
			end
			
			function getTurbineOperation_at_num(obj,vars,num)
				calllib('QBLIB', 'getTurbineOperation_at_num',vars,num);
			end
			
			function output = getCustomData_at_num(obj,var,i,j)
				output = calllib('QBLIB','getCustomData_at_num',var,i,j);
			end
			
			function output = getCustomSimulationTimeData(obj,var)
				output = calllib('QBLIB','getCustomSimulationTimeData',var);
			end
			
			function output = setAutoClearTemp(obj,var)
				output = calllib('QBLIB','setAutoClearTemp',var);
			end
			
		end
	end
	
	
	

