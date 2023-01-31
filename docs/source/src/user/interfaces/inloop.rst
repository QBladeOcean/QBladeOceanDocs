Software in Loop (SIL) Overview
*******************************
   
The Software in Loop interface in QBlade provides an easy way of controlling the whole simulation loop of a wind turbine and enable cosimulation within other software frameworks or scripting languages, such as Python or Matlab. To enable this functionality QBlade is compiled as a Dynamic Link Library (.dll, Windows) or as a Shared Object (.so, Unix) and the relevant functionality is exported into an interface.

Through the different functions that are exported the user can explicitly import QBlade projects (.qpr) or Simulation Definition Files (.sim) and then progress the simulation incrementally in time by calling the :code:`advanceTurbineSimulation()` function. At every timestep it is possible to inquire any variable of the simulation and control various aspects of the simulation in response, such as changing the inflow conditions, changing the position and orientation of the turbine or controlling the various control actuators (pitch, yaw, generator torque) of the wind turbine. A possible application for the SIL interface is a cosimulation, where the turbine floater can be modeled within a specialized software that is coupled with QBlade through force/position intercommunication. Instead of modelling the floater, the cosimulation could also model the drivetrain, controller or generator in a more sphisticated way. Another application is controller development, where the controller can run in a scripting language (such as Simulink), receiving custom signals from the simulation and controlling the turbine actuators in response. When running a multi-turbine simulation within the SIL interface the user may control each simulated turbine individually, enabling the modeling of global wind park controllers.

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

To test the SIL interface in Python you can simply start the python script :code:`sampleScript.py`, which you find in the folder :code:`\PythonInterface` of the QBlade directory. This script imports the QBlade library, sets up a simulation by importing a QBlade project file (.qpr) and then runs a simulation loop while printing out some results and finally saving the finished simulation as a new project file. This sample is just meant as a quick demo on how to interface with QBlade in Python and does not serve any other particular purpose. Adapt as needed. 

Details on the sample script: :ref:`Sample Script Running QBlade's SIL Library with Python`

Details on the script that loads QBlade into Python: :ref:`Sample Script Importing QBlade's SIL Library into Python`. 

	
Interface Function Definitions
******************************

.. code-block:: c

	#all variables and return values are c data types

	void createInstance(int clDevice = 0, int groupSize = 32)
	void loadProject(char *str)
	void loadSimDefinition(char *str)
	void initializeSimulation()
	void runFullSimulation()

	void advanceController_at_num(double *vars, int num = 0)
	void advanceTurbineSimulation()

	void storeProject(char *str)
	void closeInstance()
	
	void loadTurbulentWindBinary(char *str)
	void addTurbulentWind(double windspeed, double refheight, double hubheight, double dimensions, int gridPoints, double length, double dT, char *turbulenceClass, char *turbulenceType, int seed, double vertInf, double horInf, bool removeFiles = false)

	void setPowerLawWind(double windspeed, double horAngle, double vertAngle, double shearExponent, double referenceHeight)
	void setDebugInfo(bool isDebug)
	void setLibraryPath(char *str)
	void setTimestepSize(double timestep)
	void setRPMPrescribeType_at_num(int type, int num = 0)
	void setRampupTime(double time)
	void setInitialConditions_at_num(double yaw, double pitch, double azimuth, double rpm, int num = 0)
	void setTurbinePosition_at_num(double x, double y, double z, double rotx, double roty, double rotz, int num = 0)
	void setControlVars_at_num(double *vars, int num = 0)
	
	void getWindspeed(double x, double y, double z, double *velocity)
	void getTowerBottomLoads_at_num(double *loads, int num)
	void getTurbineOperation_at_num(double *vars, int num = 0)
	double getCustomData_at_num(char *str, double pos = 0, int num = 0)


Interface Function Documentation
********************************

In the following, the functionality that is exported from the QBlade dll or shared object is described and the function arguments and return types are given. ALl functions with the appendix **_at_num** affect the turbine specified by the argument **num** - this has only an effect for multi turbine simulations.

