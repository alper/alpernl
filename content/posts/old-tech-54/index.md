---
title: "Annotate"
date: 2005-12-04T16:13:00
author: alper
categories:
  - english
---

I have seen the first place where annotations are useful on [this blog](http://java-boilerplate.blogspot.com) by Reinier.

It is an [annotation which removes the traditional](http://java-boilerplate.blogspot.com/2005/12/annotations-for-getters-and-setters.html) Java getters and setters from the code.

private @Get @Set(Access.PROTECTED) String field;

You end up with something which is very similar to C# Properties but using standard Java syntax.

Another one which is slightly more complex is [MOX, an annotation based XML parser](http://www.zwitserloot.com/java-boilerplate/mox/tutorial.html) (you can [Digg! it](http://digg.com/programming/java_1.5_annotations_-_here_s_why_they_are_useful.) if you like).

I can see where this comes handy, if you need to parse XML in Java. In Python I would usually use something like [xmltramp](http://www.aaronsw.com/2002/xmltramp/) or whatnot.

A cross-platform Javascript solution which provides the same results would be pure heaven. I would have to look into this.

Annotations are dandy to use, but from what I have seen slightly annoying to write (same goes with generics). So we have to wait and leave the heavy lifting to the pros and then we can use the resulting library goodness.