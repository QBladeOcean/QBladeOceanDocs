Structural Definition of Bodies
===============================

For an aeroelastic wind turbine setup, each body in the multi-body setup is defined by its own structural data table. These datatables contain the crosssectional, structural information that is required to setup the beam elements, which make up a structural body. The structural bodies that can be defined with structural datatables are: **blades**, **struts**, **tower**, **torquetube**, **cable elements** and the **substructure**. Different types of elements can be used to setup these structural bodies. The different element types are briefly explained below:

Structural Element Types
************************

A structural body (blade, tower, substructure, cable) in QBlade can be modeled with one of four different element types.

Euler-Bernoulli Beam
--------------------

Euler-Bernoulli beams are the most basic type of beams in QBlade. These beams rely on the thin beam theory and thus do not consider shear forces. They are been implemented using a corotational approach, which enables the handling of large deflections and displacements.

Timoshenko Beam
---------------

Timoshenko beams represent a more advanced beam model in QBlade compared to Euler-Bernoulli beams. These beams incorporate the effects of shear deformation, making them suitable for a wider range of bodies. Similar to Euler-Bernoulli beams, Timoshenko beams are implemented with a corotational formulation to accommodate large displacements and deflections while providing a more accurate representation of the beam's behavior.

Timoshenko Beam FPM
-------------------

Timoshenko beams with a Fully Populated Stiffness Matrix (FPM) represent the most sophisticated and versatile beam model in QBlade. Timoshenko FPM beams take into account also off-diagonal coupling effects, such as bend-twist coupling, which is particularly important for an accurate modeling of very large blades. The Timoshenko FPM element is reserved to be used excludively to model rotor blades or struts.

ANCF Cable Element
------------------

The ANCF Cable element in QBlade is used for an efficient simulation of slender, cable like structures such as mooring lines and blade cables. These elements utilize Absolute Nodal Coordinate Formulation to obtain accurate and efficient results for complex mooring system configurations or tower guywires.

Structural Body Definition Files
********************************

The cross-sectional propreties of structural elements are assigned by means of cross sectional data tables. For blades, struts, the tower and torquetube, a structural body is defined within a single file that contains a structural datatable and a set of parameters that defines the spatial diecretization of the body, its structural element type, its damping properties and an optional distribution of lumped masses.

Damping of Structural Bodies
****************************

Two different damping models exists, which can be used to define the damping properties of a structural body. 

Isotropic Rayleigh Damping
--------------------------

A single Rayleigh damping coefficient can be set for each structural data table by using the keyword :code:`RAYLEIGHDMP`. This keyword defined the *stiffness proportional* Rayleigh damping coefficient :math:`\beta`. The :math:`\beta` coefficient is applied to each degree of freedom of the structural body:

:math:`C=beta*K`, 

where :math:`C`is the damping matrix and :math:`K` the stiffness matrix. The Rayleigh damping :math:`beta` coefficient is related to the fraction of critical damping :math:`Xi` as:

:math:`\zeta = \beta * \pi * f`, or 

:math:`\beta = \frac{\zeta}{\pi * f}`.

Rayleigh damping is not constant, but varies with frequency. Typically, Rayleigh damping is set for the first natural frequency of a component. Optionally, it is also possible to assign a nonuniformly distributed :math:`\beta` coefficient via the structural datatables (see :ref:`Blade / Strut Structural Data Table Columns`). 

Anisotropic Rayleigh Damping
----------------------------

For a more detailed definition of the damping properties of a structural body the anisotropic damping model is recommended. This damping model allows to define different damping properties for the different degreed of freedom (or modes) of a structural body. The anisotropic damping of a body is defined by at least four parameters (and an optional fifth parameter), followed by the keyword :code:`RAYLEIGHDMP_ANISO`.

.. code-block:: console
	:caption: : Exemplary definition of anisotropic damping properties in a structural data file.
	
	0.004048 0.003153 0.00027325 0.00000 0.00000 RAYLEIGHDMP_ANISO	

