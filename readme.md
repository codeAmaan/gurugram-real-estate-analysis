# Gurugram Real Estate Market Analysis

## Project Objective

The objective of this project is to analyze a Gurugram real estate dataset
using Python and identify patterns in property prices, localities, property
types, BHK configurations, RERA approval status, and company-level pricing.

The project also focuses on data cleaning, exploratory data analysis, and
visualization to understand the real estate market from a business
perspective.

---

## Dataset

The dataset contains information about residential properties in Gurugram.

### Dataset Size

- Initial records: 19,515
- Records after removing duplicates: 14,223
- Number of columns: 12

### Important Columns

- `Price` - Total property price
- `Status` - Property construction/availability status
- `Area` - Property area
- `Rate per sqft` - Price per square foot
- `Property Type` - Type of property
- `Locality` - Property location
- `Builder Name` - Builder associated with the property
- `RERA Approval` - RERA approval status
- `BHK Count` - Number of bedrooms
- `Society` - Society/project name
- `Company Name` - Company associated with the listing
- `Flat Type` - Type/category of property

---

## Data Cleaning

The dataset required several cleaning and preprocessing steps before analysis.

### Cleaning Steps

- Standardized column names
- Removed duplicate records
- Converted `Price` from string to numeric format
- Converted `Rate per sqft` from string to numeric format
- Removed extra spaces from categorical values
- Converted categorical text values to lowercase
- Standardized RERA approval values
- Standardized flat type values
- Investigated unusual BHK values and excluded plot properties from the BHK
  comparison

After cleaning and removing duplicate records, the dataset contained
14,223 property records.

---

## Business Questions

The analysis focuses on the following business questions:

1. Which is the costliest flat in the dataset?
2. Which locality has the highest average property price?
3. Which locality has the highest average rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does area impact price?
7. Which BHK configuration is most expensive based on rate per square foot?
8. Which property type is the costliest?
9. Do certain companies price higher?
10. Are larger homes more expensive per square foot?

---

# Project Insights

## Q1. Which is the costliest flat in the dataset?

### Result

The costliest property is a 6 BHK apartment in DLF Camellias, Sector 42,
priced at approximately **₹122.63 crore**.

### Business Insight

The dataset shows that ultra-luxury properties in premium Gurugram locations
can command extremely high total prices. DLF Camellias represents one of the
high-end properties observed in the dataset.

---

## Q2. Which locality has the highest average property price?

### Result

**Baliawas** has the highest average property price in the dataset.

### Business Insight

Properties in Baliawas have a relatively high average ticket size,
indicating a higher-value property segment within this dataset.

---

## Q3. Which locality has the highest average rate per square foot?

### Result

**Sector 42** has the highest average rate per square foot.

### Business Insight

Sector 42 shows particularly high per-square-foot pricing, indicating strong
premium positioning in the dataset.

---

## Q4. Do ready-to-move properties cost more than under-construction properties?

### Result

| Property Status | Average Price |
|---|---:|
| Ready to move | ₹4.15 crore |
| Under construction | ₹3.96 crore |

Ready-to-move properties are approximately **₹19.4 lakh more expensive on
average**.

### Business Insight

Ready-to-move properties have a higher average price in this dataset,
suggesting that immediate possession may be associated with a price premium.

However, this is an observed relationship and does not establish causation.

---

## Q5. Do RERA-approved properties command a price premium?

### Result

| RERA Status | Average Price |
|---|---:|
| RERA approved | ₹3.86 crore |
| Not RERA approved | ₹4.08 crore |

### Business Insight

RERA-approved properties did not show a higher average price in this dataset.

Other factors such as locality, property type, size, and builder may also
influence property pricing.

---

## Q6. How does area impact price?

### Result

The scatterplot does not provide a clear relationship between area and total
price because the dataset contains some extremely large area values.

### Business Insight

Outliers in property area can distort the analysis. Further outlier
investigation or treatment would be required before drawing a strong
conclusion about the area-price relationship.

---

## Q7. Which BHK configuration is most expensive based on rate per square foot?

### Result

After excluding plot properties from the BHK analysis, **6 BHK properties**
have the highest average rate per square foot among the BHK configurations
analyzed in this dataset.

### Business Insight

6 BHK properties represent the highest-priced BHK segment by average rate per
square foot in this dataset.

---

## Q8. Which property type is the costliest?

### Result

**Villas** have the highest average rate per square foot.

### Business Insight

Villas represent the highest-priced property type on a per-square-foot basis
in this dataset, indicating their positioning in the premium property segment.

---

## Q9. Do certain companies price higher?

### Result

Considering only companies with at least **10 properties**, the top 5
companies by average rate per square foot are:

| Company | Average Rate per Sqft |
|---|---:|
| Tulip | ₹28,571 |
| Prom | ₹27,359 |
| M3M | ₹24,319 |
| Tribeca | ₹24,119 |
| B | ₹24,019 |

### Business Insight

Among companies with sufficient property observations, Tulip and Prom have
the highest average rates per square foot in this dataset.

A minimum property-count threshold was used to reduce the impact of companies
with very few listings.

---

## Q10. Are larger homes more expensive per square foot?

### Result

The raw scatterplot does not show a clear relationship between property area
and rate per square foot.

### Business Insight

The available visualization does not provide enough evidence to conclude that
larger properties have a higher rate per square foot.

Further outlier treatment and statistical analysis would be useful.

---

# Visualizations

The project includes the following visualizations:

### 1. Top 10 Localities by Average Property Price

A bar chart showing the localities with the highest average property prices.

### 2. Average Rate per Square Foot by Flat Type

A bar chart comparing the average rate per square foot across different
property/flat types.

### 3. Area vs Price

A scatterplot used to explore the relationship between property area and total
property price.

### 4. Area vs Rate per Square Foot

A scatterplot used to examine whether property size is associated with the
rate per square foot.

---

# Tools & Technologies

- **Python**
- **Pandas** - Data cleaning, transformation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical and exploratory visualizations
- **Jupyter Notebook / VS Code** - Development environment
- **Git & GitHub** - Project version control and portfolio hosting

---

# Project Structure

```text
Gurugram-Real-Estate-Analysis/
│
├── data/
│   └── data of gurugram real Estate.csv
│
├── main.py
├── visualization.py
└── README.md