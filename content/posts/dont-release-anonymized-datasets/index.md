---
author: alper
categories:
  - english
  - internet
date: "2013-05-24T19:00:57+00:00"
title: Don't release anonymized datasets
aliases:
  - /dingen/2013/05/dont-release-anonymized-datasets/

---
There is no thing as an anonymized dataset. Anybody propagating this idea even tacitly is doing a disservice to the informed debate on privacy. Here's a round up with some recent cases.

### Re:publica

Just today Berlin visualization outfit [Open Data City](http://www.opendatacity.de/) published [a visualization of the devices](http://apps.opendatacity.de/relog/) that were connected to their access points during [the Re:publica conference](http://re-publica.de/) earlier this month. The visualization is a neat display of the ebb and flow of people in the various rooms during the event.

It is also a good attempt to change the discourse about data protection in Germany. The discourse tends to be locked in the full stop stance where absolutely ‘nothing is allowed’ without a ton of waivers. Because of that hassle, a lot of things which could be useful are not implemented. A more relaxed approach and a case by case decision on things would be better. In the case of Re:publica there does not seem to be any harm in making this visualization or in releasing the data (here [find it on Fusion Tables](https://www.google.com/fusiontables/data?docid=1i3b4mACuHtSZ3aR9ZFklTSIgpb9o7Y6ySSlyvj4#rows:id=1) where I uploaded it).

What I find to be a disservice to the general debate is the application of ‘pseudonymized’ data where the device ids have been processed with a salt and hash. The identifying characteristics have been removed but the ids are still linked across sessions making it possible to link identities with devices and figure out who was where exactly when during the conference.

http://twitter.com/stefanwehrmeyer/status/337972064306724866

To state again: at a professional conference such as Re:publica there would in all likelihood be no harm done if the entire dataset would be de-anonymized. The harm done is the pretense that processing a dataset in this way and then releasing it with the interlinkage across sessions is a good idea.

Which brings me to my next point.

### Equens

http://twitter.com/AlexanderNL/status/337693480014970880

Yesterday the Dutch company, [Equens](http://www.equens.com/), that processes all payment card transactions announced [a plan to sell these transactions](http://nos.nl/artikel/510009-banken-verkopen-pingedrag-klant.html) to stores. Transactions would be anonymized but still linked to a single card. This would make it trivial for anybody with a comprehensive secondary dataset (let's say [Albert Heijn](http://www.ah.nl/) or Vodafone) to figure out which real person belongs to which anonymized card. That last fact was not reported in any of the media coverage of this announcement which is also terrible.

http://twitter.com/ThijsNiks/status/337699593464709120

After a predictable uproar this plan was iced, but they will keep on testing the waters until they can implement something like this.

Today Foursquare [released all real-time checkin data](http://blog.foursquare.com/2013/05/23/giving-data-nerds-access-to-the-realtime-pulse-of-check-ins-around-the-world/) but with suitable anonymization. They publish only the location, a datetime and the gender of the person checking in. That is how this should be done.

### License plates

Being in the business of opening data we at [Hack de Overheid](http://www.hackdeoverheid.nl/) had a similar incident where a dataset of license plates was released where the plates had been md5'ed without a salt. This made it trivial to find out whether a given license plate was in that dataset.

{{< youtube Bdnwp\_Bq2QA >}}

This was quickly fixed. Again this is not a plea against opening data —which is still a good idea in most cases— but a plea for thinking about the things you do.

### AOL search data

The arch-example of poorly anonymized search data is of course still [the AOL search data leak](https://en.wikipedia.org/wiki/AOL_search_data_leak) from back in 2006. That case has been extensively documented, but not extensively learned from.

Memory online is frightfully short as is the nature of the medium but it becomes annoying if we want to make progress on something. Maybe it would be better altogether to lose the illusion that progress on anything can be made online.

For the privacy debate it would be good to keep in mind that the increasingly advanced statistical inference available means that almost all anonymization is going to fail. The only way around this is to not store data unless you have to or to accept the consequences when you do.
