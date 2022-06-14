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
The user has more modelling freedom when a hub-height wind file is used. This type of file can either be created manually or by using the IEC wind tool :footcite:`IECwindtool`.
This allows the specification of the velocity field at the hub height as a function of time. This file can either be of ``.dat`` or ``.txt`` format.
An example of a file generated with the IEC wind tool is shown in :numref:`fig-wind-hubheight`. QBlade interpolates the time between the starting time of the file
and the point where the predefined wind velocity profile (EOG in this case) should start. If the user specified simulation time exceeds the ending time in the hub-height file,
QBlade will create a constant wind field with the parameters from the last entry of the hub-height file until the end of the simulation

.. _fig-wind-hubheight:
.. figure:: hubheightfile.png
    :align: center
    :scale: 65%
    :alt: Hub height wind field example in QBlade.

    Hub-height wind file for specification of a laminar unsteady wind field. 

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
