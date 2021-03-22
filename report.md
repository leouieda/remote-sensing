# Assessment instructions: Remote Sensing Report

> These are instructions for a summative assessment that covers most of the
> practical material.

## General background

> The following is fiction. Play along.

A national government passed new legislation that mandates the national
agriculture agency of this country to monitor the environment at a national
level. The new legislation focuses on obtaining quantitative results from
observational data. To easily compare results across national borders, the
United Nations has suggested a code-of-practice workflow using satellite remote
sensing. Due to lack of in-house expertise and budget cuts in the last few
years, the agriculture agency outsources this task to an environmental
consultancy company, which will carry out a preliminary analysis using remote
sensing imagery. You are the remote sensing expert in this consultancy company.

Remote sensing can be used to monitor land cover change (you vaguely recall
hearing about this in ENVS258 at the University of Liverpool; luckily you still
have your class notes and Jupyter notebooks from the practicals). In
particular, optical multispectral imagery can be used to compute indexes (like
NDVI and dNBR) and composites (combinations of different bands to form “false”
colors). The use of freely available open-source software like scikit-image can
be used to quantitatively analyse these datasets. Multispectral images from the
Landsat 8 are available for free download and can provide an indispensable tool
for a nascent consultancy company.

## Instructions

Your main objective is to investigate the environmental impact of human action
or a natural phenomena on the environment using satellite imagery. For example:
deforestation, agricultural land usage, flooding, forest fires, landslides, and
more. You will:

* Choose an area/event of interest (search for interesting cases online)
* Research the history of the area/event and identify key questions that could be answered using satellite remote sensing (use papers/books, not just websites)
* Download and analyse Landsat 8 multispectral imagery for the area/event
* Analyse the data using the tools and techniques learned in class and/or new ones (search the scikit-image documentation for other methods that you can employ)
* Aim to be as quantitative as possible (go beyond looking at an image and calculate different indices, means, histograms, rates of change, standard deviations)
* Evaluate the environmental impact in your area/event
* Write a scientific report about your results and conclusions (see format below)

Guidelines:

* The report can have a maximum of 4 pages with 2 cm margins on all sides and Arial 11 pt font. This includes text, figures, captions, and references.
* Your report can be less than 4 pages. If you can achieve the same level of quality with less text, there will be no problem.
* Submit your report in PDF format (not Word).
* Submit your Jupyter notebooks and/or Python scripts along with the report. These will not count towards your mark but will receive formative feedback.
* Double-check your submission. Bad formatting will be penalized.
* All images must have captions and proper attribution.
* Do not use copywrited images that do not allow reuse. Figures from papers are fine with citations but random images from the internet are not. See below to learn how to search for images that can be reused.
* Figures must have labels on all axis and colorbars.

## Examples

A good report will have:

* "Why": A compelling introduction to why your study subject is interesting and important
* "How": Thorough descriptions of data and methods used (the "how")
* "What": Exploration of the images/indices/composites/averages/etc and what your analysis contributes to our understanding of the study subject

Examples of past reports include:

* Evaluation of the size and duration of a volcanic eruption, comparing with previous recorded eruptions
* Tracking deforestation trends in a small region, spatially and also in aggregate (total area / year)
* The effect of particular drought or flooding events on vegetation/crops
* Tracking the progress and/or area affected by wild fires
* Feasibility studies: can Landsat 8 imagery be used to investigate certain environmental phenomena? Be careful with this one since applications that are obviously impractical will get low marks.

These are just some examples of what can be done. Be creative and search for
different use cases that you can explore. Search the scikit-image documentation
(Links to an external site.) for new analysis methods that you can employ to
answer questions about your data.

## Format

Your report should contain all of the following sections:

