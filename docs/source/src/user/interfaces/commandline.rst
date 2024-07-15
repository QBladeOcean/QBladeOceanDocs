CLI Overview
************

.. admonition:: QBlade-EE

   This feature is only available in the Enterprise Edition of QBlade.
   
QBlade-EE can also be executed in a command line interface (CLI). The main purpose of QBlade's CLI is to batch-process large sets of simulations in parallel while reducing any computational overhead from the GUI. When processing large sets of simulations a single instance of QBlade will act as the *thread manager*, in charge of creating new QBlade instances for each simulation that is evaluated and queuing these simulations over all available threads. This approach has the advantage of being highly robust, as if one simulation crashes for any reason it wont affect any other simulation and the batch run will still complete without the need for user intervention. This section details the functionality of the QBlade CLI and its options. 

To start QBlade in CLI mode simply call QBlade's executable from the command line while adding the parameter :code:`-cli` to indicate that instead of starting QBlade in GUI mode it will be operated in CLI mode. 

:code:`QBladeEE -cli`
	
If the command above is executed, QBlade prints out the following information on the screen::

	!!!!! Welcome to QBlade EE v2.0.5.1_alpha windows Command Line Interface (CLI) !!!!!

	*************************************** OpenCL *********************************************
	Available OpenCL Devices:

	-d0 : to use CPU: OpenMp (default)
	-d1 : to use GPU: OpenCL 2.0 AMD-APP (3380.6) gfx1030
	-d2 : to use GPU: OpenCL 3.0 NEO Intel(R) UHD Graphics 770

	Specify the OpenCL device by passing -dXX to the CLI, where -d0 is the default
	Specify the OpenCL group size by passing -gXX to the CLI, where -g32 is the default
	--------------------------------------------------------------------------------------------

	************************************ Multi Threading ***************************************
	Available CPU Cores:

	- CPU cores found: 20

	Set the parallel threads by passing -tXX to the CLI, where -t1 is the default
	--------------------------------------------------------------------------------------------

	Missing arguments - type 'QBlade -cli help' for a list of options!
	
Since no options have been passed in this example of executing the CLI, the program is exiting without any actions. However, some useful information has already been printed on screen. This includes the **OpenCL Devices** as they have been detected by QBlade and the total number of **CPU Cores** that could be found on the machine. This information is useful when evaluating large sets of simulations to inform QBlade which OpenCL device to use and how many simulations should be evaluated in parallel.
	
The available functionality of the QBlade CLI can be viewed by adding :code:`help` (note that the minus sign is not required when adding the :code:`help` command, while it is mandatory when adding :code:`-cli`).

:code:`QBladeEE -cli help`
	
This command prints out an overview of all CLI functionality::

	**************************************** Help **********************************************
	
	!! CLI options can be given in any order !!
	!! Multiple files and/or directories can be specified with a single CLI call!!
	!! All directories must be input as an ABSOLUTE path !!
	
	List of CLI Options:
	
	help                      - list CLI options
	-dX                       - choose compute device X for wake calculations (X must be an integer)
	-gX                       - choose opencl group size X for wake calculations (X must be an integer)
	-tX                       - choose the number X of paraleel simulation threads used during batch evaluation (X must be an integer)
	-oX                       - choose the number X of OMP threads used in each of the parallel simulation threads (X must be an integer)
	\directory\simulation.sim - evaluates the simulation definition '\directory\simulation.sim' and save it as *.qpr1
	\directory\project.qpr    - evaluates the project '\directory\project.qpr' and save it as .qpr1
	\directory                - sets the WORKING_DIR, multiple working directories may be defined
	all_sim                   - batch evaluate all .sim files in all WORKING_DIR(s) and saves them as *.qpr1
	all_qpr                   - batch evaluate all .qpr files in all WORKING_DIR(s) and save them as *.qpr1
	no_save                   - simulations are not stored after .sim or .qpr files or cutplanes (using post_cut) have been evaluated
	remove_wind               - remove the windfield file (.bts) after a simulation definition (.sim) is evaluated
	skip                      - skip evaluation of .qpr and .sim files if a .qpr1 file exists or .sim files that were already exported
	exp_h2bin                 - adds HAWC2BINARY format to auto-export and post-export formats
	exp_h2ascii               - adds HAWC2ASCII format to auto-export and post-export formats (only if HAWC2BINARY is not exported)
	exp_ascii                 - adds ASCII format to auto-export and post-export formats
	exp_fastbin               - adds FAST BINARY format to auto-export and post-export formats
	exp_cut_txt               - adds cut-plane txt format to auto-export and post-export formats
	exp_cut_vtu               - adds cut-plane vtu format to auto-export and post-export formats
	post_exp                  - export results and cut-planes from all FINISHED .qpr and .qpr1 files in all WORKING_DIR(s)
	flt=\directory\filter.*   - sets a filter file for the generation of all auto-export and post-export formats
	dlc=\directory\dlc.*      - create simulations from the dlc table (dlc.*). requires a WORKING_DIR in which the simulations are created
	--------------------------------------------------------------------------------------------
	
