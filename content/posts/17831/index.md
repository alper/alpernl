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
  id: 17831
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
  - reading
  - science
  - software-engineering
date: "2024-12-31T14:23:39+00:00"
guid: https://alper.nl/dingen/?p=17831
parent_post_id: null
post_id: "17831"
title: ""
aliases:
  - /dingen/2024/12/17831/

---
[Monolith: Real Time Recommendation System With Collisionless Embedding Table](https://arxiv.org/abs/2209.07663)

I didn't get that much from this paper, probably because it's pretty high level and I don't have a strong background in recommendation systems.

The approach is their Cuckoo Hashmap for embedding from which they can update parameters on the fly using existing data engineering pipeline technology.

> Instead of reading mini-batch examples from the storage, a training worker consumes realtime data on-the-fly and updates the training PS. The training PS periodically syn- chronizes its parameters to the serving PS, which will take effect on the user side immediately. This enables our model to interactively adapt itself according to a user’s feedback in realtime.
