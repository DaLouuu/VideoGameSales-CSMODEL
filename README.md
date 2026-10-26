# 🎮 Video Game Sales Analysis

> **Statistical Modeling and Simulation (CSMODEL) — Major Course Output (MCO)**  
> **De La Salle University** | **Section S12** | **Group 5**

---

## 👥 Group Members
* **Marian Ricci Ariaga** (Marian) — S12
* **Rizza Mikaella Chan** (Rizza) — S12
* **Dana Louise Guillarte** (Dana) — S12
* **Samantha Erica O'Neil** (Sam) — S12
* **Chrysille Grace So** (Chrysille) — S12

---

## 📌 Project Overview
The video game industry is a multi-billion dollar market shaped by diverse player demographics, technological evolutions across console generations, and shifting critical receptions. This project conducts an exploratory data analysis (EDA) and statistical modeling study on video game sales and ratings, combining market data from **VGChartz** and review data from **Metacritic**.

### 🔍 Core Research Question
> **"How do various factors, such as platform, genre, publisher, critic and user scores, and ESRB rating, correlate to the success of video games, as measured by global sales over the past decade?"**

---

## 📊 Dataset Description
The dataset contains records of video game releases with sales exceeding 100,000 copies, along with critical ratings and regional sales figures.

| Feature | Data Type | Description |
| :--- | :--- | :--- |
| `Name` | `String` / `Object` | Name of the video game title |
| `Platform` | `Categorical` | Gaming platform/console (e.g., PS4, X360, Wii, PC, DS) |
| `Year_of_Release` | `Integer` | Year the title was officially released (1980–2020) |
| `Genre` | `Categorical` | Video game genre (Action, Sports, Shooter, RPG, etc.) |
| `Publisher` | `Categorical` | Publishing company (e.g., Electronic Arts, Nintendo, Activision) |
| `NA_Sales` | `Float` | North American sales (in millions of units) |
| `EU_Sales` | `Float` | European Union sales (in millions of units) |
| `JP_Sales` | `Float` | Japanese sales (in millions of units) |
| `Other_Sales` | `Float` | Rest of the world sales (in millions of units) |
| `Global_Sales` | `Float` | Total worldwide sales (in millions of units) |
| `Critic_Score` | `Float` | Aggregate score compiled by Metacritic staff (0–100) |
| `Critic_Count` | `Float` | Number of critic reviews used in calculating Critic_Score |
| `User_Score` | `Float` | Aggregate score from Metacritic users (0.0–10.0) |
| `User_Count` | `Float` | Number of user reviews used in calculating User_Score |
| `Rating` | `Categorical` | ESRB age rating (E, E10+, T, M, AO, K-A, RP) |

### 🧹 Data Cleaning Summary
* **Raw Records**: 17,416 rows
* **Cleaned Records**: 7,112 rows (filtered to complete observations containing all critical sales, scores, and ratings)
* **Cleaning Script**: Automated via `data_cleaning.py`, which sanitizes data types and outputs `Video_Game_Sales_Cleaned.csv`.

---

## 📈 Key Findings & EDA Highlights

1. **Release Trends Across Years & Platforms**:
   * Peak release density occurred between **2007 and 2011**, driven by the 7th-generation consoles (PlayStation 3, Xbox 360, and Nintendo Wii/DS).
   * **Action** and **Sports** represent the highest volume of distinct game titles published.

2. **Sales by Genre & Region**:
   * **Action**, **Sports**, and **Shooters** dominate total global sales.
   * **North America** represents the largest single regional market, followed by Europe, Japan, and other territories.
   * Japanese market preferences diverge noticeably, showing disproportionately high sales for Role-Playing Games (RPGs) and handheld platforms.

3. **ESRB Ratings**:
   * Games rated **`E` (Everyone)** achieve the highest cumulative sales volume, followed closely by **`M` (Mature)** and **`T` (Teen)** titles.

4. **Measures of Central Tendency & Dispersion**:
   * Global sales exhibit a strong right-skewed distribution: the median global sales is **0.29 million units**, while blockbuster outliers (such as *Wii Sports* at 82.54M) drive the mean to **0.77 million units**.
   * Top publisher by median global sales is **SquareSoft**, while publishers like **Valve** and **Hello Games** lead in median review scores and engagement.

5. **Correlational Relationships**:
   * **Critic Score vs. User Score**: Moderate-to-strong positive correlation ($r \approx 0.58$), confirming that critical praise generally aligns with community reception.
   * **Critic Score vs. Global Sales**: Positive correlation, indicating that higher Metacritic critic scores are associated with higher commercial success.

---

## 🖥️ Frontend Status & Recommendations

### Current Assessment
* **No Frontend**: The repository currently consists of Python scripts, Jupyter notebooks, and CSV data files without a user interface (UI) or web frontend.

### Recommended Frontend Enhancements
To turn this project into an interactive web demonstration, a lightweight Python-based dashboard is recommended:
1. **Streamlit / Dash Application (`app/dashboard.py`)**:
   * **Interactive Filtering**: Filter games by release year, console family, genre, and ESRB rating.
   * **Dynamic Visualizations**: Real-time sales comparisons across regions with Plotly.
   * **What-If Sales Predictor**: A trained regression model allowing users to input a game's genre, platform, and projected Metacritic score to predict estimated global sales.

---

## 📂 Recommended Project Hierarchy

```text
Video-Game-Sales-Analysis-CSMODEL/
│
├── README.md                      # Project documentation and summary
├── requirements.txt               # Python package dependencies
├── .gitignore                     # Git ignore rules for Python & Jupyter
│
├── data/
│   ├── raw/                       # Original, untouched raw data
│   │   └── Video_Game_Sales.csv
│   └── processed/                 # Sanitized data for modeling
│       └── Video_Game_Sales_Cleaned.csv
│
├── notebooks/                     # Exploratory Data Analysis & Modeling
│   └── CSMODEL_MCO.ipynb
│
├── src/                           # Modular Python scripts
│   ├── __init__.py
│   ├── data_cleaning.py           # Preprocessing & sanitation pipeline
│   ├── visualization.py           # Plotting & EDA utility functions
│   └── modeling.py                # Statistical models & regression
│
├── docs/                          # Course deliverables & documentation
│   └── Group 5 Members.txt
│
└── app/                           # (Optional) Interactive Frontend
    └── dashboard.py               # Streamlit interactive web dashboard
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DaLouuu/VideoGameSales-CSMODEL.git
   cd VideoGameSales-CSMODEL
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running Data Cleaning
Run the data cleaning script from the repository root to inspect raw distributions and export the cleaned dataset:
```bash
python src/data_cleaning.py
```

### Running the Jupyter Notebook
Launch Jupyter Notebook or JupyterLab to interact with the full statistical analysis:
```bash
jupyter notebook notebooks/CSMODEL_MCO.ipynb
```

---

## 📄 License & Academic Integrity
This repository is submitted as an academic requirement for **CSMODEL** at **De La Salle University**. All data and analysis are intended for educational and research purposes.
