# 📊 B2B Market Sizing Model (Bottom-Up Approach)

## Overview
This project estimates the total addressable market (TAM) for a B2B product using a **bottom-up market sizing approach**. A synthetic dataset of 500 companies was generated, containing key variables such as region, industry, average units per employee, unit price, and annual usage. Revenue per company and total market size are calculated and visualized for business insights.

---

## Objective
- Simulate realistic company behavior and spending on a B2B product
- Calculate company-level revenue and aggregate to estimate global market size
- Identify top industries and regions by revenue contribution
- Present summary metrics and visual charts directly in the terminal

---

## Dataset
A synthetic dataset (`b2b_market.csv`) with ~500 companies was generated with the following features:

| Column                  | Description                                  |
|-------------------------|----------------------------------------------|
| Region                  | Geographic region of the company             |
| Industry                | Industry vertical (e.g., Tech, Healthcare)   |
| Avg_Units_Per_Employee  | Average units used per employee              |
| Unit_Price_USD          | Price per unit of product (in USD)           |
| Annual_Usage            | Yearly product usage factor (scalar)         |

---

## Technologies Used
- Python
- pandas
- matplotlib
- seaborn

---

## How to Run

```bash
pip install pandas matplotlib seaborn
python market_sizing_model.py
```

Make sure the `b2b_market.csv` file is in the same directory as the script.

---

## Workflow

1. **Load Synthetic Data**  
2. **Estimate Spend per Company**  
3. **Calculate Total Revenue and Market Size**  
4. **Segment Revenue by Industry and Region**  
5. **Inline Visualizations using matplotlib/seaborn**  
6. **Print Key Insights in Terminal**

---

## Visual Outputs

- Revenue distribution by region (bar chart)
- Revenue contribution by industry (bar chart)
- Histogram of estimated spend per company

---

## Results (example)

- **Estimated Global Market Size**: `$1.24B+` per year  
- **Top Region**: North America  
- **Top Industry**: Tech  

---

## Key Takeaways

- Bottom-up analysis allows granular modeling of spend behavior.
- Synthetic datasets can effectively simulate real-world TAM scenarios.
- Industries with higher usage per employee and unit prices dominate revenue share.

---

## Future Enhancements

- Add CAGR and forecast future market size (3–5 years)
- Integrate real-world company or industry benchmarks
- Export charts and summary to PDF report or Streamlit dashboard
