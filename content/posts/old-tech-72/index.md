---
title: "30 Second Dojo"
date: 2006-01-01T18:36:00
author: alper
categories:
  - english
---

I read Rasmus's [30 second AJAX tutorial](http://rajshekhar.net/blog/archives/85-Rasmus-30-second-AJAX-Tutorial.html) [[via](http://reddit.com/info?id=22543)] and though it is nice enough in its own respect, it is missing two things: [Dojo](http://www.dojotoolkit.org) and [Python](http://www.python.org).

So I [rewrote it using Dojo](/ajax/30sec.html). I am really liking Dojo, last Friday at [the shop](http://www.topdesk.com) I used termie's [Dojo Done Quick](http://an9.org/p/file/ddq/ddq.txt) (main file seems to be down or moved) to roll my first own widget, but this is really just about [the IO part](http://dojotoolkit.org/intro_to_dojo_io.html).

Main improvement here is that after a while you get sick rolling your own XmlHttpRequest all the time, concatenating your own request parameters and checking for readyStates.

Rather than rolling your own library, use one which is terrific and takes most of the redundancy out ([working HTML](/ajax/30sec.html)):

<html>

<head>

<script type="text/javascript" src="dojo/dojo.js"></script>

<script type="text/javascript">
dojo.require("dojo.io.*");
	
function sendRequest(action) {
// Documentation here: http://manual.dojotoolkit.org/io.html
dojo.io.bind({
url: '/cgi-bin/30action.py', // URL to call
content: {action: action},
// mimetype: 'text/plain' is implied
// method: 'GET' is implied
// sync: false (asynchronous) is implied
load: function(type, data, evt) {
var parts = data.split('|');
dojo.byId(parts[0]).innerHTML = parts[1];
}
// error: function(type, errorObject) {} omitted for brevity
})
}	
</script>

</head>

<body>

<a href="javascript:sendRequest('foo')">[foo]</a>

<div id="foo">
</div>

</body>


</html>

11 lines of Javascript.

And the simple Python code:

#!/usr/bin/env python
import os

print 'Content-type: text/plain'
print

query = os.environ['QUERY_STRING']
parts = [part for part in query.split('&') if '=' in part]

query = {}
for part in parts:
	query[part.split('=')[0]] = part.split('=')[1]

if 'action' in query and query['action'] == 'foo':
	print "foo|foo done"