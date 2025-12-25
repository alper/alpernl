---
_oembed_f19c9484559190faaf3a2914d402d16a: <iframe title="My Favorite Tiling Window Manager is Finally on macOS" width="660" height="371" src="https://www.youtube.com/embed/u3eJcsa_MJk?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
_oembed_f267611d68506e446b57a7eae7371a9d: <iframe title="Niri Is My New Favorite Wayland Compositor" width="660" height="371" src="https://www.youtube.com/embed/DeYx2exm04M?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
_oembed_time_f19c9484559190faaf3a2914d402d16a: "1761579596"
_oembed_time_f267611d68506e446b57a7eae7371a9d: "1761579596"
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
date: "2025-11-01T18:49:50+00:00"
guid: https://alper.nl/dingen/?p=18420
parent_post_id: null
post_id: "18420"
title: Window Managers
url: /dingen/2025/10/window-managers/

---
Window managers have become a bit of a special interest of mine. After being a Rectangle user for most of my macOS life, I tried out [Amethyst](https://github.com/ianyh/Amethyst) and [Yabai](https://github.com/koekeishiya/yabai) and finally settled on [Aerospace](https://github.com/nikitabobko/AeroSpace).

Aerospace is nice and stable and gets the job done of me never having to manually layout my windows again. I have a couple of layouts that I mainly use and its built-in Spaces are much faster (and therefore much more useful) than the ones macOS gives you.

Turns out that window management is an area under active development both in Linux and on Windows with lots of interesting and experimental window managers now available. Maybe the entire Wayland business is finally paying out a dividend.

The one that piqued my interest the most is [Niri](https://github.com/YaLTeR/niri), a scrolling window manager where windows are laid out on an infinite horizontal strip. The window manager doesn't change the sizes of the windows. What it manages is your position on the strip.

{{< youtube DeYx2exm04M >}}

This looks really cool and an infinite view is an interesting UI paradigm that feels immediately natural.

Niri only runs on Wayland/Linux and [Jwno](https://agentkilo.itch.io/jwno/devlog/871672/scroll-jwno-scroll) is one for Windows. On macOS we never really had that much choice when it comes to ricing and customisation.

I tried [PaperWM.spoon](https://github.com/mogenson/PaperWM.spoon) (derived from [PaperWM](https://github.com/paperwm/PaperWM)) for a bit, which was promising but flaky. Then I thought I might write something myself, but the macOS accessibility APIs are an atrocious undocumented piece of sedimental software. I didn't have the time or energy to power through that mess.

Thankfully other people did have the patience and we have several contenders now:

- [paneru](https://github.com/karinushka/paneru): derived from the Yabai code
- [HyprSpace](https://github.com/BarutSRB/HyprSpace): an Aerospace fork
- [komorebi](https://github.com/LGUG2Z/komorebi): has a macOS port brewing

At the moment I'm still trying them out. Playing a bit with paneru I ran into this layout which is relatively common with sliding window managers:

{{< figure src="/dingen/wp-content/uploads/2025/10/CleanShot-2025-10-24-at-20.29.49@2x.png" alt="" caption="" >}}

What's the point of having a cut off window to your left? I don't see it. The cut-off window may be large or small but it remains entirely a waste of space.

Another issue is that the active window sticks to the left or the right of the screen when swapping its position in the strip. This is a jarring jump back and forth.

{{< figure src="/dingen/wp-content/uploads/2025/10/CleanShot-2025-10-24-at-20.32.47.gif" alt="" caption="" >}}

And finally the lack of animation negates everything that's naturally about a scrolling window manager. I think that may become a deal breaker in general.

HyprSpace was easy to try out since it uses the Aerospace configuration and builds on top of that. The scrolling works and there are some interesting ideas in there but it's buggy and unpolished.

Komorebi I sponsored now to get access to the current build. Getting it to work is fiddly because like more of these tools it depends on [skhd](https://github.com/koekeishiya/skhd) to catch keyboard shortcuts which effectively is abandonware.

Dealing with keyboard shortcuts on macOS and debugging them is its on particular hell. This is made worse if you are a person who has to switch between keyboard layouts regularly.

Komorebi is promising but is also still pretty early stage.

{{< youtube u3eJcsa\_MJk >}}

## Useful layouts

Thinking about how I use Aerospace the only truly useful layouts that I use are the following.

{{< figure src="/dingen/wp-content/uploads/2025/10/CleanShot-2025-10-24-at-21.55.30@2x.png" alt="" caption="" >}}

{{< figure src="/dingen/wp-content/uploads/2025/10/CleanShot-2025-10-24-at-21.56.01@2x.png" alt="" caption="" >}}

{{< figure src="/dingen/wp-content/uploads/2025/10/CleanShot-2025-10-24-at-21.56.12@2x.png" alt="" caption="" >}}

With the smaller windows either side could be a stack so that I can have multiple similarly sized windows behind each other that I can cycle through. I almost never use vertical tiling or any other type of division even on a larger display.

At that point what use would a scrolling window manager be where oftentimes the window to the left or right is cut off?

**Update:** After being clear to myself about the layouts I really need, I wrote a bit of shell that Aerospace calls and cycles through the 33/50/66% layouts: [https://github.com/nikitabobko/AeroSpace/discussions/839#discussioncomment-14792483](https://github.com/nikitabobko/AeroSpace/discussions/839#discussioncomment-14792483)
