# Sales workbook findings

- The workbook contains 10,018 order lines and 5,026 distinct order IDs, dated 2021-01-03 to 2024-12-30.
- Total Sales is 2,298,896.62 source currency units, whereas mean Sales per order line is 229.48. These are different metrics.
- West has the highest total Sales (725,457.82 source currency units). This does not establish the highest profit margin.
- 2024 total Sales is 733,948.35, changing 20.3% from the previous observed year. Check equivalent date coverage before using the change as a performance target.

## Definitions and limits

One workbook row is an order line, not necessarily a complete order. Order count uses distinct Order ID. Sales and Profit retain the source field definitions and unspecified currency; no currency is inferred. Margin is sum Profit / sum Sales, not average line margins. The original PBIX measures have not been refreshed or independently evaluated in Power BI Desktop. These summaries are a separately reproducible workbook analysis.

The workbook filename does not establish the original publisher or licence. It resembles a Superstore-style educational dataset, but that provenance has not been verified, so no upstream attribution or redistribution permission is invented. No new raw-data source is published; this analysis uses the workbook already present in the repository.