CLI Functionality
*****************

In this section the different CLI options are briefly explained.

:code:`-d`

	This parameter is used to specify on which OpenCL device QBlade should be executed. The default value is 0. To execute on the OpenCL device 1, the parameter would be :code:`-d1`.

:code:`-g`

	This parameter specifies the OpenCL work-group size, which has a GPU dependent impact on the OpenCL performance. The work-group size should always be a power of 2. The default value is 32. To specify a work-group size of 64 you would pass the parameter :code:`-g64`.  

:code:`-t`

	This parameter sets how many parallel instances of QBlade should be started when evaluating a batch of simulations. The default values is 1. To specify 12 parallel threads you would pass the parameter :code:`-t12`.
	
:code:`-o`

	This parameter sets how many openMp threads should be used for each parallel instance of QB. This is specifically important to fine tune the performance of QB instances in a cloud-computing environment.
	
:code:`c:\directory\simulation.sim`
	
	Passing the absolute location of a :ref:`Simulation Definition ASCII File` (\*.sim) as one of the parameters adds this simulation definition to the list of simulations that will be evaluated. Multiple simulation definitions may be added during a single CLI call. Finished simulation definitions are stored as **.qpr1**, to indicate that these are project files that have already been evaluated. Should a simulation fail for any reason the associated project is stored as ***.qpre** instead, to indicate that this is a problematic simulation.

:code:`c:\directory\project.qpr`

	Passing the absolute location of a QBlade Project File (\*.qpr) adds all simulation definitions within this project to the list of simulations that will be evaluated. Multiple project files may be added during a single CLI call. Finished project files are stored as ***.qpr1**,  to indicate that these are project files that have already been evaluated. Should a simulation fail for any reason the associated project is stored as ***.qpre** instead, to indicate that this is a problematic simulation.

:code:`c:\directory\ `
	
	Passing the absolute path of any directory adds this directory to the list of working directories (**WORKING_DIR**). Multiple directories may be added during a single CLI call.

:code:`all_sim`
	
	Adding the parameter :code:`all_sim` causes QBlade to add **all \*.sim files from all WORKING_DIR(s)** to the list of simulations that will be evaluated.

:code:`all_qpr`
	
	Adding the parameter :code:`all_qpr` causes QBlade to add **all \*.qpr files from to all WORKING_DIR(s)** to the list of projects that will be evaluated.

:code:`no_save`
	
	The parameter :code:`no_save` prevents QBlade from automatically storing finished simulations as **\*.qpr1** or **\*.qpr2** files. Sometimes those files are not explicitly needed, for example if results are automatically exported and the user wants to reduce disk memory consumption during very large batch runs.

:code:`remove_wind`
	
	The parameter :code:`remove_wind` removes the binary windfield files (\*.bts), that may be automatically generated when a simulation definition file (\*.sim) is evaluated. This can be useful to reduce disk memory usage during very large batch runs.

