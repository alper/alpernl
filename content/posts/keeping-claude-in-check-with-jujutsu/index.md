---
_g_feedback_shortcode_aa224b1b1bcd705c3e3b8dd1d69e78f827d90b07: |-
  [contact-field label="Name" type="name"  required="true" /]
  				[contact-field label="Email" type="email" required="true" /]
  				[contact-field label="Website" type="url" /]
  				[contact-field label="Message" type="textarea" /]
_g_feedback_shortcode_atts_aa224b1b1bcd705c3e3b8dd1d69e78f827d90b07:
  block_template: null
  block_template_part: null
  className: null
  customThankyou: ""
  customThankyouHeading: Your message has been sent
  customThankyouMessage: Thank you for your submission!
  customThankyouRedirect: ""
  hiddenFields: null
  id: 18270
  jetpackCRM: true
  postToUrl: null
  salesforceData: null
  show_subject: "no"
  stepTransition: fade-slide
  subject: '[alper.nl] '
  submit_button_text: Submit
  to: alper@alper.nl
  widget: 0
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
date: "2025-07-25T14:51:12+00:00"
guid: https://alper.nl/dingen/?p=18270
parent_post_id: null
post_id: "18270"
title: Keeping Claude in check with Jujutsu
aliases:
  - /dingen/2025/07/keeping-claude-in-check-with-jujutsu/

---
I've found it very useful to use [jj](https://github.com/jj-vcs/jj) to continuously and automatically snapshot the changes that Claude makes. This way if it does anything that I didn't want, it's incredibly easy to undo it and still keep a clean history.

Here's what my hackathon project looks like in the [gg](https://github.com/gulbanana/gg) client after several days of on and off development.

{{< figure src="CleanShot-2025-07-25-at-16.41.13@2x.png" alt="" caption="" >}}

You can have Claude do these steps as well. It's pretty good at `jj describe` even if a bit verbose. And in most cases it could also do `jj new` before every change, something that I forget occasionally.

I didn't bother with that because it will mess up the exact ordering of commands and then I'll be busy sorting out which edits should go into which change. Having the change viewer side by side with the Claude Code terminal gives me the most control and oversight.

This way my flow is:

- `jj new`
- Ask Claude Code to do something
- Check the output in gg
- Have Claude Code iterate
- Have Claude Code do the `jj describe`
- Either `jj new` or `jj abandon` depending on whether I think the result is going somewhere

I think at this point I kinda forgot how I would do this in git and I'm also not particularly interested in learning it anymore either.
