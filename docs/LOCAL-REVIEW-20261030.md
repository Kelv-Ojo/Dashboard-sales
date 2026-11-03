# Local Power BI review — 30 October 2026

Saved repaired copy: `salesoverview-reviewed-20261030.pbix` (710,204 bytes).
SHA-256: `83ebe265d25a09e617897f3370a9bf3bfee94608221d2ae19e7bdeb9518b30f4`.
Original `salesoverview.pbix` preserved. Nothing pushed or published.

## Repairs
- Prior-year KPI now selects PY Sales, PY Profit or PY Qty with the selected metric, including matching labels.
- Removed the empty/unavailable map area and enlarged the working state comparison.
- Corrected the YoY explanation: (current total - prior total) / prior total; total percentages are not averages of regional percentages.
- Sales, Profit and Quantity YoY display measures now return No Data for a blank/zero prior-year denominator and show one decimal place otherwise. Underlying CY/PY arithmetic is unchanged.

## Observed checks
Power BI Desktop: Sales/Profit/Quantity selectors and corresponding 2024 prior-year cards; 2021 has no prior-year data, with No Data across the YoY matrix. 2024 total YoY displays Sales 20.3%, Profit 14.2%, Qty 26.8%. Sales total 733,948.3492 agrees with the independent source-workbook annual calculation. A real report screenshot is used in the local portfolio with Sales and 2024 selected.

## Remaining release limits
Upstream publisher, currency and licence remain unverified. The dollar symbol is inherited formatting, not verified USD. No source refresh or exhaustive filter/measure certification is claimed. Existing original-file review notes still describe the original and must not be mistaken for this repaired copy. The GitHub original-file link does not contain these local repairs.