:code:`skip`
	
	Adding the parameter :code:`skip` causes QBlade to skip the evaluation of a simulation (\*.sim) or project (\*.qpr) file if an assocated finished project file (\*.qpr1) already exists, or if the results from this simulation have already been exported previously. When using *skip* during post_exp files are only exported if their filename does not exist yet.

:code:`exp_h2bin`
	
	The parameter :code:`exp_h2bin` adds the HAWC2 binary format to the list of export formats. Whenever a simulation is completed the results of this simulation will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.
	
:code:`exp_h2ascii`
	
	The parameter :code:`exp_h2ascii` adds the HAWC2 ASCII format to the list of export formats. Whenever a simulation is completed the results of this simulation will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.

:code:`exp_ascii`
	
	The parameter :code:`exp_ascii` adds the ASCII format to the list of export formats. Whenever a simulation is completed the results of this simulation will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.

:code:`exp_fastbin`
	
	The parameter :code:èxp_fastbin`adds the OpenFAST binary format (.outb) to the list of export formats. Whenever a simulation is completed the results of this simulation will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.

:code:`\directory\filter.flt`
	
	Passing the absolute location of a result filter file. All export files that will be generated contain only the variables defined in the filter file. Each line in the filter file specifies a single variable name. The variable names in the filter file need to correspond to the exact name of the variable as it is shown in QBlade's graphs.

:code:`exp_cut_txt`
	
	The parameter :code:`exp_cut_txt` adds the cut-plane TXT format to the list of export formats. Whenever a cut-plane is evaluated, its velocity field will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.

:code:`exp_cut_vtu`
	
	The parameter :code:`exp_cut_vtu` adds the cut-plane VTU format to the list of export formats. Whenever a cut-plane is evaluated, its velocity field will be automatically exported for all specified formats. As default no format is specified, so auto-export if disabled.

:code:`post_exp`
	
	The parameter :code:`post_exp` causes QBlade to automatically export the results from all finished project files (\*.qpr, \*.qpr1, \*.qpr2) in all WORKING_DIR(s). This parameter only affects simulations that are already finished when the CLI call is executed and not simulations that are being evaluated during the CLI call. Simulations are exported in all formats that have been added to the export format list.

:code:`dlc=\directory\dlc.*`
	
	This call allows to create simulations from a dlc table definition. It requires the filename of the dlc definition. Furthermore, a WORKING_DIR in which the simulations are created is required.

:code:`dlc=\directory\dlc.*`
	
	This sets a filter file that is applied during the generation of all auto-export and post-export files.

Sample CLI Call to Start a Batch Run
************************************

The following call is an example for a CLI call of QBlade to evaluate and automatically export a batch of simulation definition files located in the folder c:\\simulations\\.

	:code:`QBladeEE -cli -d1 -g64 -t12 c:\simulations\ all_sim exp_h2bin remove_wind skip`
	
After this CLI call QBlade will evaluate all simulation definitions (:code:`all_sim`) located in c:\\simulations\\ over 12 parallel threads (:code:`-t12`). OpenCL device 1 will be used (:code:`-d1`) with a work-group size of 64 (:code:`-g64`). The simulation results will automatically be exported to the HAWC2 binary format (:code:`exp_h2bin`). Simulations that have already been evaluated previously will be skipped (:code:`skip`) and the automatically generated binary wind fields will be removed after a simulation is finished (:code:`remove_wind`). After executing this call the following info is printed out on the screen::

	!!!!! Welcome to QBlade EE v2.0.5.1_alpha windows Command Line Interface (CLI) !!!!!

	*************************************** OpenCL *********************************************
	Available OpenCL Devices:

	-d0 : to use CPU: OpenMp (default)
	-d1 : to use GPU: OpenCL 1.2 CUDA Quadro P6000

	Specify the OpenCL device by passing -dXX to the CLI, where -d0 is the default
	Specify the OpenCL group size by passing -gXX to the CLI, where -g32 is the default
	--------------------------------------------------------------------------------------------

	************************************ Multi Threading ***************************************
	Available CPU Cores:

	- CPU cores found: 16

	Set the parallel threads by passing -tXX to the CLI, where -t1 is the default
	--------------------------------------------------------------------------------------------


	************************************ Input User Commands ***********************************
	1 - OpenCl device:            1
	2 - OpenCl groupsize:         64
	3 - Parallel Threads:         12
	4 - all_sim                   batch evaluate all .sim files in all WORKING_DIR(s) and saves them as .qpr1
	5 - WORKING_DIR 0:            c:\simulations
	6 - exp_h2bin                 adds HAWC2BINARY format to auto-export and post-export formats
	7 - remove_wind               removes bts windfields after auto-generation through .sim files
	8 - skip                      skip evauation of .qpr files if a .qpr1 file exists; .sim files that were already exported; cut-planes if a .qpr2 exists

	Using OpenCL on  GPU: OpenCL 1.2 CUDA Quadro P6000
	--------------------------------------------------------------------------------------------


	************************* List of sim files that will be evaluated *************************
	[1] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y-20.sim
	[2] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y0.sim
	[3] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y20.sim
	[4] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y-20.sim
	[5] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y0.sim
	[6] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y20.sim
	[7] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y-20.sim
	[8] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y0.sim
	[9] c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y20.sim
	[10] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y-20.sim
	[11] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y0.sim
	[12] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y20.sim
	[13] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis0_i0_y-20.sim
	[14] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis0_i0_y0.sim
	[15] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis0_i0_y20.sim
	[16] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis30_i0_y-20.sim
	[17] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis30_i0_y0.sim
	[18] c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis30_i0_y20.sim
	--------------------------------------------------------------------------------------------


	****************************** Simulation of sim definitions *******************************

	...queuing 18 simulations over 12 threads!

	...starting evaluation of < Queue Item 1/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y-20.sim ; with ThreadID 0x36e4 at 16:15:59 ; on 10.01.2023
	...starting evaluation of < Queue Item 2/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y0.sim ; with ThreadID 0x1134 at 16:16:00 ; on 10.01.2023
	...starting evaluation of < Queue Item 3/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis-30_i0_y20.sim ; with ThreadID 0x3fc4 at 16:16:01 ; on 10.01.2023
	...starting evaluation of < Queue Item 4/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y-20.sim ; with ThreadID 0x4094 at 16:16:02 ; on 10.01.2023
	...starting evaluation of < Queue Item 5/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y0.sim ; with ThreadID 0x11c4 at 16:16:03 ; on 10.01.2023
	...starting evaluation of < Queue Item 6/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis0_i0_y20.sim ; with ThreadID 0x3e10 at 16:16:03 ; on 10.01.2023
	...starting evaluation of < Queue Item 7/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y-20.sim ; with ThreadID 0x2d00 at 16:16:04 ; on 10.01.2023
	...starting evaluation of < Queue Item 8/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y0.sim ; with ThreadID 0x3090 at 16:16:05 ; on 10.01.2023
	...starting evaluation of < Queue Item 9/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10000_ws31_hs11_tp15_mis30_i0_y20.sim ; with ThreadID 0x3360 at 16:16:06 ; on 10.01.2023
	...starting evaluation of < Queue Item 10/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y-20.sim ; with ThreadID 0x1cbc at 16:16:07 ; on 10.01.2023
	...starting evaluation of < Queue Item 11/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y0.sim ; with ThreadID 0xdfc at 16:17:17 ; on 10.01.2023
	...starting evaluation of < Queue Item 12/18 > : c:\simulations\QB_HEXAFLOAT_LC63_s10001_ws31_hs11_tp15_mis-30_i0_y20.sim ; with ThreadID 0x2f54 at 16:17:17 ; on 10.01.2023
	
As can be seen from QBlade's console output an overview of the passed options is given, followed by an overview of the queued simulations before the evaluation of the simulations themselves starts. The information on the screen will now be updated whenever a simulation instance is finished and a new simulation instance is started to reflect on the progression of the batch run. After all simulations have been evaluated and exported QBlade will close and return to the command window.