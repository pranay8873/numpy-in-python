URBAN METRO OPERATIONS & PASSENGER ANALYTICS
===============================================

PROJECT ROLE
------------
You are a Data Analyst for an urban metro operator. Management wants to
understand passenger demand, route performance, station capacity, train
utilization and operational delays.

DATASETS
--------
metro_trips.csv       20,000 trip records
metro_stations.csv       60 station records
metro_trains.csv        120 train records
metro_incidents.csv   1,800 incident records

BUSINESS GRAIN
--------------
metro_trips.csv: one row = one train trip.
metro_incidents.csv: one row = one incident; a trip can have multiple incidents.

IMPORTANT NOTE
--------------
The datasets intentionally contain a small number of data-quality issues:
missing passenger counts, invalid station IDs, negative fares and zero
distances. These are included so the project requires genuine data cleaning.

KEY SKILLS
----------
read_csv, info, describe, isna, fillna, drop_duplicates, astype,
to_datetime, merge, groupby, agg, transform, rank, query, pivot_table,
crosstab, value_counts, nunique, map, apply, vectorization, axis,
cut, qcut, shift, rolling, pct_change, memory_usage, category,
chunksize, CSV export.

EXPECTED DELIVERABLES
---------------------
cleaned_trips.csv
route_performance.csv
station_performance.csv
train_performance.csv
delay_analysis.csv
daily_trends.csv
executive_summary.csv
evidence_based_recommendations.md
ecommerce_analysis.ipynb (or metro_operations_analysis.ipynb)

PORTFOLIO EXPECTATION
---------------------
The final repository should contain reproducible code, a README, the raw
datasets, processed outputs and a concise business findings section.
