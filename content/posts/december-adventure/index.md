---
_g_feedback_shortcode_0a80da33ffe91532df99e45f253cad89dd7fa760: |-
  [contact-field label="Name" type="name"  required="true" /]
  				[contact-field label="Email" type="email" required="true" /]
  				[contact-field label="Website" type="url" /]
  				[contact-field label="Message" type="textarea" /]
_g_feedback_shortcode_atts_0a80da33ffe91532df99e45f253cad89dd7fa760:
  block_template: null
  block_template_part: null
  className: null
  customThankyou: ""
  customThankyouHeading: Your message has been sent
  customThankyouMessage: Thank you for your submission!
  customThankyouRedirect: ""
  hiddenFields: null
  id: 17749
  jetpackCRM: true
  postToUrl: null
  salesforceData: null
  show_subject: "no"
  subject: '[alper.nl] December Adventure'
  submit_button_text: Submit
  to: alper@alper.nl
  widget: 0
_wpas_done_all: "1"
author: alper
categories:
  - berlin
  - english
  - food
  - software-engineering
  - travel
date: "2024-12-02T23:44:02+00:00"
guid: https://alper.nl/dingen/?p=17749
parent_post_id: null
post_id: "17749"
title: December Adventure
url: /dingen/2024/12/december-adventure/

---
So I felt I couldn't really bring myself to do [Advent of Code](https://adventofcode.com) this year since I have more than enough other things to do (and [watch](https://en.wikipedia.org/wiki/Arcane_(TV_series)) and [play](https://store.steampowered.com/app/333640/Caves_of_Qud/)) and with work and the kids, it's always pretty miserable to keep up.

