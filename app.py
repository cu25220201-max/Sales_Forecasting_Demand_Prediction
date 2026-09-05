import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Forecasting Dashboard", page_icon="📈", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/sales_data_cleaned.csv", parse_dates=["Order_Date"])

df = load_data()
st.title("📈 Sales Forecasting & Demand Prediction")
st.caption("Final Project • Retail Analytics • Mentor: Tarun Kumar")

st.sidebar.header("Filters")
min_date, max_date = df["Order_Date"].min().date(), df["Order_Date"].max().date()
dates = st.sidebar.date_input("Date range", (min_date, max_date), min_value=min_date, max_value=max_date)
if isinstance(dates, tuple) and len(dates) == 2:
    start_date, end_date = dates
else:
    start_date, end_date = min_date, max_date

categories = st.sidebar.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
regions = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
channels = st.sidebar.multiselect("Sales Channel", sorted(df["Sales_Channel"].unique()), default=sorted(df["Sales_Channel"].unique()))

f = df[
    (df["Order_Date"].dt.date >= start_date) &
    (df["Order_Date"].dt.date <= end_date) &
    df["Category"].isin(categories) &
    df["Region"].isin(regions) &
    df["Sales_Channel"].isin(channels)
].copy()

if f.empty:
    st.warning("No records match the selected filters.")
    st.stop()

total_sales = f["Sales"].sum()
units = f["Quantity"].sum()
orders = f["Order_ID"].nunique()
aov = f.groupby("Order_ID")["Sales"].sum().mean()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Sales", f"₹{total_sales:,.0f}")
c2.metric("Units Sold", f"{units:,.0f}")
c3.metric("Orders", f"{orders:,.0f}")
c4.metric("Avg. Order Value", f"₹{aov:,.0f}")

monthly = f.groupby(f["Order_Date"].dt.to_period("M")).agg(Sales=("Sales","sum")).reset_index()
monthly["Month"] = monthly["Order_Date"].dt.to_timestamp()

st.subheader("Monthly Sales Trend")
fig = px.line(monthly, x="Month", y="Sales", markers=True, title="Historical Monthly Sales")
fig.update_layout(xaxis_title="", yaxis_title="Sales (₹)", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    prod = f.groupby("Product", as_index=False).agg(Sales=("Sales","sum")).sort_values("Sales", ascending=False)
    st.subheader("Sales by Product")
    figp = px.bar(prod, x="Sales", y="Product", orientation="h")
    figp.update_layout(yaxis={"categoryorder":"total ascending"}, xaxis_title="Sales (₹)", yaxis_title="")
    st.plotly_chart(figp, use_container_width=True)

with right:
    cat = f.groupby("Category", as_index=False).agg(Sales=("Sales","sum")).sort_values("Sales", ascending=False)
    st.subheader("Sales by Category")
    figc = px.pie(cat, names="Category", values="Sales", hole=.45)
    st.plotly_chart(figc, use_container_width=True)

season = f.groupby(f["Order_Date"].dt.month).agg(Sales=("Sales","sum")).reset_index()
season["Month"] = pd.to_datetime(season["Order_Date"], format="%m").dt.strftime("%B")
season = season.sort_values("Order_Date")
st.subheader("Seasonal Demand Pattern")
figs = px.bar(season, x="Month", y="Sales", title="Sales by Calendar Month")
st.plotly_chart(figs, use_container_width=True)

st.subheader("6-Month Sales Forecast")
if len(monthly) >= 6:
    x = np.arange(len(monthly))
    y = monthly["Sales"].values
    coef = np.polyfit(x, y, 1)
    future_x = np.arange(len(monthly), len(monthly)+6)
    future_sales = np.maximum(np.polyval(coef, future_x), 0)
    future_dates = pd.date_range(monthly["Month"].max() + pd.offsets.MonthBegin(1), periods=6, freq="MS")
    fc = pd.DataFrame({"Month": future_dates, "Forecast Sales": future_sales})
    hist = monthly[["Month","Sales"]].rename(columns={"Sales":"Historical Sales"})
    combined = hist.merge(fc, on="Month", how="outer")
    figf = px.line(combined, x="Month", y=["Historical Sales","Forecast Sales"], markers=True)
    figf.update_layout(xaxis_title="", yaxis_title="Sales (₹)", hovermode="x unified")
    st.plotly_chart(figf, use_container_width=True)
    st.info("Forecast method: linear trend on monthly historical sales. This is a basic academic forecast.")
else:
    st.info("Select a longer date range to generate a forecast.")

peak = monthly.loc[monthly["Sales"].idxmax()]
top_product = prod.iloc[0]["Product"]
top_category = cat.iloc[0]["Category"]

st.subheader("Business Insights & Recommendations")
st.markdown(f"""
- **Peak sales month:** {peak['Month'].strftime('%B %Y')} — **₹{peak['Sales']:,.0f}**
- **Top product:** **{top_product}** — prioritize replenishment and weekly monitoring.
- **Top category:** **{top_category}** — focus inventory and promotional planning here.
- Build pre-season inventory plans using historical monthly seasonality.
- Set reorder points using demand, supplier lead time and safety stock.
- Compare actual vs forecast every month and improve the model as more data becomes available.
""")

st.subheader("Data Preview")
st.dataframe(f.sort_values("Order_Date", ascending=False).head(100), use_container_width=True)