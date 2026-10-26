# International Marketing Analytics: course repository

WU Vienna · CEMS MIM · Winter term 2026/27 · Dr Arne Floh

This repository holds what you need on your laptop for the course: the synthetic **Alpenglow** data, the list of Python packages and a short test that shows your set-up works. We set everything up together in Session 1.

## What is inside

| Path | What it is |
|---|---|
| `data/` | Alpenglow, a fictional premium chocolate brand in six European markets: weekly sales and media spend, a geo-lift experiment and customer journeys. See [`data/README.md`](data/README.md) |
| `data/kiosk/` | The chocolate kiosk of the statistics refresher: one year, 52 weeks |
| `data/fashion/` | One fashion brand on an online fashion platform in twelve European countries, SS25 and SS26 collections: page views, sales, prices, returns by article type and country (real data, anonymised). See [`data/fashion/README.md`](data/fashion/README.md) |
| `data/legacy/` | Two warm-up datasets for Session 1: video game sales and a four-brand chocolate panel |
| `sessions/01-foundations/lab.qmd` | Lab 1: Positron and GitHub Desktop tour, video game warm-up, price elasticities for six countries |
| `assets/mma.py` | Helper functions the labs import (data loading, seasonality terms, error measures) |
| `case-study/` | The group case study: brief and assessment criteria (`brief.pdf`, `brief.qmd`) and the report template `report.qmd`. Due Monday 30 November 2026, midnight |
| `requirements.txt` | The Python packages and versions we all use |
| `slides/00a_course-content-and-style_WT26-27.pdf` / `.pptx` | Course outline: instructor, learning outcomes, schedule, assessment and the group case study |
| `slides/02a_intro-to-mmm_WT26-27.pdf` / `.pptx` | Session 2: introduction to marketing mix modelling: key terms, ad spend and attribution, how MMM works, and the discussion of the HBR reading (the article itself is on Canvas) |
| `slides/01b_statistics-and-regression_WT26-27.pdf` / `.pptx` | Session 1 slides in two halves. Statistics refresher (Parts 1 to 5), all on one chocolate kiosk: scale types, mean and median, variance, standard deviation, standard error, z-scores, normal distribution, covariance and correlation, by hand in Python, and an in-class exercise on the kiosk's full year. Linear regression (Parts 6 to 10): theory, assumptions and tests, real-world uses, the chocolate data in Python, and an in-class exercise (online quiz, short coding exercise, Posit Assistant). A five-question quiz after each half; the answers follow in class |
| `sessions/01-foundations/stats_refresher.qmd` | The refresher calculations by hand in Python |
| `sessions/01-foundations/refresher_exercise.qmd` | In-class exercise of the refresher: one year at the kiosk (`data/kiosk/kiosk_year.csv`) |
| `sessions/01-foundations/regression_chocolate.qmd` | The regression code of the slides on the chocolate data |
| `sessions/01-foundations/regression_exercise.qmd` | In-class exercise of the regression part: price and sales of brand 1 |
| `slides/01e_regression-assumptions-dummies-nonlinear_WT26-27.pdf` / `.pptx` | Regression, part 2: assumptions and how to test them (residual and Q-Q plots, RESET, Breusch-Pagan, Jarque-Bera, VIF, Cook's distance, robust errors), dummy coding (reference group, the dummy trap), log-log and the other log forms, non-linear relationships (squares, turning points), the analyses in Python, and an in-class exercise (online quiz 3, coding exercise, Posit Assistant). The quiz and exercise answers follow in class |
| `sessions/01-foundations/regression_assumptions.qmd` | The code of deck 01e on the chocolate data: both models, residual plots, tests, dummies, the quadratic |
| `sessions/01-foundations/assumptions_exercise.qmd` | In-class exercise of deck 01e: which model may brand 1 trust? |
| `sessions/01-foundations/fashion_exercise.qmd` | In-class exercise of deck 01e on the fashion data: markets, the views-to-sales funnel in logs, country dummies, Switzerland as a new market |
| `exercises/` | Coding exercises: put your personal brief, template and data from Canvas here (see `exercises/README.md`) |
| `slides/01a_setup-and-registration_WT26-27.pdf` / `.pptx` | The Session 1 set-up and registration slides: accounts, installation, Positron, GitHub Desktop, Quarto, the packages, updating within Positron |
| `slides/how-brands-grow_double-jeopardy-and-distinctiveness_WT26-27.pdf` / `.pptx` | Lecture on How Brands Grow (Ehrenberg-Bass Institute), 36 slides in six parts: brand management basics (what a brand is, tangible and intangible elements, Manner as an example), the laws of brand buying (Double Jeopardy, Duplication of Purchase, the NBD-Dirichlet benchmark, light buyers), how brands grow (penetration, Kantar Brand Footprint evidence, mental and physical availability, the B2B 95:5 rule, Category Entry Points), brand distinctiveness (fame and uniqueness grid, six sourced cases from Tropicana to Cadbury), critiques and the Binet & Field debate, and a Double Jeopardy data lab with a distinctive asset audit |
| `slides/wie-marken-wachsen_double-jeopardy-und-distinctiveness_WT26-27.pdf` / `.pptx` | The same lecture in German (Austrian conventions, gender-inclusive forms), 36 slides with German speaker notes: Grundlagen der Markenführung, Gesetze des Markenkaufs, wie Marken wachsen, unverwechselbare Marken, Kritik und Grenzen, Datenlabor und Asset-Audit |
| `slides/01c_github-copilot-claude-chatgpt_WT26-27.pdf` / `.pptx` | GitHub, Copilot, Claude and ChatGPT, step by step. GitHub (Parts 1 to 6): account, GitHub Education, GitHub Desktop, cloning, pull and push, private and public repositories. Copilot in Positron (Parts 7 to 12): the free student plan, connecting Copilot, chat, completions, using AI well. Optional (Parts 13 to 18): Claude and ChatGPT in Positron, API key or subscription, Claude Code and Codex, costs and privacy |
| `slides/01d_connect-ai-assistants_WT26-27.pdf` / `.pptx` | Connect an AI assistant in Positron, the short version: GitHub Copilot in Posit Assistant (course default), Claude Code and Codex in the terminal (optional), and how to use them safely |
| `setup/setup-guide.pdf` / `.qmd` | Step-by-step set-up: accounts, Python 3.14, Positron, Quarto, GitHub Desktop, the project environment, AI assistants, updating within Positron, troubleshooting |
| `setup/check_setup.py` | Checks Python, the packages, Quarto and Git, and prints `ready` |
| `.claude/skills/polish-slides/` | Claude Code skill used to build and check the course slides: WU template, a render-and-check script (`scripts/check_deck.py`) and design patterns. Claude Code in Positron loads it automatically when you open this folder; the part on build scripts refers to the instructor's course repository |
| `.claude/skills/add-instructor-slide/` | Claude Code skill that adds the instructor's two profile slides (Module Convenor, Work Experience) to a deck on the WU template: `python scripts/add_instructor_slides.py deck.pptx` |
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
