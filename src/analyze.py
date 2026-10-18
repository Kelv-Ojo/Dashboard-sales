"""Rebuild descriptive summaries from the exact workbook already in this repo."""
from pathlib import Path
import hashlib,json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'Sales Overview Data.xlsx'
    raw=path.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='c87b3d470ecea8b7a930dc6734d492b81cde0d5e','Source snapshot changed; review before updating expectations'
    df=pd.read_excel(path,sheet_name='Sales Data')
    assert df['Row ID'].is_unique
    assert df[['Sales','Profit','Quantity','Order ID','Order Date','Region']].notna().all().all()
    assert df.Quantity.gt(0).all()
    df['Year']=pd.to_datetime(df['Order Date']).dt.year
    yearly=df.groupby('Year').agg(sales=('Sales','sum'),profit=('Profit','sum'),order_lines=('Row ID','size'),orders=('Order ID','nunique'))
    yearly['profit_margin']=yearly.profit/yearly.sales
    yearly['sales_yoy_pct']=yearly.sales.pct_change()*100
    regions=df.groupby('Region').agg(sales=('Sales','sum'),profit=('Profit','sum'),lines=('Row ID','size'))
    regions['profit_margin']=regions.profit/regions.sales
    assert abs(yearly.sales.sum()-df.Sales.sum())<1e-6
    assert abs(regions.sales.sum()-df.Sales.sum())<1e-6
    out=ROOT/'reports';out.mkdir(exist_ok=True)
    yearly.to_csv(out/'annual_sales.csv');regions.to_csv(out/'region_sales.csv')
    fig,ax=plt.subplots(figsize=(9,5))
    ax.bar(yearly.index.astype(str),yearly.sales/1000,color='#326D9C')
    ax.set(title='Annual total Sales | source workbook',xlabel='Order year',ylabel='Sales (thousands of source currency units)')
    ax.spines[['top','right']].set_visible(False)
    fig.tight_layout();fig.savefig(out/'annual_sales.png',dpi=160);plt.close(fig)
    metrics={'rows':len(df),'orders':int(df['Order ID'].nunique()),'start':str(df['Order Date'].min().date()),'end':str(df['Order Date'].max().date()),'sales_sum':float(df.Sales.sum()),'profit_sum':float(df.Profit.sum()),'mean_sales_per_line':float(df.Sales.mean()),'source_sha256':hashlib.sha256(raw).hexdigest()}
    (out/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
    top=regions.sales.idxmax();latest=yearly.iloc[-1];year=yearly.index[-1]
    (out/'findings.md').write_text(f'''# Sales workbook findings

- The workbook contains {len(df):,} order lines and {metrics['orders']:,} distinct order IDs, dated {metrics['start']} to {metrics['end']}.
- Total Sales is {metrics['sales_sum']:,.2f} source currency units, whereas mean Sales per order line is {metrics['mean_sales_per_line']:,.2f}. These are different metrics.
- {top} has the highest total Sales ({regions.loc[top,'sales']:,.2f} source currency units). This does not establish the highest profit margin.
- {year} total Sales is {latest.sales:,.2f}, changing {latest.sales_yoy_pct:.1f}% from the previous observed year. Check equivalent date coverage before using the change as a performance target.

## Definitions and limits

One workbook row is an order line, not necessarily a complete order. Order count uses distinct Order ID. Sales and Profit retain the source field definitions and unspecified currency; no currency is inferred. Margin is sum Profit / sum Sales, not average line margins. The original PBIX measures have not been refreshed or independently evaluated in Power BI Desktop. These summaries are a separately reproducible workbook analysis.

The workbook filename does not establish the original publisher or licence. It resembles a Superstore-style educational dataset, but that provenance has not been verified, so no upstream attribution or redistribution permission is invented. No new raw-data source is published; this analysis uses the workbook already present in the repository.
''')
    print(json.dumps(metrics,indent=2))

if __name__=='__main__':main()