The five parameters are related to the anisotropic damping in the following way:

 * **1:** The stiffness proportional :math:`\beta` Rayleigh damping coefficient for bending about the local y-axis (flapwise) or shear along the local x-axis.
 * **2:** The stiffness proportional :math:`\beta` Rayleigh damping coefficient for bending about the local x-axis (edgewise) or shear along the local y-axis.
 * **3:** The stiffness proportional :math:`\beta` Rayleigh damping coefficient for bending about the local z-axis (torsion).
 * **4:** The stiffness proportional :math:`\beta` Rayleigh damping coefficient along the local z-axis (elongation).
 * **5:** (optional) A mass proportional :math:`\alpha` Rayleigh damping coefficient, applied to all degrees of freedom (0.00 as default).
 
In the same way as the isotropic stiffness proportional Rayleigh damping coefficients, the Rayleigh damping :math:`beta` coefficients are related to the fraction of critical damping :math:`Xi` of the related mode shape as:

:math:`\zeta = \beta * \pi * f`, or 

:math:`\beta = \frac{\zeta}{\pi * f}`.


Blade and Strut Euler Bernoulli and Timoshenko Datatables
---------------------------------------------------------

The following table gives an overview of the entries of the structural data table for blades and struts. All entries reserved for modeling the shear stiffness are only used with Timoshenko beams and are simply ignored when defined for an Euler-Bernoulli beam.

.. table:: Blade / Strut Cross Sectional Beam Properties for Euler-Bernoulli Beams
	:widths: 10 20 30 10

	======== ==================== ========================================= =======
	Col. Nr. Name                 Explanation                               Unit
	======== ==================== ========================================= =======
	1        Length               Norm. curved length                       -
	-------- -------------------- ----------------------------------------- -------
	2        Mass density         Mass per unit length                      kg/m
	-------- -------------------- ----------------------------------------- -------
	3        Bend. stiff. X       Bending Stiffness around :math:`X_{ce}`   Nm^2
				      (:math:`EI_{xx}`)         
	-------- -------------------- ----------------------------------------- ------- 
	4        Bend. stiff. Y       Bending Stiffness around :math:`Y_{ce}`   Nm^2
				      (:math:`EI_{yy}`)  
	-------- -------------------- ----------------------------------------- ------- 
	5        Axial stiff.         Longitudinal Stiffness                    N
				      (:math:`EA`)                   
	-------- -------------------- ----------------------------------------- ------- 
	6        Tors. stiff.         Torsional Stiffness                       Nm^2
				      (:math:`GJ`)                   
	-------- -------------------- ----------------------------------------- ------- 
	7        Shear stiff.         Shear Stiffness                           N
				      (:math:`GA`) (not used with Euler beams)     
	-------- -------------------- ----------------------------------------- ------- 
	8        Str. pitch           Structural pitch angle between reference  deg
				      :math:`X` and :math:`X_{ce}` axis         
	-------- -------------------- ----------------------------------------- ------- 
	9        Shear factor X       Shear factor for force in principal       -
				      bending axis :math:`X_{ce}`  
	-------- -------------------- ----------------------------------------- ------- 
	10       Shear factor Y       Shear factor for force in principal       -
				      bending axis :math:`Y_{ce}`
	-------- -------------------- ----------------------------------------- ------- 
	11       Radius of gyration X Norm. radius of inertia corresponding to  %chord
				      a rotation around :math:`X_{ce}`   
	-------- -------------------- ----------------------------------------- ------- 
	12       Radius of gyration Y Norm. radius of inertia corresponding to  %chord
				      a rotation around :math:`Y_{ce}`    
	-------- -------------------- ----------------------------------------- ------- 
	13       Center of mass X     Norm. center of mass position :math:`X`   %chord           
	-------- -------------------- ----------------------------------------- ------- 
	14       Center of mass Y     Norm. center of mass position :math:`Y`   %chord
	-------- -------------------- ----------------------------------------- ------- 
	15       Center of elast. X   Norm. center of elasticity position       %chord
				      :math:`X`
	-------- -------------------- ----------------------------------------- ------- 
	16       Center of elast. Y   Norm. center of elasticity position       %chord
				      :math:`Y`
	-------- -------------------- ----------------------------------------- ------- 
	17       Center of shear X    Norm. center of shear position :math:`X`  %chord
	-------- -------------------- ----------------------------------------- ------- 
	18       Center of shear Y    Norm. center of shear position :math:`Y`  %chord
	-------- -------------------- ----------------------------------------- ------- 
	19       Damping Coefficient  **(optional)** This column allows to        -
				      assign distributed Rayleigh beta coeff.
	======== ==================== ========================================= ======= 


