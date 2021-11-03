Tower Influence
===============

.. _fig-towershadow:
.. figure:: towershadow.PNG
    :align: center
    :alt: towershadow

    Visualization of the tower shadow model; showing velocity magnitude.

A tower shadow model, based on the work of Bak (:footcite:t:`Moriarty2005`) is implemented in QBlade. This model is based on a superposition of the analytical solution for potential flow around a cylinder and a model for the downwind wake behind a cylinder, based on a tower drag coefficient. 
The tower shadow model only affects velocity components that are normal to the tower centerline; the z-component of the velocity, parallel to the tower centerline, remains unaffected. 
The tower shadow model is only used when the z-component of the evaluation point is smaller or equal to the tower height. 
An application of the tower model, including a comparison to CFD simulations and experimental data is found in the work of :footcite:t:`Klein2018`.

.. footbibliography::