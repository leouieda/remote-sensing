<!--
-------------------------------------------------------------------------------
This file defines the contents of each slide.
The reveal.js configuration can be found in index.html
-------------------------------------------------------------------------------
-->

<!-- .slide: class="slide-title" data-background-image="assets/title-slide.svg" data-background-color="#000000" data-background-size="contain" -->

<!-- Place the content at the bottom of the slide -->
<div class="r-stretch">
</div>

<h1 id="talk-title">
  Introduction to <br>optical remote sensing
</h1>
<p id="talk-authors">
  <a href="https://www.leouieda.com">Leonardo Uieda</a>
</p>

<!-- Place location and date side-by-side with affiliation logos -->
<div class="row talk-info">
<div class="col-large">

<!-- Permission to reuse and CC-BY license logo -->
<i class="fa fa-camera" style="margin: 0 10px 0 0"></i>
Feel free to screenshot/share/reuse this presentation
<span style="margin: 0 20px">/</span>
<a href="https://creativecommons.org/licenses/by/4.0/"><i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by" style="margin: 0 10px 0 2px"></i>CC-BY 4.0 License</a>

</div>
<div class="col-medium">

<!-- Add logos here. Need these wrappers to align them to the bottom right -->
<div class="talk-logos-container">
<div class="talk-logos">
  <a href="https://www.compgeolab.org"><img src="assets/compgeolab-banner-light.svg" alt="Computer-Oriented Geoscience Lab"></a>
  <a href="https://www.liverpool.ac.uk/"><img src="assets/university-of-liverpool-white.png" alt="University of Liverpool"></a>
</div>
</div>

</div>
</div>

===============================================================================

<!-- .slide: class="slide-transition" -->

Part 1

# Fundamentals

===============================================================================

<div class="row middle">
<div class="col">

# Aims

</div>
<div class="col">

1. <!-- .element: class="fragment" --> Introduce the basic types of remote sensing
1. <!-- .element: class="fragment" --> Identify the limitations of remote sensing
1. <!-- .element: class="fragment" --> Understand how digital images are represented
1. <!-- .element: class="fragment" --> Summarize the concept of resolution

</div>
</div>

===============================================================================

# Remote sensing is...

<ul class="fa-ul">
<li class="fragment">
<i class="fas fa-eye fa-li"></i>
Observing a system remotely, i.e. <strong>without physical contact</strong>
between sensor and system.
</li>
<li class="fragment">
<i class="fas fa-user fa-li"></i>
Experts are in <strong>high demand</strong> in various industries (particularly
with machine learning and coding mixed in).
</li>
<li class="fragment">
<i class="fas fa-globe-americas fa-li"></i>
Widespread data coverage and availability has revolutionized our ability to
<strong>monitor our changing planet</strong>.
</li>
</ul>

**In this lesson, we'll focus on multispectral satellite remote sensing.** <!-- .element: class="fragment" -->

===============================================================================

# Applications

<div class="row">
<div class="col">

* <!-- .element: class="fragment" data-fragment-index="1" --> Hazard monitoring and response
* <!-- .element: class="fragment" --> Biosphere and ocean productivity
* <!-- .element: class="fragment" --> Atmosphere and weather patterns
* <!-- .element: class="fragment" --> Mapping roads and urban areas
* <!-- .element: class="fragment" --> Prediction of agricultural yield

</div>
<div class="col-medium tiny fragment" data-fragment-index="1">

<img src="images/mauna-loa-landsat-2022-12-02-low-res.jpg">

