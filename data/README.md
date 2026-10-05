# Data

All datasets describe **Alpenglow**, a fictional Vienna-based premium chocolate brand sold in six European markets (AT, DE, FR, IT, NL, PL). The data are synthetic: they look and behave like real marketing data, but no real company or customer is behind them.

## `data/mmm/alpenglow_weekly.csv` — weekly country panel (936 rows = 6 countries × 156 weeks)

| Column | Description |
|--------|-------------|
| `week` | Monday of the ISO week, 2023-01-02 … 2025-12-22 (156 ISO weeks; 2025 holds 51 weeks) |
| `country` | ISO-2 code: AT, DE, FR, IT, NL, PL |
| `sales_units_k` | Units sold (thousands) |
| `revenue_eur_k` | Revenue (thousand EUR) = units × price |
| `price_eur` | Average realised retail price per unit (EUR) |
| `promo_share` | Share of volume sold on promotion (0–1) |
| `distribution` | Weighted distribution (share of retail outlets stocking the brand, 0–1) |
| `competitor_spend_k` | Index of competitor media spend (thousand EUR equivalent) |
| `consumer_confidence` | Consumer confidence index, de-meaned |
| `temperature_c` | Average weekly temperature (°C) |
| `xmas`, `easter`, `valentine` | Holiday dummies (pre-holiday selling weeks) |
| `spend_tv_k` | TV advertising spend (thousand EUR) |
| `spend_online_video_k` | Online video spend (thousand EUR) |
| `spend_paid_search_k` | Paid search spend (thousand EUR) |
| `spend_paid_social_k` | Paid social spend (thousand EUR) |
| `spend_ooh_k` | Out-of-home spend (thousand EUR) |

## `data/mmm/country_meta.csv` — country metadata

Population (millions), GDP per capita (thousand EUR), Hofstede scores (individualism, uncertainty avoidance, long-term orientation; approximate published values), Eurozone membership, years since market entry, retail concentration (share of top-3 retailers).

## `data/experiments/geolift_germany.csv` — geo-lift test (2 560 rows = 40 regions × 64 weeks)

A paid-social uplift (spend × 2.5) ran in 12 German regions for 8 weeks (`test_period = 1`), with 48 pre-test and 8 post-test weeks. Columns: `week`, `region`, `treated`, `test_period`, `post_period`, `paid_social_spend_k`, `sales_units_k`, `population_k`.

## `data/attribution/journeys.csv` — customer journeys (60 000 rows, one per journey)

`journey_id`, `country`, `start_date`, `path_length`, `first_touch`, `last_touch`, `mobile`, `new_customer`, touch counts per channel (`n_display`, `n_paid_search`, `n_paid_social`, `n_email`, `n_affiliate`, `n_organic`), `converted`, `order_value_eur`, `path` (channels in order, separated by ` > `).

`attribution/journeys_long.csv` holds the same journeys in long format, one row per touchpoint.

## `data/legacy/`: warm-up datasets for Session 1

- `Video_Games_Sales.csv`: sales of 16 719 video games in North America, Europe, Japan and the rest of the world (millions of units), with genre, platform, critic and user scores. Public dataset from Kaggle ("Video Game Sales with Ratings", based on VGChartz and Metacritic).
- `chocolate_dataset.xlsx`: 68 weeks of sales, prices, features and displays for four chocolate brands (Lab 1, exercise 4).
