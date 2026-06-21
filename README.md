# Marketing Funnel & Conversion Performance Analysis
**Future Interns – Data Science & Analytics Task 3**

## Dataset
Bank Marketing Campaign Dataset (UCI Machine Learning Repository)
41,188 records | 20 features | Binary conversion target (yes/no)

## Tools Used
- Python 3.14 (PyCharm)
- pandas, matplotlib, seaborn

## Funnel Results

| Stage        | Count  | Rate   |
|--------------|--------|--------|
| Contacted    | 41,188 | 100%   |
| Engaged      | 33,553 | 81.5%  |
| Warm Leads   | 1,515  | 3.7%   |
| Converted    | 4,640  | 11.3%  |

## Key Insights
- Overall conversion rate is **11.3%**
- **96.3% of leads were cold** — the biggest drop-off point
- **Cellular contact** converts at 14.7% vs telephone at 5.2%
- **Best months:** March (50%), December (49%), September (45%)
- **Worst months:** May (6.4%), July (9%)

## Recommendations
1. **Prioritize cellular outreach** — it is 3x more effective than telephone
2. **Focus campaigns in Sep–Dec and March** — conversion peaks in these months
3. **Build a warm lead pipeline** — re-contacting previous leads dramatically improves conversion
4. **Reduce May campaigns** — lowest conversion month, poor ROI
5. **Limit contact attempts to 3 or fewer** — over-contacting reduces engagement

## Files
- `funnel_analysis.py` — full analysis script
- `funnel_chart.png` — marketing funnel visualization
- `contact_conversion.png` — conversion by contact method
- `monthly_conversion.png` — conversion by month