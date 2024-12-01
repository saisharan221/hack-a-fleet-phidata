# Hack-A-Fleet v2.0: Optimizing Ferry Operations for Climate Neutrality

## Introduction

The **Hack-A-Fleet v2.0** hackathon provided an opportunity to leverage real-world data and innovative solutions to assist **Färjerederiet**, Sweden’s national ferry service, in achieving its ambitious **Vision 45**—becoming climate neutral by 2045. Using detailed ferry trip data, route schedules, and ferry specifications, we developed data-driven insights and optimization strategies aimed at reducing emissions while maintaining service quality.

Our project focused on five ferry routes operated by Färjerederiet. Each route had distinct operational challenges, necessitating tailored solutions. We applied modern data analysis tools, advanced machine learning models (e.g., OpenAI GPT-4), and optimization techniques to address these challenges.

**Please refer to the optimized_schedules folder, optimization.ipynb and ferry_schedules.ipynb**
---

## Objectives

1. **Optimize Ferry Schedules**:
   - Adjust trip frequencies based on peak and off-peak demand.
   - Identify opportunities to consolidate trips during low-demand periods.
2. **Reduce Emissions**:
   - Minimize unnecessary trips and optimize fuel efficiency.
   - Allocate ferries based on capacity and operational power to reduce fuel consumption.
3. **Enhance Operational Insights**:
   - Use data-driven visualizations to uncover demand patterns and inefficiencies.
   - Generate actionable insights to align operations with Vision 45.

---

## Datasets and Tools

### Datasets Used

1. **`ferry_trips_data.csv`**:
   - Contains trip records for five ferries (Fragancia, Jupiter, Merkurius, Nina, and Yxlan) from March 2023 to February 2024.
   - Key fields include:
     - Departure times (`time_departure`).
     - Trip types (e.g., ordinary, extra, proactive).
     - Passenger Car Equivalent (PCE) values for vehicles transported.
     - Estimated fuel consumption (`fuelcons_outbound_l`, `fuelcons_inbound_l`).
     - Distance traveled (`distance_outbound_nm`, `distance_inbound_nm`).

2. **`ferries.json`**:
   - Provides specifications for the ferries, such as PCE capacity, installed power, and operational details.

3. **Route Schedules**:
   - CSV files with detailed schedules for each route.

4. **Route Descriptions**:
   - Markdown file (`route_descriptions.md`) summarizing the characteristics of each route.

---

### Tools and Technologies

1. **Python**:
   - Core programming language for data manipulation, analysis, and visualization.

2. **Pandas**:
   - Used for efficient data cleaning, aggregation, and manipulation.

3. **Matplotlib and Seaborn**:
   - Libraries for creating informative and visually appealing graphs.

4. **OpenAI GPT-4**:
   - Used to generate optimized schedules and fleet allocations based on route-specific data and operational goals.

5. **PONTOS-HUB**:
   - Integrated real-time and historical data on ferry operations, enabling complementary insights into fuel consumption and emissions.

---

## Methodology

### 1. Data Loading and Preprocessing

We began by loading and inspecting the datasets to understand their structure and identify any missing or inconsistent values. Key preprocessing steps included:

- Parsing timestamps for trip departure times.
- Handling missing data in fields such as fuel consumption and vehicle counts.
- Calculating derived metrics like total Passenger Car Equivalent (PCE) for each trip.

---

### 2. Exploratory Data Analysis (EDA)

**Objective**: Uncover demand patterns, inefficiencies, and potential areas for optimization.

#### a) Trip Type Analysis
We analyzed the distribution of trip types (ordinary, extra, proactive, etc.) to identify patterns in operational variability.

#### b) Vehicle Demand and Capacity
- Calculated the total and average number of vehicles left at terminals for outbound and inbound trips.
- Identified high-demand periods where ferries were at or near capacity.