:code:`void createInstance(int clDevice = 0, int groupSize = 32)`
	
	This function creates a new instance of QBlade. The OpenCL device and the OpenCL group-size can both be specified in the arguments. **Calling this function is mandatory!** 
	
:code:`void loadProject(char *str)`
	
	This function loads a qblade (.qpr) project into the QBlade instance. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.

:code:`void loadSimDefinition(char *str)`
	
	This function loads a simulation definition (.sim) file into the QBlade instance. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.

:code:`void initializeSimulation()`
	
	This function initializes the simulation, e.g. the simulation is reset and structural ramp-up is carried out.
	
:code:`void runFullSimulation()`
	
	This function runs all timesteps for all turbines of the simulation as defined in the simulation object. This is equivalent to pressing the *Start Simulation* button in QBlade`s GUI. This function needs to be called after :code:`void initializeSimulation()`. When calling this function it is not possible to *interact* with the simulation before it is finished. To interact with the simulation you need to create your own simulation loop and call the functions :code:`void advanceController_at_num()` and :code:`void advanceTurbineSimulation()` at every timestep.


:code:`void advanceController_at_num(double *vars, int num = 0)`
	
	This function advancess the controller dll of the selected turbine (argument *num*). The controller outputs are automatically applied to the turbine actuators and to the generator. The controller ouputs are also returned in the *vars* array:
	
	* vars[0] = generator torque [Nm]
	* vars[1] = yaw angle [deg]
	* vars[2] = pitch blade 1 [deg]
	* vars[3] = pitch blade 2 [deg]
	* vars[4] = pitch blade 3 [deg]

:code:`void advanceTurbineSimulation()`
	
	This function advances the turbine simulation for all turbines and finishes the timestep.

:code:`void storeProject(char *str)`
	
	This functions stores a project file. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.

:code:`void closeInstance()`

	This function closes the instance of QBlade and frees the memory.
	
:code:`void loadTurbulentWindBinary(char *str)`
	
	This function allows to load a turbulent windfield that is stored in binary format. The file location has to be passed as a *char pointer*. File names can be passed as absolute or as relative paths.
	
:code:`void addTurbulentWind(double windspeed, double refheight, double hubheight,`
:code:`double dimensions, int gridPoints,double length, double dT, char *turbulenceClass,`
:code:`char *turbulenceType, int seed, double vertInf, double horInf, bool removeFiles = false)`	

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


:code:`void setPowerLawWind(double windspeed, double horAngle,`
:code:`double vertAngle, double shearExponent, double referenceHeight)`

	This function can be called before or at any time after the simulation has been initialized with :code:`initializeSimulation()` to statically or dynamically change the inflow conditions. It defines a power law wind profile (https://en.wikipedia.org/wiki/Wind_profile_power_law) and its inflow direction. The arguments for this function are:
	
	* windspeed: constant windspeed in m/s [m/s]
	* horAngle: the horizontal inflow angle in degrees [deg]
	* vertAngle: the vertical inflow angle in degrees [deg]
	* shearExponent: this is the exponent for the power law boundary layer profile, if this is set to 0 the windspeed is constant with height [-]
	* referenceHeight: this is the height at which the velocity in the boundary layer is the defined windspeed, usually set to the hubheight [m]
	* exemplary call: addTurbulentWind(12,115,115,220,20,60,0.1,"A","NTM",1000000,0,0);


:code:`void setDebugInfo(bool isDebug)`
	
	This function enables the debug output if set to true.

:code:`void setLibraryPath(char *atr)`
	
	This function sets the location of the QBlade dll or shared object so that the QBlade instance knows about its location. **Calling this function is mandatory** so that the QBlade instance knows about the location of associated binaries (XFoil, TurbSim) and possibly license files.

:code:`void setTimestepSize(double timestep)`
	
	This function can be used to set the timestep size (in [s]) if the user wants to change this value from the project or simulation definition file. It needs to be called before :code:`initializeSimulation()`.

:code:`void setRPMPrescribeType_at_num(int type, int num = 0)`
	
	This function can be used to change the rpm prescribe type. It needs to be called before :code:`initializeSimulation()`.
	
	* 0 - RPM prescribed during ramp-up only
	* 1 - RPM prescribed for the whole simulation
	* 3 - no prescribed RPM


:code:`void setRampupTime(double time)`
	
	This function can be used to change the ramp-up time from the value specified in the project or simulation file, call before :code:`initializeSimulation()`.


:code:`void setInitialConditions_at_num(double yaw, double pitch, double azimuth, double rpm, int num = 0)`
	
	This function may be used to set the turbine initial yaw [deg], collective pitch [deg], azimuthal angle [deg] and initial rotSpeed [rpm] to a value different than specified in the QBlade project or simulation input file. It needs to be called before :code:`initializeSimulation()`.

:code:`void setTurbinePosition_at_num(double x, double y, double z, double rotx, double roty, double rotz, int num = 0)`
	
	This function sets the turbine tower bottom x, y and z position [m], and xrot, yrot zrot rotation [deg]. It can be called before :code:`initializeSimulation()` if the turbine position should be offset initially or during the simulation loop if it should be changed dynamically, for example during cosimulation with a hydrodynamics software that models the floater.

:code:`void setControlVars_at_num(double *vars, int num = 0)`
	
	This function applies the control actions of the selected turbine (argument *num*) for torque, pitch and yaw angle. If it is called after the function :code:`advanceController()` the control actions from the controller can be overwritten (or modified). The following data needs to be passed in the array *vars*.
	
	* vars[0] = generator torque [Nm];
	* vars[1] = yaw angle [deg];
	* vars[2] = pitch blade 1 [deg];
	* vars[3] = pitch blade 2 [deg];
	* vars[4] = pitch blade 3 [deg];


:code:`void getWindspeed(double x, double y, double z, double *velocity)`
	
	This function can be called to get the current windspeed at the chosen position (x,y,z), returns the windspeed vector in the *double pointer* velocity.
	
	* velocity[0] = x-component [m/s];
	* velocity[1] = y-component [m/s];
	* velocity[2] = z-component [m/s];

:code:`void getTowerBottomLoads_at_num(double *loads, int num)`
	
	This function can be used to obtain the loads at the bottom of the tower. The main purpose of this is to be used in conjunction with the :code:`setTurbinePosition_at_num()` function for force/position cosimilation with a hydrodynamics solver that is modeling the floater.

:code:`void getTurbineOperation_at_num(double *vars, int num = 0)`
	
	This function returns typically useful turbine operational parameters of the selected turbine (argument *num*). The data is returned in the array *vars* which has the following content:
	
	* vars[0] = rotational speed [rad/s]
	* vars[1] = power [W]
	* vars[2] = Abs HH wind velocity [m/s]
	* vars[3] = yaw angle [deg]
	* vars[4] = pitch blade 1 [deg]
	* vars[5] = pitch blade 2 [deg]
	* vars[6] = pitch blade 3 [deg]
	* vars[7] = oop blade root bending moment blade 1 [Nm]
	* vars[8] = oop blade root bending moment blade 2 [Nm]
	* vars[9] = oop blade root bending moment blade 3 [Nm]
	* vars[10] = ip blade root bending moment blade 1 [Nm]
	* vars[11] = ip blade root bending moment blade 2 [Nm]
	* vars[12] = ip blade root bending moment blade 3 [Nm]
	* vars[13] = tor blade root bending moment blade 1 [Nm]
	* vars[14] = tor blade root bending moment blade 2 [Nm]
	* vars[15] = tor blade root bending moment blade 3 [Nm]
	* vars[16] = oop tip deflection blade 1 [m]
	* vars[17] = oop tip deflection blade 2 [m]
	* vars[18] = oop tip deflection blade 3 [m]
	* vars[19] = ip tip deflection blade 1 [m]
	* vars[20] = ip tip deflection blade 2 [m]
	* vars[21] = ip tip deflection blade 3 [m]
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
	
	This function can be used to access the current value from an arbitrary simulation variable in QBlade. Specify the data name as is would appear in any QBlade graph as a *char pointer*. If you are requesting an aerodynamic 'at section' cariable, for instance 'Angle of Attack at 0.25c (at section) Blade 1 [deg]' you can specify the normalized position along the blade length using the 'pos' variable. As an example, to get the AoA at 85% blade length from turbine 0, you would call the function the following way: :code:`getCustomData_at_num("Angle of Attack at 0.25c (at section) Blade 1 [deg]", 0.85,0)



