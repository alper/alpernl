---
author: alper
categories:
  - english
  - product-design
  - software-engineering
date: "2023-12-11T16:50:13+00:00"
title: ""
aliases:
  - /dingen/2023/12/17346/

---
Notion has formulas now (!) and here's a formula to calculate a Cost of Delay column based on two other columns:

`if(Value=="Killer" && Urgency=="ASAP", "1 Very High", if(Value=="Killer" && Urgency=="Soon" || Value=="Bonus" && Urgency == "ASAP", "2 High", if(Value=="Killer"&&Urgency=="Whenever"||Value=="Bonus"&&Urgency=="Soon"||Value=="Meh"&&Urgency=="ASAP", "3 Medium", if(Value=="Bonus"&&Urgency=="Whenever"||Value=="Meh"&&Urgency=="Soon", "4 Low", "5 Very Low"))))`