I saw this thing called [December Adventure](https://eli.li/december-adventure) though and that fits in nicely with my current push to release a major update for [Cuppings](https://cuppin.gs). If I'm going to be programming until late this month, then I'd prefer it to be on something that I can release.

I can't promise that I won't do any AoC ( [Factor](https://factorcode.org) is looking mighty cool) but I won't force myself to do anything. With that, let's get going.

### 1/12

I started working on the map view which clicking around looked like it could be really annoying. I found some dead ends and was afraid I'd have to hack in Leaflet support myself but I found a [dioxus example](https://github.com/slowtec/leaflet-rs/tree/master/examples/leaflet-dioxus-example) hidden in the [leaflet-rs](https://github.com/slowtec/leaflet-rs) repository.

Yes, I'm writing this website in Rust/WASM, why do you ask?

That example required a bunch of fiddling with the configuration and a couple of false starts, but now I have a vanilla map view.

{{< figure src="CleanShot-2024-12-02-at-23.03.35@2x.png" alt="" caption="" >}}

I can say that I'm amazed that in this ecosystem 1. an example exists 2. that example works 3. it works in my project with a bit of diffing and 4. it seems to do what I need.

I raised a PR to the project to advertise this example on its README just like it does the others so that others wouldn't have to search like I did. That PR got merged:

[https://github.com/slowtec/leaflet-rs/pull/36](https://github.com/slowtec/leaflet-rs/pull/36)

### 2/12

Today I'll see if I can tweak the map view to show the location of the cafe we tapped and get things to a point where I can commit the change.

To do this I need to figure out how to pass information along to a [router](https://dioxuslabs.com/learn/0.5/reference/router/) when we tap a venue. That should be easy enough but the Dioxus documentation is between 0.5 and 0.6 now and a lot of it is broken.

A tip from the Discord said I need to put the data into a [context](https://docs.rs/dioxus-hooks/latest/dioxus_hooks/fn.use_context.html) from a parent and then get it out again in a child. It's a bit roundabout and required some refactoring, but it works.

{{< figure src="CleanShot-2024-12-03-at-00.40.01.gif" alt="" caption="" >}}

Done on time even for a reasonable bed time.

### 3/12

Turns out my changes from yesterday did not make it to the staging server. I'll fix that and manually run the job again.

That's these annoying wasm-bindgen version errors that keep happening and that require a reinstall of this: `cargo install -f wasm-bindgen-cli --version 0.2.97` and the `dioxus-cli`. Dioxus which by the way is preparing its [long awaited 0.6.0 release](https://github.com/DioxusLabs/dioxus/releases/tag/v0.6.0-rc.0).

Yes, I build this on the same Hetzner box that hosts it. So here you go: [https://staging.cuppin.gs](https://staging.cuppin.gs)

Other than that not that much will happen today since I spent most of the evening noodling around with [Factor](https://factorcode.org) (despite my intention not to do any weird programming). It's a nice language that's very similar to [Uiua](https://www.uiua.org) which I tried out a while back but not being an array programming language makes it feel somewhat more ergonomic.

### 4/12

I can't describe how nice it is to wake up and not have to deal with a [mediocre story line involving elves](https://adventofcode.com) and try to find time to attack a programming problem.

After today, I'm going to need that quiet morning, because I spent until 01:30 debugging an issue: Going to a detail view from the frontpage worked, but loading a detail view directly would throw an error.

There were two issues at play here:

Leaflet maps don't deal well with being created multiple times so either we have to call \` `map.remove()` or we have to check whether the map has already been created and keep a reference to it somehow.

I solved it by pushing the map into a global variable:

```
thread_local!(static MAP: RefCell> = RefCell::new(None));
```

These are Rust constructs I would normally never use so that's interesting. More interesting is that they work in one go and that they work on the WASM target.

Then the error was gone but the page was blank. Not entirely sure what was happening I poked at the DOM to see all the map elements there but simply not visible. Turns out that because of the different path, the path for the stylesheet was being added to the URL like this: **http://127.0.0.1:8080/venue/176/main.css**

It just has these two lines:

```
#map {
    width: 100%;
    height: 100vh;
}
```

But without a height the map is invisible.

Both issues are solved but not committed. I'll see tomorrow whether I'm happy with the solution and how to package this up. Also I'm not sure how `main.css` is being served on production and whether the same fix will work there.

### 5/12

I couldn't help but noodle on Advent of Code a bit. Here's my day 1 part 1 in Factor: [https://github.com/alper/advent-of-code/blob/main/2024/day-01/day-01.factor](https://github.com/alper/advent-of-code/blob/main/2024/day-01/day-01.factor)

I like Factor the programming language. It's like Lisp or Haskell but without all the annoying bits.

The environment that's provided with it, I'm not so keen about. It's annoying to use and has lots of weird conventions that aren't very ergonomic.

### 6/12

I've been bad and I've finished part 2 of day 1 of the Advent of Code: [https://github.com/alper/advent-of-code/blob/main/2024/day-01/day-01.factor#L27](https://github.com/alper/advent-of-code/blob/main/2024/day-01/day-01.factor#L27)

Not so December Adventure after all maybe. I'll promise I'll finish the mapping improvements I was working on tomorrow.

### 7/12

Went on my [weekly long bike ride](https://www.strava.com/activities/13065783170). Then in the evening I didn't have that much energy for programming other than finishing Advent of Code day 3 part 1: [https://github.com/alper/advent-of-code/commit/0a74c38e7641141e10b4c48203c9e414cc492e1c](https://github.com/alper/advent-of-code/commit/0a74c38e7641141e10b4c48203c9e414cc492e1c)

(I looked at day 2 part 2 but that just looked very tedious.)

### 8/12

Got in a ton of commits on Cuppin.gs today. After fixing the map, I wanted to see what would happen if I would add all 2000 markers to the map.

{{< figure src="393608699-a57c484d-e12f-4dc7-ade8-ea39df95d2cc.png" alt="" caption="" >}}

Performance seems to be doable but this is probably not ideal for a webpage. Dynamically rendering the venues is something for later. For now I can probably get away with filtering for the 100-200 nearest locations by distance and dumping those into the map view.

Now I'm back debugging Github Actions. I'm splitting up the build and deploy of the backend and the frontend into separate actions. Compiling [dioxus-cli](https://github.com/DioxusLabs/dioxus/tree/main/packages/cli) takes forever which is a step I hope I can skip with [cargo-binstall](https://github.com/cargo-bins/cargo-binstall).

Iterating on Github Actions takes forever and there really doesn't seem to be a better way to develop this or a better CI solution that everybody is willing to use.

### 10/12

Spent some hours massaging the data that goes into the app. I had to add all new venues and after that I wanted to check whether any place in our 2k venue set had closed so we can take them off the display. This is a somewhat tedious multi-step process.

I have an admin binary that calls the Google Maps API for each venue to check the venue data and the business status (CLOSED\_TEMPORARILY and such). But to be able to do that you have to feed each place ID into the API. The only issue with place IDs is that they expire from time to time. There's a free API call that you can use to refresh them.

That expiration does not happen that often. What happens more, I found, is that a place will disappear entirely of Google Maps. For some reason it will be deleted. I don't handle that case yet so there my updaters break entirely and the quickest fix around it is to delete the venue from the database and restart.

The only data issue that I still have outstanding is when venues move their location to a different address. I have [a place around here](https://www.westberlin-bar-shop.de) that I think is still showing on its old spot.

### 11/12

Tried to run Cuppings in Xcode to be met with some weird compilation errors. Turns out that there's an Expression type in Foundation that's overriding my `SQLite.swift` Expression. It's a pretty silly reason for code to be broken: [Expression - name space conflict with Xcode 16/iOS 18](https://github.com/stephencelis/SQLite.swift/issues/1269)

Also still fighting with the frontend deployments which seem to need a `--` frozen passed to them to not proactively go update package versions.

### 14/12

Love to have a crash on startup for the Cuppings TestFlight build and then sit down today to bake a new one and upload that and for that one to work. No clue what the issue was even though I took a look at the crashlog (that I sent in myself).

I've also automated building the iOS app to be done by Xcode Cloud which should making new versions (whenever the database is updated) a lot easier.

### 16/12

Upgraded the frontend to [Dioxus 0.6.0](https://dioxuslabs.com/blog/release-060/) which just came out and has lots of quality of life issues. For my case, I did not need to change a single line of code, just change some version numbers and build a new `dioxus-cli`.

{{< figure src="CleanShot-2024-12-17-at-00.56.51@2x.png" alt="" caption="" >}}

I hope that maybe solves the `wasm-bindgen` issues on the frontend deploy. The annoying part about the build is that it takes so long that it's very hard to iterate on.

It's too late even for me to see what this does. I'm off to bed. You may or may not get a new version of the website by tomorrow morning.

### 18/12

Spent some iterations running the frontend deploy and rerunning it but now it should be working.

### 22/12

I spent the evening doing manual data munging and correcting some venue locations that hadn't been updated correctly through my data life cycle.

That forced me to clarify the two name fields the `venues` table has.

- `name` was the original name field and was pulled from the Foursquare metadata
- `google_name` is the name field that's pulled from Google Maps and was effectively leading but not updated correctly yet when refreshing the data

{{< figure src="CleanShot-2024-12-24-at-08.45.11@2x.png" alt="" caption="" >}}

So to figure that out I did a bunch of auditing in the list to see venues where there was a large discrepancy between the names. Something that happens is that a place will change its name but keep the same location and Google Maps place.

I also added a label to the iOS app to indicate whether this is a `DEBUG` build but that messed up the layout and I guess I might as well remove it. Sometimes I get confused what I'm running, but since it's just me running `DEBUG` builds on their phone, I think I can do without.

I also started a rewrite that I'm not sure I'm going to pull over the line: I wanted to remove the search dependency on [Alpine.js](https://alpinejs.dev) and replace it with [htmx](https://htmx.org). For this I asked Cursor to do the translation which it did a stab at but ultimately rather failed to do even the basic steps for it. Then I did it myself and while htmx is super easy to setup, the data juggling I have to do with what I get from Google Maps is very fragile and needs to be cleaned up (which I may or may not do given that things are working right now).

### 23/12

Working with the backend was very annoying because every time the server restarts, it would log me out. To fix that I changed the persistency of [tower-sessions](https://github.com/maxcountryman/tower-sessions) from MemoryStore to [FileSessionStorage](https://github.com/mousetail/tower-sessions-file-store) and that fixed it without issues. There is now a `.sessions` folder in the backend which needs to be ignored for `cargo watch` but other than that it's a drop-in replacement.

That means I will need to write a logout view at some point.
