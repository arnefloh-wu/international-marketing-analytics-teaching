"""Experiments and A/B testing: the sample code of the deck as a plain Python script.

The same code as ab_testing.qmd (sessions/01-foundations), for the deck "Experiments and A/B testing" of
International Marketing Analytics: the operator's retention e-mail, the A/B test of the subject line
(data/abtest/email_ab.csv) and the 2 x 2 test of first name x discount (data/abtest/email_factorial.csv).
Steps 1 to 3 are the code of slides 31 to 33; Steps 4 to 8 follow the deck (A/A tests and power, device as a
moderator, the 2 x 2 by hand and the two-way ANOVA, the logit, the market as a moderator). The explanations of
each result are in ab_testing.qmd and its rendered html.

How to run it:
- In Positron (or VS Code), open the repository folder and this file; each "# %%" line starts a cell. Run the
  cells one at a time from the top (Ctrl+Enter / Cmd+Enter); the plots appear in the Plots pane.
- Or run the whole script from a terminal, from this folder so that the ../../data paths work:
      cd sessions/01-foundations
      ../../.venv/bin/python ab_testing.py
  Each plot opens in a window; close it to continue.
"""

# %% Packages
# the packages of slide 30; Steps 1 to 3 repeat their imports, as on the slides
import numpy as np
import polars as pl
import statsmodels.formula.api as smf
from plotnine import (aes, facet_wrap, geom_histogram, geom_hline, geom_line, geom_point, geom_vline,
                      ggplot, labs)
from scipy import stats
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize, proportions_ztest

# %% Step 1: load and check the split
import polars as pl
from scipy import stats

ab = pl.read_csv("../../data/abtest/email_ab.csv")

split = (ab.group_by("version")
         .agg(pl.len().alias("n"),
              pl.col("clicked").sum().alias("clicks"),
              pl.col("clicked").mean().alias("click_rate"))
         .sort("version"))
stats.chisquare(split["n"].to_list()).pvalue  # SRM
print(split)

# %%
# SRM p of our split and of the broken split of slide 17 (20,000 vs 19,300)
print("SRM p, our test:", round(stats.chisquare(split["n"].to_list()).pvalue, 3))
print("SRM p, broken split:", round(stats.chisquare([20_000, 19_300]).pvalue, 4))

# %%
# balance check: the share on mobile and from Spain per version (slide 10)
print(ab.group_by("version")
      .agg((pl.col("device") == "mobile").mean().alias("share_mobile"),
           (pl.col("country") == "ES").mean().alias("share_spain"))
      .sort("version"))

# %% Step 2: difference, z-test, CI and power
from statsmodels.stats.proportion import (
    proportions_ztest, confint_proportions_2indep,
    proportion_effectsize)
from statsmodels.stats.power import NormalIndPower

x, n = split["clicks"].to_list(), split["n"].to_list()
z, p = proportions_ztest([x[1], x[0]], [n[1], n[0]])
lo, hi = confint_proportions_2indep(x[1], n[1],
                                    x[0], n[0])   # B - A

es = proportion_effectsize(0.039, 0.033)
print(NormalIndPower().solve_power(es, alpha=0.05, power=0.8))

# %%
# B − A in pp, the relative lift, z, p and the 95 % CI
diff = x[1] / n[1] - x[0] / n[0]
print("B - A in pp:", round(diff * 100, 2))
print("relative lift in %:", round(diff / (x[0] / n[0]) * 100, 1))
print("z:", round(z, 2), " p:", round(p, 4))
print("95 % CI in pp:", round(lo * 100, 2), "to", round(hi * 100, 2))

# %%
# guardrail: the unsubscribe rate per version and its z-test (slide 15)
unsub = (ab.group_by("version")
         .agg(pl.len().alias("n"),
              pl.col("unsubscribed").sum().alias("unsubscribes"),
              pl.col("unsubscribed").mean().alias("unsub_rate"))
         .sort("version"))
u, nu = unsub["unsubscribes"].to_list(), unsub["n"].to_list()
print("unsubscribes, B - A in pp:", round((u[1] / nu[1] - u[0] / nu[0]) * 100, 3))
print("unsubscribes, p:", round(proportions_ztest([u[1], u[0]], [nu[1], nu[0]])[1], 3))
print(unsub)

