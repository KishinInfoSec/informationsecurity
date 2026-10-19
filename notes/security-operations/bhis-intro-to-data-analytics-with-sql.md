---
title: bhis-intro-to-data-analytics-with-sql
tags: [security-operations, type/cheatsheet, phase/detection, source/bhis]
description: "BHIS webcast: exploratory data analysis for security logs with SQL and DuckDB: SELECT, GROUP BY, window functions, joins."
source_pdf: BHIS_PRESENTATION_Intro to Data Analytics using SQL w Ethan Robish.pdf
---

# Intro to Data Analytics Using SQL

Hands-on SQL for security data (honeypot logs, firewall logs, enrichment). The examples run in DuckDB directly against a CSV, so there is no database to set up.

## Background

- SQL statement families: DDL (CREATE, DROP, ALTER, TRUNCATE), DQL (SELECT), DML (INSERT, UPDATE, DELETE), DCL (GRANT, REVOKE), TCL (COMMIT, ROLLBACK).
- SQL is declarative (say what you want), ISO/ANSI standard, great for aggregations and joins, but not a general programming language.
- **OLTP** (normalized, row store, fast single-record updates: MSSQL, MariaDB, Postgres, SQLite) versus **OLAP** (denormalized, columnar, big aggregations: ClickHouse, DuckDB, Spark, Snowflake). Log analytics belongs on the OLAP side.
- Format queries on multiple lines with uppercase keywords for readability.

## Dataset used

Honeypot network data from 2013 (`marx-geo.csv`: timestamp, host, protocol, source IP, destination port, geolocation; about 451k rows). Cleaned with a one-line `sed` replace before loading.

## Exploration commands

```sql
SELECT * FROM 'marx-geo.csv' LIMIT 8;          -- peek
DESCRIBE SELECT * FROM 'marx-geo.csv';         -- column types
SUMMARIZE SELECT * FROM 'marx-geo.csv';        -- min/max/unique/null stats
SELECT * FROM read_csv('flights.csv', union_by_name = true);  -- tune the reader; same for read_json
```

## SELECT toolbox

```sql
SELECT 'literal' AS msg;                        -- aliases
SELECT count(*) FROM t;                         -- total rows
SELECT DISTINCT srcstr, dpt FROM t;
SELECT * EXCLUDE (type, datetime) FROM t;       -- DuckDB: drop columns
SELECT a + b AS sum FROM t;                     -- runtime math
FROM tbl;                                       -- DuckDB: FROM-first syntax
```

- `ORDER BY datetime DESC` for newest first; multi-level sorts supported.
- `WHERE` with `AND`/`OR`/`NOT`, `IN (135, 137, 445)`, `BETWEEN 1 AND 1025`, and `BETWEEN` on timestamps. Strings use single quotes.
- Aggregates: `min`, `max`, `count`, `avg`, `sum`. Non-aggregated columns need `GROUP BY` (DuckDB also supports `GROUP BY ALL`).
- Filter aggregates with `HAVING` (not `WHERE`):

```sql
SELECT host, count(*) AS cnt FROM 'marx-geo.csv'
GROUP BY ALL HAVING cnt > 100000;
```

- Remember the logical execution order (FROM, WHERE, GROUP BY, HAVING, window, SELECT, ORDER BY, LIMIT), which explains why aliases do not work in WHERE.

## Window functions

- Form: `function(expr) OVER (PARTITION BY ... ORDER BY ... ROWS frame)`. Partitions are independent windows; the frame slides within them.
- Running total per host: `sum(spt) OVER (PARTITION BY host ORDER BY datetime ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`.
- Rolling average over the last three rows: `avg(val) OVER frame` with `WINDOW frame AS (ROWS 2 PRECEDING)`.
- Percent of whole: `count(*) * 100.0 / sum(count(*)) OVER () AS pct` with `GROUP BY country`.
- You cannot filter window results with WHERE or HAVING. Use a CTE or subquery, or DuckDB's `QUALIFY pct > 10`.

## Joins and enrichment

- Joins combine tables, reduce rows using another table, or create combinations. `INNER` and `OUTER` are optional keywords; also LEFT, RIGHT, FULL, CROSS (Cartesian), NATURAL, POSITIONAL, SEMI, ANTI, ASOF, LATERAL.
- Enrichment example: join honeypot rows to the IANA service-name table on protocol and port to label each destination port with a service and description.

## Defender/Attacker takeaways

- Defender: DuckDB on exported logs is a fast way to baseline, count by host or country, find rare values (`ORDER BY cnt ASC`) and compute percentages without a SIEM.
- Defender: enrich with lookup tables (service names, allow lists, threat intel) using joins.
- Attacker note: unusual-port, low-count rows are what hunters look for; blending into the top talkers is a classic evasion.

## Source

BHIS webcast "Intro to Data Analytics using SQL" by Ethan Robish (BHIS SOC, threat hunting and detection engineering). Date not shown in the deck.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-data-sources]]
- [[threat-hunting-research/data-management-and-processing]]
- [[hacking-cheat-sheets/sql-injection-cheat-sheet]]
- [[enumeration/protocols-and-ports/3306-mysql]]
