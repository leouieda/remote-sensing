<!-- .slide: class="slide-title" data-background-color="#000000" data-background-image="../assets/background.jpg" data-background-repeat="no-repeat" data-background-opacity="0.15" data-background-position="center" -->

<div class="container">
<div class="col-large" style="text-align: left;">

ENVS258 Environmental Geophysics
<br>
Remote Sensing

</div>
<div class="col-small" style="text-align: right;">

[<img src="../assets/university-of-liverpool-white.png" style="width: 35%">](https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/)

</div>
</div>

<div class="r-stretch">

# Remote sensing fundamentals

</div>

## Instructor: **[Leonardo Uieda](https://www.leouieda.com)**


<i class="fas fa-envelope fa-fw"></i> [Leonardo.Uieda@liverpool.ac.uk](mailto:Leonardo.Uieda@liverpool.ac.uk)
<span style="margin: 0 20px">|</span>
<i class="fab fa-twitter fa-fw"></i> [@leouieda](https://twitter.com/leouieda)
<span style="margin: 0 20px">|</span>
[<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i> CC-BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)

---

<div class="centered">
<div>

# Aims

1. Introduce the basic types of remote sensing
1. Identify the limitations of remote sensing
1. Understand how digital images are represented
1. Summarize the concept of resolution

</div>
</div>

---

<!-- .slide: data-background-color="#000000" data-background-image="../assets/background.jpg" data-background-repeat="no-repeat" data-background-opacity="0.15" data-background-position="center" -->

# Remote sensing is...

<div class="fragment">

Observing a system remotely, i.e. **without physical contact** between sensor
and system.

Widespread data coverage and availability has revolutionized our understanding
and appreciation of our planet.

Experts are in high demand in various industries
<br>
(particularly with machine learning and coding mixed in).

**In this class, we'll focus on satellite remote sensing.**

</div>

---

# Some applications

* Hazard monitoring and response (ground subsidence, ice coverage, volcanoes,
  earthquakes, hurricanes)
* Monitoring ocean temperature and dynamics
* Identification and classification of natural resources
* Biosphere, e.g. ocean productivity
* Atmosphere, e.g. wind speeds and weather patterns
* Mapping of roads, pathways, and urban areas
* Prediction of country/continent wide agricultural yield

---

# We'll cover 3 types of remote sensing data

<div class="container">
<div class="col">

Optical
<br>
images

<img src="images/Anak_Krakatau_2018-12-20_Landsat_8_T1_SR.jpg">

<div class="tiny">

Credit: [USGS/NASA](https://commons.wikimedia.org/wiki/File:Anak_Krakatau_2018-12-20_Landsat_8_T1_SR.jpg)
(CC-BY-SA)

</div>


</div>
<div class="col">

Digital Elevation Models (DEMs)

<img src="images/mount-saint-helens-dem.jpg">

<div class="tiny">

Credit: [Steve Schilling](https://www.usgs.gov/media/images/dem-mount-st-helens-crater-glacier-and-lava-domes)
(public domain)

</div>

</div>
<div class="col">

SAR/InSAR

<img src="images/Izmit_interferogram.jpg">

<div class="tiny">

Credit: [NASA/JPL-Caltech](https://en.wikipedia.org/wiki/File:Izmit_interferogram.jpg)
(public domain)

</div>

</div>
</div>

---

<div class="centered">
<div>

# The remote sensing essentials

1. Source of energy
1. Transmission through the atmosphere
1. Reception by a sensor

</div>
</div>

---

# Sources of energy

Most remote sensing instruments use some form of **electromagnetic (EM) radiation**.

Examples of EM sources:

<div class="fragment">

* The sun
* "Hot" objects/surfaces
* Artificial/human-made

</div>

---

# Active versus passive

**Active**: Instruments generate their own EM radiation
<br>
(SAR/InSAR, altimetry, LIDAR)

**Passive**: Use reflected solar radiation or emitted by the target
<br>
(optical, thermal)

---

# Electromagnetic spectrum

<img src="images/EM_Spectrum_Properties_edit.svg">

<div class="r-stretch bottom-right">

Image credit: [Inductiveload, NASA](https://commons.wikimedia.org/wiki/File:EM_Spectrum_Properties_edit.svg) (CC-BY-SA)

</div>

---

# Reflectance properties of materials

<div class="container">
<div class="col-large">

Some light is absorbed by different materials

Dependent on the wavelength

Used to characterize materials from remote sensing data

</div>
<div class="col-small">

<img src="images/Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg">

<div class="r-stretch bottom-right">

Image credit: [Arbeck](https://commons.wikimedia.org/wiki/File:Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg) (CC-BY)

</div>

</div>
</div>

---

# Transmittance through the atmosphere

<div class="container">
<div class="col-large">

<img src="images/Solar_spectrum_pt.svg">

<div class="r-stretch bottom-left">

Image credit: [Jucá Costa](https://commons.wikimedia.org/wiki/File:Solar_spectrum_pt.svg) (CC-BY-SA)

</div>

</div>
<div class="col-small">

The atmosphere absorbs light at specific wavelength **bands**

The bands are determined by gasses (H2O, CO2, O2, O3)

</div>

</div>
</div>

---

# Absorption properties of the atmosphere

determine in which wavelengths remote sensing
<br>
satellites can operated

<img src="images/AtmosphereEMSpectrum.png" style="width: 70%;">

<div class="r-stretch bottom-left">

Image credit: [haade](https://commons.wikimedia.org/wiki/File:AtmosphereEMSpectrum.png) (CC-BY-SA)

</div>

---

# Reception of radiation

Depends on:

* Sensor type
* Sensitivity to specific wavelengths
* Resolution
* Satellite orbit
* How the signal is digitized

---

# Resolution

Temporal resolution: how often a place is imaged (influenced by satellite orbit)

Spectral resolution: how many bands (and their size) are sampled

Spatial resolution: the smallest features that can be resolved

Radiometric resolution: how many bits are used to digitize the signal

---

## Example: Bands used by optical satellites

<img src="images/optical-satellite-comparison.png" style="width: 80%;">

<div class="r-stretch bottom-left">

Image credit: [USGS](https://www.usgs.gov/media/images/comparison-landsat-7-and-8-bands-sentinel-2) (public domain)

</div>

---

<!-- END MATTER -->
<!-- ====================================================================== -->

<!--## References and further reading-->

<!--<div class="lefted">-->

<!--* List of references-->

<!--</div>-->

<!------->

<!-- .slide: class="slide-license" -->

<div class="centered">
<div>

<p class="license-icons">
<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
</p>

Unless otherwise noted,
the contents of this lecture are
licensed under the
<br>
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

</div>
</div>
