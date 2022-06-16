Wave Generator Overview
-----------------------

If an offshore simulation where the consideration of wave excitation is being carried out, it is necessary to provide the information about the sea sate in the form of
a wave field. The field may either consist of a single wave train (regular wave) or multiple, superpositioned regular waves - (irregular waves). Both types may be generated
directly in QBlade. A third possibility is the definition of a prescribed sea state, allowing the user to import externally generated wave fields. The three functionalities are described
in more detailed below. The underlying theory implemented in QBlade is described in the :ref:`Waves` section of the theory guide.

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

**Main Parameters**

* **Time Offset**: Time shift of the generated wave signal.
* **Significant Wave Height**: Height of wave train to be generated (directly linked to amplitude).
* **Significant Wave Amplitude**: Amplitude of the wave (directly linked to wave height).
* **Peak Period**: Period of the wave (directly linked to wave frequency).
* **Peak Frequency**: Frequency of the wave (directly linked to the wave period).

**Equal Energy Directional Discretization**

* **Principal Wave Direction**: Incoming wave direction.

Irregular Wave Field
--------------------
To generate an irregular wave field, the wave type *Spectrum* has to be chosen. The user is now given the option to characterize the wave field
with the remaining available inputs. In addition to the wave train characterization discussed above, spectra discretization options can be specified.

.. _fig-irregwave_user:
.. figure:: irregwave_dialogue.png
    :align: center
    :scale: 60%
    :alt: Iregular wave creation dialogue in QBlade.

    Definition of an irregular wave field in the Ocean Wave Generator.

**Main Parameters**

* **Time Offset**: Time shift of the generated wave signal.
* **Significant Wave Height**: Wave height defining shape of the wave spectrum (directly linked to amplitude).
* **Significant Wave Amplitude**: Wave amplitude defining shape of the wave spectrum (directly linked to height).
* **Peak Period**: Peak period of the wave spectrum (directly linked to wave frequency).
* **Peak Frequency**: Peak frequency of the wave spectrum (directly linked to the wave period).
* **Automatic Gamma**: Automatic or manual definition of peak shape factor of the spectrum.
* **Automatic Sigma**: Automatic or manual definition of the spectral width parameter.

**Frequency Discretization**

* **Discretization Method**: The options are equal energy or equal frequency discretization of the wave spectrum
* **Maximum Bin Width**: Maximum frequency range of the spectrum discretization.
* **Number of Frequency Bins**: Resolution of frequency discretization of the energy spectrum.
* **Random Phase Seed**: The random seed assigning the wave component phase data.

**Equal Energy Directional Discretization**
Either a unidirectional irregular wave field (Single Dir) or multidirectional wave field (Cos Spread) can be created

* **Principal Wave Direction**: Definition of the wave direction (unidirectional spectrum) or of the principal direction of the cosine spectrum.
* **Maximum Spread**: Definition of the width of the cosine spectrum.
* **Spreading Exponent**: Shape defining parameter for the directional spectrum
* **Number of Directional Bins**: Resolution of angular discretization of the directional spectrum.


Import Components
-----------------
By selecting this option the user can import a wave field using wave component data.
when this option is selected a button appears *Import Components File* which allows the user to import a ``.txt`` file containing the wave component information.  
This file must contains frequency [Hz], amplitude [m], phase [deg] and direction [deg] information of the wavefield in four columns. 
This data represents the frequency domain information of the wave. This is inverse Fourier-transformed in order to specify a time-series of the wave data.
Once calculated, the button *View Wave File* appears allowing the user to visually check the imported data.

Import Timeseries
-----------------
By selecting this option the user can import a wave field using a time series of the wave height. 
A discrete Fourier transform (DFT) is applied to the timeseries in order to represent the data in the frequency domain.
An inverse Fourier transform (IFT) is then applied to the Fourier coefficient in order to recreate the time-series data.
A set of parameters must be specified for the DFT which gives the user some control of the wave components that are generated by the DFT.
These parameters include:

* **Low Cut-Off Frequency**: The minimum frequency considered in the DFT, below which wave components are discarded (approximately low-pass filtering). 
* **High Cut-Off Frequency**: The maximum frequency considered in the DFT, above which wave components are discarded (approximately high-pass filtering). 
* **Signal Sampling Rate**: The frequency with which data from the time series is sampled before the DFT is performed. This allows the user to reduce the number of wave components that will be generated by the DFT. 
* **Amplitude Threshold**: The minimum wave component amplitude allowed after the DFT is performed. This allows the user to filter out wave components with insignificant amplitude and thereby helps to reduce the number of generated wave components.

