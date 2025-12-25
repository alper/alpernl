---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
date: "2009-01-05T15:11:24+00:00"
guid: http://alper.nl/dingen/?p=640
parent_post_id: null
post_id: "640"
title: Widget distribution and other considerations
aliases:
  - /dingen/2008/12/widget-distribution-and-other-considerations/

---
I am currently busy doing a project together with [Tam Tam](http://www.tamtam.nl) where we are tasked with developing a set of five widgets for Dutch government (assigned by the [Dutch Ministry of Home Affairs and Kingdom Relations](http://www.minbzk.nl)) as a proof of concept of how government data can be used. We're developing widgets mostly because they are seen as modern, easy to develop and they can be deployed very near to users.

As a prerequisite for building these widgets, we need to work on the data sources to make them easier to use and better fitting to the available data and potential uses. Getting these data sources sorted out also provides a longer term benefit for any other party who would be interested in using this data. Our widgets are but one potential implementation in a realm of possibilities. Anybody can take the data source the widgets use and make something different and/or better. That vision is beyond the scope of this current project but it is also being worked on.

For this project we need to find a way to develop widgets which are deployable to a multitude of platforms with as much ease as possible. There are far too many widget platforms out there, as can be seen in [this presentation by Niall Kennedy](http://www.niallkennedy.com/blog/2008/11/syndication-widgets-strategy.html) and because this is a Dutch project there is [an elephant in the room](http://www.hyves.nl) we have to take into account.

### Data sources

The data sources we got were already halfway there. Some were not machine readable, those that were, were either not very well formed or did not include as much data as one would like. We filed change requests for some modifications but these move slowly in some cases. The data sources we are going to use and republish would ultimately be:

- RSS, preferrably well formed [Atom](http://tools.ietf.org/html/rfc4287) and in some cases [RSS 2.0](http://cyber.law.harvard.edu/rss/rss.html) with media enclosures and/or geodata
- [iCalendar](http://en.wikipedia.org/wiki/ICalendar) (or xCal ((xCal seems to be mostly obsolete but it is still referenced and used in various places viz. translator, Upcoming feeds etc.))) probably wrapped in RSS
- generic XML or simpler still (CSV, TXT)

### Personal vs. Public Dashboard

For widgets there are two major contexts in which they are run, either on personal dashboards such as [iGoogle](http://www.google.com/ig) or [Netvibes](http://www.netvibes.com/) (or on public versions of these but dashboards nevertheless), but much more interestingly on social networking profile pages as a display of identity.
[![](http://img.skitch.com/20081216-t1g7yejjr343ifjgfi4b9nfx3f.png)](http://img.skitch.com/20081216-t1g7yejjr343ifjgfi4b9nfx3f.png)[![](http://img.skitch.com/20081216-jngyace421mps5fdr18djds2xs.png)](http://img.skitch.com/20081216-jngyace421mps5fdr18djds2xs.png) Ideally the widgets would work on both, though the uses of some of the data sources do not lend themselves well to be displayed on public vanity pages. Nevertheless being able to deploy widgets to both would be very welcome.

Taking the greatest common divisor of platforms restricts our set of functionality. There may be specific API methods available on each platform —most notably the social APIs exposed in the social networking platforms ((I'll talk more about [OpenSocial](http://code.google.com/apis/opensocial/) later on.))— which would enable us to make socially aware widgets. Incorporating sociality and the notion of a specific user is beyond the scope of this project. We most probably will rely on the cross platform nature of the client side and rely on the platform to supply us with a HTML rendering environment.

### Important target platforms

 [Clearspring](http://www.clearspring.com/) has [a list of ‘drop targets’](http://www.clearspring.com/docs/tech/widget-dev/drop-targets) which is pretty large. Because this is a project by the Dutch government and it is principally aimed at the Dutch public, we need to cover the online places that Dutch people use a lot first and foremost. This mostly means that we are not so interested in Orkut and Hi5 but more so in [Hyves](http://www.hyves.nl/) and [MSN Live](http://home.live.com/) ((Or whatever its brandname du jour.)).
[![](http://img.skitch.com/20081216-dtygdx6gd4j9n5tjwk83njq65y.png)](http://img.skitch.com/20081216-dtygdx6gd4j9n5tjwk83njq65y.png)
Hyves has a coverage of about 5M people in the Netherlands, MSN messenger and by extension the entire MSN platform should be bigger than that. This alone makes them very important to support and test for.

### Considerations

The government has some additional considerations which need to be taken into account when choosing a platform and or a technology.

- Dutch government tries to adhere to open standards and open source software wherever possible. This is not a hard requirement but it does influence decisions as far it is practical do so.
- Dutch government should strive to be independent of commercial partners and definitely should not mix commercial branding with governmental information.
- We need to consider a wider growth path towards the future so sustainability and scalability of efforts and platforms are considerations.
- In some cases exerting tight control over appearance and functionality of a widget may be desired.

### Platforms

There are a number of technology platforms that can be used when developing a widget. Each of these has its own advantages and disadvantages and implications for eventual deployment.

FlashAny platform that allows the use of embed codes in the HTML is a suitable host for [Flash](http://www.adobe.com/products/flash/index_fl.html) widgets. This type of widget is very popular mostly due to its ease of development and deployment, and full graphical control within the widget. Disadvantages are that ease of modification and reuse are severely limited because the platform is not very open and well known (at least not as well known as HTML), which will deter reuse and remix of widgets in the future.
After some deliberation we chose not to use Flash. Creating or reusing Flash widgets necessitates the use of [an expensive authoring environment](http://www.adobe.com/products/flash/). This does not fit into the widest possible reuse, either within government or outside of it. Most of our data sources also mandate more text based and less graphical widgets, so Flash is not strictly necessary. And finally anybody who wants to make a Flash widget can embed it into any of the chosen technology platforms without any problems. Straight HTML and JavaScriptA widget is a piece of a webpage and it happens to be that a (piece of) a webpage can also be used as a widget. Any webpage that displays a very specific piece of functionality on a limited amount of screen can function as widget.
Allowing the upload of a simple HTML page and wrapping that in an <iframe> or similar is the approach taken by some platforms and it works quite well. An advantage is that the widget may be rendered by a fragment of the same template that rendered the main webpage. Disadvantages are that the widget is not aware of its surroundings and does not have a way to set or retrieve settings. iGoogle GadgetAn [iGoogle Gadget](http://www.google.com/ig/directory?hl=en&type=gadgets) is a web page as described above wrapped in an XML document with some metadata extensions and a wrapper around some javascript calls to provide settings functionality and proxied XMLHttpRequest ((Being able to get data from arbitrary websites is normally restricted because of security considerations.)).OpenSocial GadgetAn [OpenSocial Gadget](http://code.google.com/apis/opensocial/) is an extension of the iGoogle gadget platform with some social extensions to the API which make a gadget aware of its social surroundings (logged in user, profile user, friend list) and allows gadgets to send messages to various activity streams. An iGoogle gadget will run in an OpenSocial container and essentially function as an OpenSocial gadget without social functionality.Netvibes UWAThe [Netvibes Universal Widget API](http://dev.netvibes.com/) is a way of creating a straight HTML page in such a way that it can be recompiled and served to a series of target platforms. There are some metadata extensions which have to be followed, the scripting environment is both extended to include settings and sizing, and the DOM is severely crippled ((Not being able to use document.getElementById() is something of a pain.)). The UWA relies on the fact that most widget runtimes are de facto HTML rendering environments with many similarities and bridges the differences.
Just this week [Netvibes announced the release of an OpenSocial compliant UWA](http://dev.netvibes.com/blog/2008/12/12/uwa-now-supports-the-opensocial-api/) which should make UWA widgets run on any OpenSocial container and make Netvibes itself also an OpenSocial container. A release of this new version is still forthcoming. Facebook[Facebook](http://www.facebook.com) applications need to be written in the [FBML](http://wiki.developers.facebook.com/index.php/FBML) which is specific to Facebook. There are some widget distribution options which wrap a widget and republish it as a Facebook application but currently Facebook is not a large priority for this project.Sprout[Sprout](http://sproutbuilder.com/) is a very interesting platform which provides [a web based Flash widget builder](http://sproutbuilder.com/) where anybody can very easily use drag an drop to build their own widget from standardized elements (no programming required) with both simple controls and complex ones backed by outside data sources. The provided set of elements should cater to most needs, but being able to modify and build additional controls would have been very nice.
For this project it may not be the best starting point but if we make our data sources clean and standard, anybody can plug them into [the Sprout Builder](http://sproutbuilder.com/) and rapidly build their own versions of our widgets.[![Widget Diagram](http://farm4.static.flickr.com/3261/3131122512_c216824c97.jpg)](http://www.flickr.com/photos/alper/3131122512/) I have made a diagram ( [PDF](widget-diagram.pdf)) summarizing the various options, platforms and eventual deployment targets in the widget landscape. This diagram is not complete but it gives a good impression of the complexities involved.

### Test application

To define a simple test application to write and run on the various runtimes. The application should:

- Display some HTML
- Use custom CSS to style the elements
- Be able to display images
- Be able to retrieve RSS/XML data from the same server
- Be configurable with user preferences

And some softer requirements:

- Be able to embed Flash content
- Be aware of its own dimensions
- Respond to resize and refresh actions of the widget platform

![](http://img.skitch.com/20081216-crwky6wq1td7bxibxmb7uc7k4i.png) Here is the test application as [a plain HTML file](/ajax/widgetproject/base/widget.html), a version which should run on the [iGoogle platform](/ajax/widgetproject/iGoogle/widget.html) and a version for the [Netvibes UWA](/ajax/widgetproject/netvibes/widget.html). It looks quite horrible because it does not have proper styling, but it does most of the things listed above. Translating the base HTML version to the specific platforms was not too difficult, but somewhat idiosyncratic. There are some specific metadata elements which need to be accounted for, the DOM is altered in some cases and there are platform specific calls for XMLHttpRequests that use a local proxy to retrieve data. What is immediately apparent when working is that the [documentation on the Google platform](http://code.google.com/apis/gadgets/docs/overview.html) is far more comprehensive.

This test application was then run on the various platforms and galleries where applicable to see if it would work and what the options for redistribution per platform were. The experiences of these tests have shaped our impressions of the various distribution options. Our findings are discussed in the next section.

### Galleries

Galleries sometimes have widget building options but most of them are concerned with spreading a widget to as many platforms as possible and monitoring the reach of the widget. Important considerations when picking a gallery (if any) are:

- the input options, what kind of widgets this gallery will accept
- the output options, to what platforms can this gallery spread a widget
- look and feel of the gallery and of the widget wrapper

Netvibes[![](http://img.skitch.com/20081216-gdr3qdtnsgqn571he272yfjjh.png)](http://eco.netvibes.com/)
The [Netvibes ecosystem](http://eco.netvibes.com/) provides a way for people to browse widgets submitted to the ecosystem and install them to either Netvibes or to a number of other platforms. The gallery also shows an install count per widget.
The Netvibes ecosystem accepts: UWA widgets, iCal files, SWF files.
The Netvibes ecosystem publishes to: a blog, iGoogle (install and gallery submit), Vista, Live, Dashboard and seems to work all right. Clearspring[![](http://img.skitch.com/20081216-gpdssi555ufajj6b9tdgej4usy.png)](http://www.clearspring.com/)[Clearspring](http://www.clearspring.com/) is a generic widget gallery service with methods to widgetize page content and completely manage a widget.
Clearspring accepts: SWF, HTML, Javascript (not very clear how this would work) and Image widgets.
Clearspring exports to too many platforms to mention, notably: Blogger, embed, iGoogle, Live, Dashboard, Wordpress, delicious, e-mail, Facebook, Netvibes, Typepad. Clearspring can also publish directly to the Netvibes, Live and iGoogle galleries.
The options look fairly good but the inwidget functionality borders the widget with an ugly border through which the functionality to add the widget to other platforms is implemented. GigyaCan't really get [Gigya](http://www.gigya.com/) to work. It looks mostly focused on Flash widgets but the site is a mess and the documentation is very sparse.Widgetbox[![](http://img.skitch.com/20081216-tscktq5ds5nnrwcq4uahkxrfuc.png)](http://www.widgetbox.com/) [Widgetbox](http://www.widgetbox.com/) is a partner of Netvibes
Widgetbox accepts: Flash, HTML+Javascript pasted or remote, Atom/RSS, Google Gadget
Widgetbox exports and shares with some platforms such as Blogger, Netvibes, iGoogle and Wordpress.
A Widgetbox wrapper also includes a very ugly border button that enables visitors to add the widget to their platform of choice. Widgadget[Widgadget](http://www.widgadget.com/) has severely limited creation and publication option, documentation is sparse.Spring Widgets[Spring Widgets](http://www.springwidgets.com/) offers an SDK for Flash based widget development and seems to be exclusively focused on Flash widgets.Various OpenSocial sites ( [Hyves](http://www.hyves.nl), [LinkedIn](http://www.linkedin.com), [Ning](http://www.ning.com)) have their own galleries for applications and their own policies on which to include. Most of these sites also have sandboxes where inputting the address to the gadget.xml file suffices to run an application. Hyves for instance has to give their approval of your gadget before it is included in the site.
[![](http://img.skitch.com/20081216-11an6jdkpa7cdfpdqjkahw1y2.png)](http://www.hyves.nl/gapsb/) On the subject of galleries our clients remarked that the appearance of control and non-commerciality needs to be maintained. Widget galleries which are all too present on the widget and exert a lot of control are not preferred. It is completely undesirable (and understandably so) to see the Clearspring logo mixed with government branding and data. So because galleries are not essential, they are mostly out of consideration for now.

### Conclusion

During a final meeting based on this research, we presented our findings and got some more input as to in which direction we should focus and the consequences that would have on our final platform choice.

#### HTML vs. Flash

Using HTML in favor of Flash proved to be contentious but the compromise was chosen to have the basic functionality of widgets be done in HTML markup. Interested parties can always have a Flash widget developed and embed that in a chosen technology platform or use it standalone.

#### Platform choice

Based on the techology choices and the platforms that it definitely should run on: iGoogle, Hyves, LinkedIn, Ning our choice of platform is quickly reduced to either UWA or iGoogle. UWA widgets can already be compiled to iGoogle gadgets and with the upcoming release of the next version they should also more easily run as OpenSocial apps, but this version has not been released yet. The coyness of the Netvibes team ((They announced the new version of UWA at LeWeb '08 but offer nothing but vague promises when asked for the actual code.)), together with the sparsity of their documentation makes you wonder if this latest release of OpenSocial support ((Which had already been promised a long time ago.)) isn't a last ditch attempt to regain relevancy. For all we know Netvibes may cease to exist tomorrow, so sustainability is certainly a question.

On the other side if we choose for iGoogle gadgets to be the widget platform of choice, it will run on most of our target platforms and with the new version of Netvibes it will also run in their OpenSocial container. The only thing that we will not be getting are Netvibes recompilation options for Dashboard and Vista ((How hard would it be to build an OpenSocial container to run in Dashboard?)). iGoogle/OpenSocial looks like the platform with the most momentum and momentum is worth a lot.

#### Genericity

There is a strong desire to make the widgets in the project as generic as possible to enable reuse for other applications. At a certain point there was the idea that we could make one widget to do everything, this however is not really advisable.

We defined a set of widget archetypes (news, events, images, videos, geodata, calculation, infodisplay) where a widget may fall into and we think that for the future it would be useful to have reference implementations of each archetype on file so that a request for a new widget can quickly be fulfilled by taking an archetype widget and customizing that.

For this project though, we will be making specific widget implementations which can be easily generified to their archetype. So after we make a branded news widget, any interested party can swap in the RSS feed and their own logo to make it theirs. We thought it would fit better in the modest scope of this project to deliver conclusive results instead of half-finished products.

#### Gallery

Given this choice of base platform, if we were to use a gallery to ease distribution and monitor its reach, we would probably use [Clearspring](http://www.clearspring.com) because it seems to be the most mature and functional of the lot (Clearspring is also used by the CBC (see [their presentation](http://widgetsummit.com/2008/sessions/canadian-broadcasting-corporation/) at the Widget Summit)) with Widgetbox as a close contender. But because of the all too visible branding of Clearspring and other containers, we will not be using either ((It's not a bad question to ask how we then defend the choice of Google for instance, but OpenSocial is [a relatively open platform](http://incubator.apache.org/shindig/).)).

#### Call for comment

Fortunately we do not have to make a definitive choice right now. For our set of widgets we will first be designing the functionality and doing some reviews. After that the basic functionality of the widget will be prototyped in HTML and finally the HTML will be modified to run on the target platform(s) of our choosing.

We're not committed yet, so some of our choices are still open and most of it is up for debate. If you have any questions, additions or things we have missed in our survey, we would love to hear from you in the comments.

**Update:** Though not visible on [the site](http://www.springwidgets.com/) yet, [Techcrunch reports](http://www.techcrunch.com/2009/01/10/fox-interactive-media-to-shut-down-flektor-and-springwidgets/) that Spring Widgets will be shutdown by Fox Interactive.

**Update:** Sprout Builder recently announced [a pricing model](http://sproutinc.com/pricing?utm_source=Sprout+Users+%28with+3+or+fewer+sprouts%29&utm_campaign=cd5add2ea2-Sprout_Builder_Pricing_Announcement1_14_2009&utm_medium=email) to their up until then free service.

**Update:** The overview overlooked [the yourminis widget publishing](http://www.yourminis.com/) platform. Yourminis takes SWF files and distributes these to a number of platforms.
