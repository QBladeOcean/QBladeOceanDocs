Ground Effect
=============

Ground effects can be modelled with the :doc:`../lifting_line/lifting_line` method by mirroring all vortex elements, bound and free, at the ground plane (:footcite:t:`Leishman2000`). 
A mirror image (see Figure \ref{fig:ground}) of all bound and free vortices is created at every time step using the ground as a symmetry plane. 
Such a treatment doubles the number of times that the Biot-Savart equation is calculated and thereby doubles the computational time needed for the evaluation of the convection step. 

.. _fig-groundeffect:
.. figure:: ground.PNG
    :align: center
    :alt: groundeffect

    Modeling of ground effect through mirroring of the wake.

.. footbibliography::