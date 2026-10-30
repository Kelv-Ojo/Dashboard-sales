# Original Power BI file — Desktop verification

Reviewed locally on 29 October 2026. The original `salesoverview.pbix` opened in Power BI Desktop. It was not published, refreshed from external sources or saved over the original.

## Confirmed

- A DAX aggregate query against the imported model returned **10,018 rows**, **5,026 distinct orders**, **2,298,896.62** total Sales and **733,948.35** Sales filtered to 2024. These agree with the independently checked workbook at displayed precision.
- `Total Sales = SUM('Sales Data'[Sales])`; `Total Profit = SUM('Sales Data'[Profit])` were read in the native formula bar.
- CY Sales uses the selected calendar year; PY Sales uses selected year minus one. YoY Sales divides the difference between CY/PY Sales by PY Sales and formats it with arrows and a rounded percentage. Its total is evaluated from totals, not an arithmetic mean of regional percentages.
- The 2024 sales cards show Central 147.10K, East 213.82K, South 122.91K and West 250.13K. The total is 733.95K, PY 609.86K and rounded YoY 20%.
- Year selections 2021 and 2024 were tested. For 2021, PY cards show “No Data”. Sales/Profit/Quantity selections update the main cards and charts.
- The layout contains a metric slicer, a year slicer, region-filtered cards/charts, a state/region bar chart and a matrix. No separate region slicer was observed. Page/report filter wells were empty in the inspected view; that does not mean the visuals have no filters.

## Issues and unverified areas

1. PY comparison cards continue to display **PY Sales** and sales values when Profit or Quantity is selected. This is not a correct same-metric comparison and needs repair before presenting the dashboard as fully working.
2. The explanatory textbox says total YoY is an average of regional values. The inspected DAX contradicts that wording; the textbox needs correction.
3. Map/filled-map visuals are disabled by the current application security setting. No security setting was changed, and no working-map claim is made.
4. Currency formatting uses `$`, but the workbook's upstream source/currency and redistribution rights remain unconfirmed. Customer identifiers/names and geographic fields are present. Do not describe these as verified real customer data or redistribute on an assumed sample-data licence.
5. Every remaining measure, interaction, multi-selection and source refresh was not exhaustively checked. No “all measures verified” claim is made.

The README's existing annual PNG remains a genuine Python chart, not a native dashboard screenshot. The Desktop check images are review evidence, not polished publication assets. `Slide1/2/3` remain layout images rather than populated screenshots. Keep this repository on hold for a complete dashboard release; its source-workbook arithmetic is verified separately.
