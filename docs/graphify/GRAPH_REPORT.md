# Graph Report - Selenium_experiments  (2026-09-28)

## Corpus Check
- Corpus is ~14,045 words - fits in a single context window. You may not need a graph.

## Summary
- 34 nodes · 32 edges · 4 communities (3 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- graphify_pipeline.py
- test_free.py
- Bot.py
- TestFree

## God Nodes (most connected - your core abstractions)
1. `TestFree` - 4 edges
2. `Self-contained graphify pipeline for CI. Builds a knowledge graph over this…` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 1 thin omitted)

### Community 0 - "graphify_pipeline.py"
Cohesion: 0.14
Nodes (12): graphify_analyze, graphify_build, graphify_cluster, graphify_detect, graphify_export, graphify_extract, graphify_llm, graphify_report (+4 more)

### Community 1 - "test_free.py"
Cohesion: 0.17
Nodes (11): json, pytest, selenium, selenium_webdriver_common_action_chains, selenium_webdriver_common_by, selenium_webdriver_common_desired_capabilities, selenium_webdriver_common_keys, selenium_webdriver_support (+3 more)

### Community 2 - "Bot.py"
Cohesion: 0.50
Nodes (3): csv, random, tweepy

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestFree` connect `TestFree` to `test_free.py`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Should `graphify_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._