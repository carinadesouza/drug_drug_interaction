"""
config.py — Central configuration for the DDI NLP Project.

All paths, hyperparameters, and label definitions are defined here.
Import this file at the top of every notebook:

    import sys, os
    sys.path.insert(0, os.path.abspath('../..'))   # adjust depth if needed
    from config import *
"""

import os
from pathlib import Path

# ══════════════════════════════════════════════════════════════════
#  ROOT
# ══════════════════════════════════════════════════════════════════
PROJECT_ROOT = Path(__file__).resolve().parent

# ══════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════
DATA_DIR           = PROJECT_ROOT / 'data'
RAW_DIR            = DATA_DIR / 'raw' / 'DDICorpus-2013'
RAW_TRAIN_DIR      = RAW_DIR / 'Train'
RAW_TEST_DIR       = RAW_DIR / 'Test'

PROCESSED_DIR      = DATA_DIR / 'processed'  
TRAIN_CSV          = str(PROCESSED_DIR / 'train.csv')
TEST_CSV           = str(PROCESSED_DIR / 'test.csv')
TRAIN_PROCESSED    = str(PROCESSED_DIR / 'train_processed.csv')
TEST_PROCESSED     = str(PROCESSED_DIR / 'test_processed.csv')

# ══════════════════════════════════════════════════════════════════
#  FEATURES  (pkl / npz / npy artefacts — NOT inside data/)
# ══════════════════════════════════════════════════════════════════
FEATURES_DIR            = PROJECT_ROOT / 'features'
FEATURES_MATRICES_DIR   = FEATURES_DIR / 'matrices'      # .npz / .npy
FEATURES_ARTEFACTS_DIR  = FEATURES_DIR / 'artefacts'     # .pkl (encoder, vectoriser, names)

TRAIN_FEATURES_NPZ      = str(FEATURES_MATRICES_DIR / 'train_features.npz')
TEST_FEATURES_NPZ       = str(FEATURES_MATRICES_DIR / 'test_features.npz')
Y_TRAIN_NPY             = str(FEATURES_MATRICES_DIR / 'y_train.npy')
Y_TEST_NPY              = str(FEATURES_MATRICES_DIR / 'y_test.npy')

TFIDF_VECTORISER_PKL    = str(FEATURES_ARTEFACTS_DIR / 'tfidf_vectoriser.pkl')
LABEL_ENCODER_PKL       = str(FEATURES_ARTEFACTS_DIR / 'label_encoder.pkl')
FEATURE_NAMES_PKL       = str(FEATURES_ARTEFACTS_DIR / 'feature_names.pkl')

# ══════════════════════════════════════════════════════════════════
#  MODELS  (transformer weights only — classical PKLs go to features/)
# ══════════════════════════════════════════════════════════════════
MODELS_DIR          = PROJECT_ROOT / 'models'
BIOBERT_DIR         = str(MODELS_DIR / 'biobert')
PUBMEDBERT_DIR      = str(MODELS_DIR / 'pubmedbert')
SCIBERT_DIR         = str(MODELS_DIR / 'scibert')
MODELS_SHARED_DIR   = str(MODELS_DIR / 'shared')   # y_test.npy, label2id.json

# Prediction arrays saved inside each model's own folder
BIOBERT_PREDS_NPY     = str(MODELS_DIR / 'biobert'    / 'biobert_predictions.npy')
PUBMEDBERT_PREDS_NPY  = str(MODELS_DIR / 'pubmedbert' / 'pubmedbert_predictions.npy')
SCIBERT_PREDS_NPY     = str(MODELS_DIR / 'scibert'    / 'scibert_predictions.npy')

# ══════════════════════════════════════════════════════════════════
#  RESULTS
# ══════════════════════════════════════════════════════════════════
RESULTS_DIR         = PROJECT_ROOT / 'results'

# metrics sub-folders (one per notebook phase that saves CSVs)
METRICS_DIR             = RESULTS_DIR / 'metrics'
METRICS_EDA_DIR         = METRICS_DIR / 'eda'
METRICS_BASELINE_DIR    = METRICS_DIR / 'baseline'
METRICS_COMPARISON_DIR  = METRICS_DIR / 'comparison'

# plots sub-folders (one per notebook phase that saves figures)
PLOTS_DIR               = RESULTS_DIR / 'plots'
PLOTS_EDA_DIR           = PLOTS_DIR / 'eda'
PLOTS_BASELINE_DIR      = PLOTS_DIR / 'baseline'
PLOTS_BIOBERT_DIR       = PLOTS_DIR / 'biobert'
PLOTS_PUBMEDBERT_DIR    = PLOTS_DIR / 'pubmedbert'
PLOTS_SCIBERT_DIR       = PLOTS_DIR / 'scibert'
PLOTS_COMPARISON_DIR    = PLOTS_DIR / 'comparison'

# ── Specific output file paths ────────────────────────────────────
EDA_CLASS_SUMMARY_CSV   = str(METRICS_EDA_DIR  / 'eda_class_summary.csv')
EDA_SOURCE_SUMMARY_CSV  = str(METRICS_EDA_DIR  / 'eda_source_summary.csv')

