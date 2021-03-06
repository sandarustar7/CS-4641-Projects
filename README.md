# CS-4641-Projects
<p>A collection of project materials from CS 4641 at Georgia Tech</p>
<h1> Group Project: </h1>
<p>In a group of 4, we used basketball player's statistics to attempt to predict their position/role. We tried applying our models over a variety of seasons to measure how the importance of positions change over time.</p>
<p>The project writeup is available at: https://github.gatech.edu/pages/mlipscomb30/cs4641group43/ </p>
<p>I've also included the code that I used to train our models and create our graphs.</p> 
<p>Here's a breakdown of what I included, since its not organized well.</p>
<ul>
  <li>Season-Scraper.ipynb: Used for data scraping the 2000-2001 and 2009-2010 seasons, cleaning up the data, and putting it into a .csv</li>
  <li>Models-and-Graphs.ipynb: Loads the data in the .csv's and applies various models to the data and generates comparison graphs. *Note*: There is some weirdness because I generated two of the datasets but another team mate generated the other dataset, with the true labels separated from the features</li>
  <li>*.csv files: These are the datasets we used.</li>
  <li>graphs folder: Contains all of the graphs we used for the project writeup. Graphs will get saved to the root of the folder, then I move the graphs we keep into the good folder</li>
</ul>
<p>Also note that in Project2.ipynb there's some extra neural network stuff that wasn't used in the final project</p>
<h1> Class Assignments </h1>
<p>
I've also have the assignments in a private repository (https://github.com/sandarustar7/ML-Algorithm-Implementations but it will probably just give a 404). All of the assignments except for Random Forest are based on numpy (Random forest uses arrays of sklearn DecisionTreeClassifiers).</p>
<p>Here's an overview of the contents:</p> 
HW2: <br>
  <ul>
  <li>Gaussian Mixture Model</li>
  <li>KMeans</li>
  <li>Semisupervised (Gaussian Naive Bayes)<br></li>
  </ul>
  <br>
HW3: <br>
  <ul>
  <li>Image Compression (SVD)</li>
  <li>Isomap</li>
  <li>Naive Bayes</li>
  <li>Principle Component Analysis</li>
  <li>Linear Regression and Ridge Regression</li>
  </ul>
  <br>
HW4: <br>
  <ul>
  <li>Neural Network (2 layers, using relu, sigmoid, tanh functions)</li>
  <li>Random Forest </li>
  </ul>

