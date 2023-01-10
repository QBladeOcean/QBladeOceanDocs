Wind Field Generator Overview
-----------------------------

If an unsteady simulation is being carried out, it is necessary to define the wind field.
This provides important information for the calculation of aerodynamic quantities. 
Three types of wind fields can be generated for use in QBlade. These are described individually below.

Uniform Wind Field 
------------------
A uniform wind field is specified directly within the *Wind Input Type* of the turbine simulation dialogue, shown in :numref:`fig-wind-pane` (see :doc:`../simulation/simulation`).
The necessary input parameters including velocity, horizontal inflow angle and directional shear are defined here.
In the case that the atmospheric boundary layer is to be modelled, this can be selected with the wind shear type radio button. 
The corresponding shear parameters can then by specified (see :doc:`../../theory/environment/wind/wind`). 

.. _fig-wind-pane:
.. figure:: winddialogue.png
    :align: center
    :scale: 80%
    :alt: Uniform wind field creation dialogue in QBlade.

    Specification of a uniform wind field within the turbine simulation dialogue. 
	
Hub Height File
---------------
The user has more modelling freedom when a hub-height wind file is used. This type of file can either be created manually or by using the IEC wind tool :footcite:`IECwindtool`. This allows the specification of the velocity field at the hub height as a function of time. QBlade interpolates the time between the starting time of the file and the point where the predefined wind velocity profile (EOG in this case) should start. If the user specified simulation time exceeds the ending time in the hub-height file, QBlade will create a constant wind field with the parameters from the last entry of the hub-height file until the end of the simulation. An exemplary hubheight input file that described an extreme operating gust (EOG) at 20m/s is shown below:

