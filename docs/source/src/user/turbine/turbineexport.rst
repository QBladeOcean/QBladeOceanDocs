Turbine Export
==============

Turbine objects can be exported as a QBlade project file (``.qpr``) or into the text based ``.trb`` format. When a turbine object is exported into the ``.trb`` format, the associated blade (``.bld``) file is automatically created. Furthermore, the structural definition files (if the turbine has a structural model) and the controller parameters are also auomatically placed into the folder structure See an exemplary ``.trb`` file below:

.. code-block:: console

	----------------------------------------QBlade Turbine Definition File----------------------------------------------
	Generated with : QBlade IH v2.0.2_alpha windows
	Archive Format: 310002
	Time : 12:07:32
	Date : 29.06.2022

	----------------------------------------Object Name-----------------------------------------------------------------
	NREL_5MW_Servo_OC3                       OBJECTNAME         - the name of the turbine object

	----------------------------------------Rotor Definition------------------------------------------------------------
	Aero/NREL_5MW.bld                        BLADEFILE          - the path of the blade file that is used in this turbine definition
	0                                        TURBTYPE           - the turbine type (0 = HAWT or 1 = VAWT)
	3                                        NUMBLADES          - the number of blades (a Structural Model overrides this value)
	0                                        ROTORCONFIG        - the rotor configuration (0 = UPWIND or 1 = DOWNWIND)
	0                                        ROTATIONALDIR      - the direction of rotor rotation (0 = STANDARD or 1 = REVERSED)
	1                                        DISCTYPE           - type of rotor discretization (0 = from Bladetable, 1 = linear, 2 = cosine) 
	20                                       NUMPANELS          - the number of aerodynamic panels per blade (unused if DISCTYPE = 0)

	----------------------------------------Turbine Geometry Parameters-------------------------------------------------
	These values are only used if no Structural Model is defined for this Turbine, in case of a Structural Model the geometry is defined in the Structural Input Files!!
	10.5000                                  OVERHANG           - the rotor overhang [m] (HAWT only)
	0.0000                                   SHAFTTILT          - the shaft tilt angle [deg] (HAWT only)
	0.0000                                   ROTORCONE          - the rotor cone angle [deg] (HAWT only)
	0.0000                                   CLEARANCE          - the rotor clearance to ground [m] (VAWT only)
	0.0000                                   XTILT              - the rotor x-tilt angle [deg] (VAWT only)
	0.0000                                   YTILT              - the rotor y-tilt angle [deg] (VAWT only)
	126.0000                                 TOWERHEIGHT        - the tower heigh [m]
	1.8000                                   TOWERTOPRAD        - the tower top radius [m]
	2.5200                                   TOWERBOTRAD        - the tower bottom radius [m]

	----------------------------------------Aerodynamic Models----------------------------------------------------------
	0                                        DYNSTALLTYPE       - the dynamic stall model: 0 = none; 1 = OYE; 2 = GORMONT-BERG or 3 = ATEFLAP
	8                                        TF_OYE             - Tf constant for the OYE dynamic stall model
	6                                        AM_GB              - Am constant for the GORMONT-BERG dynamic stall model
	3                                        TF_ATE             - Tf constant for the ATEFLAP dynamic stall model
	2                                        TP_ATE             - Tp constant for the ATEFLAP dynamic stall model
	1                                        2PLIFTDRAG         - include the 2 point lift drag correction? (0 = OFF or 1 = ON)
	0                                        HIMMELSKAMP        - include the Himmelskamp Stall delay? (0 = OFF or 1 = ON) (HAWT only)
	0                                        TOWERSHADOW        - include the tower shadow effect (0 = OFF or 1 = ON)
	1                                        TOWERDRAG          - the tower drag coefficient [-] (if a Structural Model is used the tower drag is defined in the tower input file)

	----------------------------------------Wake Type------------------------------------------------------------------
	1                                        WAKETYPE           - the wake type: 0 = free vortex wake; 1 = unsteady BEM (unsteady BEM is only available for HAWT)

	----------------------------------------Vortex Wake Parameters------------------------------------------------------
	Only used if waketype = 0
	0                                        WAKEINTTYPE        - the wake integration type: 0 = EF; 1 = PC; 2 = PC2B
	1                                        WAKEROLLUP         - calculate wake self-induction (0 = OFF or 1 = ON)
	1                                        TRAILINGVORT       - include trailing vortex elements (0 = OFF or 1 = ON)
	1                                        SHEDVORT           - include shed vortex elements (0 = OFF or 1 = ON)
	0                                        CONVECTIONTYPE     - the wake convection type (0 = BL, 1 = HH, 2 = LOC)
	1.00                                     WAKERELAXATION     - the wake relaxation factor [0-1]
	1.00                                     FIRSTWAKEROW       - first wake row length [-]
	200000                                   MAXWAKESIZE        - the maximum number of wake elements [-]
	100                                      MAXWAKEDIST        - the maxmimum wake distance from the rotor plane (normalized by dia) [-]
	0.00100                                  WAKEREDUCTION      - the wake reduction factor [-]
	0                                        WAKELENGTHTYPE     - the wake length type (0 = counted in rotor revolutions, 1 = counted in time steps)
	1000000.00                               CONVERSIONLENGTH   - the wake conversion length (to particles) [-]
	0.50                                     NEARWAKELENGTH     - the near wake length [-]
	2.00                                     ZONE1LENGTH        - the wake zone 1 length [-]
	4.00                                     ZONE2LENGTH        - the wake zone 2 length [-]
	6.00                                     ZONE3LENGTH        - the wake zone 3 length [-]
	2                                        ZONE1FACTOR        - the wake zone 1 factor (integer!) [-]
	2                                        ZONE2FACTOR        - the wake zone 2 factor (integer!) [-]
	2                                        ZONE3FACTOR        - the wake zone 3 factor (integer!) [-]

	----------------------------------------Vortex Core Parameters------------------------------------------------------
	Only used if waketype = 0
	1.00                                     BOUNDCORERADIUS    - the fixed core radius of the bound blade vortex (fraction of local chord) [0-1]
	0.05                                     WAKECORERADIUS     - the intial core radius of the free wake vortex (fraction of local chord) [0-1]
	800.00                                   VORTEXVISCOSITY    - the turbulent vortex viscosity
	0                                        VORTEXSTRAIN       - calculate vortex strain 0 = OFF, 1 = ON
	20                                       MAXSTRAIN          - the maximum element strain, before elements are removed from the wake [-]

	----------------------------------------Gamma Iteration Parameters--------------------------------------------------
	Only used if waketype = 0
	0.40                                     GAMMARELAXATION    - the relaxation factor used in the gamma (circulation) iteration [0-1]
	0.00100                                  GAMMAEPSILON       - the relative gamma (circulation) convergence criteria
	100                                      GAMMAITERATIONS    - the maximum number of gamma (circulation) iterations (integer!) [-]

	----------------------------------------Unsteady BEM Parameters------------------------------------------------------
	12                                       POLARDISC          - the polar discretization for the unsteady BEM (integer!) [-]
	0                                        BEMTIPLOSS         - use BEM tip loss factor, 0 = OFF, 1 = ON
	0.00                                     BEMSPEEDUP         - initial BEM convergence acceleration time [s]

	----------------------------------------Structural Model-------------------------------------------------------------
	Structure/OC3_Sparbuoy_Main_LPMD.str     STRUCTURALFILE     - the input file for the structural model (leave blank if unused)
	0                                        GEOMSTIFFNESS      - enable geometric stiffness, 0 = OFF, 1 = ON

	----------------------------------------Turbine Controller-----------------------------------------------------------
	3                                        CONTROLLERTYPE     - the type of turbine controller 0 = none, 1 = BLADED, 2 = DTU, 3 = TUB
	TUBCon_1.3.9_64Bit                       CONTROLLERFILE     - the controller file name, WITHOUT file ending (.dll or .so ) - leave blank if unused
	Control/TUBCon_Params_V1.3.9_NREL5MW.xml PARAMETERFILE      - the controller parameter file name (leave blank if unused)