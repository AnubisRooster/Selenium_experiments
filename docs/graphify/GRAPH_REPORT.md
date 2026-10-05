# Graph Report - Selenium_experiments  (2026-10-05)

## Corpus Check
- Corpus is ~14,045 words - fits in a single context window. You may not need a graph.

## Summary
- 34 nodes · 32 edges · 4 communities (0 shown, 4 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- TestFree

## God Nodes (most connected - your core abstractions)
1. `TestFree` - 4 edges
2. `Self-contained graphify pipeline for CI. Builds a knowledge graph over this…` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 4 thin omitted)

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestFree` connect `TestFree` to `test_free.py`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Should `graphify_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._