.. code-block:: console

	Time	Wind	Horiz.	Vert.	LinH.	Vert.	LinV.	Gust
		Speed	Dir	Speed	Shear	Shear	Shear	Speed
	0.000	20.000	0.000	0.000	0.000	0.200	0.000	0.000	
	60.000	20.000	0.000	0.000	0.000	0.200	0.000	0.000	
	60.100	20.000	0.000	0.000	0.000	0.200	0.000	-0.000	
	60.200	20.000	0.000	0.000	0.000	0.200	0.000	-0.004	
	60.300	20.000	0.000	0.000	0.000	0.200	0.000	-0.012	
	60.400	20.000	0.000	0.000	0.000	0.200	0.000	-0.028	
	60.500	20.000	0.000	0.000	0.000	0.200	0.000	-0.054	
	60.600	20.000	0.000	0.000	0.000	0.200	0.000	-0.092	
	60.700	20.000	0.000	0.000	0.000	0.200	0.000	-0.144	
	60.800	20.000	0.000	0.000	0.000	0.200	0.000	-0.209	
	60.900	20.000	0.000	0.000	0.000	0.200	0.000	-0.289	
	61.000	20.000	0.000	0.000	0.000	0.200	0.000	-0.384	
	61.100	20.000	0.000	0.000	0.000	0.200	0.000	-0.493	
	61.200	20.000	0.000	0.000	0.000	0.200	0.000	-0.614	
	61.300	20.000	0.000	0.000	0.000	0.200	0.000	-0.747	
	61.400	20.000	0.000	0.000	0.000	0.200	0.000	-0.889	
	61.500	20.000	0.000	0.000	0.000	0.200	0.000	-1.037	
	61.600	20.000	0.000	0.000	0.000	0.200	0.000	-1.188	
	61.700	20.000	0.000	0.000	0.000	0.200	0.000	-1.338	
	61.800	20.000	0.000	0.000	0.000	0.200	0.000	-1.485	
	61.900	20.000	0.000	0.000	0.000	0.200	0.000	-1.622	
	62.000	20.000	0.000	0.000	0.000	0.200	0.000	-1.748	
	62.100	20.000	0.000	0.000	0.000	0.200	0.000	-1.856	
	62.200	20.000	0.000	0.000	0.000	0.200	0.000	-1.944	
	62.300	20.000	0.000	0.000	0.000	0.200	0.000	-2.007	
	62.400	20.000	0.000	0.000	0.000	0.200	0.000	-2.041	
	62.500	20.000	0.000	0.000	0.000	0.200	0.000	-2.043	
	62.600	20.000	0.000	0.000	0.000	0.200	0.000	-2.011	
	62.700	20.000	0.000	0.000	0.000	0.200	0.000	-1.942	
	62.800	20.000	0.000	0.000	0.000	0.200	0.000	-1.834	
	62.900	20.000	0.000	0.000	0.000	0.200	0.000	-1.686	
	63.000	20.000	0.000	0.000	0.000	0.200	0.000	-1.498	
	63.100	20.000	0.000	0.000	0.000	0.200	0.000	-1.271	
	63.200	20.000	0.000	0.000	0.000	0.200	0.000	-1.005	
	63.300	20.000	0.000	0.000	0.000	0.200	0.000	-0.703	
	63.400	20.000	0.000	0.000	0.000	0.200	0.000	-0.366	
	63.500	20.000	0.000	0.000	0.000	0.200	0.000	0.000	
	63.600	20.000	0.000	0.000	0.000	0.200	0.000	0.393	
	63.700	20.000	0.000	0.000	0.000	0.200	0.000	0.807	
	63.800	20.000	0.000	0.000	0.000	0.200	0.000	1.237	
	63.900	20.000	0.000	0.000	0.000	0.200	0.000	1.678	
	64.000	20.000	0.000	0.000	0.000	0.200	0.000	2.124	
	64.100	20.000	0.000	0.000	0.000	0.200	0.000	2.568	
	64.200	20.000	0.000	0.000	0.000	0.200	0.000	3.003	
	64.300	20.000	0.000	0.000	0.000	0.200	0.000	3.425	
	64.400	20.000	0.000	0.000	0.000	0.200	0.000	3.825	
	64.500	20.000	0.000	0.000	0.000	0.200	0.000	4.198	
	64.600	20.000	0.000	0.000	0.000	0.200	0.000	4.539	
	64.700	20.000	0.000	0.000	0.000	0.200	0.000	4.841	
	64.800	20.000	0.000	0.000	0.000	0.200	0.000	5.101	
	64.900	20.000	0.000	0.000	0.000	0.200	0.000	5.314	
	65.000	20.000	0.000	0.000	0.000	0.200	0.000	5.477	
	65.100	20.000	0.000	0.000	0.000	0.200	0.000	5.587	
	65.200	20.000	0.000	0.000	0.000	0.200	0.000	5.642	
	65.300	20.000	0.000	0.000	0.000	0.200	0.000	5.642	
	65.400	20.000	0.000	0.000	0.000	0.200	0.000	5.587	
	65.500	20.000	0.000	0.000	0.000	0.200	0.000	5.477	
	65.600	20.000	0.000	0.000	0.000	0.200	0.000	5.314	
	65.700	20.000	0.000	0.000	0.000	0.200	0.000	5.101	
	65.800	20.000	0.000	0.000	0.000	0.200	0.000	4.841	
	65.900	20.000	0.000	0.000	0.000	0.200	0.000	4.539	
	66.000	20.000	0.000	0.000	0.000	0.200	0.000	4.198	
	66.100	20.000	0.000	0.000	0.000	0.200	0.000	3.825	
	66.200	20.000	0.000	0.000	0.000	0.200	0.000	3.425	
	66.300	20.000	0.000	0.000	0.000	0.200	0.000	3.003	
	66.400	20.000	0.000	0.000	0.000	0.200	0.000	2.568	
	66.500	20.000	0.000	0.000	0.000	0.200	0.000	2.124	
	66.600	20.000	0.000	0.000	0.000	0.200	0.000	1.678	
	66.700	20.000	0.000	0.000	0.000	0.200	0.000	1.237	
	66.800	20.000	0.000	0.000	0.000	0.200	0.000	0.807	
	66.900	20.000	0.000	0.000	0.000	0.200	0.000	0.393	
	67.000	20.000	0.000	0.000	0.000	0.200	0.000	0.000	
	67.100	20.000	0.000	0.000	0.000	0.200	0.000	-0.366	
	67.200	20.000	0.000	0.000	0.000	0.200	0.000	-0.703	
	67.300	20.000	0.000	0.000	0.000	0.200	0.000	-1.005	
	67.400	20.000	0.000	0.000	0.000	0.200	0.000	-1.271	
	67.500	20.000	0.000	0.000	0.000	0.200	0.000	-1.498	
	67.600	20.000	0.000	0.000	0.000	0.200	0.000	-1.686	
	67.700	20.000	0.000	0.000	0.000	0.200	0.000	-1.834	
	67.800	20.000	0.000	0.000	0.000	0.200	0.000	-1.942	
	67.900	20.000	0.000	0.000	0.000	0.200	0.000	-2.011	
	68.000	20.000	0.000	0.000	0.000	0.200	0.000	-2.043	
	68.100	20.000	0.000	0.000	0.000	0.200	0.000	-2.041	
	68.200	20.000	0.000	0.000	0.000	0.200	0.000	-2.007	
	68.300	20.000	0.000	0.000	0.000	0.200	0.000	-1.944	
	68.400	20.000	0.000	0.000	0.000	0.200	0.000	-1.856	
	68.500	20.000	0.000	0.000	0.000	0.200	0.000	-1.748	
	68.600	20.000	0.000	0.000	0.000	0.200	0.000	-1.622	
	68.700	20.000	0.000	0.000	0.000	0.200	0.000	-1.485	
	68.800	20.000	0.000	0.000	0.000	0.200	0.000	-1.338	
	68.900	20.000	0.000	0.000	0.000	0.200	0.000	-1.188	
	69.000	20.000	0.000	0.000	0.000	0.200	0.000	-1.037	
	69.100	20.000	0.000	0.000	0.000	0.200	0.000	-0.889	
	69.200	20.000	0.000	0.000	0.000	0.200	0.000	-0.747	
	69.300	20.000	0.000	0.000	0.000	0.200	0.000	-0.614	
	69.400	20.000	0.000	0.000	0.000	0.200	0.000	-0.493	
	69.500	20.000	0.000	0.000	0.000	0.200	0.000	-0.384	
	69.600	20.000	0.000	0.000	0.000	0.200	0.000	-0.289	
	69.700	20.000	0.000	0.000	0.000	0.200	0.000	-0.209	
	69.800	20.000	0.000	0.000	0.000	0.200	0.000	-0.144	
	69.900	20.000	0.000	0.000	0.000	0.200	0.000	-0.092	
	70.000	20.000	0.000	0.000	0.000	0.200	0.000	-0.054	
	70.100	20.000	0.000	0.000	0.000	0.200	0.000	-0.028	
	70.200	20.000	0.000	0.000	0.000	0.200	0.000	-0.012	
	70.300	20.000	0.000	0.000	0.000	0.200	0.000	-0.004	
	70.400	20.000	0.000	0.000	0.000	0.200	0.000	-0.000	
	70.500	20.000	0.000	0.000	0.000	0.200	0.000	0.000	


