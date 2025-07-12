import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("b2b_market.csv")
pd.set_option('display.float_format', '{:,.2f}'.format)

# Preview data
print("🔍 Sample data:")
print(df.head())

# -----------------------------
# 2. Compute Spend per Company
# -----------------------------
df['Estimated_Spend_Per_Company'] = (
    df['Avg_Units_Per_Employee'] * df['Unit_Price_USD'] * df['Annual_Usage']
)

# -------------------------------
# 3. Compute Revenue Per Company
# -------------------------------
df['Total Revenue ($)'] = df['Avg_Units_Per_Employee'] * df['Unit_Price_USD'] * df['Annual_Usage']

# -----------------------------
# 3. Total Market Size Estimate
# -----------------------------
estimated_market_size = df['Estimated_Spend_Per_Company'].sum()
print(f"\n💰 Estimated B2B Market Size (Bottom-Up): ${estimated_market_size:,.2f}")

# -----------------------------
# 4. Segment Analysis
# -----------------------------
segment_analysis = df.groupby('Industry')['Estimated_Spend_Per_Company'].sum().sort_values(ascending=False)
print("\n📊 Spend by Industry Segment:")
print(segment_analysis)

# -------------------------------
# 5. Summary Stats & Printouts
# -------------------------------
total_market = df['Total Revenue ($)'].sum()
top_region = df.groupby("Region")['Total Revenue ($)'].sum().idxmax()
top_industry = df.groupby("Industry")['Total Revenue ($)'].sum().idxmax()

print("📊 B2B Market Sizing Model (Bottom-Up Approach)")
print("--------------------------------------------------")
print(df[["Region", "Industry", "Total Revenue ($)"]].head(10))
print("--------------------------------------------------")
print(f"✅ Estimated Total Market Size: ${total_market:,.0f} per year")
print(f"🏆 Top Revenue Region: {top_region}")
print(f"🏆 Top Revenue Industry: {top_industry}")

# -----------------------------
# 6. Visualization
# -----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['Estimated_Spend_Per_Company'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Estimated Spend Per Company")
plt.xlabel("Spend in USD")
plt.ylabel("Number of Companies")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df.groupby("Region")["Total Revenue ($)"].sum().plot(
    kind='bar',
    title="Revenue by Region",
    ylabel="USD",
    xlabel="Region"
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df.groupby("Industry")["Total Revenue ($)"].sum().plot(
    kind='bar',
    title="Revenue by Industry",
    ylabel="USD",
    xlabel="Industry",
    color='orange'
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()