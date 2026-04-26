# ML Query Optimiser

ML Query Optimiser is a machine learning project that simulates database workloads, detects anomalous SQL query behavior, and recommends optimization actions. The repository combines a Jupyter notebook for data generation, feature engineering, anomaly detection, and rewrite simulation with a Streamlit dashboard for interactive result analysis. It is designed as a practical portfolio-style project that demonstrates how ML can support database performance monitoring and query tuning.

## Project Overview

The project follows an end-to-end workflow:

1. Create a realistic synthetic database workload in SQLite.
2. Generate and log large volumes of SQL queries with performance metadata.
3. Engineer features such as execution time, complexity score, scan ratio, and time per row.
4. Detect inefficient or unusual queries using an Isolation Forest model.
5. Classify likely root causes and simulate optimization actions.
6. Visualize anomalies, performance improvements, and optimization outcomes in a Streamlit dashboard.

## Repository Structure

```text
ML_Query_Optimiser/
├── Dashboard/
│   └── Dashboard.py
└── Notebook/
    └── Query_anomaly_detection&optimization-2.ipynb
```

## Key Features

- Synthetic database and query workload generation
- Query performance logging and feature engineering
- ML-based anomaly detection using Isolation Forest
- Simulated root cause analysis for slow or inefficient queries
- Query optimization recommendation and rewrite evaluation
- Interactive dashboard for monitoring results and performance gains

## Tech Stack

- Python
- Jupyter Notebook
- SQLite
- pandas
- scikit-learn
- matplotlib
- Streamlit

## How It Works

The notebook builds the full experiment pipeline. It first creates a realistic dataset of SQL activity, then derives performance-related features from each query. These features are used to train an anomaly detection model that flags unusual query behavior. The detected anomalies are then analyzed for likely causes, and multiple optimization strategies are simulated to estimate possible performance improvements.

The dashboard reads the exported result files and presents summary metrics, histograms, box plots, root-cause distributions, top slow queries, and optimization effectiveness charts.

## Running the Project

### 1. Install dependencies

Create a Python environment and install the required libraries:

```bash
pip install pandas matplotlib scikit-learn streamlit jupyter
```

### 2. Run the notebook

Open and execute the notebook:

```bash
jupyter notebook "Notebook/Query_anomaly_detection&optimization-2.ipynb"
```

Running the notebook generates the result files used by the dashboard, including:

- `anomalies.csv`
- `ai_optimizer_results.csv`
- `df_real.csv`

### 3. Launch the dashboard

From the project root, start Streamlit:

```bash
streamlit run Dashboard/Dashboard.py
```

Note: `Dashboard.py` expects the generated CSV files to be available when the app starts. If needed, place those files in the location from which you run the dashboard so Streamlit can load them correctly.

## Outputs

After running the notebook and dashboard, you can inspect:

- anomalous queries detected by the model
- likely root causes behind slow performance
- optimized query variants and estimated time savings
- aggregate metrics such as improvement rate and total time saved

## Use Cases

- Demonstrating ML applications in database performance analysis
- Showcasing anomaly detection on query execution patterns
- Building a portfolio project around data engineering and ML operations
- Exploring query optimization concepts in a practical workflow

## Future Improvements

- Add a `requirements.txt` file for reproducible setup
- Save generated CSV files into a dedicated `data/` directory
- Improve dashboard file-path handling
- Connect the pipeline to a real database workload instead of only synthetic data
- Replace simulated optimizations with database-aware rewrite logic

## License

No license file is currently included in this repository. Add one if you plan to distribute or open-source the project formally.
