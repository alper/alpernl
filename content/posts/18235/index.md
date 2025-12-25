---
  [contact-field label="Name" type="name"  required="true" /]
  				[contact-field label="Email" type="email" required="true" /]
  				[contact-field label="Website" type="url" /]
  				[contact-field label="Message" type="textarea" /]
  block_template: null
  block_template_part: null
  className: null
  customThankyou: ""
  customThankyouHeading: Your message has been sent
  customThankyouMessage: Thank you for your submission!
  customThankyouRedirect: ""
  hiddenFields: null
  id: 18235
  jetpackCRM: true
  postToUrl: null
  salesforceData: null
  show_subject: "no"
  subject: '[alper.nl] '
  submit_button_text: Submit
  to: alper@alper.nl
  widget: 0
author: alper
categories:
  - english
  - software-engineering
date: "2025-05-27T06:00:25+00:00"
guid: https://alper.nl/dingen/?p=18235
parent_post_id: null
post_id: "18235"
title: ""
aliases:
  - /dingen/2025/05/18235/

---
I fully agree with Paolo Scanferla here that very complex typing ("hyper-typing") is an impediment to get anything done but besides the technical aspects, here are some ratchets here that are very pernicious.

1. Creating very complex typing is hard to argue against ("But don't you see how this is safer?") and simplicity rarely wins in group programming environments. You're essentially arguing against somebody who's posturing as being very clever ("It's very easy and safe this way.").
1. Once you lose the initial argument and the complexity gets in, it's impossible to get out again. It will only expand in your code base and make everything it touches also overly complex. Getting this out is several orders of magnitude more work than getting it in and can only be done by (the very few) people who understand the entire thing. Those people have made an excellent manoeuvre for their own job security and against everybody else's productivity.
1. This kind of typing is not incidental. The very design of Typescript and its increasingly more and more complex type system is meant to enable this. Language features that are there will always be used and regularly misused. It's near impossible to guard against that. That's why I consider any language with an overly expressive type system to be suspect (and this is why Go is good). Liking Typescript is a code smell on the person.

[https://pscanf.com/s/341](https://pscanf.com/s/341)