# %% Step 3: the factorial regression and plot
import statsmodels.formula.api as smf
from plotnine import aes, geom_line, geom_point, ggplot

fa = pl.read_csv("../../data/abtest/email_factorial.csv")
m = smf.ols("clicked ~ personal * discount",
            data=fa.to_pandas()).fit()
m.params * 100                     # in pp

cells = (fa.group_by("personal", "discount")
         .agg(pl.col("clicked").mean().alias("rate")))
(ggplot(cells, aes("discount", "rate",
                   colour="factor(personal)"))
 + geom_line() + geom_point()).show()

# %%
print((m.params * 100).round(2))   # in pp

# %%
# the four cells: customers, click rate and unsubscribe rate, and the SRM check (slide 23)
fa_cells = (fa.group_by("personal", "discount")
            .agg(pl.len().alias("n"),
                 pl.col("clicked").mean().alias("click_rate"),
                 pl.col("unsubscribed").mean().alias("unsub_rate"))
            .sort("personal", "discount"))
print("SRM p:", round(stats.chisquare(fa_cells["n"].to_list()).pvalue, 3))
print(fa_cells)

# %% Step 4: chance and power: A/A tests
# 2,000 simulated A/A tests (seed 7)
rng = np.random.default_rng(7)
gaps, significant = [], []
for run in range(2000):
    y = rng.random(40_000) < 0.033
    a, b = y[:20_000].sum(), y[20_000:].sum()
    gaps.append(100 * (b - a) / 20_000)
    significant.append(proportions_ztest([a, b], [20_000, 20_000])[1] < 0.05)
aa = pl.DataFrame({"gap_pp": gaps, "significant": significant})

# %%
# how often chance alone looks "significant", and how rare our +0.60 pp is
print("share with p < 0.05:", aa["significant"].mean())
print("SD of the gaps in pp:", round(aa["gap_pp"].std(), 3))
print("share with a gap of 0.60 pp or more:", (aa["gap_pp"].abs() >= 0.6).mean())
(ggplot(aa, aes("gap_pp")) + geom_histogram(binwidth=0.05) + geom_vline(xintercept=0.6, colour="blue")
 + labs(x="Difference B − A in 2,000 A/A tests (pp)", y="Number of tests")).show()

# %% Step 4: chance and power: sample size and the power curve
# customers per version for 3.3 % → 3.9 %, 3.6 % and 4.3 %
for p1 in [0.039, 0.036, 0.043]:
    need = NormalIndPower().solve_power(proportion_effectsize(p1, 0.033), alpha=0.05, power=0.8)
    print(p1, np.ceil(need))

# %%
# power for 1,000 to 40,000 customers per version
n_grid = np.arange(1_000, 40_001, 1_000)
curve = pl.DataFrame({"n": n_grid, "power": NormalIndPower().power(es, nobs1=n_grid, alpha=0.05)})
print(curve.filter(pl.col("n").is_in([2_000, 5_000, 10_000, 20_000, 40_000])))
(ggplot(curve, aes("n", "power")) + geom_line() + geom_hline(yintercept=0.8, linetype="dashed")
 + labs(x="Customers per version", y="Power")).show()

# %% Step 5: does B work for everyone? Device as a moderator
# customers, clicks and click rate by device and version (slide 18)
device = (ab.group_by("device", "version")
          .agg(pl.len().alias("n"),
               pl.col("clicked").sum().alias("clicks"),
               pl.col("clicked").mean().alias("click_rate"))
          .sort("device", "version"))
print(device)

# %%
# customers, B − A in pp and the z-test of Step 2 within each device
mob = device.filter(pl.col("device") == "mobile")
desk = device.filter(pl.col("device") == "desktop")
print("customers on mobile and desktop:", mob["n"].sum(), desk["n"].sum())
print("mobile: B - A in pp", round((mob["click_rate"][1] - mob["click_rate"][0]) * 100, 2))
print("desktop: B - A in pp", round((desk["click_rate"][1] - desk["click_rate"][0]) * 100, 2))
print("p mobile:", round(proportions_ztest(mob["clicks"].to_list(), mob["n"].to_list())[1], 4))
print("p desktop:", round(proportions_ztest(desk["clicks"].to_list(), desk["n"].to_list())[1], 4))

