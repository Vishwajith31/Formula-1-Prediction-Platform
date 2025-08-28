# 🏎️ Formula 1 Grand Prix Analytics & ML-Powered Strategy Prediction

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastF1](https://img.shields.io/badge/FastF1-Latest-red.svg)](https://github.com/theOehrly/Fast-F1)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A comprehensive data science pipeline analyzing Formula 1 race performance, pit strategy effectiveness, and driver/team outcomes using machine learning and advanced motorsport feature engineering.

---

## 📊 Project Overview

This project leverages the FastF1 Python API to extract, engineer, and model F1 race data, focusing on:

- **🎯 Race outcome prediction** using ML classification models
- **⚡ Pit stop strategy effectiveness** analysis (undercut/overcut battles)
- **📈 Pace consistency modeling** and driver performance variance
- **🌧️ Weather impact** on strategic decisions and race outcomes
- **📱 Interactive data exploration** (planned Streamlit dashboard)

### Key Differentiators

- **Custom motorsport feature engineering** beyond standard metrics
- **Rigorous methodology** with explicit assumption testing and limitation documentation
- **End-to-end reproducible pipeline** from raw telemetry to deployment-ready insights
- **Strategic focus** on actionable racing insights, not just statistical modeling

---

## 🚀 Current Achievements

### 1. Data Pipeline & Feature Engineering ✅

- **Automated data extraction** from FastF1 API across multiple seasons
- **Advanced feature engineering:**
  - Pace variance (lap time consistency metrics)
  - Pit stop reconstruction from stint transitions
  - Grid-to-finish performance deltas
  - Weather impact integration
  - Team and driver performance profiling

### 2. Machine Learning Models ✅

**Points Finish Prediction Model:**
```bash
Model Type: XGBoost Classifier
Accuracy: 84%
Precision/Recall: 0.84-0.85 (balanced performance)
Target: InPoints (Top 10 finish binary classification)
```


**Key Feature Insights:**
- **Grid Position** remains the dominant predictor (as expected)
- **Team strength** and **stint strategy** provide meaningful incremental value
- **Pace consistency** often more important than raw speed for points finishes
- **Weather effects** less predictive as simple binary feature (improvement opportunity)

### 3. Strategic Analysis Framework ✅

- **Rival pair detection algorithm** for undercut/overcut pit battles
- **Position change tracking** methodology (pre/post pit windows)
- **Success rate quantification** framework ready for multi-season analysis

---

## 📊 Key Visualizations

### Model Performance Analysis
![Feature Importance](visualizations/feature_importance.png)
*XGBoost classifier reveals grid position and team as strongest predictors, with strategic factors providing additional lift*

### Strategic Insights
![Pit Strategy Impact](visualizations/finishing_position_vs_pitstops.png)  
*Analysis of relationship between pit stop frequency and race finishing positions*

![Undercut Effectiveness](visualizations/undercut_success_failure.png)
*Success rates of undercut attempts in head-to-head pit strategy battles*

---

## 📁 Project Structure

```bash
F1-DATA-ANALYSIS-PROJECT/
├── app/
│   ├── .ipynb_checkpoints/
│   └── streamlit_app.py              # Interactive dashboard application
├── data/
│   ├── .ipynb_checkpoints/
│   ├── archive/                      # Historical data backups
│   ├── cleaned/                      # Processed race data
│   └── features/                     # Engineered feature datasets
├── models/
│   ├── .ipynb_checkpoints/
│   └── random_forest_f1.pkl          # Trained model artifacts
├── notebooks/
│   ├── .ipynb_checkpoints/
│   ├── cleanenv/
│   ├── 01_data_overview.ipynb        # Initial data exploration
│   ├── 02_driver_team_analysis.ipynb # Driver and team performance analysis
│   ├── 03_ml_prediction.ipynb       # Machine learning modeling
│   └── xgboost_tree_plot.png        # Model visualization
├── results/
│   └── model_results_summary.csv    # Model performance metrics
├── scripts/
│   ├── .ipynb_checkpoints/
│   ├── build_season_features.py     # Feature engineering pipeline
│   └── laps_extraction.py           # Data extraction from FastF1
├── visualizations/
│   ├── .ipynb_checkpoints/
│   ├── figures/                     # General analysis plots
│   ├── model_visualisations/        # ML model performance charts
│   └── strategic_analysis/          # Pit strategy and tactical insights
├── .gitignore                       # Version control exclusions
└── requirements.txt                 # Project dependencies

```

---

## 🛠️ Technology Stack

**Data Processing:**
- FastF1 - F1 telemetry and timing data (`laps_extraction.py`)
- pandas, NumPy - Data manipulation (`build_season_features.py`)

**Machine Learning:**
- scikit-learn - ML algorithms and evaluation
- XGBoost - Gradient boosting models
- Random Forest, XGBoost - Classification models
- Model persistence with pickle (`random_forest_f1.pkl`)

**Visualization:**
- matplotlib, seaborn - Statistical plotting
- plotly - Interactive visualizations (planned)
- Jupyter Notebooks - Interactive development environment
- Custom visualization pipeline organized by analysis type

**Deployment (Planned):**
- Streamlit - Interactive dashboard
- Docker - Containerization
- AWS/Heroku - Cloud deployment

---

## 🏁 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**
  git clone https://github.com/yourusername/f1-analytics.git
  cd f1-analytics

2. **Create virtual environment (recommended):**
  python -m venv f1_env
  source f1_env/bin/activate  # Windows: f1_env\Scripts\activate

3. **Install dependencies:**
  pip install -r requirements.txt

4. **Verify installation:**
  python -c “import fastf1; print(‘Setup complete!’)”

### Quick Start

Extract race data
  from src.data_extraction import extract_race_data race_data = extract_race_data(2023, ‘Hungarian GP’)
Engineer features
  from src.feature_engineering import engineer_features features = engineer_features(race_data)
Train model
  from src.models.points_predictor import PointsPredictor model = PointsPredictor() accuracy = model.train(features)


---

## 📈 Key Insights Discovered

1. **Grid position dominance confirmed** - Starting position remains the strongest race outcome predictor, but strategic factors provide meaningful incremental predictive power

2. **Pit strategy context dependency** - Undercut/overcut effectiveness varies significantly by track characteristics, weather conditions, and stint timing

3. **Consistency vs speed trade-off** - Drivers with lower lap time variance often outperform faster but inconsistent competitors in points accumulation

4. **Team strategic differences** - Quantifiable and persistent differences in pit strategy execution across constructors

5. **Weather complexity** - Simple rainfall binary classification insufficient; timing and intensity granularity needed for better prediction

---

## 🔄 Limitations & Methodology Notes

### Current Limitations
- **Single-race processing constraint** due to computational efficiency requirements
- **Binary rainfall classification** lacks timing and intensity granularity
- **Pit execution quality** not isolated from strategic decision effectiveness
- **External race events** (Safety Car, red flags) not explicitly modeled

### Intellectual Rigor Approach
- All assumptions explicitly tested and documented
- Alternative explanations considered for each finding
- Limitations and potential biases clearly stated
- Code structured for reproducibility and educational value

---

## 🚧 Roadmap & Future Development

### Phase 1: Complete Core Analytics (Current)
- [x] Points finish prediction model (84% accuracy achieved)
- [x] Pit strategy analysis framework
- [ ] Multi-race undercut/overcut success rate validation
- [ ] Post-pit position change supervised model

### Phase 2: Qualifying Analysis Module
- [ ] Grid vs race performance correlation modeling
- [ ] Qualifying position prediction from practice sessions
- [ ] Weather impact differential (qualifying vs race)

### Phase 3: Interactive Dashboard Development
- [ ] **Streamlit application** with dynamic driver/race selectors
- [ ] Real-time ML predictions for user scenarios
- [ ] Interactive strategy exploration tools
- [ ] Historical performance trend analysis

### Phase 4: Production Deployment
- [ ] **Docker containerization** for reproducible deployment
- [ ] **Cloud deployment** with automated data refresh pipeline
- [ ] **CI/CD integration** for continuous race data updates
- [ ] REST API development for external access

### Phase 5: Advanced Analytics
- [ ] Championship prediction modeling (season-long)
- [ ] Causal inference for strategy effectiveness
- [ ] Real-time race strategy recommendation system

---

## 📚 Documentation & Reproducibility

This project emphasizes:
- **Transparent methodology** with all analysis steps documented
- **Assumption testing** with explicit challenges to conventional wisdom
- **Reproducible results** through version-controlled code and clear documentation
- **Educational value** with commented code explaining domain-specific decisions

---

## 🤝 Contributing

This is primarily a portfolio project, but feedback on methodology, additional analyses, or code optimization is welcome. Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes with clear documentation
4. Submit a pull request with detailed description

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FastF1 community** for providing comprehensive, accessible F1 data
- **Formula 1** for inspiring data-driven sports analytics
- **Open source data science ecosystem** for tools and methodological guidance
- **Motorsport strategy experts** whose insights inform feature engineering approaches

---

## 📞 Contact

**[Vishwajith Somarampet]**  
📧 [vishwasomarampet029@gmail.com]  
💼 [LinkedIn Profile](https://www.linkedin.com/in/vishwajithsoma31/?trk=opento_sprofile_topcard)  
📱 [GitHub](https://github.com/Vishwajith31)

---

*Last Updated: August 2025*
  
