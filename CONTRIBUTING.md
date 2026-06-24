# Contributing to the OpenCyberCity Docs

#### Hopefully, you already know how to write Markdown. If not, check out the [Markdown Guide](https://www.markdownguide.org/).

#### The site is built with [Sphinx](https://www.sphinx-doc.org/) using [MyST](https://myst-parser.readthedocs.io/) (Markdown for Sphinx).
---

## How it works

Unlinke a normal website, Sphinx does not automatically figure out the navigation tree from the folder structure. Instead, it uses explicit `toctree` structures to declare the hierarchy of pages. The navigation tree is built from two things:

**Landing pages** — a `.md` file that sits *beside* a folder of the same name. The landing page is the parent of all the pages in that folder, and its toctree declares them as children.

```
docs/source/
|-- get_started.md              <- the section's landing page
|-- get_started/                <- the section's child pages
    |-- software.md             <- the sub-section's landing page
    |-- software/               <- the sub-section's child pages
        |-- software_basics.md  <- a child page
```

What this looks like in the sidebar:

<img src="images/sidebar.png" width="300px" alt="Sidebar screenshot" />

---
For example, `usage.md` is the landing page for the `usage/` folder. Its toctree declares all the pages in that folder as children, so they appear in the sidebar under "Usage."

```md
# Usage

How to operate the OpenCyberCity systems.

```{toctree}
:maxdepth: 1 // Show one level deep in the sidebar
:glob:       // Use globbing to include all pages in the folder

usage/*      // Include all Markdown files in the usage folder
```
**IMPORTANT:** Without `:glob:`, Sphinx reads every line in the toctree body as a literal docname. So `usage/*` would make Sphinx look for a page literally named "usage/*", fail to find it, and throw a warning with a broken/empty entry. The `*` does nothing on its own. Using `:glob:`, however, does sort things alphabetically, so to customize the order of things, you must list things explicitly:
```
```{toctree}
usage/street_lights
usage/traffic_lights
```

## Adding a section

Look at the `usage` section.

This pairing is the core convention to remember. Every section that has children is **a `.md` landing page next to a folder of the same name**:

- `usage.md`  + `usage/`
- `device_setup.md` + `device_setup/`
- `architecture.md` + `architecture/`
- `get_started.md` + `get_started/`

And it nests. Inside `usage/`, `street_lights.md` is a landing page sitting next to a `street_lights/` folder that holds `street_lights_gui.md`. You can go as deep as you need.

To add a new section, simply create the directory, and make a landing page that cooresponds to that newly created directory.

### Why is `usage.md` outside the `usage/` folder?

Basically: **a section's landing page is the parent of its children, not one of them.**

Sphinx identifies every page by a "docname," which cooresponds with its path under `source/` without the extension:

| File | docname | URL |
|------|---------|-----|
| `usage.md` | `usage` | `/usage.html` |
| `usage/street_lights.md` | `usage/street_lights` | `/usage/street_lights.html` |

Because `usage.md` lives beside the folder, its docname is `usage`, which makes it the parent of everything named `usage/...`. Its toctree then pulls the folder's contents in as children, and et voilla!:

```
Usage                 <- usage.md
├── Street Lights     <- usage/street_lights.md
└── Traffic Lights    <- usage/traffic_lights.md
```

Always remember: **landing page beside the folder, never inside it!!!**

---

## Toctrees

A `toctree` (table of contents tree) is what declares which pages are children of the current page. Here's `device_setup.md`:

````markdown
# Device Setup

Here are the setup instructions for different systems.

```{toctree}
:maxdepth: 2
:glob:

device_setup/*
````

What everthing does:

- ` ```{toctree} ` ... ` ``` ` — the constructer
- **`:maxdepth: 1`** — how many levels deep to show under this entry in the sidebar. `1` shows just the immediate children; higher numbers expand grandchildren inline.
- **`:glob:`** — lets you use `*` in the body instead of listing every page explictly.
- **The body (`device_setup/*`)** — one entry per line. Each line is either an explicit docname or, with `:glob:`.

### Glob paths are relative to the file

`usage.md` writes `usage/*`, but `usage/street_lights.md` writes just `street_lights/*` **not** `usage/street_lights/*`. Paths in a toctree are **relative to the folder containing the `.md` file**. Since `street_lights.md` is already inside `usage/`, it only needs the `street_lights/` folder.

`device_setup/*` matches every page directly inside `device_setup/` (e.g. `device_setup/pi`, `device_setup/jetson`). It does **not** recurse into deeper folders, those get pulled in by their own landing page's toctree. 

### Glob order is alphabetical

`:glob:` includes matching pages in **alphabetical order by docname**. As we add more stuff, we will likely start listing things out explicitly.

### Useful options

- **`:caption: Some Title`** — adds a bold heading above this group in the sidebar. The "CONTENTS:" label you see comes from the caption in `index.md`.
- **`:hidden:`** — includes the pages in the navigation tree but does not render the clickable list in the page body. 
---

## `index.md` is special

`docs/source/index.md` is the **root** of the whole site. It's the one toctree that lists the top-level sections **explicitly** (no `:glob:`) so their order is controlled by hand:

````markdown
```{toctree}
:maxdepth: 2
:caption: Contents:

get_started
device_setup
architecture
usage
```
````

Reorder these lines to reorder the top-level sections in the sidebar. (Explicitly written here so Get Started shows up at the top)

---

## Step by Step Instructions

### Add a page to an existing section

1. Create the `.md` file inside that section's folder, e.g. `usage/launch.md`.
The section's landing page (`usage.md`) globs `usage/*`, so it's picked up automatically. It will appear alphabetically.

### Add a brand-new top-level section

Say you want a "factory" section:

1. Create the landing page `docs/source/factory.md` with a title, an intro, and a toctree that globs its folder:

   ````markdown
   # Factory

   idk factory stuff

   ```{toctree}
   :maxdepth: 1
   :glob:

   factory/*
   ```
   ````

2. Create the folder `docs/source/factory/` and add your child pages there (e.g. `factory/arm.md`).
3. Add `factory` to the toctree in `index.md`, in the position you want it to appear.

### Add a nested subsection (a child that itself has children)

Same pattern, one level down. Inside `factory/`, create `arm.md` next to a `arm/` folder, give `arm.md` a toctree globbing `arm/*`, and put the deeper pages in `arm/`.

---

## Build and preview your changes

All commands run from the `docs/` directory.

```bash
make rebuild   # clean + full HTML build
make serve     # clean + build, then serve at http://localhost:6767
```

**Use `make rebuild` (not a plain `make html`) after changing any toctree or moving files.** Sphinx leaves weird build artifacts sometimes (dw i put in an issue)

`make serve` rebuilds and then launches a local webserver to host the site, use it instead of double-clicking the HTML file. Opening pages directly via `file://` causes some issues. You can pass a different port with `make serve PORT=9000`. (i still think port 6767 is the best)

**If you want to learn more, <a href="https://en.wikipedia.org/wiki/RTFM">RTFM.</a> Here is the link: <a href="https://www.sphinx-doc.org/">manual (docs)</a>. Half of this was copy/pasted from there anyway**