Turbulent Wind Field 
--------------------
The final type of wind file which can be set up is a fully turbulent wind file.
This can be either generated through the *Wind Input Type* button of the turbine simulation dialogue, as shown in :numref:`fig-wind-pane` or by directly generating this within the
turbulent wind module, shown in :numref:`fig-wind-module`. 

.. _fig-wind-module:
.. figure:: windbutton.png
    :align: center
    :alt: Wind field creation dialogue in QBlade.

    The wind field creation symbol in the QBlade main tool bar. 
	
When a new turbulent wind file is created, a range of parameters must be specified as shown by the turbulent wind dialogue in :numref:`fig-turb-dia`.
After these have been selected, clicking on the *Create* button automatically passes the information to the TurbSim program :footcite:`TurbSimGuide`.
This is linked to the QBlade release, so that no additional user input is required.
The input parameters are described in detail in the following sections. 

Grid Parameters
^^^^^^^^^^^^^^^

These parameters dictate the spatial dimensions of the generated turbulent wind grid.
A turbulent *box* is be generated which is then translated through the field of interest at the average velocity (defined below) 
as is consistent with Taylor's hypothesis for a turbulent flow :footcite:`BatchelorBook`.

* **Seed**: The random seed used to generate the wind field.
* **Time**: Determines the length of the generated turbulent box.
* **Timestep**: Specifies the discretisation in free stream (:math:`x`) direction.  
* **Grid Width**: Specifies box size in lateral (:math:`y`) direction.
* **Grid Height**: Specifies box size in vertical (:math:`z`) direction.
* **Grid Y Points**: Specifies spatial discretisation in :math:`y` direction.
* **Grid Z Points**: Specifies spatial discretisation in :math:`z` direction.
* **Hub Height**: Specifies the vertical position of the box center.

Turbine Class
^^^^^^^^^^^^^
These determine the turbine class as defined in the IEC 61400 design standard :footcite:`IEC61400-1`.

* **Turbine Class**: Specifies the design turbine class.
* **Turbulence Class**: Specifies the design turbulence class.
* **I_ref**: Specifies the turbulence intensity.
* **V_ref**: Specifies the reference velocity.

Flow Parameters
^^^^^^^^^^^^^^^
These parameters specify the parameters and model inputs required for generation of the turbulent velocity field. 

* **Mean Wind Speed**: Specifies the mean translational velocity of the frozen turbulent flow field.
* **Horizontal Inflow**: Specifies the horizontal inflow angle.
* **Vertical Inflow**: Specifies the vertical inflow angle.
* **IEC 61400 1-ed**: Specifies the version of the IEC standard applied.
* **Wind Type**: Specifies the wind class of the generated wind field.
* **Spectral Model**: Specifies the form of the spectral tensor applied to generate the stochastic velocity fluctuations.
* **Wind Profile Type**: Specifies the model used to represent the atmospheric shear layer.
* **Reference Height**: Specifies the reference height of the aforementioned shear layer model.
* **Shear Exponent**: Specifies the shear exponent of the aforementioned shear layer model (if exponential model chosen).
* **Roughness Length**: Specifies the reference height of the aforementioned shear layer model (if logarithmic model chosen).
* **Jet Height**: Specifies the jet height of the aforementioned shear layer model (if jet model chosen).
* **ETMC value**: Specifies the extreme turbulence model :math:`c` value (if ETM model chosen).
* **Remove TurbSim Files**: If checked, the TurbSim files generated (and subsequently read by QBlade) is deleted.
* **Close Console**: If checked, the console which is called to generate the TurbSim file is automatically closed upon completion of TurbSim file generation.
 
.. _fig-turb-dia:
.. figure:: turbulentwind.png
    :align: center
    :scale: 75%
    :alt: Turbulent wind field creation dialogue in QBlade.

    The turbulent wind field creation dialogue. 

.. footbibliography::
