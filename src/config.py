"""Configuration settings for NYC School SAT analysis."""

# Analysis parameters
MATH_THRESHOLD_PERCENTAGE = 0.8  # 80% of maximum score
MAX_SAT_SECTION_SCORE = 800
TOP_N_SCHOOLS = 10

# File paths
DATA_PATH = "data/raw/schools.csv"
FIGURES_OUTPUT_DIR = "outputs/figures"
REPORTS_OUTPUT_DIR = "outputs/reports"

# Visualization settings
FIGURE_SIZE = (10, 6)
HISTOGRAM_BINS = 30
DPI = 300