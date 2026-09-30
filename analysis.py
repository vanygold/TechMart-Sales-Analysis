import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD DATA
# ==========================================

data = pd.read_csv("sales_data.csv")


# ==========================================
# 2. DATA CLEANING
# ==========================================

data["Date"] = pd.to_datetime(data["Date"])


# ==========================================
# 3. CALCULATE REVENUE
# ==========================================

data["Revenue"] = data["Quantity"] * data["Price"]


# ==========================================
# 4. OVERALL BUSINESS PERFORMANCE
# ==========================================

total_revenue = data["Revenue"].sum()
total_quantity = data["Quantity"].sum()

average_revenue_per_unit = total_revenue / total_quantity

print("Total revenue: ₦", total_revenue)
print("Total units sold:", total_quantity)
print("Average revenue per unit: ₦", round(average_revenue_per_unit))


# ==========================================
# 5. PRODUCT ANALYSIS
# ==========================================

product_revenue = data.groupby("Product")["Revenue"].sum()
product_quantity = data.groupby("Product")["Quantity"].sum()

print("\nRevenue by product:")
print(product_revenue.sort_values(ascending=False))

print("\nUnits sold by product:")
print(product_quantity.sort_values(ascending=False))


# ==========================================
# 6. CATEGORY ANALYSIS
# ==========================================

category_revenue = data.groupby("Category")["Revenue"].sum()

print("\nRevenue by category:")
print(category_revenue.sort_values(ascending=False))


# ==========================================
# 7. REGIONAL ANALYSIS
# ==========================================

region_revenue = data.groupby("Region")["Revenue"].sum()
average_region_revenue = data.groupby("Region")["Revenue"].mean()

print("\nRevenue by region:")
print(region_revenue.sort_values(ascending=False))

print("\nAverage revenue per sale by region:")
print(average_region_revenue.sort_values(ascending=False))


# ==========================================
# 8. MONTHLY ANALYSIS
# ==========================================

data["Month"] = data["Date"].dt.month

monthly_revenue = data.groupby("Month")["Revenue"].sum()

print("\nMonthly revenue:")
print(monthly_revenue)


# ==========================================
# 9. VISUALIZATIONS
# ==========================================

# Revenue by product
# Revenue by product
ax = product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₦)")
plt.xticks(rotation=45)

for bar in ax.patches:
    ax.annotate(
        f"₦{bar.get_height():,.0f}",
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.tight_layout()
plt.savefig("visualizations/revenue_by_product.png")
plt.close()

# Revenue by region
ax = region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₦)")
plt.xticks(rotation=45)

for bar in ax.patches:
    ax.annotate(
        f"₦{bar.get_height():,.0f}",
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.tight_layout()
plt.savefig("visualizations/revenue_by_region.png")
plt.close()


# Monthly revenue
ax = monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₦)")
plt.xticks([1, 2, 3], ["January", "February", "March"])

for x, y in zip(monthly_revenue.index, monthly_revenue.values):
    ax.annotate(
        f"₦{y:,.0f}",
        (x, y),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=8
    )

plt.tight_layout()
plt.savefig("visualizations/monthly_revenue.png")
plt.close()
# ==========================================
# 10. BUSINESS INSIGHTS
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

print("1. Smartphones generated the highest revenue at ₦4,200,000.")

print("2. Lagos generated the highest total revenue at ₦5,235,000.")

print("3. The Phones category generated the highest category revenue at ₦5,460,000.")

print("4. March recorded the highest monthly revenue at ₦4,905,000.")

print("5. Mouse had the highest number of units sold with 23 units.")

print("6. Abuja had the highest average revenue per sale at ₦585,000.")

# ==========================================
# 11. PROJECT CONCLUSION
# ==========================================

print("\n========== PROJECT CONCLUSION ==========")

print(
    "TechMart generated ₦11,490,000 in revenue from 95 units sold "
    "across 23 sales records."
)

print(
    "Smartphones were the highest-revenue product, while Mouse had "
    "the highest number of units sold."
)

print(
    "Lagos generated the highest total revenue, and March was the "
    "strongest month during the period analyzed."
)

print(
    "The analysis shows that product performance, regional performance, "
    "and monthly trends can help the business understand its sales "
    "performance and make better decisions."
)

