---
title: "Tableless"
date: 2006-08-18T11:40:00
author: alper
categories:
  - english
  - internet
---

Desiging websites without tables is still too difficult and both counter-intuitive and counter-productive to be a realistic alternative for the vast majority of people.

The people who insist on tableless designs are sadist zealots who should come out and play in the real world. As long as there is no decent standards or tool support, ditching tables is impractical.

I just came upon two cases which are quite difficult if not impossible to handle without tables. I would like to be proven wrong.

- **Vertical Centering**

There is a [solution to vertical alignment](http://www.jakpsatweb.cz/css/css-vertical-center-solution.html) using CSS but getting that to work cross browser is so hackish and uses superfluous markup.

Using the valign="center" property of a TD element accomplishes the same task easily.


- **Full height columns**

One of the most standard layouts is the three column layout where all columns are stretched vertically to match the length of the tallest column. This fundamental markup element is impossible to achieve using CSS.

[PPK suggests a script example](http://www.quirksmode.org/dom/3column.html) which fixes it by reading the height value of the tallest column and setting the heights of the other columns appropriately.

Though I appreciate the script, I don't think it is a very sound semantic layout practice to use behavioural script to fix presentation. Furthermore, the script is as of yet too quirky for real use.

Three columns are pretty easy to do using a table with one row and three cells. So why bother with more complicated solutions?

**[Dojo](http://dojotoolkit.org)** of course makes most of these problems go away with its [LayoutContainer](http://archive.dojotoolkit.org/nightly/tests/widget/test_LayoutContainer.html) but I'm not ready yet to make my simple web page into a full blown dojo application.