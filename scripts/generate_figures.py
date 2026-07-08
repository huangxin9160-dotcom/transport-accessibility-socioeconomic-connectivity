"""
Generate simple example plots from figure source data.

This script is provided to show the figure-data workflow. Final journal figures may
require additional cartographic processing.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def plot_si_ni() -> None:
    df = pd.read_csv(ROOT / "derived_data" / "si_ni_ccd_results.csv")
    si_col = "Si" if "Si" in df.columns else "S_i"
    ni_col = "Ni" if "Ni" in df.columns else "N_i"
    df = df.dropna(subset=[si_col, ni_col])

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(df[si_col], df[ni_col])
    ax.set_xlabel("Spatial Integration (Si)")
    ax.set_ylabel("Social Networks Connectedness (Ni)")

    for _, row in df.iterrows():
        ax.text(row[si_col], row[ni_col], row["agglomeration_id"], fontsize=7)

    fig.tight_layout()
    fig.savefig(ROOT / "derived_data" / "example_si_ni_plot.pdf")
    plt.close(fig)


def plot_cr5_change() -> None:
    df = pd.read_csv(ROOT / "derived_data" / "cr5_2000_2020_results.csv")
    df = df.dropna(subset=["CR5_2000", "CR5_2020"])

    if df.empty:
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df["agglomeration_id"], df["CR5_2000"], marker="o", label="2000")
    ax.plot(df["agglomeration_id"], df["CR5_2020"], marker="o", label="2020")
    ax.set_ylabel("CR5")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(ROOT / "derived_data" / "example_cr5_change.pdf")
    plt.close(fig)


if __name__ == "__main__":
    plot_si_ni()
    plot_cr5_change()
