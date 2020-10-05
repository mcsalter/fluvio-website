# Documentation for Writers

Fluvio Website was written in Hugo. Checkout [Hugo Documentation](https://gohugo.io/documentation/) for the directory layout and other introductory information. This document describes the formatting and the customizations created for Fluvio website.

## Formatting and Short Codes

The following document has a list of formatting and short code samples: 

* [https://fluvio.io/docs/samples](https://fluvio.io/docs/samples)

The content for the page is generated from the following markdown: 

* [https://github.com/infinyon/fluvio-website/blob/stable/content/docs/samples.md](https://github.com/infinyon/fluvio-website/blob/stable/content/docs/samples.md)


## Tutorial Section

The Tutorials page displays a variety of guides that are used to teach users about Fluvio.
Each guide has language-specific adaptations for each programming language.
Each tile on the page represents a specific guide, and the icons on the tile represent
the language adaptations that are available for that particular guide.

![Tutorial page screenshot](./.github/assets/tutorial-panels.png)

Each guide has a root file that describes the language-specific tutorials available. For
example, we have a "Hello world" guide described by the [`hello-world.md`] root file.
This root file just contains information describing all of the tutorials for this guide.
This is used to tell Hugo how to render the tiles and icons on the tutorials main page.

Two important fields are `group` and `tags`. The group field is used to organize several
language-specific tutorials into a single guide group. The tags field is used to indicate
which langage adaptations are available and which icons to show on the tile.

For example, [`hello-world.md`] has 3 tags:

[`hello-world.md`]: ./content/tutorials/hello-world.md

```
---
title: '"Hello World" ...'
desc: ...
group: hello-world
tags:
  - node
  - rust
  - swift
githubAuthors:
  - ...
difficulty: low
weight: 10
```

The `front matter` parameters for the **root** file are defined as follows:

* **title**: header of the tile
* **desc**: description of the tile
* **group**: label that links all programming language related files to this tile
* **tags**: programming language supported by this tile - each programming language must have a separate labeled with the same group name
* **githubAuthors**: github usernames of the authors this tile displayed as github avatars
* **difficulty**: [low, medium, high] controls the difficulty icon of the tile
* **weight**: controls the tile position in the list

Each tile must have at least two files joined by the `group` name:

* **root file**: a file with no content such as `hello-world.md` that controls the tile content and defines the group label.
* **programming language files**: one or more files such as `hello-world-node.md`, `hello-world-rust.md`, etc. - one file per tag. The file name does not matter as the content is joined by the group label.

Each `programming language file` is managed through the `front matter` and the optional `short code` defined below. 

For example, [`hello-world-node.md`] has the following `front matter`:

[`hello-world-node.md`]: ./content/tutorials/hello-world-node.md

```
---
title: '"Hello World" ...'
hidden: true
group: hello-world
tag: node
weight: 10
toc: true
---
```

The `front matter` parameters for the **programming language** file are defined as follows:

* **title**: header of the file
* **hidden**: all programming language files **must be hidden** otherwise they are displayed as tiles
* **group**: the label that links all programming language to the root file
* **tag**: the programming language associated to this file
* **weight**: the order in which this file should be displayed in the `short-code` described below
* **toc**: if true, the TOC is automatically computed and displayed

The `short code` is a script that generates the language selection buttons. In general the language selector short code should be placed right below the front matter:

```
{{< lang-selector >}}
```

If there is only one programming language, the short code may be omitted.

**NOTE**: Each programming language has a corresponding icon that must be added to the following directory:

```
./static/img/tiles/
```

and mapped in the following `partial`:

```
./layouts/partials/tutorial/print-languages.html
```