# %%
# B × mobile in one regression: does the effect of B depend on the device?
d = ab.with_columns(B=(pl.col("version") == "B").cast(pl.Int64),
                    mobile=(pl.col("device") == "mobile").cast(pl.Int64))
m_device = smf.ols("clicked ~ B * mobile", data=d.to_pandas()).fit()
print("B:mobile in pp:", round(m_device.params["B:mobile"] * 100, 2))
print("p:", round(m_device.pvalues["B:mobile"], 3))

# %% Step 6: the 2 × 2 by hand: simple effects, main effects, interaction
# the effects from the four click rates of Step 3, in pp
r00, r01, r10, r11 = fa_cells["click_rate"].to_list()   # personal, discount: 00, 01, 10, 11
print(pl.DataFrame({
    "effect": ["name, no discount", "name, with discount", "discount, generic", "discount, first name",
               "main effect name", "main effect discount", "interaction"],
    "pp": [r10 - r00, r11 - r01, r01 - r00, r11 - r10,
           (r10 - r00 + r11 - r01) / 2, (r01 - r00 + r11 - r10) / 2, (r11 - r01) - (r10 - r00)],
}).with_columns((pl.col("pp") * 100).round(2)))

# %% Step 6: regression and two-way ANOVA
# the model of Step 3: coefficients with p-values, then the two-way ANOVA
print(m.summary())
print(anova_lm(m, typ=2))

# %%
# effect coding (−0.5 / +0.5): the coefficients are the main effects; SEs in pp
fa_e = fa.with_columns(pe=pl.col("personal") - 0.5, de=pl.col("discount") - 0.5)
m_e = smf.ols("clicked ~ pe * de", data=fa_e.to_pandas()).fit()
print((m_e.params * 100).round(2))
print((m_e.bse * 100).round(2))

# %% Step 7: the logit reads the interaction differently
# the 2 × 2 as a logit: log-odds coefficients and odds ratios
lg = smf.logit("clicked ~ personal * discount", data=fa.to_pandas()).fit(disp=0)
print(np.exp(lg.params).round(2))   # odds ratios
print(lg.summary())

# %%
# the four cells on the log-odds scale: log(rate / (1 - rate))
print(fa_cells.with_columns(log_odds=(pl.col("click_rate") / (1 - pl.col("click_rate"))).log()))

# %% Step 8: does the interaction differ by market?
# the regression of Step 3 in each market: the interaction in pp (slide 27)
germany = fa.filter(pl.col("country") == "DE").to_pandas()
spain = fa.filter(pl.col("country") == "ES").to_pandas()
m_de = smf.ols("clicked ~ personal * discount", data=germany).fit()
m_es = smf.ols("clicked ~ personal * discount", data=spain).fit()
print("Germany:", round(m_de.params["personal:discount"] * 100, 2), "pp, p",
      round(m_de.pvalues["personal:discount"], 3))
print("Spain:", round(m_es.params["personal:discount"] * 100, 2), "pp, p",
      round(m_es.pvalues["personal:discount"], 3))

# %%
# the difference of the interaction, Spain − Germany
m_three = smf.ols("clicked ~ personal * discount * C(country)", data=fa.to_pandas()).fit()
term = "personal:discount:C(country)[T.ES]"
print("Spain - Germany in pp:", round(m_three.params[term] * 100, 2))
print("p:", round(m_three.pvalues[term], 3))

# %%
# click rate per cell and market, one panel per market
markets = (fa.group_by("country", "personal", "discount")
           .agg(pl.col("clicked").mean().alias("rate"))
           .sort("country", "personal", "discount"))
print(markets)
(ggplot(markets, aes("discount", "rate", colour="factor(personal)"))
 + geom_line() + geom_point() + facet_wrap("country")
 + labs(x="Discount", y="Click rate", colour="First name")).show()

