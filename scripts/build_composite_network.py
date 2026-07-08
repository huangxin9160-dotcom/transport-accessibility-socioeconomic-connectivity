"""
Build a composite socioeconomic network from mobility and corporate investment flows.

Inputs:
- data_sample/mobility_flow_sample.csv
- data_sample/investment_flow_sample.csv

Outputs:
- composite edge list with normalized mobility, normalized investment and combined edge weight.

Raw mobile phone signalling data and raw corporate registration records are not included because
of third-party licensing and privacy restrictions.
"""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def minmax_normalize(series: pd.Series) -> pd.Series:
    series = series.fillna(0)
    span = series.max() - series.min()
    if span == 0:
        return series * 0
    return (series - series.min()) / span


def build_composite_network(mobility_path: Path, investment_path: Path, output_path: Path) -> None:
    mobility = pd.read_csv(mobility_path)
    investment = pd.read_csv(investment_path)

    df = mobility.merge(
        investment,
        on=["origin_city", "destination_city", "year"],
        how="outer",
    ).fillna(0)

    df["mobility_norm"] = minmax_normalize(df["mobility_flow"])
    df["investment_norm"] = minmax_normalize(df["investment_flow"])
    df["composite_weight"] = 0.5 * df["mobility_norm"] + 0.5 * df["investment_norm"]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    build_composite_network(
        ROOT / "data_sample" / "mobility_flow_sample.csv",
        ROOT / "data_sample" / "investment_flow_sample.csv",
        ROOT / "derived_data" / "composite_network_sample.csv",
    )
