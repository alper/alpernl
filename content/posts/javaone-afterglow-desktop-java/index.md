---
author: alper
categories:
  - internet
date: "2007-06-27T23:36:53+00:00"
tags:
  - internet
  - reizen
title: JavaONE Afterglow - Desktop Java
aliases:
  - /dingen/2007/06/javaone-afterglow-desktop-java/

---
Ik was gisteren op de JavaONE Afterglow in Affligem en hier zijn mijn aantekeningen van een sessie daar (geconverteerd van Markdown):

Java on the Desktop by Sebastien Stormacq

# How much Java is out there?

91% of all PCs run Java platform
Distribution through OEMs and JR software redistribution agreements

Q: What is the state of bundled video codecs for the Java platform (FLV)?

## Example applications

Lightzone
Myspace video uploader (IILWY.com does the same with Flash and does it very well)

Note for Roel: Inglewood

sweet spots:
First wave of applets
enterprise applications
developer tools (Eclipse)
large consumer deskotp applications (Azureus)

Q: Under attack from Flash, XUL and Silverlight, C#/Mono

# Badnews

Goodnews: aware of problems and working on solutions (hopefully) soon

## Startup time (coldstart)

- Coldstart: 5-10 seconds, not acceptable
- Warmstart (after a recent run of VM): < 1-2 seconds
  Coldstart: about disk cache, java platform reads a lot from disk
  Solutions:
- preloading Java on the OS level
- Rearranging rt.jar

Quickstarter: preloads memory pages with help from the OS
pages can be flushed if needed

## Install time and process

7-15MB download which extracts to 40+ MB
Lots of small files

Solution: Kernel JVM
Bare essentials to get your program running immediately
Additional dependencies later via web
Kernel is 2MB: Core JRE, Web Start, Plug-in, Installer

Roel questions hom big a part are the Corba and RMI parts?

## JRE software detection and installation

No good way to detect JR software existence and version from browser
Developers use "Get Java" button which takes users away from the site

Applets constrained to lowest-common-denominator APIs
between MS VM or JDK 1.1

Solution: deployment toolkit
Javascript solution hosted by Sun
Redirects to download site, polls for succesful install and redirects back to original site

This already exists.

## Windows Graphics Acceleration

Directx9 based pipeline
High performance for Swing and 2D

## Nimbus

Modern look and feel

http://nimbus.dev.java.net
Scaleable and resolution independnt

Looks quite pretty.

## Coming soon: consumer Java Runtime Environment

In Java6

- Quickstarter
- Kernel
- Deployment toolkit
- Windows Grphics acceleration
- Nimbus look & feel

Planning is subject to change

## Media

Java Technology needs a standard media solutino
Support for native formast through native players
Swing components for video/audio playback

Q: No builtin codecs?

Cross platform codec for standardization in the Java world

## 3D

You can do 3D with Java right now

## Animation

Modern desktops are getting more animated
Widget toolkits which do not support this run the risk of looking outdated

Swing supports basic control animation, very manual to do more

Need:
\\* Better timing facilities
\\* Animations and effects

## Components

Translucent windows
Shaped top-level components

# Simplifying GUI development with Netbeans

## Netbeans GUI builder: Matisse

Simple and intuitive GUI layout

Suggests component alignment and spacing

Introduces the Group-Layout manager

Transparent Internationalization

Q: How does this work?
WYSIWIG code builds a DOM of controls
this DOM is serialized into Java Code
edits in the Java code are parsed and the visual representation of the dom is redrawn

## Swing Application Framework

Goals:
\\* As small and simple as possible
\\* Explain it in one hour
\\* Standard basic appliaction architecture
\\* Works very well for small/medium apps
\\* No integral docking framework, generic data model, scripting language, GUI markup schema

## Lifecycle

## Actions

Nice encapsulation, behaviour
manages enable/selected state

Overhead in creating Action classes
Visual properties should be l8n
Asynchronous Actions are difficult
enable/selection wiring can be a mess

@Action
"sayHello" ActionMap entry
ActionEvent argument is optional

Background thread for
\\* computationally intensive tasks
\\* task that might block
Monitor for:
\\* starting, interrupting, finishing
\\* progress
\\* messages
\\* descriptive information
SwingWorker does most of this

Task extends SwingWorker

## Resources

## Tasks

## Session State

user preferences like window size etc.

Create subclass of Application
Create and show your GUI in the startup method
Use Application-Context services to

# Flickr Photo Viewer

Demo taks using Netbeans running on Solaris running on Parallels on a Macbook Pro

Mac version of Java has a bug concerning multiple screens

Demos a Flickr picture retriever using Matisse

Wysiwig buildup allows you to build flexible resizable GUIs

Uses a precoded Flickr.java file with a lot of code
It would be easier (in a scripting language) to do a REST call and parse the resulting XML (2 lines of code)

Action of retrieving an image from Flickr blocks the GUI

Alper: This would have saved me hours and hours while still at university.

http://appframework.dev.java.net

# Beans Binding

Source object
Target object

Source to target: Converter
Target to source: Converter + Validator

Another demo showing how to bind beans from various controllers to each other

And another demo showing a (no lines of code written) database connection and Access style data editor

Java FX Script by David Delabassee

# What is JavaFX Script?

Programming language for the java Platform

Simple syntax somewhere between ActionScript and Javascript

Shows Silver Surfer application
with animation and other graphical effects and playing of video through the Java Quicktime binding

- Object oriented
- Declarative syntax
- Statically typed + type inference
- Automatic data binding
- Extensive Widget libarry encompassing swing and Java 2D

Tutorial widget where you can adjust the values of JavaFX objects and their properties live.

Have built a JavaFX version of a lot of Flash applications to demo that the same thing is possible using Java.

Q: Java tring to kill the Flash hegemony? Both have a ridiculous amount of presence and penetration. Flash does not have a strong mobile presence yet but Java is already there, could capitalize on that presence.

Insted of using Quicktime binding on the mobile, use a binding to run 3GP files natively and stuff

Roel: Quicktime for Java (ask Reinier)

HTML5 wants to adjust HTML to be capable of most of this out of the box.

jfx.org to learn more
JavaFX Mobile

Deploy the exact same application both on desktop, web and mobile
