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

# Optical Remote Sensing

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

1. Introduce the concept of multispectral images
1. Explore the applications of this type of data
1. Understand how to analyze these data quantitatively
1. Consider the factors that limit their usability

</div>
</div>

---

<!-- .slide: class="slide-transition"  data-background-color="#000000" data-background-image="../assets/background.jpg" data-background-repeat="no-repeat" data-background-opacity="0.15" data-background-position="center" -->

<div class="centered">
<div>

# Principles of Optical Imaging

</div>
</div>

---

# Previously...


The 3 essentials of remote sensing:

**Source**: determines the distribution of energy in the EM spectrum
(if a source produces infrared, we'll never measure reflected blue)

**Atmosphere**: absorbs and scatters some wavelengths strongly

**Reception**: depends on the sensor and reflectance of materials

---

# Previously...

<div class="container">
<div class="col-large">

<img src="../images/AtmosphereEMSpectrum.png" style="width: 100%;">

</div>
<div class="col-small small">

The gases in the atmosphere absorb and scatter certain wavelengths of
electromagnetic radiation.

</div>
</div>

This limits the wavelength **bands** in which
<br>
remote sensing satellites can operate.

<div class="r-stretch bottom-left">

Image credit: [haade](https://commons.wikimedia.org/wiki/File:AtmosphereEMSpectrum.png) (CC-BY-SA)

</div>

---

# Multispectral optical remote sensing

**Passive** remote sensing (uses reflected radiation from the Sun).

<div class="container">
<div class="col-large">

<img src="../images/optical-satellite-comparison.png" style="width: 100%;">

</div>
<div class="col-small small">

Satellites carry sensors that can take **images of multiple wavelength bands
individually** (hence multispectral).

The collection of images from all bands is called a **scene**.
</div>
</div>

<div class="r-stretch bottom-left">

Image credit: [USGS](https://www.usgs.gov/media/../images/comparison-landsat-7-and-8-bands-sentinel-2) (public domain)

</div>

---

# Advantages of multiple bands

<div class="container">
<div class="col-large">

Information beyond the visible bands can be crucial for **classification** of
materials and their properties.

For example, **vegetation** can be distinguished from soil/rock by identifying the
jump in reflectance between **red and near-infrared**.


</div>
<div class="col-small">

<img src="../images/Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg">

<div class="r-stretch bottom-right">

Image credit: [Arbeck](https://commons.wikimedia.org/wiki/File:Incoming_spectral_reflectance_from_different_objects_to_a_sensor_system.svg) (CC-BY)

</div>

</div>
</div>

---

# Thermal bands

Bands with wavelengths > 10,000 nm allow calculation of
the surface temperature on land and oceans.

<div class="container">
<div class="col">

<img src="../images/MODIS_sst.png" >

</div>
<div class="col small">

Crucial input for ocean and climate models.

Used to monitor volcanic activity and fires, which are often obscured by
smoke and clouds.

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: [Giorgiogp2](https://commons.wikimedia.org/wiki/File:MODIS_sst.png) (CC-BY-SA)

</div>

---

# Example Landsat8 scene



<div class="r-stretch bottom-left">

Image credit: Leonardo Uieda (CC-BY)

</div>

---

# Panchromatic band

Measures across a wider range of wavelengths than normal bands.

Increased sampled energy allows for **higher spatial resolution** when compared to other bands.

Can be used to sharpen the other bands (known as pan-sharpening).

Image comparing.



---

<!-- .slide: class="slide-transition"  data-background-color="#000000" data-background-image="../assets/background.jpg" data-background-repeat="no-repeat" data-background-opacity="0.15" data-background-position="center" -->

<div class="centered">
<div>

# Quantitative Image Analysis

</div>
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
