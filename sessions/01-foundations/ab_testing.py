"""Experiments and A/B testing: the sample code of the deck as a plain Python script.

The same code as ab_testing.qmd (sessions/01-foundations), for the deck "Experiments and A/B testing" of
International Marketing Analytics: the operator's retention e-mail, the A/B test of the subject line
(data/abtest/email_ab.csv) and the 2 x 2 test of first name x discount (data/abtest/email_factorial.csv).
Steps 1 to 3 are the code of slides 31 to 33: load, dummy coding and the split check; the effect of B with OLS
(clicked ~ split, the moderators mobile and spain, the guardrail, the optional sample size); the 2 x 2 with OLS
(clicked ~ personal * discount) and its interaction plot. The explanations of each result are in ab_testing.qmd
and its rendered html.

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
import polars as pl
import statsmodels.formula.api as smf
from plotnine import aes, geom_col, geom_line, geom_point, ggplot, labs

# %% Step 1: load, dummy coding and the split check
import polars as pl

ab = pl.read_csv(
    "../../data/abtest/email_ab.csv")

# dummy coding: 1 = yes, 0 = no
ab = ab.with_columns(
    mobile=(pl.col("device") == "mobile")
    .cast(pl.Int64),
    spain=(pl.col("country") == "ES")
    .cast(pl.Int64))

# split check: customers per group
print(ab.group_by("split", "version")
      .agg(n=pl.len(),
           click_rate=pl.col("clicked").mean(),
           mobile=pl.col("mobile").mean())
      .sort("split"))

# %%
# the split per market: 10,000 per version in Germany and in Spain
print(ab.group_by("country", "version")
      .agg(n=pl.len())
      .sort("country", "version"))

# %%
# bar chart: the click rate per version (slide 6)
rates = ab.group_by("version").agg(click_rate=pl.col("clicked").mean())
(ggplot(rates, aes("version", "click_rate"))
 + geom_col()
 + labs(x="Version", y="Click rate")).show()

# %% Step 2: the effect of B with OLS
import statsmodels.formula.api as smf

# B - A: the coefficient of the dummy split
m = smf.ols("clicked ~ split",
            data=ab.to_pandas()).fit()
print((m.params * 100).round(3))     # pp
print(m.pvalues.round(4))
print((m.conf_int() * 100).round(2))  # CI

# moderator: does B work better on mobile?
m_mob = smf.ols("clicked ~ split * mobile",
                data=ab.to_pandas()).fit()
print((m_mob.params * 100).round(3))
print(m_mob.pvalues.round(4))

# %%
# the relative lift: B − A as a share of A, in %
print(round(m.params["split"] / m.params["Intercept"] * 100, 1))

# %%
# the guardrail: unsubscribes, the same model (slides 14 and 15)
m_unsub = smf.ols("unsubscribed ~ split", data=ab.to_pandas()).fit()
print((m_unsub.params * 100).round(3))   # pp
print(m_unsub.pvalues.round(3))

# %%
# B − A on mobile and on desktop: the model of slide 32 on each group (slide 18)
m_m = smf.ols("clicked ~ split", data=ab.filter(pl.col("mobile") == 1).to_pandas()).fit()
m_d = smf.ols("clicked ~ split", data=ab.filter(pl.col("mobile") == 0).to_pandas()).fit()
print("mobile:", round(m_m.params["split"] * 100, 2), "pp, p", round(m_m.pvalues["split"], 4))
print("desktop:", round(m_d.params["split"] * 100, 2), "pp, p", round(m_d.pvalues["split"], 4))
print("customers:", m_m.nobs, m_d.nobs)

# %%
# customers per version for 3.3 % → 3.9 % with 80 % power
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

print(NormalIndPower().solve_power(proportion_effectsize(0.039, 0.033), alpha=0.05, power=0.8))

# %% Step 3: the 2 × 2 with OLS and its plot
from plotnine import ggplot, aes, labs
from plotnine import geom_line, geom_point

fa = pl.read_csv(
    "../../data/abtest/email_factorial.csv")
m2 = smf.ols("clicked ~ personal * discount",
             data=fa.to_pandas()).fit()
print((m2.params * 100).round(3))   # pp
print(m2.pvalues.round(4))

# interaction plot: click rate per cell
cells = (fa.group_by("personal", "discount")
         .agg(rate=pl.col("clicked").mean()))
(ggplot(cells)
 + aes("discount", "rate",
       colour="factor(personal)")
 + geom_line() + geom_point()
 + labs(colour="First name")).show()

# %%
# the four cells: customers, click rate and unsubscribe rate (slide 23)
print(fa.group_by("personal", "discount")
      .agg(n=pl.len(),
           click_rate=pl.col("clicked").mean(),
           unsub_rate=pl.col("unsubscribed").mean())
      .sort("personal", "discount"))

# %%
# the 2 × 2 by market: the dummy spain and the three-way term
fa = fa.with_columns(spain=(pl.col("country") == "ES").cast(pl.Int64))
m3 = smf.ols("clicked ~ personal * discount * spain", data=fa.to_pandas()).fit()
print((m3.params * 100).round(2))
print(m3.pvalues.round(3))
