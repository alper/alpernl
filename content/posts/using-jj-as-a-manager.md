---
_g_feedback_shortcode_0b696feb5f243383ccac6464a7a3f30583c48dc4: |-
  [contact-field label="Name" type="name"  required="true" /]
  				[contact-field label="Email" type="email" required="true" /]
  				[contact-field label="Website" type="url" /]
  				[contact-field label="Message" type="textarea" /]
_g_feedback_shortcode_atts_0b696feb5f243383ccac6464a7a3f30583c48dc4:
  block_template: null
  block_template_part: null
  className: null
  customThankyou: ""
  customThankyouHeading: Your message has been sent
  customThankyouMessage: Thank you for your submission!
  customThankyouRedirect: ""
  hiddenFields: null
  id: 18115
  jetpackCRM: true
  postToUrl: null
  salesforceData: null
  show_subject: "no"
  subject: '[alper.nl] Using jj as a manager'
  submit_button_text: Submit
  to: alper@alper.nl
  widget: 0
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
date: "2025-02-26T08:16:21+00:00"
guid: https://alper.nl/dingen/?p=18115
parent_post_id: null
post_id: "18115"
title: Using jj as a manager
url: /dingen/2025/02/using-jj-as-a-manager/

---
I think when people ask what's so great about [jj](https://github.com/jj-vcs/jj) they tend to go deep into things such as [mega-merge strategies](https://v5.chriskrycho.com/journal/jujutsu-megamerges-and-jj-absorb/) and [stacked PRs](https://github.com/lazywei/fj). These things are cool, no doubt, but jj can be useful starting from the very small.

In my case as a manager I commit a lot of small stuff, documentation updates, nits, fixes (and also larger bits of code). I got this down to be pretty fast using all [the git aliases](https://github.com/jhillyerd/plugin-git) available.

In an ideal world I'd be doing most of my work in a worktree (which takes ages to create in our monorepo) and I could pass the change quickly in my clean main checkout folder. That would then go like this:

```
gcb random-new-branch
ga docs.md
gcm "Documentation update" # Or immediately gcam
gpu
```

But of course as a manager, my life is made out of interruptions so odds are that my main checkout folder is not clean and contains changes for something else I started but did not get to finish. Now I have a bunch of bad options:

1. Quickly finish the old work and push it so I can work on the new thing
1. Create a worktree for this tiny thing
1. Stash the old work and risk forgetting about it entirely
1. Think all of the above is too much effort and I'd just rather drop this
1. Go to Github.com and pass the change through the web site (best option if I can do it in one go)

With jj I don't have to deal with most of this. Whenever I have something new I want to work on I can type: ` jj new main` and I'm good to go. Whatever work in progress I might've had, has already been snapshotted and will still be there when I want to resume work on it.

And when it's ready, I can do ` jj git push -c` and it will send my change to our forge without me having to name the branch. I still have to describe the change but all in all jj has turned 4 steps into 2 and removed the potential blockers from this process.