Sample Script Running QBlade's SIL Library with Python
******************************************************
The following code example (*sampleScript.py*) is an example for a light weight Python script that utilizes the QBlade SIL interface. There are many ways to improve this, e.g. the library could be loaded into multiple separate processes for parallelization and sophisticated algorithms could be implemented instead of using a standard controller. This exemplary script only uses a small amount of the functionality that is exported by the QBlade library for purely illustrative purposes. 

In this Python example script the library is loaded by calling the script *QBladeLIBImport.py*, which handles the library import. After *QBladeLIBImport.py* has been imported (:code:`import QBladeLIBImport as QBLIB`) and the QBlade library has been loaded :code:`QBLIB.loadLibrary("./QBladeCE_2.0.5.2.dll")` any function of the QBlade library can be accessed by calling :code:`QBLIB.function_XYZ()`. All lines of code that are needed to load the QBlade library into python are highlighted in the example below.

After the QBlade library has been loaded a simulation object is imported and a simulation is started over 500 timesteps. During the simulation loop different data is obtained from the turbine simulation. The turbine controller that is defined in the simulation object is advanced and its signals are passed to the turbine actuators. After the simulation loop has finished the simulation is stored into a project file, for later inspection, and the library is unloaded from python.


.. code-block:: python
	:linenos:
	:caption: : sampleScript.py
	:emphasize-lines: 1, 2, 5
	
	from ctypes import *
	import QBladeLibImport as QBLIB

	#loading the QBlade library from the folder below the location of sampleScript.py, if calling this script not from the script folder directly you need to use an absolute path instead!
	QBLIB.loadLibrary("../QBladeCE_2.0.5.2.dll")    

	#creation of a QBlade instance from the library
	QBLIB.createInstance(1,32)

	#loading a project or sim-file, in this case the DTU_10MW_Demo project or simulation definition file
	#QBLIB.loadSimDefinition(b"./DTU_10MW_Demo.sim") #uncomment this line to load a simulation definition file
	QBLIB.loadProject(b"./NREL_5MW_Sample.qpr") 

	#initializing the sim and ramp-up phase, call before starting the simulation loop
	QBLIB.initializeSimulation()

	#we will run the simulation for 500 steps before storing the results
	number_of_timesteps = 500

	#start of the simulation loop
	for i in range(number_of_timesteps):

		#assign the c-type double array 'loads' with length [6], initialized with zeros
		loads = (c_double * 6)(0) 
		#retrieve the tower loads and store the in the array 'loads' by calling the function getTowerBottomLoads_at_num()
		QBLIB.getTowerBottomLoads_at_num(loads,0)
		
		#uncomment the next line to try changing the position of the turbine dynamically
		#QBLIB.setTurbinePosition_at_num(-0.2*i,0,0,0,i*0.1,i*0.1,0) 
		
		#example how to extract a variable by name from the simulation, call as often as needed with different variable names, extracting rpm and time in the lines below
		rpm = QBLIB.getCustomData_at_num(b"Rotational Speed [rpm]",0,0) 
		time = QBLIB.getCustomData_at_num(b"Time [s]",0,0) #example how to extract the variable 'Time' by name from the simulation
		AoA = QBLIB.getCustomData_at_num(b"Angle of Attack at 0.25c (at section) Blade 1 [deg]",0.85,0) #example how to extract the variable 'Angle of Attack' by name at 85% blade length from the simulation 
		
		#example how to extract a 3 length double array with the x,y,z windspeed components at a global position of x=-50,Y=0,Z=100m from the simulation
		windspeed = (c_double * 3)(0) 
		QBLIB.getWindspeed(-50,0,100,windspeed)

		#assign the c-type double array 'ctr_vars' with length [6], initialized with zeros
		ctr_vars = (c_double * 5)(0); 
		#advance the turbine controller and store the controller signals in the array 'ctr_vars'
		QBLIB.advanceController_at_num(ctr_vars,0)
		
		#passthe controller signals in 'ctr_vars' to the turbine by calling setControlVars_at_num(ctr_vars,0) 
		QBLIB.setControlVars_at_num(ctr_vars,0) 
		
		#print out a few of the recorded data, in this case torque, tower bottom force along z (weight force) and rpm
		print("Time:","{:3.2f}".format(time),"   Windspeed:","{:2.2f}".format(windspeed[0]),"  Torque:","{:1.4e}".format(ctr_vars[0]),"    RPM:","{:2.2f}".format(rpm),"   Pitch:","{:2.2f}".format(ctr_vars[2]),"   AoA at 85%:","{:2.2f}".format(AoA))

		#advance the simulation
		QBLIB.advanceTurbineSimulation() 

	#the simulation loop ends here after all 'number_of_timesteps have been evaluated
		
	#storing the finished simulation in a project as DTU_10MW_Demo_finished.qpr, you can open this file to view the results of the simulation inside QBlade's GUI
	QBLIB.storeProject(b"./NREL_5MW_Sample_completed.qpr")

	#closing the QBlade instance to free memory
	QBLIB.closeInstance()

	#unloading the QBlade library
	del QBLIB.QB_LIB 
	
