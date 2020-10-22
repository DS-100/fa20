---
layout: page
title: Lecture 15 – Bias and Variance
nav_exclude: true
---

# Lecture 15 – Bias and Variance

Presented by Fernando Perez

Content by Fernando Perez, Ani Adhikari, Suraj Rampure

- [slides](https://docs.google.com/presentation/d/15LDeDKNxpIa9j0_dHZr1F5AzrbVEUoM5OWOxgqYUKM0/edit?usp=sharing)
- [video playlist](https://www.youtube.com/playlist?list=PLQCcNQgUcDfo-QpRDqzf_3IUOYQ6jnuAo)
- [Bias-Variance decomposition derivation](../../resources/assets/lectures/lec15/lec15-bias-variance-derivation.html)

**Important:** The algebra behind the decomposition of model risk into observational variance, model variance, and bias, is not in the slides or video but is in the link above. You should read it **after** watching this lecture. Also, you may want to review [Lecture 3](http://ds100.org/fa20/lecture/lec03) for a refresher on random variables.

The Quick Check for this lecture is due **Monday, October 26th at 11:59PM.** A random one of the following Google Forms will give you an alphanumeric code once you submit; you should take this code and enter it into the "Lecture 15" question in the "Quick Check Codes" assignment on Gradescope to get credit for submitting this Quick Check.

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
<td><strong>15.1</strong> <br> Variance of random variables. Walking through an alternate calculation of variance. Variance of a linear transformation. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/3W_TtAHxlXQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSeU8a1bVqVtvu82Opw4n3dNlvLpP5JPx6gy6JH1tPFHCAFCJg/viewform" target="\_blank">15.1</a></td>
</tr>
<tr>
<td><strong>15.2</strong> <br> Deriving the variance of a sum. Understanding covariance, correlation, and independence. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/8ovh_lGuMdQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSewRWkZ5vOLbO7zoQbPkiSlkcHJk9s3BW-aBJUpMPyPH9v2Xg/viewform" target="\_blank">15.2</a></td>
</tr>
<tr>
<td><strong>15.3</strong> <br> Variance of an i.i.d. sum. Variance of the Bernoulli and binomial distributions. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/t4gPC6LDS1c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSfvnzx2LeTC4EKK72KEf9LHVhQkuSKsUJuUyCrMbWl9WZ7bRg/viewform" target="\_blank">15.3</a></td>
</tr>
<tr>
<td><strong>15.4</strong> <br> Variability of the sample mean. Reviewing inferential concepts from Data 8, but with the framework of random variables. </td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/CwXhjoBt25I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSce8iejVjmHjlJGUjbw7mbskFVvqDzS6XFe9VZ_c6_DsL_BRw/viewform" target="\_blank">15.4</a></td>
</tr>
<tr>
<td><strong>15.5</strong> <br>Introducing the data generating process and prediction error. Model risk.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/mPz-jIl9H7s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSewQ5vHKA30nkeESdbiCKISmafTtOCurxw1fmpNvd0a3jCi5A/viewform" target="\_blank">15.5</a></td>
</tr>
<tr>
<td><strong>15.6</strong> <br>Looking at different sources of error in our model – observation variance, model variance, and bias – and discussing how to mitigate them.</td>
<td><iframe width="300" height="300" height src="https://youtube.com/embed/mmjYEOeOEM4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSegBG0lw56mX_iiJBLGe7VfT5Hz3b0aVppPuSgcWzDsXliMCQ/viewform" target="\_blank">15.6</a></td>
</tr>
<tr>
<td><strong>15.7</strong> <br>Decomposing model risk into the sum of observation variance, model variance, and the square of bias.</td>
<td><iframe width="300" height="500" height src="https://youtube.com/embed/DEYCRlXvwg4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
<td><a href="https://docs.google.com/forms/d/e/1FAIpQLSesORFx-WhNSODExsb5k_32E0AOYEVqxiOcrarQjyKE75Xyrg/viewform" target="\_blank">15.7</a></td>
</tr>