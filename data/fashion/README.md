# Fashion brand in twelve European countries

`fashion_countries.csv`: sales of one fashion brand on a large online fashion platform, by **article type** and **country**, for two collections: Spring/Summer 2025 (`SS25`) and Spring/Summer 2026 (`SS26`). Real data, anonymised for teaching: the brand is not named, and volumes and money are rescaled by undisclosed factors. Shares, conversion, elasticities and country differences are as in the original. Each row adds up a whole season (no weekly data, no media spend).

403 rows: 187 in SS25 (11 countries, 17 article types), 216 in SS26 (12 countries, 18 article types). Switzerland (`CH`) is new in SS26; Sweden (`SE`) almost disappears.

| Column | Meaning |
|---|---|
| `season` | collection: `SS25` or `SS26` |
| `country` | market: AT, BE, CH, CZ, DE, DK, FI, FR, IT, NL, PL, SE |
| `article_type` | e.g. Dress, T-shirt top, Trouser, Bikini combination |
| `offered_articles` | number of articles offered (rescaled) |
| `pdp_views` | product detail page views (rescaled) |
| `add_to_basket_pct` | share of page views with an add to basket, % |
| `conversion_pct` | sold articles per 100 page views, % |
| `sold_articles` | articles sold (rescaled) |
| `avg_item_value` | average gross price per sold article, incl. VAT (rescaled) |
| `nmv` | net merchandise value: sales net of VAT (rescaled) |
| `discount_pct` | average discount on sold articles, % |
| `size_availability_pct` | average share of sizes in stock, % |
| `return_rate_pct` | estimated return rate, %; SS26 only (missing for SS25) |

Notes for analysis:

- 18 rows have no sales (`sold_articles` = 0): filter them out before taking logs.
- `nmv / (sold_articles * avg_item_value)` is about 1 / (1 + VAT rate) of the country: 0.84 in DE (19 %), 0.93 in CH (8.1 %), 0.80 in DK and SE (25 %).
- The data are cross-sectional: the price coefficient compares article types and countries, not a price change.

Prepared and anonymised by the instructor; the raw exports are not part of the repository.
