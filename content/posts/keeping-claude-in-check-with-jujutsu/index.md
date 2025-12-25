---
author: alper
categories:
  - english
  - software-engineering
date: "2025-07-25T14:51:12+00:00"
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
