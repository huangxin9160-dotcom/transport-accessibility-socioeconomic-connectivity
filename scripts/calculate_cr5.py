"""
Calculate CR5 from weighted node strength.

CR5 is the share of total socioeconomic flow captured by the five strongest nodes within
an urban agglomeration.
"""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def calculate_node_strength(edge_list: pd.DataFrame) -> pd.DataFrame:
    out_strength = edge_list.groupby("origin_city")["composite_weight"].sum()
    in_strength = edge_list.groupby("destination_city")["composite_weight"].sum()

    strength = pd.concat([out_strength, in_strength], axis=1).fillna(0)
    strength.columns = ["out_strength", "in_strength"]
    strength["node_strength"] = strength["out_strength"] + strength["in_strength"]
    return strength.rename_axis("city").reset_index()


def calculate_cr5(node_strength: pd.DataFrame, top_n_nodes: int = 5) -> float:
    total = node_strength["node_strength"].sum()
    if total == 0:
        return 0.0
    top_nodes = node_strength.sort_values("node_strength", ascending=False).head(top_n_nodes)
    return top_nodes["node_strength"].sum() / total


if __name__ == "__main__":
    edges_path = ROOT / "derived_data" / "composite_network_sample.csv"
    if not edges_path.exists():
        raise FileNotFoundError(
            "Run scripts/build_composite_network.py before calculating CR5."
        )

    edges = pd.read_csv(edges_path)
    strength = calculate_node_strength(edges)
    cr5 = calculate_cr5(strength)

    strength.to_csv(ROOT / "derived_data" / "node_strength_sample.csv", index=False)
    pd.DataFrame({"CR5": [cr5]}).to_csv(ROOT / "derived_data" / "cr5_sample.csv", index=False)