Blade and Strut Timoshenko FPM Datatable
----------------------------------------

The following table gives an overview of the entries of the structural data table for blades and struts:

.. table:: Blade / Strut Cross Sectional Beam Properties for Timoshenko FPM Beams
	:widths: 10 20 30 10

	======== ==================== ========================================= =======
	Col. Nr. Name                 Explanation                               Unit
	======== ==================== ========================================= =======
	1        Length               Norm. curved length                       -
	-------- -------------------- ----------------------------------------- -------
	2        Beam offset X        Offset in local x-direction (norm with c) -
	-------- -------------------- ----------------------------------------- -------
	3        Beam offset Y        Offset in local y-direction (norm with c) -
	-------- -------------------- ----------------------------------------- ------- 
	4        Pitch                Structural pitch, applied to matrix       deg
	-------- -------------------- ----------------------------------------- ------- 
	5        K11                  (1,1) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- ------- 
	6        K12                  (1,2) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	7        K13                  (1,3) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	8        K14                  (1,4) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	9        K15                  (1,5) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	10       K16                  (1,6) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	11       K22                  (2,2) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	12       K23                  (2,3) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	13       K24                  (2,4) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	14       K25                  (2,5) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	15       K26                  (2,6) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	16       K33                  (3,3) entry for the stiffness matrix      N
	-------- -------------------- ----------------------------------------- -------
	17       K34                  (3,4) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	18       K35                  (3,5) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	29       K36                  (3,6) entry for the stiffness matrix      Nm
	-------- -------------------- ----------------------------------------- -------
	20       K44                  (4,4) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	21       K45                  (4,5) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	22       K46                  (4,6) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	23       K55                  (5,5) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	24       K56                  (5,6) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	25       K66                  (6,6) entry for the stiffness matrix      Nm^2
	-------- -------------------- ----------------------------------------- -------
	26       M11                  (1,1) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- ------- 
	27       M12                  (1,2) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	28       M13                  (1,3) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	29       M14                  (1,4) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	30       M15                  (1,5) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	31       M16                  (1,6) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	32       M22                  (2,2) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	33       M23                  (2,3) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	34       M24                  (2,4) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	35       M25                  (2,5) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	36       M26                  (2,6) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	37       M33                  (3,3) entry for the mass matrix           kg
	-------- -------------------- ----------------------------------------- -------
	38       M34                  (3,4) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	39       M35                  (3,5) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	40       M36                  (3,6) entry for the mass matrix           kgm
	-------- -------------------- ----------------------------------------- -------
	41       M44                  (4,4) entry for the mass matrix           kgm^2
	-------- -------------------- ----------------------------------------- -------
	42       M45                  (4,5) entry for the mass matrix           kgm^2
	-------- -------------------- ----------------------------------------- -------
	43       M46                  (4,6) entry for the mass matrix           kgm^2
	-------- -------------------- ----------------------------------------- -------
	44       M55                  (5,5) entry for the mass matrix           kgm^2
	-------- -------------------- ----------------------------------------- -------
	45       M56                  (5,6) entry for the mass matrix           kgm^2
	-------- -------------------- ----------------------------------------- -------
	46       M66                  (6,6) entry for the mass matrix           kgm^2
	======== ==================== ========================================= ======= 



