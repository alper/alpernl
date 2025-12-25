---
_g_feedback_shortcode_212926d71c219ce7496a2ed2a0d89e450c9d857a: |-
  [contact-field label="Name" type="name"  required="true" /]
  				[contact-field label="Email" type="email" required="true" /]
  				[contact-field label="Website" type="url" /]
  				[contact-field label="Message" type="textarea" /]
_g_feedback_shortcode_atts_212926d71c219ce7496a2ed2a0d89e450c9d857a:
  block_template: null
  block_template_part: null
  className: null
  customThankyou: ""
  customThankyouHeading: Your message has been sent
  customThankyouMessage: Thank you for your submission!
  customThankyouRedirect: ""
  hiddenFields: null
  id: 18243
  jetpackCRM: true
  postToUrl: null
  salesforceData: null
  show_subject: "no"
  subject: '[alper.nl] '
  submit_button_text: Submit
  to: alper@alper.nl
  widget: 0
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
  - work
date: "2025-06-05T22:03:50+00:00"
guid: https://alper.nl/dingen/?p=18243
parent_post_id: null
post_id: "18243"
title: ""
aliases:
  - /dingen/2025/06/18243/

---
It's relevant to my interests to read how others have massively scaled the systems we use. Discord has a solid write-up here of how to deal with Elastic Search.

Which is all good and well, but I'm a bit sad that we have so much systems software written in Java which in some cases works well (Kafka, Spring) but in other cases is a bit of a slog (Elastic, Cassandra). There are Rust/C++ search stores out there which out of the box beat a Java solution 2-5x on speed and 1/10th on memory usage. Those are numbers that make a huge difference at scale.

[https://discord.com/blog/how-discord-indexes-trillions-of-messages](https://discord.com/blog/how-discord-indexes-trillions-of-messages)