BASELINE_RESULTS_CSV    = str(METRICS_BASELINE_DIR   / 'results_summary.csv')
BASELINE_HANDOFF_CSV    = str(METRICS_BASELINE_DIR   / 'phase5_handoff.csv')

BIOBERT_RESULTS_CSV     = str(METRICS_COMPARISON_DIR / 'biobert_results.csv')
PUBMEDBERT_RESULTS_CSV  = str(METRICS_COMPARISON_DIR / 'pubmedbert_results.csv')
SCIBERT_RESULTS_CSV     = str(METRICS_COMPARISON_DIR / 'scibert_results.csv')
FULL_COMPARISON_CSV     = str(METRICS_COMPARISON_DIR / 'full_comparison.csv')
STATISTICAL_TESTS_CSV   = str(METRICS_COMPARISON_DIR / 'statistical_tests.csv')

# ══════════════════════════════════════════════════════════════════
#  LABEL DEFINITIONS  (shared across all phases)
# ══════════════════════════════════════════════════════════════════
LABEL_ORDER = ['false', 'effect', 'mechanism', 'advise', 'int']
LABEL2ID    = {'advise': 0, 'effect': 1, 'false': 2, 'int': 3, 'mechanism': 4}
ID2LABEL    = {v: k for k, v in LABEL2ID.items()}
NUM_LABELS  = 5
VALID_LABELS = frozenset({'false', 'effect', 'mechanism', 'advise', 'int'})

# ══════════════════════════════════════════════════════════════════
#  REPRODUCIBILITY
# ══════════════════════════════════════════════════════════════════
RANDOM_STATE = 42

# ══════════════════════════════════════════════════════════════════
#  PREPROCESSING  (Phase 3)
# ══════════════════════════════════════════════════════════════════
PREPROCESS_BATCH_SIZE  = 64
PREPROCESS_PROGRESS_N  = 500
FLAG_SELF_PAIRS        = True

# ══════════════════════════════════════════════════════════════════
#  FEATURE EXTRACTION  (Phase 4)
# ══════════════════════════════════════════════════════════════════
MAX_TFIDF_FEATURES = 5000
FILTER_SELF_PAIRS  = True

# ══════════════════════════════════════════════════════════════════
#  CLASSICAL MODELS  (Phase 5)
# ══════════════════════════════════════════════════════════════════
CV_FOLDS      = 5

SVM_C         = 0.5
SVM_MAX_ITER  = 3000

LR_C          = 1.0
LR_MAX_ITER   = 1000

RF_N_ESTIMATORS = 200
RF_MAX_DEPTH    = 20

NB_ALPHA      = 0.1

BENCHMARK_MIN    = 0.55
BENCHMARK_TARGET = 0.60
BENCHMARK_MAX    = 0.65

# ══════════════════════════════════════════════════════════════════
#  TRANSFORMER MODELS  (Phase 6)
# ══════════════════════════════════════════════════════════════════
BIOBERT_MODEL_ID    = 'dmis-lab/biobert-base-cased-v1.2'
PUBMEDBERT_MODEL_ID = 'microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract'
SCIBERT_MODEL_ID    = 'allenai/scibert_scivocab_cased'

TRANSFORMER_MAX_LEN    = 128
TRANSFORMER_BATCH_SIZE = 16
TRANSFORMER_EPOCHS     = 4
TRANSFORMER_LR         = 2e-5
TRANSFORMER_WARMUP     = 0.1
TRANSFORMER_WD         = 0.01
USE_DRUG_MASKING       = True

# ══════════════════════════════════════════════════════════════════
#  VISUALISATION COLOURS  (shared across all phases)
# ══════════════════════════════════════════════════════════════════
LABEL_COLOURS = {
    'false':     '#888780',
    'effect':    '#378ADD',
    'mechanism': '#7F77DD',
    'advise':    '#EF9F27',
    'int':       '#D85A30',
}
MODEL_COLOURS = {
    'Rule-based':          '#B4B2A9',
    'Naive Bayes':         '#9FE1CB',
    'Logistic Regression': '#FAC775',
    'Random Forest':       '#7F77DD',
    'Linear SVM':          '#378ADD',
    'BioBERT':             '#1D9E75',
    'PubMedBERT':          '#EF9F27',
    'SciBERT':             '#D85A30',
}

# ══════════════════════════════════════════════════════════════════
#  DIRECTORY CREATION  — run once on import
# ══════════════════════════════════════════════════════════════════
_dirs_to_create = [
    PROCESSED_DIR,
    FEATURES_MATRICES_DIR,
    FEATURES_ARTEFACTS_DIR,
    MODELS_DIR / 'biobert',
    MODELS_DIR / 'pubmedbert',
    MODELS_DIR / 'scibert',
    MODELS_DIR / 'shared',
    METRICS_EDA_DIR,
    METRICS_BASELINE_DIR,
    METRICS_COMPARISON_DIR,
    PLOTS_EDA_DIR,
    PLOTS_BASELINE_DIR,
    PLOTS_BIOBERT_DIR,
    PLOTS_PUBMEDBERT_DIR,
    PLOTS_SCIBERT_DIR,
    PLOTS_COMPARISON_DIR,
]

for _d in _dirs_to_create:
    Path(_d).mkdir(parents=True, exist_ok=True)
