"""
Calculate Spatial Integration (Si), Social Networks Connectedness (Ni), and
Coupling Coordination Degree (CCD).

This script uses aggregate inputs. It does not require raw restricted data.
"""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def calculate_ccd(si: float, ni: float, alpha: float = 0.5, beta: float = 0.5) -> float:
    if pd.isna(si) or pd.isna(ni) or si < 0 or ni < 0 or si + ni == 0:
        return np.nan
    coupling = 2 * np.sqrt(si * ni) / (si + ni)
    coordination = alpha * si + beta * ni
    return np.sqrt(coupling * coordination)


def classify_regime(si: float, ni: float, si_threshold: float, ni_threshold: float) -> str:
    if pd.isna(si) or pd.isna(ni):
        return "Not classified"
    if si >= si_threshold and ni >= ni_threshold:
        return "High-Coupling"
    if si >= si_threshold and ni < ni_threshold:
        return "Social-Lagging"
    if si < si_threshold and ni >= ni_threshold:
        return "Spatial-Lagging"
    return "Low-Coupling"


def main() -> None:
    df = pd.read_csv(ROOT / "derived_data" / "si_ni_ccd_results.csv")

    si_col = "Si" if "Si" in df.columns else "S_i"
    ni_col = "Ni" if "Ni" in df.columns else "N_i"

    si_threshold = df[si_col].dropna().mean()
    ni_threshold = df[ni_col].dropna().mean()

    df["CCD_recalculated"] = df.apply(
        lambda row: calculate_ccd(row[si_col], row[ni_col]),
        axis=1,
    )
    df["regime_recalculated"] = df.apply(
        lambda row: classify_regime(row[si_col], row[ni_col], si_threshold, ni_threshold),
        axis=1,
    )

    df.to_csv(ROOT / "derived_data" / "si_ni_ccd_recalculated.csv", index=False)


if __name__ == "__main__":
    main()