Visualization
-------------
After a wave field has been created, visual and quantitative evaluation can be carried out in the *3D* View or *Graph View* display window. 
A time resolved animation of the wave field can be carried out in the *Time control* box.

.. _fig-vis:
.. figure:: demo_wavefield.png
    :align: center
    :alt: Visualization of an exemplary wavefield

    Visualization of a exemplary wavefield.

Import and Export Functionality
-------------------------------
QBlade allows the user to import and export wave fields either in the four column format described in :ref:`Import Components` or in a ``.Iwa`` format. 
The ``.Iwa`` format contains all of the parameters necessary to define the time and frequency domain descriptions of a wave field.
This functionality can be found in the menu toolbar below the *Wave* tab. An exemplary ``.lwa`` file is shown below:

.. code-block:: console

	----------------------------------------QBlade Wave Definition File-------------------------------------------------
	Generated with : QBlade CE v 2.0 windows-pre-release
	Archive Format: 310001
	Time : 21:17:57
	Date : 14.06.2022

	----------------------------------------Object Name-----------------------------------------------------------------
	Jonswap_Wave                            OBJECTNAME          - the name of the linear wave definition object

	----------------------------------------Main Parameters-------------------------------------------------------------
	0.000                                   TIMEOFFSET          - the time offset from t=0s [s]
	3                                       WAVETYPE            - the type of wave: 0 = TIMESERIES, 1 = COMPONENTS, 2 = SINGLE, 3 = JONSWAP, 4 = ISSC, 5 = TORSETHAUGEN
	8.100                                   SIGHEIGHT           - the significant wave height (Hs) [m]
	12.700                                  PEAKPERIOD          - the peak period (Tp) [s]
	1                                       AUTOGAMMA           - use gamma according to IEC: 0 = OFF, 1 = ON (JONSWAP & TORSE only)
	1.000                                   GAMMA               - custom gamma (JONSWAP & TORSE only)
	1                                       AUTOSIGMA           - use sigmas according to IEC (JONSWAP & TORSE only)
	0.070                                   SIGMA1              - sigma1 (JONSWAP & TORSE only)
	0.090                                   SIGMA2              - sigma1 (JONSWAP & TORSE only)
	0                                       DOUBLEPEAK          - if true a double peak TORSETHAUGEN spectrum will be created, if false only a single peak (TORSE only)
	1                                       AUTOORCHI           - automatic OCHI-HUBBLE parameters from significant waveheight (OCHI only)
	0.077                                   MODFREQ1            - modal frequency 1, must be "< modalfreq1 * 0.5" (OCHI only)
	0.133                                   MODFREQ2            - modal frequency 2, should be larger than 0.096 (OCHI only)
	6.804                                   SIGHEIGHT1          - significant height 1, should be larger than height 2 (OCHI only)
	4.374                                   SIGHEIGHT2          - significant height 2 (OCHI only)
	3.000                                   LAMBDA1             - peak shape 1 (OCHI only)
	0.932                                   LAMBDA2             - peak shape 2 (OCHI only)

	----------------------------------------Frequency Discretization ---------------------------------------------------
	0                                       DISCTYPE            - frequency discretization type: 0 = equal energy; 1 = equal frequency
	1                                       AUTOFREQ            - use automatic frequency range (f_in = 0.5*f_p, f_out = 10*f_p)
	0.039                                   FCUTIN              - cut-in frequency
	0.787                                   FCUTOUT             - cut-out frequency
	0.050                                   MAXFBIN             - maximum freq. bin width [Hz]
	200                                     NUMFREQ             - the number of frequency bins
	12345                                   RANDSEED            - the seed for the random phase generator range [0-65535]

	----------------------------------------Directional Discretization (Equal Energy)-----------------------------------
	0                                       DIRTYPE             - the directional type, 0 = UNIDIRECTIONAL, 1 = COSINESPREAD
	0.000                                   DIRMEAN             - mean wave direction [deg]
	60.000                                  DIRMAX              - directional spread [deg]
	2.000                                   SPREADEXP           - the spreading exponent
	40                                      NUMDIR              - the number of directional bins


.. footbibliography::

