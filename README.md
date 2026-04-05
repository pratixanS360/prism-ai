# prism-ai

Preference-based path optimization routing system focused on A->B routing in Krakow with user preferences (scenic, cafes, markets).

## Current Status

Step 1 (project scaffolding) is complete.

Implemented in this step:
- Source package layout under `src/`
- Shared configuration in `src/config.py`
- Notebook and test folders
- Cache directory placeholder under `data/cache/`

## Project Structure

```text
prism-ai/
├── data/
│   └── cache/
├── notebooks/
├── src/
│   ├── config.py
│   ├── data/
│   ├── routing/
│   └── visualization/
├── tests/
├── plan.md
├── requirements.txt
└── README.md
```

## Quick Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The central configuration module is `src/config.py`.

It currently defines:
- Krakow defaults (`KRAKOW_PLACE_NAME`, `KRAKOW_CENTER`)
- Canonical cache paths via `get_paths()`
- MVP baseline routing defaults via `DEFAULT_ROUTING`

## Next Step

Implement graph ingestion and caching for Krakow in `src/data/graph_loader.py`.