Sample Script Importing QBlade's SIL Library into Python
********************************************************

The script *QBladeLibImport.py* which loads the QBlade library into Python and imports its functionality is shown below. Since the QBlade library is loaded upon calling the function :code:`loadLibrary()` defined in the script, the imported library functions are defined as *global*, to make them available outside of the function scope of :code:`loadLibrary()`. This script is imported into the 

.. code-block:: python
	:linenos:
	:caption: : QBladeLibImport.py

	from ctypes import *

	#this is the first function that is called in sampleScript.py to load the QBlade library 
	def loadLibrary(shared_lib_path):

		global QB_LIB
		
		try:
			#loading the library into python here, using ctypes
			QB_LIB = CDLL(shared_lib_path)
			print("Successfully loaded ", QB_LIB)
		except Exception as e:
			print(e)
			
		#setting the shared_lib_path, so that the library knows about its location!
		QB_LIB.setLibraryPath(shared_lib_path.encode('utf-8')) 

		#the imported functions are defined below
		 
		global loadProject
		loadProject = QB_LIB.loadProject
		loadProject.argtype = c_char_p
		loadProject.restype = c_void_p

		global loadSimDefinition
		loadSimDefinition = QB_LIB.loadSimDefinition
		loadSimDefinition.argtype = c_char_p
		loadSimDefinition.restype = c_void_p

		global getCustomData_at_num
		getCustomData_at_num = QB_LIB.getCustomData_at_num
		getCustomData_at_num.argtypes = [c_char_p, c_double, c_int]
		getCustomData_at_num.restype = c_double

		global getWindspeed
		getWindspeed = QB_LIB.getWindspeed
		getWindspeed.argtypes = [c_double, c_double, c_double, c_double * 3]
		getWindspeed.restype = c_void_p

		global storeProject
		storeProject = QB_LIB.storeProject
		storeProject.argtype = c_char_p
		storeProject.restype = c_void_p

		global setLibraryPath
		setLibraryPath = QB_LIB.createInstance
		setLibraryPath.argtype = c_char_p
		setLibraryPath.restype = c_void_p

		global createInstance
		createInstance = QB_LIB.createInstance
		createInstance.argtypes = [c_int, c_int]
		createInstance.restype = c_void_p

		global closeInstance
		closeInstance = QB_LIB.closeInstance
		closeInstance.restype = c_void_p

		global addTurbulentWind
		addTurbulentWind = QB_LIB.addTurbulentWind
		addTurbulentWind.argtypes = [c_double, c_double, c_double, c_double, c_int, c_double, c_double, c_char_p, c_char_p, c_int, c_double, c_double, c_bool]
		addTurbulentWind.restype = c_void_p

		global loadTurbulentWindBinary
		loadTurbulentWindBinary = QB_LIB.loadTurbulentWindBinary
		loadTurbulentWindBinary.argtype = c_char_p
		loadTurbulentWindBinary.restype = c_void_p

		global setTimestepSize
		setTimestepSize = QB_LIB.setTimestepSize
		setTimestepSize.argtype = c_double
		setTimestepSize.restype = c_void_p

		global setInitialConditions_at_num
		setInitialConditions_at_num = QB_LIB.setInitialConditions_at_num
		setInitialConditions_at_num.argtypes = [c_double, c_double, c_double, c_double, c_int]
		setInitialConditions_at_num.restype = c_void_p

		global setRPMPrescribeType_at_num
		setRPMPrescribeType_at_num = QB_LIB.setRPMPrescribeType_at_num
		setRPMPrescribeType_at_num.argtypes = [c_int, c_int]
		setRPMPrescribeType_at_num.restype = c_void_p

		global setRampupTime
		setRampupTime = QB_LIB.setRampupTime
		setRampupTime.argtype = c_double
		setRampupTime.restype = c_void_p

		global setTurbinePosition_at_num
		setTurbinePosition_at_num = QB_LIB.setTurbinePosition_at_num
		setTurbinePosition_at_num.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int]
		setTurbinePosition_at_num.restype = c_void_p

		global getTowerBottomLoads_at_num
		getTowerBottomLoads_at_num = QB_LIB.getTowerBottomLoads_at_num
		getTowerBottomLoads_at_num.argtypes = [c_double * 6, c_int]
		getTowerBottomLoads_at_num.restype = c_void_p

		global initializeSimulation
		initializeSimulation = QB_LIB.initializeSimulation
		initializeSimulation.restype = c_void_p

		global advanceTurbineSimulation
		advanceTurbineSimulation = QB_LIB.advanceTurbineSimulation
		advanceTurbineSimulation.restype = c_void_p

		global advanceController_at_num
		advanceController_at_num = QB_LIB.advanceController_at_num
		advanceController_at_num.argtypes = [c_double * 5, c_int]
		advanceController_at_num.restype = c_void_p

		global setDebugInfo
		setDebugInfo = QB_LIB.setDebugInfo
		setDebugInfo.argtype = c_bool
		setDebugInfo.restype = c_void_p

		global setControlVars_at_num
		setControlVars_at_num = QB_LIB.setControlVars_at_num
		setControlVars_at_num.argtypes = [c_double * 5, c_int]
		setControlVars_at_num.restype = c_void_p

		global getTurbineOperation_at_num
		getTurbineOperation_at_num = QB_LIB.getTurbineOperation_at_num
		getTurbineOperation_at_num.argtypes = [c_double * 41, c_int]
		getTurbineOperation_at_num.restype = c_void_p

		global setPowerLawWind
		setPowerLawWind = QB_LIB.setPowerLawWind
		setPowerLawWind.argtypes = [c_double, c_double, c_double, c_double, c_double]
		setPowerLawWind.restype = c_void_p
		
		global runFullSimulation
		runFullSimulation = QB_LIB.runFullSimulation
		runFullSimulation.restype = c_void_p