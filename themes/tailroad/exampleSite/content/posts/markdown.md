---
title: Markdown Documentaion
description: A demo post showcasing Hugo theme styling for text, images, and code.Formatting Syntax
date: 2025-05-27
categories: ["Tutorials"]
tags: ["demo", "markdown", "blog"]
menu:
  main:
    title: Markdown
image: /images/documentation.png
pinned: true
---

This page offers a brief overview of what it’s like to use Markdown.  Should be very easy to pick up simply by looking at a few examples of it in action.

<!--more-->


## Heading 2 (H2)
This is a **sample blog post** demonstrating how your Hugo theme renders Markdown. Below are examples of common formatting.

### Heading 3 (H3)
- **Bold** and *italic* text.  
- A [link to Google](https://google.com).  
- `Inline code` snippets.


#### Heading 4 (H4)
To create a blockquote, add a > in front of a paragraph.
> A blockquote.  
> *— Author Name*
>> Blockquote inside a blockquote

### Lists
**Unordered List:**
- Noodles  
- Pasta  
  - Spaghetti  
- [x] Milk 
- [ ] Bread


**Ordered List:**  
1. First step  
2. Second step  
6. Even 6 is shown as '3'
    1. Nested Step
    3. Another one

### Horizontal Rules
Three ways to create horizontal lines

---
***
-------

### Links and Media
To create a link, enclose the link text in brackets (e.g., [Example]) and then follow it immediately with the URL in parentheses (e.g., (https://example.org)).

[Hugo's documentation](https://gohugo.io "Tooltip on hover") is the best place to look for any help needed. It is easy to show a www.example.org or an <admin@example.org> using Markdown. Images can be loaded in the same but should start with an exclamation ![Books](/images/books.jpg)

### Tables

Tables aren't part of the core Markdown spec, but Hugo supports them.

| ID  | Make      | Model   | Year |
| --- | --------- | ------- | ---- |
| 1   | Honda     | Accord  | 2009 |
| 2   | Toyota    | Camry   | 2012 |
| 3   | Hyundai   | Elantra | 2010 |

Colons can be used to align columns.

| Tables      | Are           | Cool         |
|:----------- |:-------------:| ------------:|
| align: left | align: center | align: right |
| align: left | align: center | align: right |
| align: left | align: center | align: right |

You can also use inline Markdown.

| Inline     | Markdown  | In                | Table      |
| ---------- | --------- | ----------------- | ---------- |
| *italics*  | **bold**  | ~~strikethrough~~ | `code`     |


### Code and Technical Writing

```python
def hello_world():
    print("Welcome to Hugo!")
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
```

{{< highlight go "linenos=inline, hl_lines=3 6-8, style=emacs" >}}
package main

import "fmt"

func main() {
    for i := 0; i < 3; i++ {
        fmt.Println("Value of i:", i)
    }
}
{{< /highlight >}}

### abbr, sub, sup, kbd, etc.
<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd>X</kbd> to win. Or press <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>F</kbd></kbd> to show FPS counter.

<mark>As a unit of information in information theory, the bit has alternatively been called a shannon</mark>, named after Claude Shannon, the founder of field of information theory.

### Figure with Caption
{{< figure
  src="https://picsum.photos/200/300.jpg"
  alt="Tailroad Screenshot"
  link="https://picsum.photos/"
  align="center"
  caption="Screenshot"
  class="ma0 w-75"
>}}

### Hidden Text
{{< details summary="Hidden Content - Click to expand" >}}
**Hidden text** will be revealed only on click
{{< /details >}}

### Instagram Content
{{< instagram CxOWiQNP2MO >}}

### QRCode 
{{< qr text="https://gohugo.io" />}}

### Twitter (x)
{{< x user="SanDiegoZoo" id="1453110110599868418" >}}

### Youtube Video
{{< youtube 0RKpf3rK57I >}}