#### c) Fuel Consumption and Distance
- Visualized average fuel consumption and distances traveled for outbound and inbound trips, aggregated by route and ferry.
- Highlighted routes and times with the highest inefficiencies.

#### d) PCE Distribution
- Examined the distribution of Passenger Car Equivalents (PCE) to understand typical trip loads.
- Identified periods of over- or under-utilization.

---

### 3. Optimization Strategies

Using insights from EDA, we defined optimization goals tailored to each route’s characteristics. These strategies were implemented in collaboration with OpenAI GPT-4, which generated specific recommendations for schedules and fleet usage.

#### a) Optimization Goals

1. **Aspöleden**:
   - Retain only the ferry **Yxlan** during late-night hours (10 PM–6 AM).
   - Schedule trips every 50 minutes during off-peak times.
   - Use both ferries during peak hours to meet demand.

2. **Oxdjupsleden**:
   - Reduce trip frequency to one trip every 15 minutes during late-night hours.
   - Retain **Fragancia** (lower emissions) for all operations.

3. **Furusundsleden**:
   - Operate only **Merkurius** during winter weekdays.
   - Retain both ferries during summer holidays and weekends.
   - Use **Gulli** (lower capacity) for off-peak trips to reduce fuel consumption.

4. **Vaxholmsleden**:
   - Retain only **Castella** during late-night hours, with trips every 20 minutes.
   - Use both **Nina** and **Castella** during peak hours.

5. **Ljusteröleden**:
   - Retain both ferries during summer weekends and holidays for peak demand.
   - Reduce trips during winter weekdays, using only **Jupiter** during off-peak times.
   - Use **Frida** (lower capacity) for low-demand hours to minimize emissions.

#### b) OpenAI GPT-4 Integration

We formulated detailed prompts containing:
- Route descriptions and operational challenges.
- Current schedules and fleet specifications.
- Specific optimization goals (e.g., reducing trips, reallocating ferries).

GPT-4 generated:
1. Optimized schedules in CSV format.
2. Fleet assignments for peak and off-peak hours.
3. Feasibility analysis for proposed changes.
4. Simulated metrics for emissions reduction and demand fulfillment.

---

### 4. Implementation

- **Schedule Adjustments**: Modified trip frequencies and fleet allocations based on GPT-4 recommendations.
- **Simulations**: Evaluated the impact of optimizations on demand fulfillment and emissions reduction.
- **Visualization**: Created graphs to compare pre- and post-optimization metrics, including demand levels, fuel consumption, and PCE distributions.

---

### 5. Key Insights

#### a) Demand Patterns
- High demand during morning and evening peaks required additional capacity.
- Late-night trips were often underutilized, presenting opportunities for consolidation.

#### b) Emissions Reduction
- Significant emissions savings were achieved by:
  - Reducing trip frequencies during off-peak periods.
  - Allocating ferries with lower installed power for low-demand trips.

#### c) Operational Feasibility
- Seasonal adjustments (e.g., reducing trips in winter) were practical and aligned with traffic patterns.
- Geographic proximity allowed selective merging of certain routes (e.g., Vaxholmsleden and Oxdjupsleden).

---

## Challenges and Limitations

1. **Data Availability**:
   - Some trips lacked complete data for fuel consumption and distances, requiring imputation or exclusion.

2. **Real-Time Integration**:
   - Incorporating real-time data from PONTOS-HUB was partially implemented due to time constraints.

3. **Feasibility in Practice**:
   - While optimizations showed significant potential, real-world implementation would require stakeholder collaboration and infrastructure adjustments.

---



## Conclusion

Through data-driven analysis and AI-powered optimization, we successfully proposed actionable strategies to enhance Färjerederiet’s ferry operations. These strategies promise to reduce emissions, improve efficiency, and support the organization's Vision 45 goals.

This project demonstrates the power of combining real-world data, advanced analytics, and AI to address critical environmental challenges in the transportation sector.
