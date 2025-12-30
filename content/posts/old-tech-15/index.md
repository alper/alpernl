---
title: "WiFi Goodness"
date: 2005-10-14T15:25:00
author: alper
categories:
  - english
  - delft
  - internet
---

Having just received the new iBook logging in to the WiFi network of our university proved to be somewhat frustrating. Like most univerity networks ours is also completely sealed off with paranoid security restrictions.

To get on the network I had to use some account I had received five years ago and never used ever since. Of course I had forgotten my login details but these were easily obtained.

The second frustration that hit us was that the preferred way of connecting to the wireless network involves a [making a VPN connection](http://luchthaven.tudelft.nl/content/stap5.htm) to the network. The university provides a VPN client by Cisco which looks completely un-Macish and useless. One frustration is that it requires you to retype your password on every connect.

[The website](http://luchthaven.tudelft.nl/) provided by the university implied that it should also be possible to [connect using 802.1X](http://luchthaven.tudelft.nl/content/stap4.htm) but it was not completely clear how to do this. Not wanting to settle for the horror of VPN, I looked further into the [802.1X](http://en.wikipedia.org/wiki/802.1X) issue.

The website also suggest using various proprietary clients to connect using 802.1X but I found out most modern operating systems have it enabled in the network stack. It seems that it is a secure way of connecting to wireless networks which is widely in use on university networks.

I prodded my friend [Reinier](http://www.blogger.com/profile/13753148) via MSN to try it out (I was not on the campus so I couldn't) and after some fiddling he managed to get it to work and gave me a terse instruction how to repeat it.

Now I am at the campus and also have gotten it to work and have made a series of screenshots accompanying the process. These steps seem to work for Reinier and me. They may not all be strictly necessary and you can try to use less options or different settings. YMMV.

In the Wireless menu of your Mac you select the *WLAN* network and then *Open Internet Connect*.

![WiFi Menu](http://static.flickr.com/26/52392929_1bebd524b2_o.png)[](http://www.flickr.com/photos/alper/52392929/)

In Internet Connect choose *File* and then *New 802.1X Connection*.

![New 802.1X Connection](http://static.flickr.com/30/52392928_2bf250aaf8_o.png)[](http://www.flickr.com/photos/alper/52392928/)

In the *802.1X* tab of *Internet Connect* we are going to make a new configuration. Don't worry about the details, we are going to fill these in on the next screen.

![Internet Connect 802.1X](http://static.flickr.com/24/52392927_2ed4ff83b5_o.png)[](http://www.flickr.com/photos/alper/52392927/)

Give your configuration an appropriate name. As the *Network Port* select your AirPort. The *User Name* should be your Service Account User Name + *"@tudelft"* (I have no clue how Reinier figured this out), the *Password* is your Service Account Password. The *Wireless Network* is *WLAN* and for *Authentication* you have to use *TTLS*.

![Edit 802.1X Configuration](http://static.flickr.com/24/52392926_4b1e675096_m.jpg)[](http://www.flickr.com/photos/alper/52392926/)

Next we configure the *TTLS Authentication* to use *PAP* for *Inner Authentication* and *anonymous@tudelft* for Outer Identity.

![Configure TTLS Authentication](http://static.flickr.com/29/52392925_56d997bca1_m.jpg)[](http://www.flickr.com/photos/alper/52392925/)

That's it. Your WiFi internet should be ready to go and you never have to use a stinking VPN client anymore.