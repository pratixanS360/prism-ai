"""Project-level configuration for the Krakow routing MVP."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# Krakow city center point (lat, lon) used for map defaults.
KRAKOW_CENTER = (50.0614, 19.9366)
KRAKOW_PLACE_NAME = "Krakow, Poland"


@dataclass(frozen=True)
class Paths:
    """Filesystem paths used by the project."""

    repo_root: Path
    data_dir: Path
    cache_dir: Path
    graphml_path: Path
    poi_cache_path: Path


def get_paths() -> Paths:
    """Return canonical repository paths relative to this file."""
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "data"
    cache_dir = data_dir / "cache"
    return Paths(
        repo_root=repo_root,
        data_dir=data_dir,
        cache_dir=cache_dir,
        graphml_path=cache_dir / "krakow.graphml",
        poi_cache_path=cache_dir / "krakow_poi.parquet",
    )


@dataclass(frozen=True)
class RoutingDefaults:
    """Baseline routing weights used in the MVP."""

    scenic_weight: float = 0.2
    cafe_weight: float = 0.2
    market_weight: float = 0.2
    max_detour_ratio: float = 1.35


DEFAULT_ROUTING = RoutingDefaults()