* Title and author name
* Abstract: An abstract of approximately 4-6 lines that summarizes this report. Briefly state the problem, main findings, interpretation, and conclusions. Write this last.
* Introduction: An introduction which informs in more detail about the problem to solve, and the approach to take. State the motivation for this study, results from previous studies, and your main goals.
* Data: A section presenting which data was used in the report (describe the data type, satellite, where you downloaded it from, how you selected the data, etc). Make sure you include: row/path numbers, exact dates for all scenes, at least one true colour composite.
* Methodology: What type of analysis was performed on that data. We have covered several in class. You can find other indices, composites, and statistics online and in textbooks. The scikit-image website has examples of advanced image processing methods that could be useful here.
* Results: A section which presents and describes the results without any interpretation. Just a plain description of the results (e.g., In Figure 3 we present the coherence values obtained using summer acquisitions. The values of coherence spanned the range from 0.4 to 0.9, with 80% of the pixels with values above 0.5).
* Discussion: A section where the results are discussed and interpreted based on your knowledge of the problem and background information (what you researched for your introduction). Use common sense, literature references, and relate key information from lectures and practicals to your results. Discuss the possible sources of error and uncertainty in your estimates. This section should focus on your results, not only previous results!
* Conclusions: A short section starting with a restatement of the problem, where results and discussions come together to formalize newly obtained knowledge.
* References: Use the ACS or the Harvard style (your choice). Please be consistent the the citation style (don't mix multiple styles).

## Common pitfalls to avoid

* Grand conclusions based on little evidence: If you analysed a single scene, do not stretch your conclusions to a whole country/continent. It's not expected that you will solve global issues in a 4-page report.
* Too much focus on previous results: Your discussion should focus on what you obtained, not the previous literature. Use the literature to compare with your results but don't  give it the primary focus.
* Missing information about the data sources: Anyone should be able to fully reproduce the results presented in your report. This cannot be done without key information about the data, like the row/path numbers, exact dates of the scenes, level of data (1 or 2), etc.
* Forgetting to take uncertainty into account when making conclusions: It's no use discussing the sources of uncertainty in your estimates and then ignoring them when making conclusions. See the first point about grand conclusions.
* Citing only websites: It's OK to have 1 or 2 website references for information about Landsat 8, for example. But if a majority of your references are websites, then that is a problem. Search for primary sources (articles and textbooks) instead. Wikipedia pages include links to primary sources. Read and cite those instead.
* Using inappropriate methods for the application: Just because we saw NDVI and NBR in class, it doesn't mean that they work for everything. Try different methods and search for other indices/composites that may be more appropriate for your study.

## General tips

* Read these instructions carefully! Then read them again.
* Pay close attention to the marking rubric! Make sure you check all of the boxes.
* Use an appropriate resolution for your figures. You can save good quality figures using the plt.savefig function.
* Use meaningful variables names (temperature instead of x).
* If you get an error, read the error message to find out what went wrong. Include the full error when asking a question.
* If your code doesn't seem to work, don’t change the code until you know why this happened and what you can do to fix it. Randomly changing the code and hoping it will work is a great way to waste your time.
* Google search is your best friend. Answers from StackOverflow are generally good sources of information.
* Backup your notebooks, data, and report!

## Resources

Sources of inspiration: https://earthobservatory.nasa.gov and https://worldview.earthdata.nasa.gov

Composite combinations to try: https://earthobservatory.nasa.gov/features/FalseColor/page6.php

Documentation for the software we use:

* scikit-image: https://scikit-image.org
* matplotlib: https://matplotlib.org
* numpy: https://numpy.org/doc/stable

Searching for openly licensed images to use in your report: https://www.youtube.com/watch?v=ISu51NB5Z28

## Downloading Landsat 8 images from EarthExplorer

Use the [USGS EarthExplorer website](https://earthexplorer.usgs.gov/) to
download scenes from Landsat 8 for your report or to explore for your own
learning.

* You'll need to register for a free account.
* Prioritize Landsat 8 Collection 2 Level 2 data to get surface reflectance and surface temperature instead of top-of-the-atmosphere reflections.
* Make note of the path and row numbers and the dates of the scenes you're downloading (include them on your report). Without them, there is no way to reproduce your findings.
* The date range should be between 2015 and now
* Level 2 products are only available between -60 and 60 latitude

Here is a video tutorial about how to use the website and some tips:
https://www.youtube.com/watch?v=Wn_G4fvitV8
