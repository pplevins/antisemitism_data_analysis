# 🕵️ Antisemitism Data Analysis

This project analyzes tweets for antisemitic content using a structured pipeline
that loads, cleans, processes, and reports on a dataset of tweets.
It provides insights into patterns of antisemitic language and behavior across social media.

---

## 📁 Project Structure

```
antisemitism_data_analysis/
│
├── data/                      # Input datasets
│   └── tweets_dataset.csv
│
├── result/                    # Output results
│   ├── result.json
│   └── tweets_dataset_cleaned.csv
│
├── src/                       # Core source code
│   ├── main.py                # Entry point
│   ├── data_loader.py         # Dataset loading and preprocessing
│   ├── data_analyzer.py       # Analysis and detection logic
│   ├── report_builder.py      # Generates summaries or reports
│   └── manager.py             # Workflow orchestration
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Features

- Load and preprocess large-scale tweet datasets
- Detect and flag potential antisemitic content
- Generate cleaned datasets and JSON reports
- Modular architecture for easy extension

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/pplevins/antisemitism_data_analysis.git
cd antisemitism_data_analysis

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# Run the analysis pipeline
python src/main.py
```

The output will be generated in the `result/` folder:

- `result.json`: Summary statistics and flagged content
- `tweets_dataset_cleaned.csv`: Cleaned tweet dataset

---

## 📊 Example Output

```
{
  "total_tweets": {
        "antisemitic": 1250,
        "non_antisemitic": 5691,
        "total": 6941,
        "unspecified": 0
    }
}
```

---

## 📚 Requirements

- Python 3.7+
- See `requirements.txt` for full package list.

---