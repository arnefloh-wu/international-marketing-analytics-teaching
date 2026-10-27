# Customer churn: readings, practice and data

This guide goes with the deck "Logistic regression across countries" and [`logit_churn.qmd`](logit_churn.qmd): sources for the slides, datasets and thesis topics. The running example, `telco_churn.csv`, is **simulated**; everything else here is real and comes with its source.

## 1. How the sources were checked, and how to read the tags

- **Articles.** Each DOI was checked against a Semantic Scholar/OpenAlex record (via the Consensus index) and at least one independent bibliographic source (publisher page, RePEc/IDEAS, DBLP, a university repository or an author CV). Crossref could not be reached when the list was compiled (October 2026), so do a final Crossref or Zotero pass before you cite a reference in a thesis.
- **Practice figures** come from extracts of the named document and carry a date. **Law** is a teaching summary, not legal advice, checked against news and law-firm reports, not always the primary text.
- **Datasets.** Sizes and base rates were computed on downloaded copies for IBM Telco, Churn_Modelling, Online Retail II (2009–10 sheet), Hotel Booking, Orange/MLC++ and the Cell2Cell mirror; the others come from their documentation. Several licence pages could not be opened, and the licence column says so.

| Tag | Meaning |
|---|---|
| *(abstract)* | Number seen only in the abstract or a publisher summary. Check the paper before you quote it. |
| † | One detail (volume, issue, pages or authors) not re-confirmed, so only author, year, title and journal are given. |
| **[P]** | Figure from an extract of the primary document (annual report, regulator, court, the firm's own release). |
| **[2H]** | Second-hand figure (press, analyst, trade site). Treat it as indicative. |
| **[L]** | Legal provision stated from the compiler's knowledge of the statute; not checked against the text when this list was compiled. |
| OA | Open access: "yes" = a free author or repository copy was found; "not found" = none showed up in the search (which does not mean none exists); "not checked" = not searched for. |

## 2. Start here: five readings

1. **Ascarza et al. (2018)**, "In pursuit of enhanced customer retention management", *Customer Needs and Solutions*. The framing review by churn researchers and practitioners; free copy on LBS Research Online. https://doi.org/10.1007/s40547-017-0080-0
2. **Neslin et al. (2006)**, "Defection detection", *Journal of Marketing Research*. The tournament that made logit the benchmark and top-decile lift the yardstick. https://doi.org/10.1509/jmkr.43.2.204
3. **Ascarza (2018)**, "Retention futility", *Journal of Marketing Research*. The customers most likely to churn are not necessarily the ones an offer saves. https://doi.org/10.1509/jmr.16.0163
4. **Mood (2010)**, "Logistic regression: Why we cannot do what we think we can do", *European Sociological Review*. Why odds ratios cannot simply be compared across countries or models. https://doi.org/10.1093/esr/jcp006
5. **Long & Mustillo (2021)**, "Using predictions and marginal effects to compare groups", *Sociological Methods & Research*. The workflow the deck follows; author drafts on the Indiana University site. https://doi.org/10.1177/0049124118799374

## 3. Articles by strand

### 3.1 Churn prediction: logit compared with machine learning

| Reference | Takeaway in one line | OA |
|---|---|---|
| Neslin, S. A., Gupta, S., Kamakura, W., Lu, J., & Mason, C. H. (2006). Defection detection: Measuring and understanding the predictive accuracy of customer churn models. *Journal of Marketing Research, 43*(2), 204–211. https://doi.org/10.1509/jmkr.43.2.204 | Shows why logit is the benchmark: in a tournament on one US carrier's data, "logit" and "tree" approaches did best and lost little accuracy three months later *(abstract)*. | not found |
| Lemmens, A., & Croux, C. (2006). Bagging and boosting classification trees to predict churn. *Journal of Marketing Research, 43*(2), 276–286. https://doi.org/10.1509/jmkr.43.2.276 | Bagging and boosting beat binary logit on US wireless data; balanced samples need a bias correction of the predicted probabilities *(abstract)*. | yes (Tilburg repository) |
| Coussement, K., & Van den Poel, D. (2008). Churn prediction in subscription services: An application of support vector machines while comparing two parameter-selection techniques. *Expert Systems with Applications, 34*(1), 313–327. https://doi.org/10.1016/j.eswa.2006.09.038 | For newspaper subscriptions, SVMs beat logit only with optimal tuning, and random forests beat both SVM variants. | not found (earlier working paper on RePEc) |
| Risselada, H., Verhoef, P. C., & Bijmolt, T. H. A. (2010). Staying power of churn prediction models. *Journal of Interactive Marketing, 24*(3), 198–208. https://doi.org/10.1016/j.intmar.2010.04.002 | Every method's performance deteriorates within a few periods because coefficients drift: re-estimate regularly. | not found |
| Verbeke, W., Dejaeger, K., Martens, D., Hur, J., & Baesens, B. (2012). New insights into churn prediction in the telecommunication sector: A profit driven data mining approach. *European Journal of Operational Research, 218*(1), 211–229. https://doi.org/10.1016/j.ejor.2011.09.031 | On 11 operator datasets, many classifiers including logit perform comparably, oversampling generally does not help, and choosing models by maximum profit raises profit *(abstract)*. | not found |
| Coussement, K., Lessmann, S., & Verstraeten, G. (2017). A comparative analysis of data preparation algorithms for customer churn prediction: A case study in the telecommunication industry. *Decision Support Systems, 95*, 27–36. https://doi.org/10.1016/j.dss.2016.11.007 | Good data preparation lifts a logit's AUC by up to 14.5 % and top-decile lift by up to 34 %, making it competitive with eight advanced algorithms *(abstract)*. | yes (HAL) |
| De Caigny, A., Coussement, K., & De Bock, K. W. (2018). A new hybrid classification algorithm for customer churn prediction based on logistic regression and decision trees. *European Journal of Operational Research, 269*(2), 760–772. https://doi.org/10.1016/j.ejor.2018.02.009 | The logit leaf model (a tree forms segments, a logit in each leaf) matches random forests and keeps logit interpretability. | not found |
| Óskarsdóttir, M., Bravo, C., Verbeke, W., Sarraute, C., Baesens, B., & Vanthienen, J. (2017). Social network analytics for churn prediction in telco: Model building, evaluation and network architecture. *Expert Systems with Applications, 85*, 204–220. https://doi.org/10.1016/j.eswa.2017.05.028 | Across eight call-record datasets, a plain classifier such as logit plus network features was the best set-up *(abstract)*. | not found |
| Gattermann-Itschert, T., & Thonemann, U. W. (2022). Proactive customer retention management in a non-contractual B2B setting based on churn prediction with random forests. *Industrial Marketing Management, 107*, 134–147. https://doi.org/10.1016/j.indmarman.2022.09.023 | In a B2B field experiment, contacting the highest-risk customers cut churn compared with random targeting. | not found |

### 3.2 Evaluation, targeting and profit

| Reference | Takeaway in one line | OA |
|---|---|---|
| Ascarza, E. (2018). Retention futility: Targeting high-risk customers might be ineffective. *Journal of Marketing Research, 55*(1), 80–98. https://doi.org/10.1509/jmr.16.0163 | Two field experiments show that targeting by response to the offer (uplift) reduces churn more than targeting by risk; Paul E. Green Award 2018, Weitz-Winer-O'Dell Award 2023. | not found |
| Ascarza, E., Iyengar, R., & Schleicher, M. (2016). The perils of proactive churn prevention using plan recommendations: Evidence from a field experiment. *Journal of Marketing Research, 53*(1), 46–60. https://doi.org/10.1509/jmr.13.0483 | Recommending cheaper plans to mobile customers raised churn to 10 % against 6 % in the control group over three months *(abstract)*. | yes (author PDF, Columbia) |
| Lemmens, A., & Gupta, S. (2020). Managing churn to maximize profits. *Marketing Science, 39*(5), 956–973. https://doi.org/10.1287/mksc.2020.1229 | Rank customers by the offer's incremental effect on churn and cash flow, net of cost; in two field experiments this beat risk ranking *(abstract)*. | yes (SSRN working paper 2964906) |
| Ascarza, E., Neslin, S. A., Netzer, O., Anderson, Z., Fader, P. S., Gupta, S., Hardie, B. G. S., Lemmens, A., Libai, B., Neal, D., Provost, F., & Schrift, R. (2018). In pursuit of enhanced customer retention management: Review, key issues, and future directions. *Customer Needs and Solutions, 5*(1–2), 65–81. https://doi.org/10.1007/s40547-017-0080-0 | Separates "who is at risk" from "who should be targeted" and reviews retention metrics and campaign design. | yes (LBS Research Online) |
| Verbraken, T., Verbeke, W., & Baesens, B. (2013). A novel profit maximizing metric for measuring classification performance of customer churn prediction models. *IEEE Transactions on Knowledge and Data Engineering, 25*(5), 961–973. https://doi.org/10.1109/TKDE.2012.50 | The expected maximum profit (EMP) measure picks the classifier and the share of customers to contact under uncertain costs and benefits. | not found |
| Godinho de Matos, M., Ferreira, P., & Belo, R. (2018). Target the ego or target the group: Evidence from a randomized experiment in proactive churn management. *Marketing Science, 37*(5), 793–811. https://doi.org/10.1287/mksc.2018.1099 | Calling likely churners cut churn by 1.9 pp from a 17.2 % baseline; calling their friends too cut it by a further 1.3 pp *(abstract)*. | SSRN version (10.2139/ssrn.2591671) |
| Devriendt, F., Berrevoets, J., & Verbeke, W. (2021). Why you should stop predicting customer churn and start using uplift models. *Information Sciences, 548*, 497–515. https://doi.org/10.1016/j.ins.2019.12.075 | In a financial-services retention case, uplift models beat churn-prediction models on campaign profit. | yes |
| Van Calster, B., et al. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine, 17*, 230. https://doi.org/10.1186/s12916-019-1466-7 | A model can rank well and still predict the wrong level; check calibration whenever probabilities feed into money. | yes (PMC6912996) |
| van den Goorbergh, R., van Smeden, M., Timmerman, D., & Van Calster, B. (2022). The harm of class imbalance corrections for risk prediction models: Illustration and simulation using logistic regression. *Journal of the American Medical Informatics Association, 29*(9), 1525–1534. https://pmc.ncbi.nlm.nih.gov/articles/PMC9382395/ | Under-, oversampling and SMOTE gave poorly calibrated logits and did not improve AUC. | yes (PMC) |

Three method notes (†, cite as shown): King & Zeng (2001), *Political Analysis* †, on correcting the intercept after sampling on the outcome ([Cambridge page](https://www.cambridge.org/core/journals/political-analysis/article/logistic-regression-in-rare-events-data/1E09F0F36F89DF12A823130FDF0DA462)); Elkan (2001), IJCAI †, on choosing the threshold from error costs (https://mlanthology.org/ijcai/2001/elkan2001ijcai-foundations); Gutierrez & Gérardy (2017), PMLR 67 †, a review of uplift modelling (https://proceedings.mlr.press/v67/gutierrez17a.html).

### 3.3 Drivers of churn and switching

| Reference | Takeaway in one line | OA |
|---|---|---|
| Keaveney, S. M. (1995). Customer switching behavior in service industries: An exploratory study. *Journal of Marketing, 59*(2), 71–82. https://doi.org/10.1177/002224299505900206 | Over 800 critical incidents from over 500 customers fall into eight switching causes, from pricing to core service failure *(abstract)*. | not found |
| Bolton, R. N. (1998). A dynamic model of the duration of the customer's relationship with a continuous service provider: The role of satisfaction. *Marketing Science, 17*(1), 45–65. https://doi.org/10.1287/mksc.17.1.45 | In a hazard model of cellular customers, prior satisfaction lengthens the relationship and failures weigh more than gains. | not found |
| Gustafsson, A., Johnson, M. D., & Roos, I. (2005). The effects of customer satisfaction, relationship commitment dimensions, and triggers on customer retention. *Journal of Marketing, 69*(4), 210–218. https://doi.org/10.1509/jmkg.2005.69.4.210 | Survey satisfaction, calculative commitment and prior churn predict later observed churn at a Swedish telecom (Telia). | yes (Cornell eCommons) |
| Burnham, T. A., Frels, J. K., & Mahajan, V. (2003). Consumer switching costs: A typology, antecedents, and consequences. *Journal of the Academy of Marketing Science, 31*(2), 109–126. https://doi.org/10.1177/0092070302250897 | Procedural, financial and relational switching costs together explain more of the intention to stay than satisfaction does *(abstract)*. | not found |
| Mittal, V., & Kamakura, W. A. (2001). Satisfaction, repurchase intent, and repurchase behavior: Investigating the moderating effect of customer characteristics. *Journal of Marketing Research, 38*(1), 131–142. https://doi.org/10.1509/jmkr.38.1.131.18832 | For 100,040 car buyers, the same rated satisfaction means different repurchase rates in different groups *(abstract)*. | not found |
| Gao, L. (X.), de Haan, E., Melero-Polo, I., & Sese, F. J. (2023). Winning your customers' minds and hearts: Disentangling the effects of lock-in and affective customer experience on retention. *Journal of the Academy of Marketing Science, 51*(2), 334–371. https://doi.org/10.1007/s11747-022-00898-z | Lock-in cuts churn by about 48–49 % when the experience is poor, and the effect fades once it is good *(abstract)*. | yes (University of Zaragoza repository) |

### 3.4 Churn and switching across countries

| Reference | Takeaway in one line | OA |
|---|---|---|
| Patterson, P. G., & Smith, T. (2003). A cross-cultural study of switching barriers and propensity to stay with service providers. *Journal of Retailing* †. https://doi.org/10.1016/S0022-4359(03)00009-5 | Switching barriers work largely alike in Australia and Thailand but differ across industries. | not checked |
| Lee, J., Lee, J., & Feick, L. (2001). The impact of switching costs on the customer satisfaction-loyalty link: Mobile phone service in France. *Journal of Services Marketing, 15*(1), 35–48. https://doi.org/10.1108/08876040110381463 | In French mobile, high switching costs keep some dissatisfied customers: loyal-looking is not the same as satisfied. | not found |
| Liu, B. S.-C., Furrer, O., & Sudharshan, D. (2001). The relationships between culture and behavioral intentions toward services. *Journal of Service Research, 4*(2), 118–129. https://doi.org/10.1177/109467050142004 | After poor service, customers from low-individualism or high-uncertainty-avoidance cultures are less likely to switch. | not checked |
| Zhang, S., van Doorn, J., & Leeflang, P. S. H. (2014). Does the importance of value, brand and relationship equity for customer loyalty differ between Eastern and Western cultures? *International Business Review, 23*(1), 284–292. https://doi.org/10.1016/j.ibusrev.2013.05.002 | Chinese consumers are more loyal overall, yet the loyalty drivers are stronger for Dutch consumers: intercepts and slopes differ *(abstract)*. | not checked |
| Frank, B., Enkawa, T., & Schvaneveldt, S. J. (2015). The role of individualism vs. collectivism in the formation of repurchase intent: A cross-industry comparison of the effects of cultural and personal values. *Journal of Economic Psychology, 51*, 261–278. https://doi.org/10.1016/j.joep.2015.08.008 | Across six countries, country-level individualism matters more than personal individualism and strengthens the satisfaction effect *(abstract)*. | not checked |
| Blut, M., Beatty, S. E., & Northington, W. M. (2022). Cultural personal values and switching costs perceptions: Beyond Hofstede. *Journal of Business Research, 150*, 339–353. https://doi.org/10.1016/j.jbusres.2022.06.005 | In 16 countries, vertical individualism has the strongest link with perceived switching costs *(abstract)*. | not checked |
| Schumann, J. H., von Wangenheim, F., Stringfellow, A., Yang, Z., Blazevic, V., Praxmarer, S., Shainesh, G., Komor, M., Shannon, R. M., & Jiménez, F. R. (2010). Cross-cultural differences in the effect of received word-of-mouth referral in relational service exchange. *Journal of International Marketing, 18*(3), 62–80. https://doi.org/10.1509/jimk.18.3.62 | Across 11 countries, only uncertainty avoidance moderated the word-of-mouth effect: do not add every Hofstede interaction *(abstract)*. | not checked |
| Thompson, F. M., & Chmura, T. (2015). Loyalty programs in emerging and developed markets: The impact of cultural values on loyalty program choice. *Journal of International Marketing, 23*(3), 87–103. https://doi.org/10.1509/jim.14.0125 | Cultural values shape which loyalty rewards customers prefer, and some cultures shun programmes for immediate promotions. | not checked |
| Morgeson, F. V., III, Mithas, S., Keiningham, T. L., & Aksoy, L. (2011). An investigation of the cross-national determinants of customer satisfaction. *Journal of the Academy of Marketing Science, 39*(2), 198–215. https://doi.org/10.1007/s11747-010-0232-3 | In 19 nations (about 257,000 interviews), satisfaction levels differ for cultural and institutional reasons *(abstract)*. | not found |
| Aksoy, L., Buoye, A., Aksoy, P., Larivière, B., & Keiningham, T. L. (2013). A cross-national investigation of the satisfaction and loyalty linkage for mobile telecommunications services across eight countries. *Journal of Interactive Marketing, 27*(1), 74–82. https://doi.org/10.1016/j.intmar.2012.09.003 | In mobile telecom in eight countries (3,393 customers), the satisfaction-loyalty link depends on culture and has thresholds *(abstract)*. | not found |
| Morgeson, F. V., III, Sharma, P. N., & Hult, G. T. M. (2015). Cross-national differences in consumer satisfaction: Mobile services in emerging and developed markets. *Journal of International Marketing, 23*(2), 1–24. https://doi.org/10.1509/jim.14.0127 | Satisfaction matters less for loyalty in emerging than in developed mobile markets. | not found |
| Steenkamp, J.-B. E. M., & Geyskens, I. (2006). How country characteristics affect the perceived value of web sites. *Journal of Marketing, 70*(3), 136–150. https://doi.org/10.1509/jmkg.70.3.136 | With 8,886 consumers in 23 countries, institutions (rule of law) and culture moderate what drives perceived value *(abstract)*. | not checked |
| Samaha, S. A., Beck, J. T., & Palmatier, R. W. (2014). The role of culture in international relationship marketing. *Journal of Marketing, 78*(5), 78–98. https://doi.org/10.1509/jm.13.0185 | A meta-analysis over 36 countries finds individualism the strongest cultural moderator of relationship marketing *(abstract)*. | not checked |
| Pick, D., & Eisend, M. (2014). Buyers' perceived switching costs and switching: A meta-analytic assessment of their antecedents. *Journal of the Academy of Marketing Science, 42*(2), 186–204. https://doi.org/10.1007/s11747-013-0349-2 | Over 170 samples, switching costs have only a weak negative effect on switching, moderated by culture *(abstract)*. | not checked |
| Pick, D., & Eisend, M. (2016). Customer responses to switching costs: A meta-analytic investigation of the moderating influence of culture. *Journal of International Marketing* †. https://doi.org/10.1509/jim.15.0139 | Over 25 countries, economic development decides whether switching costs reduce or increase switching: even the sign can change *(abstract)*. | not found |
| Buehler, S., Dewenter, R., & Haucap, J. (2006). Mobile number portability in Europe. *Telecommunications Policy, 30*(7), 385–399. https://doi.org/10.1016/j.telpol.2006.04.001 | Porting speed and charges appear to explain part of the cross-country differences in number-portability use. | not checked |
| Usero Sánchez, B., & Asimakopoulos, G. (2012). Regulation and competition in the European mobile communications industry: An examination of the implementation of mobile number portability. *Telecommunications Policy, 36*(3), 187–196. https://doi.org/10.1016/j.telpol.2011.12.008 | In EU mobile markets, churn falls as porting charges rise and porting takes longer: baselines differ for institutional reasons. | not checked |
| Wei, X., & Zhu, K. X. (2018). The asymmetric impact of customer information portability on service competition: Evidence from the global wireless industry. *Production and Operations Management, 27*(5), 839–858. https://doi.org/10.1111/poms.12830 | Across 218 operators in 52 countries, contracts became more important as lock-in after number portability *(abstract)*. | not checked |

### 3.5 Measurement across countries

| Reference | Takeaway in one line | OA |
|---|---|---|
| Steenkamp, J.-B. E. M., & Baumgartner, H. (1998). Assessing measurement invariance in cross-national consumer research. *Journal of Consumer Research, 25*(1), 78–90. https://doi.org/10.1086/209528 | Comparing relationships needs metric invariance and comparing means needs scalar invariance; test before you pool survey scores. | not found |
| Baumgartner, H., & Steenkamp, J.-B. E. M. (2001). Response styles in marketing research: A cross-national investigation. *Journal of Marketing Research, 38*(2), 143–156. https://doi.org/10.1509/jmkr.38.2.143.18840 | In 11 EU countries, five response styles bias scale scores and the correlations between them *(abstract)*. | not found |

### 3.6 Comparing logit models across groups, and interactions

| Reference | Takeaway in one line | OA |
|---|---|---|
| Allison, P. D. (1999). Comparing logit and probit coefficients across groups. *Sociological Methods & Research, 28*(2), 186–208. https://doi.org/10.1177/0049124199028002003 | If unexplained variation differs across groups, comparing coefficients (or group interactions) can mislead. | not found |
| Williams, R. (2009). Using heterogeneous choice models to compare logit and probit coefficients across groups. *Sociological Methods & Research, 37*(4), 531–559. https://doi.org/10.1177/0049124109335735 | Model group differences in scale explicitly (location-scale models) rather than apply Allison's correction routinely. | yes (preprint, Notre Dame) |
| Mood, C. (2010). Logistic regression: Why we cannot do what we think we can do, and what we can do about it. *European Sociological Review, 26*(1), 67–82. https://doi.org/10.1093/esr/jcp006 | Odds ratios absorb unobserved heterogeneity, so report average marginal effects (AMEs) or linear probability models. | not found |
| Long, J. S., & Mustillo, S. A. (2021). Using predictions and marginal effects to compare groups in regression models for binary outcomes. *Sociological Methods & Research, 50*(3), 1284–1320. https://doi.org/10.1177/0049124118799374 | Predicted probabilities and marginal effects do not depend on how the coefficients are scaled, so compare groups with them. | yes (author drafts, Indiana) |
| Mize, T. D. (2019). Best practices for estimating, interpreting, and presenting nonlinear interaction effects. *Sociological Science, 6*, 81–117. https://doi.org/10.15195/v6.a4 | Interpret interactions with second differences, AMEs at representative values and plots. | yes (CC BY) |
| Ai, C., & Norton, E. C. (2003). Interaction terms in logit and probit models. *Economics Letters, 80*(1), 123–129. https://doi.org/10.1016/S0165-1765(03)00032-6 | The interaction effect is not the product-term coefficient and can even have the opposite sign. | not found |
| Hoetker, G. (2007). The use of logit and probit models in strategic management research: Critical issues. *Strategic Management Journal, 28*(4), 331–343. https://doi.org/10.1002/smj.582 | A checklist of four problem areas: coefficients, interactions, group comparisons and fit. | not checked |
| Swait, J., & Louviere, J. (1993). The role of the scale parameter in the estimation and comparison of multinomial logit models. *Journal of Marketing Research, 30*(3), 305–314. https://doi.org/10.1177/002224379303000303 | Identical true effects estimated in two data sets with different error variance must differ in size; a likelihood-ratio test separates the two. | not checked |
| Wiersema, M. F., & Bowen, H. P. (2009). The use of limited dependent variable techniques in strategy research: Issues and methods. *Strategic Management Journal, 30*(6), 679–692. https://doi.org/10.1002/smj.758 | The significance of a marginal effect has to be computed, not read off the coefficient table. | not checked |
| Karlson, K. B., Holm, A., & Breen, R. (2012). Comparing regression coefficients between same-sample nested models using logit and probit. *Sociological Methodology* †. https://doi.org/10.1177/0081175012444861 | A method for comparing coefficients between nested logit models on the same sample. | not checked |

For a counterpoint, see Kuha & Mills (2020), Sociological Methods & Research, https://doi.org/10.1177/0049124117747306 (volume and pages not verified).

Also on the course's earlier reference list (details as given there; no DOI listed): Greene, Chidlow & Strange (2022), *International Business Review* 31(4), 102011, a primer on multinomial choice models; Bryan & Jenkins (2016), *European Sociological Review*, on why country-level effects are unreliable with few countries.

### 3.7 Frontiers 2019–2026

| Reference | Takeaway in one line | OA |
|---|---|---|
| Yang, J., Eckles, D., Dhillon, P., & Aral, S. (2024). Targeting for long-term outcomes. *Management Science, 70*(6), 3841–3855. https://doi.org/10.1287/mnsc.2023.4881 | In churn experiments at *The Boston Globe*, a policy learned from short-term surrogates performed as well as one learned on long-term outcomes *(abstract)*. | not checked |
| Haupt, J., & Lessmann, S. (2022). Targeting customers under response-dependent costs. *European Journal of Operational Research, 297*(1), 369–379. https://doi.org/10.1016/j.ejor.2021.05.045 | If the incentive is paid only on response, profitable targeting needs both the treatment effect and the response probability. | not checked |
| Simester, D., Timoshenko, A., & Zoumpoulis, S. I. (2020). Targeting prospective customers: Robustness of machine-learning methods to typical data challenges. *Management Science, 66*(6), 2495–2522. https://doi.org/10.1287/mnsc.2019.3308 | Model-based targeting loses its edge under covariate and concept shift, the problem of moving a model to another country (setting: prospecting, not churn). | not checked |
| Einav, L., Klopack, B., & Mahoney, N. (2025). Selling subscriptions. *American Economic Review, 115*(5), 1650–1671. https://doi.org/10.1257/aer.20231612 | Cancellations spike when payment cards are replaced; inertia roughly doubles seller revenue *(abstract)*. | not checked |
| Reme, B.-A., Røhr, H. L., & Sæthre, M. (2022). Inattention in contract markets: Evidence from a consolidation of options in telecom. *Management Science, 68*(2), 1019–1038. https://doi.org/10.1287/mnsc.2021.3975 | A price-change letter woke up Norwegian mobile customers: monthly churn rose from 1 % to 1.6 % even where costs would fall *(abstract)*. | not checked |
| Godinho de Matos, M., & Ferreira, P. (2020). The effect of binge-watching on the subscription of video on demand: Results from randomized experiments. *Information Systems Research, 31*(4), 1337–1360. https://doi.org/10.1287/isre.2020.0948 | Households induced to binge-watch during a free trial were less likely to subscribe afterwards: usage is not monotone in retention. | not checked |
| Luguri, J., & Strahilevitz, L. J. (2021). Shining a light on dark patterns. *Journal of Legal Analysis, 13*(1), 43–109. https://doi.org/10.1093/jla/laaa006 | Mild dark patterns more than doubled sign-ups and aggressive ones nearly quadrupled them in US experiments *(abstract)*. | not checked |
| Sheil, A., Acar, G., Schraffenberger, H., Gellert, R., & Malone, D. (2024). Staying at the roach motel: Cross-country analysis of manipulative subscription and cancellation flows. In *Proceedings of CHI '24*. ACM. https://doi.org/10.1145/3613904.3642881 | An audit of news-site cancellation flows in four countries found deliberate barriers such as forced phone calls; check the paper for the countries. | not checked |
| Ascarza, E., & Israeli, A. (2022). Eliminating unintended bias in personalized policies using bias-eliminating adapted trees (BEAT). *PNAS, 119*(11), e2115293119. https://doi.org/10.1073/pnas.2115293119 | Dropping protected attributes does not remove bias in targeting and can even increase it. | not checked |
| Kozodoi, N., Jacob, J., & Lessmann, S. (2022). Fairness in credit scoring: Assessment, implementation and profit implications. *European Journal of Operational Research* †. https://doi.org/10.1016/j.ejor.2021.06.023 | Several fairness criteria can be met approximately at once; fair in-processing methods cut discrimination at relatively low profit cost. | not checked |
| De Bock, K. W., Coussement, K., De Caigny, A., et al. (2024). Explainable AI for operational research: A defining framework, methods, applications, and a research agenda. *European Journal of Operational Research, 317*(2), 249–272. https://doi.org/10.1016/j.ejor.2023.09.026 | A framework that balances performance, attributable and responsible analytics; a logit is attributable by design. | not checked |
| De Caigny, A., Coussement, K., De Bock, K. W., & Lessmann, S. (2020). Incorporating textual information in customer churn prediction models based on a convolutional neural network. *International Journal of Forecasting, 36*(4), 1563–1578. https://doi.org/10.1016/j.ijforecast.2019.03.029 | Text from customer contacts improves churn prediction but does not replace structured data. | not checked |
| Vo, N. N. Y., Liu, S., Li, X., & Xu, G. (2021). Leveraging unstructured call log data for customer churn prediction. *Knowledge-Based Systems* †. https://doi.org/10.1016/j.knosys.2020.106586 | Transcribed call content from about 200,000 financial-services customers predicts churn *(abstract)*. | not checked |
| Chajia, M., & Nfaoui, E. H. (2024). Customer churn prediction approach based on LLM embeddings and logistic regression. *Future Internet, 16*(12), 453. https://doi.org/10.3390/fi16120453 | A logit on LLM text embeddings was the best telecom churn model in this comparison. Caveat: an MDPI journal, accuracy only, no profit metric. | not checked |
| De Caigny, A., Coussement, K., Verbeke, W., Idbenjra, K., & Phan, M. (2021). Uplift modeling and its implications for B2B customer churn prediction: A segmentation-based modeling approach. *Industrial Marketing Management* †. https://doi.org/10.1016/j.indmarman.2021.10.001 | An uplift version of the logit leaf model beats three popular uplift models for a European software provider and stays interpretable. | not checked |
| Janssens, B., Bogaert, M., Bagué, A., & Van den Poel, D. (2024). B2Boost: Instance-dependent profit-driven modelling of B2B churn. *Annals of Operations Research, 341*(1), 267–293. https://doi.org/10.1007/s10479-022-04631-5 | With very skewed B2B customer values, evaluate on expected profit (EMPB), not accuracy; implemented in the Python package `empulse`. | not checked |
| Ferreira, P., Telang, R., & De Matos, M. G. (2019). Effect of friends' churn on consumer behavior in mobile networks. *Journal of Management Information Systems, 36*(2), 355–390. https://doi.org/10.1080/07421222.2019.1598683 | Each friend who churns raises a user's monthly churn by 0.06 pp against a 2.15 % baseline: churn spreads through networks *(abstract)*. | not checked |

**Working paper, not peer-reviewed:** Miller, K. M., Sahni, N. S., & Strulov-Shlain, A. (2023). *Sophisticated consumers with inertia: Long-term implications from a large-scale field experiment* [Working paper]. SSRN. https://doi.org/10.2139/ssrn.4065098. In an experiment with readers of a European newspaper, offering auto-renewing promotions lowered take-up, as if consumers anticipated their own inertia. Headline magnitudes differ between drafts, so quote the version you cite.

### 3.8 Books and teaching resources

- Blattberg, R. C., Kim, B.-D., & Neslin, S. A. (2008). *Database marketing: Analyzing and managing customers*. Springer. Cite the churn-management chapter (campaign profit, Part 5) by its title from SpringerLink.
- Hofstede, G., Hofstede, G. J., & Minkov, M. (2010). *Cultures and organizations: Software of the mind* (3rd ed.). McGraw-Hill.
- James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An introduction to statistical learning with applications in Python* (ISLP). Springer. Free PDF at https://www.statlearning.com/; classification, resampling and lasso chapters with statsmodels labs.
- Schwarz, J. S., Chapman, C., & Feit, E. M. (2020). *Python for marketing research and analytics*. Springer. https://doi.org/10.1007/978-3-030-49720-0. Chapter 8 includes logistic regression; Colab notebooks at https://github.com/python-marketing-research/python-marketing-research-1ed.
- Verbeke, W., Baesens, B., & Bravo, C. (2017/2018). *Profit-driven business analytics*. Wiley. ISBN 9781119286554. Profit-based evaluation (MP, EMP) and uplift by the authors of the EMP papers (chapter contents not confirmed).
- Arel-Bundock (2026), *Model to Meaning*, CRC; free at https://marginaleffects.com (from the course's earlier reference list).
- Documentation: statsmodels [`get_margeff`](https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.LogitResults.get_margeff.html) and [`fit_regularized`](https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.Logit.fit_regularized.html); scikit-uplift ["Two models approaches"](https://scikit-uplift.readthedocs.io/en/v0.2.0/user_guide/models/two_models.html); EMP in R ([`EMP`](https://cran.r-project.org/package=EMP)) and Python (`empulse`, not installed in the course environment).

## 4. Practical insights

### 4.1 Churn rates differ by country, and by metric

| Country | Operator | Metric as reported | Period | Value | Tag | Source |
|---|---|---|---|---|---|---|
| Germany | O2 Telefónica | Postpaid churn, monthly | Q1 / Q2 / Q3 / Q4 2024 | 1.1 / 1.0 / 1.1 / 1.2 % | [P] | [Data Tables Q1 2025, 14 May 2025](https://www.telefonica.de/file/public/465/20250514-o2-Telefonica-Data-Tables-Q1-25-EN.pdf?attachment=1) |
| Germany | O2 Telefónica (O2 brand) | Implied annualised postpaid churn | 2022 / 2023 / 2024 | 13.1 / 11.6 / 12.2 % | [P] | [Annual Report 2024](https://www.telefonica.de/file/public/826/ANNUAL-REPORT-2024-EN-Telefonica-Deutschland-Holding-AG_protected.pdf?attachment=1) |
| Spain | Telefónica España | Headline churn, monthly | FY2024; FY2025; Q1 2026 | 0.9 % ("best since 2013") [P]; 0.8 % [2H]; 0.7 % [2H] | mixed | [Telefónica FY2024 results release](https://www.telefonica.com/en/communication-room/press-room/telefonica-increases-revenue-e41315-million-2024-meets-financial-targets/); [Capital.es on FY2025](https://capital.es/empresas/telefonica-celebra-resultados-excepcionales-en-espana-en-2025-con-crecimiento-financiero-y-comercial/168633); [RCR Wireless, 14 May 2026](https://www.rcrwireless.com/20260514/carriers/telefonica-brazil-germany-ai-infra-cap) |
| Brazil | Telefónica Brasil (Vivo) | Mobile contract churn, monthly | FY2024 | 0.9 % | [P] | [Telefónica FY2024 results release](https://www.telefonica.com/en/communication-room/press-room/telefonica-increases-revenue-e41315-million-2024-meets-financial-targets/) |
| UK | Virgin Media O2 (O2 brand) | Contract churn, monthly | Q2 2025 | 1.1 % | [P] | [VMO2 Q2 2025 earnings release](https://news.virginmediao2.co.uk/wp-content/uploads/2025/07/Virgin-Media-O2-Q2-2025-Earnings-Release.pdf) |
| USA | T-Mobile US | Postpaid phone churn, monthly | FY2025 (Q4 2025) | 0.93 % (1.02 %) | [P] | [T-Mobile Q4 2025 results](https://www.t-mobile.com/news/business/t-mobile-q4-2025-earnings) |
| USA | Verizon | Consumer postpaid phone churn, monthly | Q4 2024; Q4 2025 | 0.89 % [P]; 0.95 % [2H] | mixed | [Verizon 8-K Q4 2024](https://www.sec.gov/Archives/edgar/data/732712/000073271225000003/a2024q4exhibit992.htm); [Morningstar](https://www.morningstar.ca/ca/news/263878/verizon-earnings-price-increases-drive-solid-financial-results-amid-soft-customer-metrics.aspx) |
| Canada | BCE (Bell) | Mobile phone postpaid churn, monthly | FY2024 / FY2025 | 1.33 / 1.22 % | [P] | [BCE Q4 2025 release, 5 Feb 2026](https://www.bce.ca/cs-assets/2025-q4-news-release.pdf-blt1dfab326361bdeb1) |
| Australia | Telstra | Postpaid handheld churn, **annual** | FY25 | 13.3 % | [P] | [Telstra FY25 results transcript, 14 Aug 2025](https://www.telstra.com.au/content/dam/tcom/about-us/investors/pdf-i/telstra-full-year-results-FY25-presentation-transcript.pdf) |
| India | Bharti Airtel | Mobile churn, monthly (mostly prepaid) | Sep 2024 → Mar 2026 | 3.2 % → 2.4 % | [P], read from table rows; verify | [Airtel Q4 FY26 IR pack](https://assets.airtel.in/static-assets/cms/investor/docs/quarterly_results/2025-26/Q4/Quarterly-IR-Pack-Bharti-Airtel-Consolidated.pdf) |

- **Mature contract markets cluster at about 0.7–1.2 % a month;** prepaid-heavy India runs at about 2.5–3 %.
- **Definitions differ:** monthly or annualised, postpaid phones or all contracts, one brand or all brands. Deutsche Telekom states that its churn rate "is determined and reported based on the local markets of the respective countries" [P] ([DT Interim Report H1 2025](https://report.telekom.com/interim-report-q2-2025/management-report/development-of-business-in-the-operating-segments/europe.html)). A cross-country model needs one harmonised definition.
- **Monthly and annual rates convert** with annual = 1 − (1 − m)¹²: 1.0 % a month is about 11.4 % a year. The two O2 rows differ in scope (all brands vs the O2 brand), so they are not one rate in two units.

### 4.2 Switching and number portability

- **Austria, RTR Telekom Monitor, annual report 2024** [P]: Q2 2024 was an outlier ("Ausreißer") caused by large business customers porting whole blocks of numbers. Churn data contain business outliers. [RTR (PDF)](https://www.rtr.at/TKP/aktuelles/publikationen/publikationen/m/tm/RTR_Telekom_Monitor_Jahresbericht-2024.pdf)
- **UK, Ofcom Pricing and Consumer Engagement 2025** [P/2H]: out-of-contract bundle customers pay about £78 a month against £69 in contract. Customers who stay are not necessarily satisfied; some are inert. [Ofcom (PDF)](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/multi-sector/pricing/2025/pricing-and-consumer-engagement-report.pdf?v=413104)

### 4.3 Streaming and other subscriptions

- **Antenna, US premium streaming, 2025 year in review (Q1 2026)** [P]: weighted average monthly churn 4.6 % in December 2025 against 4.8 % a year earlier; "4 in 10 churned subscribers return to the service within 12 months". Churn is not an absorbing state. [Antenna](https://www.antenna.live/insights/antenna-q126-state-of-subscriptions-report-premium-svod-2025-year-in-review)
- **Antenna, "serial churners", 2024 data** [2H]: people who cancelled three or more services in two years are 23 % of US subscribers but 42 % of cancellations. [Señal News, 6 Jan 2025](https://senalnews.com/en/data/usa-premium-svod-added-35-million-new-subscribers-quarterly-in-2024)
- **Kantar, Spain, 26 Apr 2023** [P]: after Netflix launched paid sharing, it had over 1 million fewer users in Q1 2023 and its churn rate tripled quarter on quarter. Same firm, same policy, different response by country. [Kantar](https://kantar.com/inspiration/fmcg/netflix-crackdown-on-password-sharing-results-in-over-1-million-fewer-subscribers-in-spain)
- **Deloitte, *Digital Media Trends* 2025 (US survey, Oct 2024)** [P]: 39 % had cancelled at least one paid streaming service in six months; later Deloitte pieces give other figures, so the sources conflict. A six-month survey incidence is not a monthly churn rate. [Deloitte](https://www.deloitte.com/us/en/insights/industry/technology/digital-media-trends-consumption-habits-survey/2025.html)
- **Recurly, 2022 customer data** [P, dated]: average subscription churn 5.6 %, of which 4.0 % voluntary and 1.4 % involuntary (failed payments). Involuntary churn has its own predictors. [Recurly](https://recurly.com/blog/churn-rate-guide/)
- **Basic-Fit, Annual Report 2025**: average membership length 24 months in 2025 against 23 in 2024 [P for 24/23 months]; seven countries including Austria and Germany [2H for the country list]. [Basic-Fit (PDF)](https://corporate.basic-fit.com/docs/Annual%20Report%202025%20Basic-Fit%20N.V..pdf?a=6s8OLgbFvb17FZcYXu2K4c)

### 4.4 Price rises and churn

- **Netflix, Q1 2023 shareholder letter, 18 Apr 2023** [P]: on paid sharing in Canada, New Zealand, Spain and Portugal, "we see a cancel reaction in each market when we announce the news"; in Canada paid memberships later rose above the pre-launch level. [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1065280/000106528023000119/ex991_q123.htm)
- **Spotify, Q3 2025 earnings call** [2H]: "steady retention rates" after price rises in more than 150 markets ([Music Business Worldwide](https://www.musicbusinessworldwide.com/spotify-leadership-talk-price-hikes-the-companys-ubiquity-strategy-and-more-on-q3-earnings-call/)); the CFO's Q4 outlook reflected "the expected small amount of churn we see when we raise prices" ([Music Week](https://www.musicweek.com/digital/read/as-streaming-prices-increase-again-uk-faces-up-to-mature-market-leaving-behind-double-digit-growth/092860)).
- **Virgin Media O2, Q4 2025 release** [P]: a net loss of 164,800 mobile contracts, "primarily due to October price rise announcement elevating churn in the now closed 30-day exit window". [VMO2 (PDF)](https://news.virginmediao2.co.uk/wp-content/uploads/2026/02/Virgin-Media-O2-Q4-2025-Earnings-Release.pdf)
- **Swisscom, Q2 2026 slides** [2H]: the 1 April 2026 price rise "led to higher churn and increased migration to the lower-priced Wingo brand". Define the outcome at brand or group level. [Investing.com](https://www.investing.com/news/company-news/swisscom-q2-2026-slides-cash-flow-surges-24-on-integration-gains-93CH-4840324)
- **Disney+ and Hulu, September 2025 (Antenna)** [2H]: churn roughly doubled in a month with both a programme suspension and a price-rise announcement; Antenna called the attribution "unclear". Without a design you cannot attribute the spike to price. [StreamTV Insider](https://www.streamtvinsider.com/content/did-kimmel-kerfuffle-cause-disney-hulu-churn-double-its-complicated)

### 4.5 Retention economics, read critically

- **Reichheld & Sasser (1990), "Zero Defections", *Harvard Business Review*, Sep–Oct 1990** [P, via Bain reprint]: "Reducing defections 5 % boosts profits 25 % to 85 %". Caveats [2H]: the "5 %" is five percentage points of defection, the examples assume the improvement costs nothing, and Carroll & Reichheld (1992) later disputed the calculations. [Bain](https://www.bain.com/insights/zero-defections-quality-comes-to-services-harvard-business-review-hbr/)
- **Gallo (2014), HBR.org, 29 Oct 2014** [2H; hbr.org not accessible, quoted on a Salesforce blog]: acquiring a customer is "anywhere from five to 25 times more expensive" than retaining one.
- **McKinsey (Jain & Surana, Dec 2017)** [P, consultancy client claims]: analytics-driven base management can cut churn by "up to 15 %"; one operator with more than 50 offers cut churn by 10–15 % over 18 months. [McKinsey](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/reducing-churn-in-telecom-through-advanced-analytics)
- **Stochastic Solutions (Radcliffe & Simpson), practitioner white paper** [2H]: of two telecom retention campaigns, one was profitable and the other made a net loss because contacting "sleeping dogs" triggered churn. [Stochastic Solutions (PDF)](https://stochasticsolutions.com/pdf/SavedAndDrivenAway.pdf)
- **Booking.com (Bernardi, Mavridis & Estevez, KDD 2019)** [2H, summary]: "model performance is not the same as business performance" [The Morning Paper, 7 Oct 2019](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)

### 4.6 Europe's rules for churn and retention

- **European Electronic Communications Code, Directive (EU) 2018/1972** [L]: Art. 105 caps consumer commitment periods at 24 months, allows termination with at most one month's notice after automatic prolongation, and gives a right to withdraw when the provider changes the contract, unless the change is purely administrative or exclusively benefits the end user. Art. 106 requires a ported number to be activated within one working day of the agreed date. [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2018/1972/oj)
- **Germany, § 309 Nr. 9 BGB** (since 1 March 2022), as reported by Fieldfisher: new consumer contracts can no longer be tacitly extended for another fixed term; afterwards they run indefinitely with at most one month's notice. **§ 312k BGB** (since 1 July 2022), as reported by Stiftung Warentest: online B2C continuing contracts must offer a clearly labelled cancellation button. [Fieldfisher](https://www.fieldfisher.com/de-de/insights/gesetz-fur-faire-verbrauchervertrage); [test.de](https://www.test.de/Gesetz-fuer-faire-Verbrauchervertraege-Langlaufende-Vertraege-werden-fairer-5600636-0/)
- **BGH, judgment of 16 July 2026, I ZR 200/25 (vzbv v. FitX)**, as reported by vzbv and LTO (full judgment not read): the confirmation page after the cancellation button may contain only what § 312k requires, so a prominent offer to pause the gym contract instead of cancelling was unlawful. Retention therefore has to be proactive. [vzbv](https://www.vzbv.de/urteile/kuendigen-ohne-tricks); [LTO](https://www.lto.de/recht/nachrichten/n/bgh-izr20025-online-kuendigung-fitnessstudio-vertrag-kein-hinweis-auf-pausieren)
- **GDPR** [L]: Art. 21(2)–(3) gives an absolute right to object to profiling for direct marketing; Art. 22 restricts decisions based solely on automated processing with legal or similarly significant effects. Two CJEU rulings, as reported in legal summaries: in *SCHUFA* (C-634/21, 7 Dec 2023; [A&O Shearman](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gdpr)), generating a score can itself be an automated decision where a third party's decision "depends decisively" on it; in *Dun & Bradstreet Austria* (C-203/22, 27 Feb 2025), a customer refused a mobile contract on the basis of a credit score is entitled to an intelligible explanation of the procedure and principles applied, and handing over the algorithm is not enough.
- **EU AI Act, Regulation (EU) 2024/1689** [L]: Annex III lists credit scoring (point 5(b)) and life and health insurance pricing (point 5(c)) as high-risk; a typical marketing churn model is not listed (our reading, not a legal opinion). The Digital Omnibus postpones stand-alone Annex III obligations to 2 Dec 2027, as reported by [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); check publication in the Official Journal.
- **UK and US, for contrast**: FCA PS21/5 (in force January 2022) bars home and motor insurers from charging renewing customers more than equivalent new customers [P/2H] ([FCA EP25/2](https://www.fca.org.uk/publications/corporate-documents/evaluation-paper-25-2-general-insurance-pricing-practices-remedies)), and since 17 Jan 2025 Ofcom bans inflation-linked price-rise terms in new mobile and broadband contracts, as reported by [Telecoms.com](https://telecoms.com/operator-ecosystem/ofcom-bans-telcos-from-enacting-inflation-linked-mid-contract-price-rises) [2H]. In the US, the FTC's "click-to-cancel" rule was vacated in full by the Eighth Circuit on 8 July 2025 (*Custom Communications v. FTC*), as reported by [Latham & Watkins](https://www.lw.com/en/insights/eighth-circuit-vacates-ftc-click-to-cancel-rule).

Teaching summary, not legal advice; check the primary texts.

**Gaps.** The research could not retrieve Vodafone's per-market churn, per-country regulator tables (Eurobarometer, EC Scoreboard, BEREC, BNetzA, RTR portings), Ofcom's mobile switching share, Kantar streaming churn for Germany, France and Spain, or firms' engineering blogs on churn models.

## 5. Datasets for exercises and theses

### 5.1 Comparison

| Dataset | Rows × columns | Churn definition and base rate | Countries | Licence → may it be shared? | Real or synthetic | Best use |
|---|---|---|---|---|---|---|
| `telco_churn.csv` (course) | 11,000 × 11 | `churn` = cancelled within the next 12 months; DE 15.4 %, AT 14.6 %, ES 34.7 %, PL 28.5 % | DE, AT, ES, PL | Course material in this repository | **Simulated** (`data/generate_churn_data.py`, seed 33) | Learning the mechanics |
| IBM Telco Customer Churn | 7,043 × 21 | `Churn` = left within the last month; 26.5 % | none (US, fictional) | IBM GitHub repo is Apache-2.0; IBM never confirmed a data-specific licence → probably OK with attribution | Fictional IBM sample | Learning the mechanics |
| Bank "Churn_Modelling" | 10,000 × 14 | `Exited` = closed the account; 20.4 % | France, Germany, Spain | Not stated (Kaggle copies; origin SuperDataScience course) → unclear, assume no; **not in the course repository** | Synthetic | A country effect |
| UCI Online Retail II | full data: 1,067,371 transactions × 8 | Derived; with the recipe below on the 2009–10 sheet, 31.6 % of 2,975 customers | full data: 43 countries; 2009–10 sheet: 40 countries, UK 93 % of customers | CC BY 4.0 → yes, with attribution | Real | Defining churn yourself |
| Hotel Booking Demand | 119,390 × 32 | `is_canceled` (cancellation, not churn); 37.0 % | 177 countries of origin (488 bookings without a country) | Article and data CC BY 4.0 (*Data in Brief*) → yes (confirm on the Elsevier page) | Real | Many countries |
| UCI Iranian Churn | 3,150 × 14 | `Churn` over a 12-month window; about 15.7 % | Iran only | UCI's standard CC BY 4.0 (not verified live) → yes, with attribution | Real | In-class alternative |
| Flash Eurobarometer 243 (GESIS ZA4980); also EB 81.1 (ZA5878) | about 25,000 respondents (EB 243) | Self-reported switching of provider (bank, mobile, electricity and others) | 27 EU countries | GESIS data-use terms (free registration, research and teaching, no redistribution); **not in the course repository** | Real survey | Many countries; theses |
| Orange/MLC++ telecom churn | 3,333 × 21 | `Churn?`; 14.5 % | 51 US states | Not stated; `modeldata` package is MIT, but the data is from MLC++/SGI → unclear; **not in the course repository** | Artificial | Toy example only |
| Cell2Cell (Duke/Teradata tournament) | about 71,000 × about 78 (original) | `churndep`; oversampled to about 50 % (true rate about 2 % a month) | none (US) | None stated; academic-only distribution → no; **not in the course repository** | Real, anonymised | Reading Neslin et al. (2006) |
| Olist Brazilian e-commerce | about 99,000 orders, 9 tables | Derived repeat purchase; about 97 % buy once, so the label is degenerate | 27 Brazilian states | CC BY-NC-SA 4.0 (not verified live) → yes (non-commercial, share-alike) | Real | Text-feature theses only |

Not recommended for this course: Orange KDD Cup 2009 (50,000 × 230 anonymised variables, churn about 7.3 %; competition terms, no open licence), KKBox WSDM Cup 2018 (Taiwanese music streaming, about 30 GB of logs; Kaggle competition rules) and Sparkify (Udacity, simulated event log; no licence stated).

**Files without a clear open licence (Churn_Modelling, Cell2Cell, KDD Cup 2009, KKBox, Sparkify, Orange/MLC++) are not provided or linked here, except Churn_Modelling (Kaggle). Never commit them; if you obtain them yourself, keep them out of public repositories, including your group repository.** The same applies to Eurobarometer files under the GESIS terms.

The snippets below were run with the course environment (`.venv/bin/python -I`, polars 1.44.2) on 27 October 2026: as printed for `telco_churn.csv`, IBM Telco and Hotel Booking (read from their URLs) and Churn_Modelling (on a downloaded copy); the Online Retail II recipe on a CSV copy of the 2009–10 sheet, its `read_excel` lines and the Eurobarometer line only on small mock files, because UCI and GESIS could not be reached.

### 5.2 Profiles and loading code

Paths assume you run the code from `sessions/01-foundations/` or from the folder of your download.

#### `telco_churn.csv` (course data, simulated)

The running example of the deck and of `logit_churn.qmd`: one mobile operator, 11,000 customers in Germany (4,000), Austria (1,500), Spain (3,000) and Poland (2,500). Columns: `customer_id`, `country`, `age`, `tenure_months`, `monthly` (1 = month-to-month contract, 0 = 24-month contract), `monthly_fee` (EUR), `price_increase` (a price rise in the last six months), `complaints` (complaint calls in the last six months), `satisfaction` (survey score 1 to 5), `retention_offer` (1 = randomly picked for the retention-offer pilot), `churn`. Its numbers are not facts about real markets.

```python
import polars as pl

telco = pl.read_csv("../../data/churn/telco_churn.csv")
telco.group_by("country", maintain_order=True).agg(n=pl.len(), churn=pl.col("churn").mean())
```

#### IBM Telco Customer Churn

- **What and link:** a fictional US telecom customer base from IBM's sample data (contract, services, charges, tenure, demographics): https://github.com/IBM/telco-customer-churn-on-icp4d. The course repository also keeps an older copy in `data/legacy/`.
- **Licence:** IBM GitHub repo is Apache-2.0; IBM never confirmed a data-specific licence. Attribute it as "IBM sample data".
- **Traps:** 11 blank `TotalCharges` (all tenure 0), so the column loads as text; `TotalCharges` ≈ tenure × `MonthlyCharges` (r = 0.9996); many "No internet service" levels repeat `InternetService`; no country variable.
- **Use for:** the mechanics: dummies, odds ratios, AMEs, the contract effect (churn 42.7 % month-to-month, 2.8 % two-year).

```python
import polars as pl

url = ("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
       "master/data/Telco-Customer-Churn.csv")
telco = (
    pl.read_csv(url, schema_overrides={"TotalCharges": pl.String})
    .with_columns(
        TotalCharges=pl.col("TotalCharges").str.strip_chars().cast(pl.Float64, strict=False),
        churn=(pl.col("Churn") == "Yes").cast(pl.Int8),
    )
)
telco.shape                        # (7043, 22); 11 nulls in TotalCharges
```

#### Bank customer churn ("Churn_Modelling")

- **What and link:** 10,000 bank customers in France (5,014), Germany (2,509) and Spain (2,477). Download from Kaggle with a free account, for example https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling; use the Kaggle page as the source, not a third-party mirror.
- **Licence:** not stated by the originator; unclear, assume no redistribution. Not in the course repository; keep your download out of public repositories.
- **Traps:** almost certainly simulated (uniform salary and tenure). `NumOfProducts` nearly separates the classes (82.7 % churn with three products, 100 % with four), so enter it as categories and expect separation warnings. 36 % of balances are exactly 0.
- **Use for:** a country effect: 32.4 % churn in Germany against about 16 % in France and Spain; with controls, Germany's odds ratio against France is about 2.1.

```python
import polars as pl

bank = pl.read_csv("Churn_Modelling.csv")        # saved from Kaggle
bank.group_by("Geography").agg(n=pl.len(), churn=pl.col("Exited").mean())
```

#### UCI Online Retail II (churn you define yourself)

- **What and link:** all transactions of a UK-based online retailer (giftware, many wholesale customers), 1 Dec 2009 to 9 Dec 2011, in two Excel sheets: https://archive.ics.uci.edu/dataset/502/online+retail+ii (xlsx, about 43.5 MB, zipped; no login). `ucimlrepo.fetch_ucirepo(id=502)` is an untested alternative.
- **Licence:** CC BY 4.0. Cite Chen, D. (2019). Online Retail II [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D
- **Traps:** about 20 % of rows have no `Customer ID`; cancellations are invoices starting with "C"; outside the UK, countries are thin cells; **the churn label depends entirely on your cut-off and window.**

Reading the xlsx needs an Excel engine: polars' default is `fastexcel` (`pip install fastexcel`); the course environment has `openpyxl`. The two sheets may share days in early December 2010, so check and drop the overlap before stacking them:

```python
import polars as pl

sheets = pl.read_excel("online_retail_II.xlsx", sheet_id=0, engine="openpyxl",   # 0 = all sheets
                       schema_overrides={"Invoice": pl.String, "StockCode": pl.String})
first, second = sheets.values()                          # 2009-10 sheet, 2010-11 sheet
last_day = first["InvoiceDate"].max()
print(second.filter(pl.col("InvoiceDate") <= last_day).height, "overlapping rows in sheet 2")
tx = pl.concat([first, second.filter(pl.col("InvoiceDate") > last_day)], how="vertical_relaxed")
```

Recipe for a churn label: customers with a purchase before the cut-off; churn = 1 if they buy nothing in the next 161 days.

```python
from datetime import date, timedelta

cutoff = date(2010, 7, 1)
end = cutoff + timedelta(days=161)                      # 2010-12-09

buys = (
    tx.filter(pl.col("Customer ID").is_not_null(),
              ~pl.col("Invoice").str.starts_with("C"),  # drop cancellations
              pl.col("Quantity") > 0)
      .with_columns(day=pl.col("InvoiceDate").dt.date(),
                    amount=pl.col("Quantity") * pl.col("Price"))
)
before = buys.filter(pl.col("day") < cutoff)
active = (buys.filter(pl.col("day").is_between(cutoff, end))
              .select("Customer ID").unique().with_columns(active=pl.lit(1)))

customers = (
    before.group_by("Customer ID")
    .agg(recency_days=(pl.lit(cutoff) - pl.col("day").max()).dt.total_days(),
         frequency=pl.col("Invoice").n_unique(),
         monetary=pl.col("amount").sum(),
         country=pl.col("Country").mode().first())
    .join(active, on="Customer ID", how="left")
    .with_columns(churn=pl.col("active").is_null().cast(pl.Int8))
    .drop("active")
)
customers["churn"].mean()                               # 0.316 for 2,975 customers (2009-10 sheet)
```

Another cut-off or window gives another base rate; report your definition.

#### Hotel Booking Demand ("booking churn")

- **What and link:** bookings at two Portuguese hotels (resort and city), arrivals July 2015 to August 2017, with the guest's country of origin: 177 countries of origin (488 bookings without a country). Article: Antonio, N., de Almeida, A., & Nunes, L. (2019). Hotel booking demand datasets. *Data in Brief, 22*, 41–49 (open access copy: https://repositorio.iscte-iul.pt/bitstream/10071/16929/1/Hotelbookingdemanddatasets.pdf).
- **Licence:** article and data CC BY 4.0 (confirm on the Elsevier page); cite Antonio, de Almeida & Nunes (2019).
- **Traps:** cancellation, not the end of a relationship; `reservation_status` and `reservation_status_date` leak the outcome; "NA" and "NULL" mean missing; the very high Portuguese cancellation rate (56.6 %) is probably partly an artefact of how origin is recorded.

```python
import polars as pl

url = ("https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
       "master/data/2020/2020-02-11/hotels.csv")
hotels = (
    pl.read_csv(url, null_values=["NA", "NULL"], infer_schema_length=20000)
    .drop("reservation_status", "reservation_status_date")   # leak the outcome
)
hotels.shape                       # (119390, 30)
```

#### Flash Eurobarometer 243: switching service providers (2008)

- **What and link:** an EU-27 survey with roughly 1,000 respondents per country on switching bank accounts, loans, insurance, mobile and fixed phone, electricity and gas, plus perceived ease of switching. GESIS ZA4980, https://doi.org/10.4232/1.4980 (catalogue: https://search.gesis.org/research_data/ZA4980?lang=en); free registration. EB 81.1 (2014, ZA5878, https://doi.org/10.4232/1.12832) asks about changing the telecom bundle provider.
- **Licence:** GESIS data-use terms: research and teaching, no redistribution. Nothing goes into the course repository or your group repository.
- **Traps:** self-reported switching, not observed churn; check the questionnaire wording and the weights.
- **Use for:** the only genuinely international, real switching data found.

```python
import pandas as pd
import polars as pl

eb = pl.from_pandas(pd.read_stata("ZA4980_vX-X-X.dta"))   # use the file name of your download
```

## 6. Thesis niches

Numbered as on deck slide 54 (niches 1–5), followed by the further niches. These are gaps in our search, not proof of absence; check the recent literature again before you commit.

1. **Multilevel churn logit.** *Question:* what share of churn variance sits at the country level, and do switching costs, regulation or uncertainty avoidance explain it? *Data:* a multinational firm with 15 or more markets; fallback Eurobarometer switching microdata linked to country indicators. *Anchors:* Simester et al. (2020); Ferreira et al. (2019); no direct precedent found.
2. **Model portability.** *Question:* how much discrimination, calibration and profit does a churn logit lose in a new country, and what do reweighting and recalibration recover? *Data:* Churn_Modelling (train on France, test on Germany and Spain), extended with partner data. *Anchors:* Simester et al. (2020); Janssens et al. (2024).
3. **Uplift across countries: are "persuadables" country-specific?** *Question:* does a retention offer's effect differ by country, and does a country-aware uplift logit earn more than a pooled one? *Data:* Churn_Modelling with a semi-synthetic randomised treatment; a real A/B test with a partner. *Anchors:* Lemmens & Gupta (2020); Devriendt et al. (2021).
4. **Pause, cancel or stay.** *Question:* does offering a subscription pause lower 12-month churn or only delay it, and does this differ between Germany/Austria and less regulated markets after BGH I ZR 200/25? *Data:* a vignette experiment in Germany, Austria and a non-EU market, or partner data from a DACH subscription firm. *Anchors:* Einav et al. (2025); Miller et al. (2023, working paper).
5. **Response styles and scale.** *Question:* can one cross-national churn logit handle response styles in the satisfaction score and country differences in scale together? *Data:* partner data that link survey satisfaction to observed churn in several countries. *Anchors:* Baumgartner & Steenkamp (2001); Williams (2009). This niche follows from Part 3 of the deck rather than from a search gap.
6. **Cancellation friction across jurisdictions.** *Question:* are online cancellation flows less obstructive where cancel-button rules exist? *Data:* replicate the Sheil et al. (2024) audit on 60–100 services in 4–6 countries. *Anchors:* Sheil et al. (2024); Luguri & Strahilevitz (2021).
7. **Fair and explainable retention targeting.** *Question:* do risk- or uplift-based offers under-serve groups by age, gender or nationality, and what does debiasing cost? *Data:* IBM Telco and Churn_Modelling; optionally a user study of explanation formats. *Anchors:* Ascarza & Israeli (2022); Kozodoi et al. (2022); De Bock et al. (2024).
8. **Do LLM text features travel across languages?** *Question:* do embeddings of reviews or complaints add the same value to a churn logit in different languages and markets? *Data:* Olist (Portuguese reviews; churn as no repurchase within *k* months) plus a second-language partner corpus. *Anchors:* De Caigny et al. (2020); Chajia & Nfaoui (2024); Vo et al. (2021).
9. **Prepaid and network churn in emerging markets.** *Question:* do top-up rhythms and contacts' churn predict inactivity earlier than monthly usage? *Data:* partner data from an operator or fintech in CEE, Africa or Asia; churn as no top-up for 30, 60 or 90 days. *Anchors:* Ferreira et al. (2019); Reme et al. (2022).
10. *Optional, B2B/SaaS.* *Question:* does a profit-weighted logit beat a standard logit for accounts whose values are very skewed across country subsidiaries? *Data:* partner data. *Anchors:* De Caigny et al. (2021); Janssens et al. (2024).

## 7. Where this guide is used

The deck draws on Section 4 for slides 5–6 (practice) and 47 (regulation), on Section 3 for slides 17–23 and 55 (research frontiers, Section 3.7), on Section 5 for slides 49–50 (datasets) and on Section 6 for slide 54 (niches); the code and the exercise are in [`logit_churn.qmd`](logit_churn.qmd).
