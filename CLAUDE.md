# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Asset-only package containing weather symbol fonts for SmartMet rendering tools (qdcontour, qdcontour2). No C++ source, no tests, no CI. RPM name: `smartmet-fonts`.

## Build Commands

```bash
make rpm          # Build RPM (only target in Makefile)
```

There is no `make`, `make test`, or `make install` — fonts are installed only via RPM to `/usr/share/fonts/smartmet/`.

## Fonts

- **Frontier** (otf + ttf) — weather front symbols
- **synop** (otf + ttf) — synoptic weather symbols
- **Mirri** (ttf only) — additional weather symbols

`Fontmap.GS` maps font names to files for Ghostscript. `to_otf.pe` is a FontForge script for converting TTF to OTF.

## Packaging

The RPM spec installs all OTF files plus `Mirri.ttf` and `Fontmap.GS` to `/usr/share/fonts/smartmet/`, then runs `fc-cache` post-install. The package is `noarch`.
