# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a data analysis project focused on analyzing NYC public school SAT performance data using Python and Jupyter notebooks. The project answers three key questions about school performance through exploratory data analysis and is now organized into a modular structure with reusable components.

## Architecture & Structure

```
nyc_public_school_case_datacamp/
├── data/
│   ├── raw/                    # Original datasets
│   │   └── schools.csv         # NYC school SAT data (375 schools)
│   └── processed/              # Cleaned/transformed data
├── notebooks/
│   └── analysis.ipynb          # Main analysis notebook
├── src/                        # Python modules
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── data_processing.py     # Data loading and cleaning functions
│   ├── analysis.py            # Core analysis functions
│   └── visualization.py       # Plotting and output utilities
├── outputs/
│   ├── figures/               # Generated plots and charts
│   └── reports/               # Analysis results (CSV files)
├── requirements.txt           # Python dependencies
└── .gitignore                # Git ignore rules
```

- **Modular Design**: Analysis functions separated into logical modules
- **Data Organization**: Raw data separated from processed outputs
- **Dependency Management**: Formal requirements.txt for reproducibility

## Core Components

### Data Structure
The `schools.csv` dataset contains:
- `school_name`: Name of the school
- `borough`: NYC borough (Manhattan, Brooklyn, Bronx, Queens, Staten Island)
- `building_code`: School building identifier
- `average_math`, `average_reading`, `average_writing`: SAT section scores (max 800 each)
- `percent_tested`: Percentage of students who took the SAT

### Analysis Questions Addressed
1. Which NYC schools have the best math results? (≥80% of max score = 640+)
2. What are the top 10 performing schools based on combined SAT scores?
3. Which borough has the largest standard deviation in combined SAT scores?

## Development Workflow

### Setup and Installation
1. Clone the repository and navigate to project directory
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure proper folder structure is in place

### Running the Analysis
1. **Notebook Analysis**: Open `notebooks/analysis.ipynb` in Jupyter
2. **Modular Usage**: Import functions from `src/` modules for custom analysis
3. **Configuration**: Modify `src/config.py` for analysis parameters

### Using the Modular Structure
```python
from src.data_processing import load_schools_data, clean_data, calculate_total_sat
from src.analysis import get_best_math_schools, get_top_schools_by_total_sat
from src.visualization import plot_score_distribution, save_analysis_results
from src.config import DATA_PATH, MATH_THRESHOLD_PERCENTAGE

# Load and process data
df = load_schools_data(DATA_PATH)
df_clean = clean_data(df)
df_with_total = calculate_total_sat(df_clean)

# Run analysis
threshold = get_math_threshold(MATH_THRESHOLD_PERCENTAGE)
best_math = get_best_math_schools(df_with_total, threshold)
```

### Dependencies
- pandas>=2.0.0 (data manipulation)
- matplotlib>=3.7.0 (visualization)  
- jupyter>=1.0.0 (notebook interface)

### Data Processing Pipeline
1. Load CSV data from `data/raw/schools.csv`
2. Handle missing values (drop NaN entries)
3. Calculate derived metrics (total_SAT score)
4. Group by borough for statistical analysis
5. Generate visualizations and save to `outputs/figures/`
6. Export results to `outputs/reports/`

## Key Analysis Patterns

- **Best Performance Threshold**: Math scores ≥640 (80% of maximum 800)
- **Combined SAT Score**: Sum of math + reading + writing averages
- **Statistical Analysis**: Standard deviation calculations by borough
- **Data Cleaning**: Drops rows with NaN values (375 → 355 schools)

## Module Documentation

### `src/data_processing.py`
- `load_schools_data()`: Load CSV data into DataFrame
- `clean_data()`: Remove rows with missing values
- `calculate_total_sat()`: Add total_SAT column
- `get_math_threshold()`: Calculate score thresholds

### `src/analysis.py`
- `get_best_math_schools()`: Filter schools above math threshold
- `get_top_schools_by_total_sat()`: Get top N schools by total SAT
- `get_borough_stats()`: Calculate borough-level statistics
- `get_largest_std_borough()`: Find borough with highest SAT score variance

### `src/visualization.py`
- `plot_score_distribution()`: Create score histograms
- `plot_null_values()`: Visualize missing data patterns
- `save_analysis_results()`: Export DataFrames to CSV

### `src/config.py`
Configuration constants for analysis parameters, file paths, and visualization settings.

## Development Notes

- **Modular Architecture**: Functions extracted from notebook for reusability
- **Configuration Management**: Centralized settings in `config.py`
- **Output Organization**: Separate directories for figures and reports
- **Dependency Management**: Formal `requirements.txt` for reproducibility
- **Documentation**: Comprehensive docstrings in all modules
- **Text Content**: Includes both English and Portuguese documentation