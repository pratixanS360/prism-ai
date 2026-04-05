## Plan: Krakow Preference Routing MVP

Build an end-to-end MVP in two stages: first a notebook-based prototype for fast algorithm validation, then a lightweight map app surface. The core engine will compute A→B routes on a Krakow road graph using weighted optimization that balances distance with preference scores (scenic, cafes, markets), where scenic supports multiple selectable strategies and POI preference maximizes nearby amenities while keeping routes reasonably short.

**Steps**
1. Phase 1: Foundation and Data
2. Define project structure and execution entrypoints (notebook-first), with clear folders for graph data cache, POI cache, routing engine, and map rendering. This unblocks all downstream implementation.
3. Build Krakow graph ingestion pipeline using OSMnx for full city boundary, with local caching and deterministic reload behavior. Store graph metadata and cache timestamp for reproducibility.
4. Build POI extraction pipeline for cafes and markets from OSM tags, index POIs spatially (Rtree/GeoPandas), and cache normalized features for route scoring. Depends on step 2.
5. Phase 2: Routing Engine and Preference Model
6. Define edge feature model and scoring contracts: base travel cost plus additive/multiplicative penalties/rewards for scenic and POI accessibility. Depends on steps 3-4.
7. Implement scenic as selectable strategies under one toggle family: green/parks proximity, quieter street classes, and optional elevation/view preference if data is available. Fallback safely when a strategy lacks data. Depends on step 6.
8. Implement cafes/markets objective as weighted maximization of nearby POI density while preserving route efficiency via bounded detour penalty. Depends on step 6.
9. Implement route solver wrapper (Dijkstra/A*) that accepts user toggles and weights, producing primary route and optional baseline shortest path for comparison. Depends on steps 7-8.
10. Phase 3: Notebook MVP and Map Output
11. Create notebook flow: choose A/B points, select toggles, run routing, render output map with route geometry and POI overlays, plus a small metrics panel (distance, estimated time, POI count, scenic score). Depends on step 9.
12. Add visual comparison mode in notebook (shortest vs preference route) to validate tradeoffs and tune default weights. Parallel with step 11 once core rendering exists.
13. Phase 4: Hardening and Handoff
14. Add automated tests for scoring and routing invariants (monotonicity, weight edge cases, no-route handling), plus fixture-based Krakow mini-graph tests for stable CI/runtime checks. Depends on step 9.
15. Add documentation for setup, data refresh, notebook usage, and preference semantics; include known limits and calibration guidance. Depends on steps 11-14.
16. Optional next increment (after MVP sign-off): expose notebook engine through a minimal web endpoint/UI without changing core routing modules. Depends on steps 1-15.

**Relevant files**
- /home/pratixan/Work/Personal/prism-ai/README.md — expand into architecture, setup, usage, and preference definitions.
- /home/pratixan/Work/Personal/prism-ai/requirements.txt — confirm/add runtime packages for notebook/app surface and testing.
- /home/pratixan/Work/Personal/prism-ai/src/config.py — Krakow boundary settings, cache paths, scoring defaults.
- /home/pratixan/Work/Personal/prism-ai/src/data/graph_loader.py — OSMnx graph ingestion and caching.
- /home/pratixan/Work/Personal/prism-ai/src/data/poi_loader.py — POI fetch/normalize/index pipeline.
- /home/pratixan/Work/Personal/prism-ai/src/routing/scoring.py — edge and route scoring logic.
- /home/pratixan/Work/Personal/prism-ai/src/routing/solver.py — weighted shortest-path wrapper and route outputs.
- /home/pratixan/Work/Personal/prism-ai/src/visualization/map_renderer.py — route/POI map rendering.
- /home/pratixan/Work/Personal/prism-ai/notebooks/krakow_route_mvp.ipynb — notebook-first interactive workflow.
- /home/pratixan/Work/Personal/prism-ai/tests/test_scoring.py — scoring correctness tests.
- /home/pratixan/Work/Personal/prism-ai/tests/test_solver.py — routing behavior tests.

**Verification**
1. Data validation: confirm graph and POI caches are created for Krakow and reload without network on second run.
2. Functional checks: for identical A/B points, verify toggles produce route changes consistent with objective (shortest vs scenic vs POI-leaning).
3. Metric checks: verify distance increase remains within configured detour tolerance for POI/scenic modes.
4. Edge-case checks: invalid coordinates, disconnected components, and empty POI neighborhoods return controlled errors/fallbacks.
5. Test suite: run unit tests for scoring/solver plus one notebook smoke run from clean environment.

**Decisions**
- Included scope: End-to-end MVP for Krakow with A→B routing, notebook-first interface, simple preference toggles, and weighted optimization.
- Scenic decision: implement multiple scenic strategy options as selectable/scorable features under scenic preference.
- POI decision: maximize nearby cafes/markets while constraining excessive detours.
- Excluded from MVP: production-grade frontend, multi-stop routing/TSP, real-time traffic integration, and guaranteed pass-through POI sequencing.

**Further Considerations**
1. Decide initial default weights for scenic/cafe/market preferences (recommend conservative defaults to keep detours modest).
2. Decide whether elevation-based scenic mode is included in MVP or deferred behind optional data availability.
3. Decide whether walking or driving network is the primary default mode for first benchmark results.