Tower / Torquetube Euler Bernoulli and Timoshenko Data Tables
-------------------------------------------------------------

The following table gives an overview of the entries of the structural data table:

.. table:: Tower / Torquetube Cross Sectional Beam Properties
	:widths: 10 20 30 10

	======== ==================== ========================================= =======
	Col. Nr. Name                 Explanation                               Unit
	======== ==================== ========================================= =======
	1        Length               Norm. curved length                       -
	-------- -------------------- ----------------------------------------- -------
	2        Mass density         Mass per unit length                      kg/m
	-------- -------------------- ----------------------------------------- -------
	3        Bend. stiff. X       Bending Stiffness around :math:`X_{ce}`   Nm^2
				      (:math:`EI_{xx}`)         
	-------- -------------------- ----------------------------------------- ------- 
	4        Bend. stiff. Y       Bending Stiffness around :math:`Y_{ce}`   Nm^2
				      (:math:`EI_{yy}`)  
	-------- -------------------- ----------------------------------------- ------- 
	5        Axial stiff.         Longitudinal Stiffness                    N
				      (:math:`EA`)                   
	-------- -------------------- ----------------------------------------- ------- 
	6        Tors. stiff.         Torsional Stiffness                       Nm^2
				      (:math:`GJ`)                   
	-------- -------------------- ----------------------------------------- ------- 
	7        Shear stiff.         Shear Stiffness                           N
				      (:math:`GA`) (not used with Euler beams)     
	-------- -------------------- ----------------------------------------- ------- 
	8        Str. pitch           Structural pitch angle between reference  deg
				      :math:`X` and :math:`X_{ce}` axis         
	-------- -------------------- ----------------------------------------- ------- 
	9        Shear factor X       Shear factor for force in principal       -
				      bending axis :math:`X_{ce}`  
	-------- -------------------- ----------------------------------------- ------- 
	10       Shear factor Y       Shear factor for force in principal       -
				      bending axis :math:`Y_{ce}`
	-------- -------------------- ----------------------------------------- ------- 
	11       Radius of gyration X Norm. radius of inertia corresponding to  %chord
				      a rotation around :math:`X_{ce}`   
	-------- -------------------- ----------------------------------------- ------- 
	12       Radius of gyration Y Norm. radius of inertia corresponding to  %chord
				      a rotation around :math:`Y_{ce}`    
	-------- -------------------- ----------------------------------------- ------- 
	13       Center of mass X     Norm. center of mass position :math:`X`   %chord           
	-------- -------------------- ----------------------------------------- ------- 
	14       Center of mass Y     Norm. center of mass position :math:`Y`   %chord
	-------- -------------------- ----------------------------------------- ------- 
	15       Center of elast. X   Norm. center of elasticity position       %chord
				      :math:`X`
	-------- -------------------- ----------------------------------------- ------- 
	16       Center of elast. Y   Norm. center of elasticity position       %chord
				      :math:`Y`
	-------- -------------------- ----------------------------------------- ------- 
	17       Center of shear X    Norm. center of shear position :math:`X`  %chord
	-------- -------------------- ----------------------------------------- ------- 
	18       Center of shear Y    Norm. center of shear position :math:`Y`  %chord
	-------- -------------------- ----------------------------------------- ------- 
	19       Diameter             Cross section diameter                    m
	-------- -------------------- ----------------------------------------- ------- 
	20       Drag                 **(optional)** Drag coefficient for         -      
				      aerodynamic drag
	-------- -------------------- ----------------------------------------- ------- 
	21       Damping Coefficient  **(optional)** This column allows to        -
				      assign distributed Rayleigh beta coeff.
	======== ==================== ========================================= ======= 