# End-to-End ML OPS Project: Thyroid Disease Classification

> A comprehensive machine learning operations (MLOps) project for thyroid disease prediction and analysis using modern ML workflows, logging infrastructure, and production-ready practices.

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Features](#features)
- [Project Pipeline](#project-pipeline)
- [Configuration](#configuration)
- [Logging](#logging)
- [Results](#results)
- [Docker Support](#docker-support)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [References](#references)
- [Contact](#contact)

---

## 🎯 Overview

This is an **end-to-end Machine Learning Operations (MLOps)** project that implements best practices for building, deploying, and maintaining machine learning models. The project focuses on **thyroid disease classification** using patient demographics, medical history, and hormone test results.

### Key Objectives
- Build a robust ML pipeline with proper version control and reproducibility
- Implement comprehensive data exploration and analysis
- Create production-ready model training and evaluation
- Establish logging and monitoring infrastructure
- Deploy the model using Flask REST API
- Containerize the application with Docker

---

## 🔍 Problem Statement

Thyroid disease is a common endocrine disorder affecting millions worldwide. Early detection and classification is critical for patient management. This project aims to:

1. **Predict thyroid disease status** (Normal vs Hyperthyroid)
2. **Analyze risk factors** and their relationships to disease
3. **Provide interpretable predictions** with confidence metrics
4. **Build a scalable, production-ready** prediction system

### Target Variable
- **Diagnosis**: Classification of thyroid status
  - Normal (Healthy)
  - Hyperthyroid (Overactive thyroid)

---

## 📊 Dataset

### Overview
- **Total Records**: 908 patients
- **Total Features**: 17 columns (after processing)
- **Target Variable**: Diagnosis (Binary Classification)
- **Missing Values**: 0 (100% complete dataset)
- **Data Quality**: High - No duplicates or anomalies

### Feature Categories

#### Demographics (2 features)
- **Age**: Patient age (18-79 years)
- **Sex**: Gender (Female/Male)

#### Medical History (11 binary features)
- Family history of thyroid disease
- Pregnancy status
- Thyroid medications
- Medical procedures (surgery, radioactive iodine)
- Comorbid conditions

#### Hormone Test Results (4 numeric features)
- TSH (Thyroid Stimulating Hormone)
- T3 (Triiodothyronine)
- T4 (Thyroxine)
- Thyroid Antibodies

### Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Patients | 908 |
| Female | 626 (68.9%) |
| Male | 282 (31.1%) |
| Hyperthyroid Cases | 262 (28.9%) |
| Normal Cases | 646 (71.1%) |
| Average Age | 50.1 years |
| BMI Range | 14.0 - 38.7 |

> For detailed dataset information, see [DATASET.md](DATASET.md)

---

## 📁 Project Structure

```
End-to-End-MLOPS/
│
├── src/mlProject/                    # Source code package
│   ├── __init__.py
│   ├── components/                   # Modular components
│   │   └── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── configuration.py         # Config management
│   ├── constants/
│   │   └── __init__.py
│   ├── entity/
│   │   ├── __init__.py
│   │   └── config_entity.py         # Entity definitions
│   ├── pipeline/                     # ML pipeline stages
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py                # Logging system
│       └── common.py                # Common utilities
│
├── research/
│   └── experiments.ipynb            # EDA & exploration (28 cells)
│
├── config/
│   └── config.yaml                  # Configuration file
│
├── templates/
│   └── index.html                   # Flask UI template
│
├── data/                            # Data directory
│   └── thyroid_dataset.xlsx         # Raw dataset
│
├── artifacts/                       # Generated artifacts
│   └── (models, preprocessors, etc.)
│
├── logs/                            # Application logs
│   └── app_*.log                    # Timestamped log files
│
├── app.py                           # Flask REST API
├── main.py                          # Entry point
├── setup.py                         # Package setup
├── requirements.txt                 # Python dependencies
├── params.yaml                      # Pipeline parameters
├── schema.yaml                      # Data schema
├── Dockerfile                       # Docker container config
├── DATASET.md                       # Dataset documentation
├── LOGGING_GUIDE.md                 # Logging documentation
└── Readme.md                        # This file
```

---

## 💻 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone Repository
```bash
git clone https://github.com/pooja/End-to-End-MLOPS.git
cd End-to-End-MLOPS
```

### Step 2: Create Virtual Environment
```bash
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python main.py
```

You should see initialization logs and confirmation messages.

---

## 🚀 Quick Start

### 1. Run Data Exploration
```bash
# Open and run the Jupyter notebook for EDA
jupyter notebook research/experiments.ipynb
```

The notebook includes:
- Data loading and inspection
- Statistical analysis
- Distribution analysis (14 numeric features)
- Correlation analysis
- Missing value checks
- Target variable distribution
- Multi-condition analysis

### 2. Start Flask API
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### 3. Make Predictions
```bash
# Health check
curl http://localhost:5000/health

# Example prediction (JSON POST)
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "sex": "Female",
    "thyroid_level": 2.5
  }'
```

---

## 📝 Usage

### Data Exploration
Navigate to `research/experiments.ipynb` for comprehensive exploratory data analysis:

```python
# Load data
df = pd.read_excel('data/thyroid_dataset.xlsx')

# View basic info
print(df.info())
print(df.describe())

# Run visualizations (already included in notebook)
# - Age distribution
# - Sex-based thyroid prevalence
# - Pregnancy impact
# - Correlation heatmap
# - Medical condition analysis
# - Target variable balance
```

### Training Pipeline
```python
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.pipeline import training_pipeline

# Initialize configuration
config = ConfigurationManager()

# Run the training pipeline
pipeline = training_pipeline.TrainingPipeline(config)
pipeline.run()
```

### Making Predictions
```python
from src.mlProject.utils.common import load_object
import pickle

# Load trained model
model = load_object(path='artifacts/model.pkl')

# Make prediction
prediction = model.predict(X_test)
```

---

## ✨ Features

### Data Processing
- ✅ Complete dataset (908 records, 0 missing values)
- ✅ Comprehensive EDA (28 Jupyter cells)
- ✅ Multi-condition analysis
- ✅ Feature distribution analysis
- ✅ Data quality validation

### Logging & Monitoring
- ✅ Dual-handler logging system (console + file)
- ✅ Timestamped log files
- ✅ Configurable log levels
- ✅ Request/response logging in Flask
- ✅ Error tracking and diagnostics

### ML Pipeline
- 🔄 Data validation and preprocessing
- 🔄 Feature engineering
- 🔄 Model training and hyperparameter tuning
- 🔄 Model evaluation and metrics
- 🔄 Model persistence (serialization)

### API & Deployment
- ✅ Flask REST API with CORS support
- ✅ Health check endpoint
- ✅ Prediction endpoint
- ✅ Error handling and validation
- ✅ Docker containerization support

### Development Tools
- ✅ Version control integration (.gitignore)
- ✅ Configuration management (YAML)
- ✅ Package management (setup.py)
- ✅ Requirements tracking
- ✅ Comprehensive documentation

---

## 🔄 Project Pipeline

### Phase 1: Data Exploration (✅ Complete)
- **Notebook**: `research/experiments.ipynb`
- **Status**: 28 cells with comprehensive analysis
- **Outputs**: 
  - Age, sex, pregnancy analysis
  - Correlation heatmap
  - Distribution visualizations
  - Data quality report

### Phase 2: Data Preprocessing (🔄 In Development)
**Planned Components**:
- Data validation and cleaning
- Feature scaling (normalization/standardization)
- Categorical encoding
- Outlier detection and handling
- Feature selection
- Train/validation/test split

### Phase 3: Model Training (🔄 In Development)
**Planned Components**:
- Multiple model architectures
- Hyperparameter tuning
- Cross-validation
- Model comparison
- Best model selection

### Phase 4: Model Evaluation (🔄 In Development)
**Planned Components**:
- Performance metrics (accuracy, precision, recall, F1)
- ROC-AUC curves
- Confusion matrix
- Feature importance analysis

### Phase 5: Deployment (🔄 In Development)
**Planned Components**:
- Model serving
- API endpoints
- Docker containerization
- Monitoring and logging

---

## ⚙️ Configuration

### Configuration Files

#### `config/config.yaml`
Main configuration file for pipeline parameters:
```yaml
# Will be populated with:
# - Data paths
# - Model parameters
# - Train/test ratios
# - Preprocessing options
```

#### `params.yaml`
Experiment parameters:
```yaml
# Will include:
# - Hyperparameters
# - Thresholds
# - Algorithm choices
```

#### `schema.yaml`
Data schema and validation rules:
```yaml
# Will define:
# - Column names and types
# - Acceptable value ranges
# - Data constraints
```

### Environment Variables
Create a `.env` file (not included in git) for sensitive configurations:
```env
FLASK_ENV=development
DEBUG=True
LOG_LEVEL=INFO
DATABASE_URL=your_db_url
```

---

## 📋 Logging

The project implements comprehensive logging with:

### Log Levels
- **DEBUG**: Detailed diagnostics
- **INFO**: General information
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical errors

### Log Output
- **Console**: INFO level and above
- **File**: DEBUG level and above (logs/app_*.log)

### Usage Example
```python
from src.mlProject.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Processing started")
logger.error("An error occurred")
```

> For detailed logging guide, see [LOGGING_GUIDE.md](LOGGING_GUIDE.md)

---

## 📊 Results

### Current Status
- **Data Exploration**: ✅ Complete
  - 908 patient records analyzed
  - 14 numeric features profiled
  - 71.1% class imbalance identified
  - Zero missing values confirmed

### Target Metrics (Planned)
- **Accuracy**: Target > 85%
- **Precision**: Target > 0.80 (minimize false positives)
- **Recall**: Target > 0.75 (catch thyroid cases)
- **F1-Score**: Target > 0.77 (balanced performance)

### Key Findings from EDA
1. **Class Imbalance**: 2.47:1 ratio (Normal vs Hyperthyroid)
2. **Demographics**: 68.9% female (higher thyroid prevalence)
3. **Medical Conditions**: Average 0.74 conditions per patient
4. **Age Distribution**: Ranges 18-79, roughly uniform
5. **Data Quality**: 100% complete, no duplicates

---

## 🐳 Docker Support

### Build Docker Image
```bash
docker build -t thyroid-ml-app:latest .
```

### Run Docker Container
```bash
docker run -p 5000:5000 thyroid-ml-app:latest
```

### Docker Compose (Optional)
```bash
docker-compose up -d
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 code style
- Add docstrings to functions
- Include unit tests
- Update documentation
- Add log messages for debugging

---

## 🛠️ Troubleshooting

### Issue: Import errors when running `main.py`
**Solution**:
```bash
pip install -e .
python main.py
```

### Issue: Jupyter notebook kernel not found
**Solution**:
```bash
pip install ipykernel
python -m ipykernel install --user --name venv
```

### Issue: Port 5000 already in use
**Solution**:
```bash
# On Linux/Mac
lsof -i :5000
kill -9 <PID>

# Or use different port in app.py
flask run --port 5001
```

### Issue: Data file not found
**Solution**:
- Ensure `data/thyroid_dataset.xlsx` exists
- Check file paths in configuration
- Verify read permissions

### Issue: Logging not working
**Solution**:
- Ensure `logs/` directory exists: `mkdir logs`
- Check file permissions: `chmod 755 logs/`
- Verify logger configuration in `src/mlProject/utils/logger.py`

---

## 📚 References

### Dataset
- Original source: Healthcare ML dataset
- Format: Excel (.xlsx)
- Features: Demographic, medical history, hormone tests

### Technologies Used
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **ML Framework**: scikit-learn
- **Web Framework**: Flask, Flask-CORS
- **Configuration**: PyYAML, python-box
- **Containerization**: Docker
- **Notebook**: Jupyter

### Documentation
- [DATASET.md](DATASET.md) - Comprehensive dataset documentation
- [LOGGING_GUIDE.md](LOGGING_GUIDE.md) - Logging system documentation
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

## 👤 Contact

**Author**: Pooja Babar  
**Email**: babarpooja2002@gmail.com  
**GitHub**: [@pooja](https://github.com/pooja)  
**Repository**: [End-to-End-MLOPS](https://github.com/pooja/End-to-End-MLOPS)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## ⭐ Acknowledgments

- Dataset source and medical domain experts
- Open-source community (pandas, scikit-learn, Flask)
- MLOps best practices and standards
- Contributors and reviewers

---

## 🗓️ Project Timeline

| Phase | Status | Timeline |
|-------|--------|----------|
| Data Exploration | ✅ Complete | Week 1-2 |
| Data Preprocessing | 🔄 In Progress | Week 2-3 |
| Model Training | ⏳ Planned | Week 3-4 |
| Model Evaluation | ⏳ Planned | Week 4-5 |
| Deployment | ⏳ Planned | Week 5-6 |

---

**Last Updated**: March 2026  
**Version**: 0.0.1

