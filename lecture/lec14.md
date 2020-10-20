---
layout: page
title: Lecture 14 – Feature Engineering
nav_exclude: true
---

# Lecture 14 – Feature Engineering

Presented by Joseph Gonzalez

Content by Joseph Gonzalez, John DeNero, Josh Hug

- [slides](https://docs.google.com/presentation/d/1cS7XP4B2mBqk97gMx2Y44cos4cnyHhua-dssuCuj8zU/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfpBiBBWILVRpmzprp__8lIP)
- [code](https://data100.datahub.berkeley.edu/hub/user-redirect/git-sync?repo=https://github.com/DS-100/fa20&subPath=lecture/lec14/)
- code HTML: [Part 1](../../resources/assets/lectures/lec14/lec14-part1.html), [Part 2](../../resources/assets/lectures/lec14/lec14-part2.html), [Part 3](../../resources/assets/lectures/lec14/lec14-part3.html)
- (supplementary) [video](https://youtu.be/f-adF9gh1xo) and [code HTML](http://www.ds100.org/su20/resources/assets/lectures/live04/live4.html) from a live lecture in Summer 2020 that reinforced some of the mathematical ideas in this lecture

**Important:** This lecture is a combination of two lectures from previous semesters (this is why the video titles don't match our numbering). Read this before proceeding with the lectures, as it details which concepts you should focus on.

Sections 14.1 through 14.4 discuss the core techniques of feature engineering. Slides are linked above, and code is in "Part 1" and "Part 2".
- 14.1: Throughout this lecture, Radial Basis Functions are used as an example. For our purposes, they are purely an example, and are not in-scope.
- 14.2, 14.3: Entirely in scope.
- 14.4: Of the three techniques discussed, one-hot encoding is most important, though the others are still in scope.

Sections 14.5 through 14.7 discuss pitfalls to be aware of in feature engineering. There are no accompanying slides; these ideas are primarily explained in the lecture notebook "Part 3".
- 14.5: Focus on the numerical ideas here, not the syntax of model creation (though the code is linked above).
- 14.6: The focus of this video is about the content at the end where our design matrix has too many columns, not about the details of Radial Basis Functions.
- 14.7: See the above comment.

The Quick Check for this lecture is due **Monday, October 26th at 11:59PM.** To get credit for this lecture's Quick Checks, you will have to fill out all of the following Google Forms as well as the mid-semester survey, linked on the course website and on Piazza (as well as in one of the following forms).


<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Video</th>
<th>Quick Check</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>14.1</strong> <br>A demonstration of how to use scikit-learn to fit linear models.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/lFzRiinHSzU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSejnJAKdxySVRwnQAKUo2GkveqhEl2dkA7O3XSQ8831w4psVA/viewform" target="\_blank">14.1</a></td>
</tr>
<tr>
<td><strong>14.2</strong> <br>Feature functions, as a method of transforming existing numerical data, and encoding non-numerical data for use in modeling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/ET44iB169no" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLScZNUjkD5kVrFsZE50zGLY6pawRP-ZYzZZj-aLXOBA472CVhw/viewform" target="\_blank">14.2</a></td>
</tr>
<tr>
<td><strong>14.3</strong> <br>Defining what it means for a model to be linear. The constant feature. More sophisticated numerical features.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/moL6aeW94Ps" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSf5tE_6RRpRJjG172b7Eor5x8hAVPKlhfgb9F8Ehs0Vez2HzA/viewform" target="\_blank">14.3</a></td>
</tr>
<tr>
<td><strong>14.4</strong> <br>Numerically encoding categorical data using various encodings (one-hot, bag of words, n-gram).</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/y6mxtlWYo54" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdGaAyC1P2PrUiG6nNchFmmyXQQwI5g5JXlJpOm5E1-JIPfZw/viewform" target="\_blank">14.4</a></td>
</tr>
<tr>
<td><strong>14.5</strong> <br>Issues we may run into when our design matrix has redundant features.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/M11bB0Yd2is" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfLfIwIHlX9wEQoOmmKwZJEE88fLm51_VLzsi3yQONDazyVcA/viewform" target="\_blank">14.5</a></td>
</tr>
<tr>
<td><strong>14.6</strong> <br>Issues we may run into when our design matrix has more features than observations. Radial basis functions.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/iwbqbPg740I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSdvfcAPfpTbVK-96CqcAZFDyMKMBKdS7XT7vfeO9SvQDfHChw/viewform" target="\_blank">14.6</a></td>
</tr>
<td><strong>14.7</strong> <br>Overfitting our model to the data we used to train it leads to poor generalizability to unseen data, which is the goal of modeling.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/b6l9eVGERxY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeRp1nJX_Tea_hqBT3sgC-UnnTGiXuFkcrXMgs4nC1c9H_Phw/viewform" target="\_blank">14.7</a></td>
