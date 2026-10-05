# International Marketing Analytics: course repository

WU Vienna · CEMS MIM · Winter term 2026/27 · Dr Arne Floh

This repository holds what you need on your laptop for the course: the synthetic **Alpenglow** data, the list of Python packages and a short test that shows your set-up works. We set everything up together in Session 1.

## What is inside

| Path | What it is |
|---|---|
| `data/` | Alpenglow, a fictional premium chocolate brand in six European markets: weekly sales and media spend, a geo-lift experiment and customer journeys. See [`data/README.md`](data/README.md) |
| `data/legacy/` | Two warm-up datasets for Session 1: video game sales and a four-brand chocolate panel |
| `sessions/01-foundations/lab.qmd` | Lab 1: Positron and GitHub Desktop tour, video game warm-up, price elasticities for six countries |
| `assets/mma.py` | Helper functions the labs import (data loading, seasonality terms, error measures) |
| `case-study/` | The group case study: brief and assessment criteria (`brief.pdf`, `brief.qmd`) and the report template `report.qmd`. Due 30 November 2026, 23:59 |
| `requirements.txt` | The Python packages and versions we all use |
| `setup/check_setup.py` | Checks Python, the packages, Quarto and Git, and prints `ready` |
| `test_stack.qmd` | Single-file stack test: installs and loads polars, plotnine, great_tables and statsmodels, reads the data from GitHub and renders a table, a chart and a regression |

## Get it onto your laptop

1. **Clone** with GitHub Desktop: *File → Clone repository → URL* and paste `https://github.com/arnefloh-wu/international-marketing-analytics-teaching`. Pick a folder without spaces or cloud syncing, for example `C:\Users\you\wu\ima` or `~/wu/ima`. The repository is public, so you do not need to be added.
2. **Open** the folder in Positron: *File → Open Folder*. The folder is now your project.
3. **Set up Python**: *Command Palette → Python: Create Environment → Venv → Python 3.14*, and tick `requirements.txt`. Positron creates `.venv` and installs the packages.
4. **Check**: in the Positron console run

   ```python
   %run setup/check_setup.py
   ```

   It ends with `ready`.
5. **Test**: open `test_stack.qmd`, run its first cell once (Ctrl/Cmd + Enter), then press *Preview* (Ctrl/Cmd + Shift + K). A short report with a table, a chart and regression results appears.

## Getting updates

Before every session: GitHub Desktop → *Fetch origin* → *Pull origin*. Keep your own work in your own files (or in your group's repository), so pulling never overwrites it.

## Labs

Open a lab in Positron (for Session 1: `sessions/01-foundations/lab.qmd`), select the project's `.venv` and run the cells top to bottom with Ctrl/Cmd + Enter, or press *Preview* to render the whole document. New labs appear here before each session: pull first.
