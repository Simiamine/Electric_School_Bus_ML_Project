import pandas as pd
from sklearn.preprocessing import StandardScaler

def select_relevant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Garde les colonnes utiles pour l’analyse non supervisée."""
    # 🔧 Nettoyage des noms de colonnes : suppression des espaces
    df.columns = df.columns.str.strip()

    selected_cols = {
        "1a. State": "state",
        "1c. LEA ID": "lea_id",
        "1o. Locale broad type (number)": "locale_type",
        "3a. Number of ESBs committed": "esb_committed",
        "3b. Number of delivered or operating ESBs": "esb_operating",
        "3i. Percent of fleet that is electric": "percent_fleet_electric",
        "4b. Number of students in district": "nb_students",
        "4d. Percentage of schools in district that are Title I schoolwide eligible": "pct_title_1",
        "4e. Percentage of students in district eligible for free or reduced price lunch": "pct_free_lunch",
        "4f. Median household income": "median_income",
        "4g. Percent of population below the poverty level": "pct_poverty",
        "5f. PM2.5 concentration": "pm25",
        "5h. Ozone concentration": "ozone",
        "5l. Average rate of asthma among adults aged 18 and older": "asthma_rate"
    }

    df_clean = df[list(selected_cols.keys())].rename(columns=selected_cols)
    return df_clean


def clean_and_impute(df: pd.DataFrame) -> pd.DataFrame:
    """Remplit les valeurs manquantes avec la moyenne et encode les catégories."""
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

    # 🧼 Remplir les NaN numériques avec la moyenne
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # 🧼 Valeur par défaut pour les catégories (ex : locale_type)
    if "locale_type" in df.columns:
        df["locale_type"] = df["locale_type"].fillna(-1)

    return df


def normalize_features(df: pd.DataFrame) -> pd.DataFrame:
    """Normalise les colonnes numériques pour le clustering."""
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)

    # 🏷️ Ajouter la colonne de catégorie (non normalisée)
    if "locale_type" in df.columns:
        df_scaled["locale_type"] = df["locale_type"].values

    return df_scaled


def prepare_district_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Pipeline complet pour préparer les données district-level."""
    df_selected = select_relevant_columns(df_raw)
    df_cleaned = clean_and_impute(df_selected)
    df_ready = normalize_features(df_cleaned)
    return df_ready