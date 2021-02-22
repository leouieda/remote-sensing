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

# Digital Elevation Models

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

1. Introduce the concept of a digital elevation model (DEM)
1. Present the basics of LIDAR and its use for DEM generation
1. Understand how to calculate derived quantities of DEMs
1. Explore their applications in geoscience

</div>
</div>

---

<!-- .slide: class="slide-transition"  data-background-color="#000000" data-background-image="../assets/background.jpg" data-background-repeat="no-repeat" data-background-opacity="0.15" data-background-position="center" -->

<div class="centered">
<div>

# Introduction

</div>
</div>

---

# Height of topography

<div class="container">
<div class="col-large">

<img src="../images/srtm15p.png">

</div>
<div class="col-small small">

Used in many parts of Earth Sciences and Engineering:

* Gravimetric terrain correction
* Modelling sediment/water transport
* Flood assessment
* Landslide hazard prediction

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: Leonardo Uieda (CC-BY)

</div>

---

# Measuring topography

Measure the height as a function of position (**point cloud**).

<div class="container">
<div class="col">

<img src="../images/Colored_pointcloud.png" style="width: 100%;">

</div>
<div class="col small">

Different methods but many do this:

1. Measure the distance between the surface and a sensor.
1. Measure the position of the sensor (GPS).
1. Subtract the distance from the sensor height.

</div>
</div>

<div class="small">

</div>

<div class="r-stretch bottom-left">

Image credit: [Waikinl](https://commons.wikimedia.org/wiki/File:Colored_pointcloud.png) (CC-BY-SA)

</div>

---

# Producing a DEM

<div class="small">

A **digital elevation model** (DEM) is produced from point cloud data
<br>
through interpolation onto a regular grid (a **raster**).

</div>

<div class="container">
<div class="col-large">

<img src="../images/dem-generation.png">

</div>
<div class="col-small small">


Grid points are evenly distributed with a chosen spacing (often called the
"resolution" of the DEM).

Raster data are easier to manipulate, plot, and process than point data.

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: Leonardo Uieda (CC-BY)

</div>

---

# LiDAR

<div class="container">
<div class="col-large small">

Light Detection And Ranging is widely used to measure surface heights
(point clouds).

The instrument sends short pulses of laser **infrared light** and listens for
the echoes.

The distance is the speed of light times half of the two-way travel time.

`$ d = \dfrac{\Delta t}{2} \times c $`

</div>
<div class="col-small">

<img src="../images/LiDAR-i_lend.jpg" style="width: 85%;">

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: Modified from [Marek9134](https://commons.wikimedia.org/wiki/File:LiDAR-i_lend.gif) (CC-BY-SA)

</div>

---

# Multiple surfaces

<div class="container">
<div class="col-large small">

Reflections of a single pulse happen on multiple surfaces:
top of the canopy and bare ground, water surface and lake bottom, etc.

Interpreters can pick out each surface to map individually.

Used to study biomass, depth of glacial lakes, and topography in densely
vegetated areas.

</div>
<div class="col-small">

<img src="../images/lidar-schematic.svg" style="width: 65%;">

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: Modified from [Anthony Beck](https://commons.wikimedia.org/wiki/File:Airborne_Laser_Scanning_Discrete_Echo_and_Full_Waveform_signal_comparison.svg) (CC-BY-SA)

</div>

---

# LiDAR in archeology

<div class="container">
<div class="col-large small">

LiDR produces high resolution DEMs that can penetrate vegetation coverage.

Can reveal archeological sites that would not be visible.

For example, LiDAR was recently used to
[map Maya ruins under dense forest in Guatemala](https://www.bbc.co.uk/news/world-latin-america-42916261).

</div>
<div class="col-small smaller">

<img src="../images/King's_Castle,_Wells_LIDAR_(DTM_1m).png" >

LiDAR DEM of the King's Castle iron age settlement in Somerset, England.

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: [Yodin](https://commons.wikimedia.org/wiki/File:King%27s_Castle,_Wells_LIDAR_(DTM_1m).png) (OGLv3)

</div>

---

# LiDAR in geology

<div class="container">
<div class="col-large smaller">

<img src="../images/lidar.gif" >

Aerial photograph, unfiltered (top of the canopy) LiDAR, and bare earth LiDAR DEM
showing the San Andreas Fault.

</div>
<div class="col-small small">

LiDAR DEMs can reveal faults, river meanders, lava flows, terrain change (from
multiple surveys), and more.

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: [USGS](https://www.usgs.gov/media/images/san-andreas-fault-2) (public domain)

</div>

---

# LiDAR in glaciology

<div class="container">
<div class="col-large smaller">

<img src="../images/Flying_over_the_Greenland_Ice_Sheet,_July_2014.jpg">

Aerial photograph of the Greenland ice sheet showing blue melt water lakes and
rivers.

</div>
<div class="col-small small">

<img src="../images/ICESat-2_spacecraft_model.png">

LiDAR aboard NASA's Icesat-2 satellite is used to monitor sea ice thickness, ice
sheet topography, melt water lakes, and topography worldwide.

</div>
</div>

<div class="r-stretch bottom-left">

Image credit: [Bernt Rostad](https://commons.wikimedia.org/wiki/File:Flying_over_the_Greenland_Ice_Sheet,_July_2014.jpg) (CC-BY)
and [NASA](https://commons.wikimedia.org/wiki/File:ICESat-2_spacecraft_model.png) (public domain)

</div>

---

<!-- END MATTER -->
<!-- ====================================================================== -->

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
