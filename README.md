# Sales Overview Dashboard

An interactive Power BI portfolio project for exploring sales performance across years and regions, including current-year and previous-year comparisons.

## Dashboard preview

![Sales dashboard preview 1](Slide1.jpg)

<details>
<summary>More dashboard views</summary>

![Sales dashboard preview 2](Slide2.jpg)

![Sales dashboard preview 3](Slide3.jpg)

</details>

## What the report explores

- **Year comparisons:** Compare current-year (CY) and previous-year (PY) metrics.
- **Interactive selections:** Explore performance using year and region slicers.
- **Regional performance:** Compare average sales values for the selected region.
- **Missing prior-year data:** The documented report behavior displays “No Data” when no previous-year data is available.

The original project notes describe the CY and PY regional metrics as averages of sales values. Interpret these as averages rather than total revenue unless the measure definition in the report says otherwise.

## Open the project

1. Download this repository using **Code → Download ZIP**, then extract it.
2. Open [salesoverview.pbix](salesoverview.pbix) in Power BI Desktop.
3. Use the year and region slicers to explore the report.
4. To refresh the data, keep [Sales Overview Data.xlsx](Sales%20Overview%20Data.xlsx) locally available. If Power BI reports a missing source, update the workbook path in its data source settings.

You can browse the images above without installing Power BI.

## Repository contents

| File | Purpose |
| --- | --- |
| [salesoverview.pbix](salesoverview.pbix) | Interactive Power BI report |
| [Sales Overview Data.xlsx](Sales%20Overview%20Data.xlsx) | Included sales workbook |
| Slide1.jpg, Slide2.jpg, Slide3.jpg | Report preview images |

## Tools and skills

Power BI · Excel · Data visualization · Year-over-year analysis · Interactive filtering

## Reproducibility notes

The repository includes the report and workbook. Dataset provenance, refresh requirements, cleaning steps, and DAX measure definitions should be documented before treating the analysis as fully reproducible.

## Contributing

For a bug report, include the selected year and region, the affected visual, and expected versus observed behavior. For report changes, explain the measure or visual affected and include a screenshot.

## License status

The previous README stated MIT licensing, but this repository does not currently include a LICENSE file. A standalone license and clarification of the workbook's usage rights would make reuse terms explicit.

## Related work

- [Heart Disease Data Analysis](https://github.com/Kelv-Ojo/Heart-disease)
- [E-Commerce Chatbot](https://github.com/Kelv-Ojo/Chat_bot)
