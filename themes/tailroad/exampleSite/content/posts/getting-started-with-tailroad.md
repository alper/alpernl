---
title: Getting Started with TailRoad
description: Instructions for setting up a new site with Tailroad theme
date: 2025-05-27
image: /images/teacher.png
categories:
  - "Tutorials"
tags:
  - "demo"
  - "markdown"
  - "blog"
toc: true
---

Inspired by the Mainroad theme, I created this theme with a similar structure but wanted to avoid spending excessive time writing tedious CSS. Instead, I leveraged the power of Tailwind CSS for styling. The name Tailroad is a blend of both — Tail from Tailwind and road from Mainroad.
<!--more--> 

# Tailroad — A Clean, Responsive Hugo Theme with Tailwind CSS

Tailroad is a minimal, responsive theme for [Hugo](https://gohugo.io), built using [Tailwind CSS](https://tailwindcss.com). It’s designed for simplicity, speed, and flexibility.

[Demo](https://tailroad.netlify.app) | [Download](https://github.com/sathishbs/tailroad.git)

![Final Screen shot: TODO](images/screenshot.png)

## Features

- Built with Tailwind CSS v4
- Light/Dark mode toggle
- Responsive design
- Search with keyboard shortcuts
- Modular layout using Hugo partials
- Support for tags, categories, authors
- Pagination and summaries
- Disqus comments integration
- Scroll-to-top button

## Getting Started

**Prerequisites**
1. Install [Hugo](https://gohugo.io/installation/). 
2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 1. Create a site
To quickly get started with a new Hugo site using `Tailroad` theme, create a new site with YAML configuration. Navigate into the project directory and add the Tailroad theme as a Git submodule. Enable the theme by appending theme: tailroad to hugo.yaml file.

```bash
hugo new site quickstart --format yaml
cd quickstart
git init
git submodule add https://github.com/sathishbs/tailroad.git themes/tailroad
echo "theme: tailroad" >> hugo.yaml
```
### 2. Install & Configure
Since the Tailroad theme relies on Tailwind CSS v4 for styling, a few essential configurations are required to ensure proper integration. You’ll need to update your hugo.yaml file to include settings that enable Tailwind processing and asset building. This typically involves specifying the theme, setting the base URL, enabling Hugo modules, and configuring any build-related settings required by the theme. Add or update your hugo.yaml file with the following configuration to get started smoothly

```bash
cd quickstart
npm install --save-dev tailwindcss @tailwindcss/cli
npm install --save-dev @tailwindcss/typography
```

Edit hugo.yaml and append the below configuration
```yaml
# Refer to this link https://gohugo.io/functions/css/tailwindcss/  
build:
  buildStats:
    enable: true
  cachebusters:
  - source: assets/notwatching/hugo_stats\.json
    target: css
  - source: (postcss|tailwind)\.config\.js
    target: css
module:
  mounts:
  - source: assets
    target: assets
  - disableWatch: true
    source: hugo_stats.json
    target: assets/notwatching/hugo_stats.json
```

### 3. Run Hugo Server
We have completed the basic configuration required to see the theme working.  Run the below command and hit http://localhost:1313 to view the site that was created. **Keep the server running as we make the changes below**

```bash
hugo server -D
```

![Screen Shot](images/homepage.png)

### 4. Add Content to the site.
To add content to  Hugo site, use the hugo new command followed by the desired content path. 

```bash
hugo new content content/posts/my-first-post.md
```

Hugo created the file in the content/posts directory. Open the file with your editor and append the below content.

```md
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
## Introduction

This is **bold** text, and this is *emphasized* text.

Visit the [Hugo](https://gohugo.io) website!
```

### 5. Main Sections
By default TailRoad theme ignores every post that is created. Configure the section to display in the home page.  Let the theme know that it should display the posts folder that we created ealier that is holding **my-first-post.md** file.

```yaml
params:
  mainSections: ['posts']
```

### 6. Search Functionality
The Tailroad theme utilizes JSON to power its built-in search functionality. To enable this feature, you'll need to configure Hugo to generate a JSON output specifically for the homepage. Add the following configuration to your **hugo.yaml** file to activate search support in the Tailroad theme.

```yaml
outputs:
  home: ['html', 'rss', 'json']
```