Example infrared image of the
[December 2022 Mauna Loa volcano eruption](https://www.leouieda.com/blog/mauna-loa.html)
using data from the Landsat 9 multispectral remote sensing satellite.
Image source: [Uieda (2022) - CC0](https://doi.org/10.6084/m9.figshare.21677246)

</div>
</div>

===============================================================================

# The remote sensing essentials are...

<div class="large">

<ul class="fa-ul">
<li class="fragment">
<i class="fas fa-sun fa-li"></i>
A source of energy
</li>
<li class="fragment">
<i class="fas fa-cloud fa-li"></i>
Transmission through the atmosphere
</li>
<li class="fragment">
<i class="fas fa-satellite fa-li"></i>
Reception by the sensor
</li>
</ul>

</div>

===============================================================================

# Sources of energy


Most remote sensing instruments use some form of
<br>
**electromagnetic (EM) radiation**.

Examples of EM sources:

<div class="fragment">

* The sun
* "Hot" objects/surfaces
* Artificial/human-made

</div>

===============================================================================

# Active versus passive

**Active**: Instruments generate their own EM radiation
<br>
(SAR/InSAR, altimetry, LIDAR)

<div class="fragment">

**Passive**: Use radiation reflected or emitted by the target
<br>
(optical, thermal)
<br>
<span class="fragment"><strong>👆🏽 we'll focus on this one</strong></span>
</div>

===============================================================================

# Electromagnetic spectrum

<div class="r-stretch">

<img src="images/EM_Spectrum_Properties_edit.svg">

</div>
<div class="footnote">

Image credit: [Inductiveload, NASA](https://commons.wikimedia.org/wiki/File:EM_Spectrum_Properties_edit.svg) (CC-BY-SA)

</div>

===============================================================================

# Reflectance properties of materials

<div class="row middle">
<div class="col text-left">

Some light is **absorbed** by materials

Some light is **reflected** by materials

Proportion of absorption/reflection depends on the wavelength
and the material

<p class="fragment" data-fragment-index="2">
Used to <strong>characterize different materials</strong> from multispectral
remote sensing data
</p>

</div>
<div class="col fragment" data-fragment-index="1">

<img src="images/Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg" style="width: 90%">

<div class="footnote">

Image credit: [Arbeck](https://commons.wikimedia.org/wiki/File:Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg) (CC-BY)

</div>

</div>
</div>

===============================================================================

# Transmittance through the atmosphere

<div class="row middle">
<div class="col-medium">

<img src="images/Solar_spectrum_pt.svg">

<div class="footnote-left">

Image credit: [Jucá Costa](https://commons.wikimedia.org/wiki/File:Solar_spectrum_pt.svg) (CC-BY-SA)

</div>

</div>
<div class="col fragment">

Atmosphere **absorbs** light at specific wavelength **bands**

Bands are determined by atmospheric **gasses**
<br>
(H₂O, CO₂, O₂, O₃)

</div>
</div>

===============================================================================

# Impacts on satellite remote sensing

<div class="small">

Absorption by the atmosphere determines in
<br>
<strong>which wavelengths satellites can operated</strong>

</div>
<div class="fragment">

<img src="images/AtmosphereEMSpectrum.png">

<div class="footnote">

Image credit: [haade](https://commons.wikimedia.org/wiki/File:AtmosphereEMSpectrum.png) (CC-BY-SA)

</div>
</div>

===============================================================================

# Reception of radiation

Depends on:

* <!-- .element: class="fragment" --> Sensor type
* <!-- .element: class="fragment" --> Sensitivity to specific wavelengths
* <!-- .element: class="fragment" --> Sensor resolution
* <!-- .element: class="fragment" --> Satellite orbit
* <!-- .element: class="fragment" --> How the signal is digitized

===============================================================================

# Resolution

<div class="text-left">

**Temporal resolution:**
<span class="fragment">how often a place is imaged (satellite orbit repeat)</span>

**Spectral resolution:**
<span class="fragment">how many bands are sampled and their width</span>

**Spatial resolution:**
<span class="fragment">the smallest features that can be resolved</span>

**Radiometric resolution:**
<span class="fragment">how many bits are used to digitize the signal</span>

</div>

===============================================================================

## Example: Bands used by optical satellites

<img src="images/optical-satellite-comparison.png" style="width: 80%;">

<div class="tiny">

Bands available on the
[Landsat 8](https://landsat.gsfc.nasa.gov/) (operated by NASA/USGS)
and [Sentinel 2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
(operated by ESA) satellites and their spatial resolution (in meters)

</div>

<div class="footnote">

Image credit: [Kääb et al. (2016)](https://doi.org/10.3390/rs8070598) (CC-BY)

</div>

===============================================================================

<!-- .slide: class="slide-transition" -->

Part 2

# Quantitative optical <br> remote sensing

===============================================================================

<div class="row middle">
<div class="col">

# Aims

</div>
<div class="col">

1. <!-- .element: class="fragment" --> Introduce the concept of multispectral images
1. <!-- .element: class="fragment" --> Explore the applications of this type of data
1. <!-- .element: class="fragment" --> Understand how to analyze these data quantitatively
1. <!-- .element: class="fragment" --> Consider the factors that limit their usability

</div>
</div>

===============================================================================

# Multispectral optical remote sensing

**Passive** remote sensing (uses reflected radiation from the Sun)

<div class="row">
<div class="col small fragment" data-fragment-index="1">

Satellites carry sensors that can take images of **multiple wavelength bands
individually**

<p class="fragment" data-fragment-index="3">
The collection of images from all bands is called a <strong>scene</strong>
</p>

</div>
<div class="col-large fragment" data-fragment-index="2">

<img src="images/landsat8-bands-liverpool.svg">

<div class="footnote">

Image credit: Leonardo Uieda (CC-BY)

</div>

</div>
</div>

===============================================================================

# Why multiple bands?

<div class="row">
<div class="col">

Information beyond the visible bands can be crucial for **classification** of
materials and their properties.

<div class="col fragment" data-fragment-index="1">

For example:
**vegetation** can be distinguished from soil/rock by identifying
the characteristic jump between **red and near-infrared**

</div>

</div>
<div class="col fragment" data-fragment-index="1">

<img src="images/Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg" style="width: 90%">

<div class="footnote">

Image credit: [Arbeck](https://commons.wikimedia.org/wiki/File:Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg) (CC-BY)

</div>

</div>
</div>

===============================================================================

# Thermal bands

Calculation of **surface temperature** on land and oceans

<div class="row middle">
<div class="col-medium fragment tiny">

<img src="images/MODIS_sst.png">

Sea surface temperature measured by the [MODIS sensor](https://modis.gsfc.nasa.gov/)
of the Terra and Aqua satellites (operated by NASA).
<br>
Image credit: [Giorgiogp2](https://commons.wikimedia.org/wiki/File:MODIS_sst.png) (CC-BY-SA)

</div>
<div class="col small fragment">

Monitor volcanic eruptions and wild fires (not as affected by smoke/clouds)

Input for ocean and climate models

Lower spatial resolution

</div>
</div>

===============================================================================

# Panchromatic band

<div class="row">
<div class="col">

Measures across a **broad range of wavelengths**

<div class="fragment" data-fragment-index="1">

Increase in energy sampled allows for **higher spatial resolution**

</div>
<div class="fragment" data-fragment-index="3">

Can be used to increase the resolution of other bands
([pansharpening](https://en.wikipedia.org/wiki/Pansharpened_image))

</div>

</div>
<div class="col-medium fragment" data-fragment-index="2">

<img src="images/panchromatic-rbg-resolution.svg">

<div class="footnote">

Image credit: Leonardo Uieda (CC-BY)

</div>

</div>
</div>

===============================================================================

# NASA/USGS Landsat Program

<div class="row">
<div class="col tiny">

<img src="images/Landsat_Data_Continuity_Mission_Observatory_testing.jpg" style="width: 90%;">

Landsat 8 undergoing testing before launch.
<br>
Image credit: [Orbital Sciences Corporation](https://en.wikipedia.org/wiki/File:Landsat_Data_Continuity_Mission_Observatory_testing.jpg) (public domain)

</div>
<div class="col-medium">

<ul class="fa-ul">
<li class="fragment">
<i class="fas fa-history fa-li"></i>
Operating since the 1970s
</li>
<li class="fragment">
<i class="fas fa-satellite fa-li"></i>
<a href="https://en.wikipedia.org/wiki/Landsat_8">Landsat 8</a>: launched in
2013 with 11 bands and is still operating
</li>
<li class="fragment">
<i class="fas fa-satellite fa-li"></i>
<a href="https://en.wikipedia.org/wiki/Landsat_9">Landsat 9</a>: launched in
2021, also with 11 bands, to complement the temporal resolution of Landsat 8
</li>
<li class="fragment">
<i class="fas fa-satellite fa-li"></i>
<a href="https://landsat.gsfc.nasa.gov/satellites/landsat-next/">Landsat Next (10)</a>:
planned for 2030 with 26 (!) bands and up to 3x better spatial resolution
</li>
<li class="fragment">
<i class="fab fa-creative-commons-pd fa-li"></i>
Data are released to the <strong>public domain</strong>
</li>
<li class="fragment">
<i class="fas fa-download fa-li"></i>
Freely downloaded from <a href="https://earthexplorer.usgs.gov/">USGS EarthExplorer</a>
</li>
</ul>

</div>
</div>

===============================================================================



===============================================================================

===============================================================================

===============================================================================

===============================================================================

===============================================================================

<!-- .slide: class="slide-license" data-background-image="assets/contact-slide.svg" data-background-size="contain" data-background-color="#000000" -->

<div class="r-stretch centered">
<div class="">

<p class="license-icons">
<i class="fab fa-github"></i>
</p>

Source code for this presentation:
<br>
[github.com/leouieda/remote-sensing](https://github.com/leouieda/remote-sensing)

<p class="license-icons" style="margin-top: 5rem;">
<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
</p>

Unless otherwise noted,
the contents of this presentation are
licensed under the
<br>
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

</div>
</div>
<div class="footnote-left">

The background image is a Landsat 8 scene (panchromatic band) of the Mersey
river delta.
<br>
White dots are on the right are offshore wind turbines.

</div>
