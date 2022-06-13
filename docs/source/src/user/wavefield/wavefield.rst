Ocean Wave Generator
====================

If an offshore simulation where the consideration of wave excitation is being carried out, it is necessary to provide the information about the sea sate in the form of
a wave field. The field may either consist of a single wave train (regular wave) or multiple, superpositioned regular waves - (irregular waves). Both types may be generated
directly in QBlade. A third possibility is the definition of a prescribed sea state, allowing the user to import externally generated wave fields. The three functionalities are described
in more detailed below. The underlying theory implemented in QBlade is described in the :ref:`Sea` section of the theory guide.

Any wave field generated in QBlade requires that a new wave is created by selecting this option in the *Controls* box. 
This opens the *Linear Waves* dialogue, where the wave generation options are displayed. 
In the *Main Seastate Parameters* box, the wave train is defined (amplitude and frequency). 
The *Equal Energy Frequency Discretization* box allows the user to tune the discretization parameters of the energy spectrum. 
Finally, the *Equal Energy Directional Discretization* box lets the user define directional properties of the wave.

Regular Wave
------------
To generate a regular wave, the wave type *Single Wave* has to be chosen in the *Linear Waves* dialogue. 
The user now has the option to characterize the single wave train with the remaining available inputs. 
These parameters define the shape and direction of an Airy wave (see :ref:`Linear Wave Theory`).

Main Parameters

* **Time Offset**: Time shift of the generated wave signal.
* **Significant Wave Height**: Height of wave train to be generated (directly linked to amplitude).
* **Significant Wave Amplitude**: Amplitude of the wave (directly linked to wave height).
* **Peak Period**: Period of the wave (directly linked to wave frequency).
* **Peak Frequency**: Frequency of the wave (directly linked to the wave period).

Equal Energy Directional Discretization:

* **Principal Wave Direction**: Incoming wave direction.

Irregular Wave Field
--------------------
To generate an irregular wave field, the wave type *Spectrum* has to be chosen. The user is now given the option to characterize the wave field
with the remaining available inputs. In addition to the wave train characterization discussed above, spectra discretization options can be specified.

.. _fig-irregwave_user:
.. figure:: irregwave_dialogue.png
    :align: center
    :scale: 70%
    :alt: Iregular wave creation dialogue in QBlade.

    Definition of an irregular wave field in the Ocean Wave Generator.

Main Parameters

* **Time Offset**: Time shift of the generated wave signal.
* **Significant Wave Height**: Wave height defining shape of the wave spectrum (directly linked to amplitude).
* **Significant Wave Amplitude**: Wave amplitude defining shape of the wave spectrum (directly linked to height).
* **Peak Period**: Peak period of the wave spectrum (directly linked to wave frequency).
* **Peak Frequency**: Peak frequency of the wave spectrum (directly linked to the wave period).
* **Automatic Gamma**: Automatic or manual definition of peak shape factor of the spectrum.
* **Automatic Sigma**: Automatic or manual definition of the spectral width parameter.

Equal Energy Frequency Discretization

* **Maximum Bin Width**: Maximum frequency range of the spectrum discretization.
* **Number of Frequency Bins**: Resolution of frequency discretization of the energy spectrum.
* **Random Phase Seed**: The random seed assigning the wave train phases.

Equal Energy Directional Discretization:
Either a unidirectional irregular wave field (Single Dir) or multidirectional wave field (Cos Spread) can be selected

* **Principal Wave Direction**: Definition of the wave direction (unidirectional spectrum) or of the principal direction of the cosine spectrum.
* **Maximum Spread**: Definition of the width of the cosine spectrum.
* **Spreading Exponent**: Shape defining parameter for the directional spectrum
* **Number of Directional Bins**: Resolution of angular discretization of the directional spectrum.


Import Components
-----------------
By selecting this option the user can import a wave field using wave train data.
when this option is selected a button appears *Load Wave File* which allows the user to import a ``.txt`` file containing the wave train information.  
This file must contains frequency [Hz], amplitude [m], phase [deg] and direction [deg] information of the wavefield in four columns. 
This data represents the frequency domain information of the wave. This is inverse Fourier-transformed in order to specify a time-series of the wave data.
Once calculated, the button *View Wave File* appears allowing the user to visually check the imported data.

Import Timeseries
-----------------
By selecting this option the user can import a wave field using a time series of the wave height. 
A discrete Fourier transform (DFT) is applied to the timeseries in order to represent the data in the frequency domain.
An inverse Fourier transform (IFT) is then applied to the Fourier coefficient in order to recreate the time-series data.
A set of parameters must be specified for the DFT which allows the user to improve the representation of the timeseries.
These parameters include:

* **Cut-in Frequency**: The minimum frequency considered in the IFT, below which data is discarded (approximately low-pass filtering). 
* **Cut-out Frequency**: The maximum frequency considered in the IFT, above which data is discarded (approximately high-pass filtering). 
* **Signal Sampling Rate**: The frequency with which data from the time series is sampled in order to generate the DFT. This allows the user to reduce the size of the wave train data. 
* **Amplitude Threshold**: The maximum amplitude allowed in the IFT. This allows the user to avoid spurious large amplitude wave trains from occuring.

Visualization
-------------
After a wave field has been created, visual and quantitative evaluation can be carried out in the *3D* View or *Graph View* display window. 
A time resolved animation of the wave field can be carried out in the *Time control* box.

Import and Export Functionality
-------------------------------
QBlade allows the user to import and export wave fields either in the four column format described in :ref:`Import Components` or in a ``.Iwa`` format. 
The ``.Iwa`` format contains all of the parameters necessary to define the time and frequency domain descriptions of a wave field.
This functionality can be found in the menu toolbar below the *Wave* tab.

.. _fig-vis:
.. figure:: demo_wavefield.png
    :align: center
    :scale: 70%
    :alt: Visualization of a demonstrational wavefield

    Visualization of a demonstrational wavefield.


.. footbibliography::

