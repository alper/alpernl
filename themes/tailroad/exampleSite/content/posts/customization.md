---
date: '2025-05-29T10:42:17-04:00'
draft: false
title: 'Customization of the Theme with Configuration'
description: Describes common Mainroad theme configuration 
categories:
  - "Tutorials"
  - "Hugo"
tags:
  - "markdown"
menu: 
    main:
        title: Customization
---
This page outlines common TailRoad configuration parameters, which can be set either in your Hugo configuration file or directly in a page's Front Matter.

<!--more-->

# Configuraion Guide

For additional configuration options not covered here, consult the official [Hugo docs](https://gohugo.io/documentation/).  

## Essential Tailwind CSS Setup
To ensure the *TailRoad* theme functions correctly, the following configuration must be included in your Hugo config file. Without these settings, Tailwind CSS will fail to generate properly.

For detailed guidance, refer to [Hugo's documentation](https://gohugo.io/functions/css/tailwindcss/ ).

```yaml
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

### Organizing Content with Main Sections
Create as many sections as possible using the command `hugo new content docs/document1.md` or `hugo new content blogs/blog1.md`.  By default *TailRoad* theme ignores the folders those are not defined in the mainSections configuration. Add the new section names to the below config.

```yaml
params:
  mainSections: ['posts', 'docs, 'blogs']
```

## Header
### Logo
*TailRoad* lets you customize the site header with either a logo or a title. If both are provided, the logo will be prioritized. If neither is specified, the site’s default title will be displayed as the logo.

```yaml
[Params.logo]
params:  
  logo:
    image: images/logo.svg 
    title: MySite
```

> **Note:** Since *TailRoad* uses a sticky header, logo image is constrained to a maximum height of 40px or 2.5rem. 


### Menu(s)
*TailRoad* supports header and footer menus. You can define these menus in the main config.yaml file. In the next section, we’ll cover how to add a post to a menu using front matter.

**hugo.yaml**
```yaml
menu:
  main:
    - identifier: home
      name: Home
      url: /
      weight: -100 # Lowest weight takes the position on the page
    - identifier: about
      name: About
      url: /about/
      weight: -90 
  footer:
    - identifier: contact
      name: Coffee
      url: /hugo/coffee/
```

**Front Matter**
A new menu item vlog is shown in the main menu.  if title is not provided page title is displayed as the menu

```yaml
---
title: How I travelled the world 
date: 2025-05-25
menu:
  main: # main or footer will work and accordingly both can be specified
    title: vlog
#menu: main also works page title is shown as menu.
---
```

### Sidebar
Sidebar is not enabled by default in the *TailRoad* theme. Need to enable in the config using the below.

```yaml
params:
    sidebar:
        enable: true # Default is false
```

#### Widgets
* Widgets on the sidebar are displayed in the order of specification. Accepted values are recent, categories, tags, social.  
* With the recents widget enable how many recent posts the widget should show is configured using recentsCount. 
* How many posts are under the category or tags is shown using showCounts to true. By default it is false.

```yaml
params:
    sidebar:
        widgets: ['recent', 'categories', 'social']
        recentsCount: 6 # Default is 5
        showCounts: true # Default is false
```

#### Social Widget
Everything in the social is optional how ever the display is different for the custom social elements.

```yaml
params:
    sidebar:
        social:
            email: admin@example.com
            linkedin: example-2b0a8b140
            github: example
            facebook: example
            twitter: example
            instagram: example
            telegram: example
            custom:
                gitlab:
                name: GitLab 
                icon: images/gitlab.svg
                url: https://gitlab.com/example
                bitbucket: 
                name: BitBucket
                icon: images/bitbucket.svg
                url: https://gitlab.com/example

```

### Posts (Main content)
*TailRoad* theme displays the posts as cards in the main content area.  The only configuration that acts on the posts is how many posts per page.

```yaml
pagination:
  pagerSize: 8
```

### Pinned Posts
By default posts are sorted in date desecending.  However, *TailRoad* theme supports to pin posts and display the post that is most required first. Make a note all the pinned posts are sorted as per the date posted.  Make the posts pinned through the frontmatter.

```yaml
---
title: Pinned post
pinned: true
---
```

### Comments
*TailRoad* supports comments from Github Giscus. Create a new public repository to store the comments and create an entry in the [giscus app] to generate a script that and get those values into the config yaml.  

```yaml
Params:
  giscus:
    repo: ""
    repoid: ""
    category: ""
    categoryid: ""
    mapping: ""    
    theme: ""
    lang: ""
```

## Footer
Specify any specific footer message using the copyright

```yaml
params:  
   copyright: example.org.  Some rights reserved.
```

### FrontMatter 
Front matter plays a major role in the configuration of the post.  While config.yaml/toml specifies site level configuration front matter is page specific configuratiion.  Front matter is the first few lines that either starts with `---` or `+++`.

```yaml
---
title: Title of the page
description: Description of the page
date: date this post is created
draft: is this a draft that should be published
image: Image that is displayed in the card.
comments: false # disable comments for this page
categories:
  - "Category 1"
  - "Category 2"
tags:
  - "Test"
  - "Another test"
menu: main # Optional, main, footer
---
```