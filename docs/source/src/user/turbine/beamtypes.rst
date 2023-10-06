Structural Beam Types
---------------------

A structural body (blade, tower, etc...) in QBlade can be modeled with one of three different beam types.

Euler-Bernoulli Beam
^^^^^^^^^^^^^^^^^^^^

Euler-Bernoulli beams are the most basic type of beams in QBlade. These beams rely on the thin beam theory and thus do not consider shear forces. They are been implemented using a corotational approach, which enables the handling of large deflections and displacements.

Timoshenko Beam
^^^^^^^^^^^^^^^

Timoshenko beams represent a more advanced beam model in QBlade compared to Euler-Bernoulli beams. These beams incorporate the effects of shear deformation, making them suitable for a wider range of bodies. Similar to Euler-Bernoulli beams, Timoshenko beams are implemented with a corotational formulation to accommodate large displacements and deflections while providing a more accurate representation of the beam's behavior.

Timoshenko Beam FPM
^^^^^^^^^^^^^^^^^^^

Timoshenko beams with a Fully Populated Stiffness Matrix (FPM) approach represent the most sophisticated and versatile beam model in QBlade. Timoshenko FPM beams take into account also off-diagonal coupling effects, such as bend-twist coupling, which is particularly important for an accurate modeling of very large blades.

ANCF Cable Elements
^^^^^^^^^^^^^^^^^^^

The ANCF Cable element in QBlade is used for an efficient simulation of slender, cable like structures such as mooring lines and blade cables. These elements utilize Absolute Nodal Coordinate Formulation to obtain accurate and efficient results for complex mooring system configurations or tower guywires.