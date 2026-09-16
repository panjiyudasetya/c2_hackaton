---
id: confluence:898105355
source: confluence
type: page
space: TC
title: Original vs. Denormalized data model
author: Yaren Aslan
date: '2025-10-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/898105355
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/898105355
---
# Original vs. Denormalized data model

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/898105355  

## Content

**red**: fact tables

**blue**: dimension tables

# Original data model

* The way the tables and relationships stand in datamart
* Multiple star schemas for visit related data (Berth Visit, Terminal Visit, Port Visit levels)
* Power BI best practices require no active relationship between fact tables

**Pros**

* Everything belongs to the right level (port turnaround time in port visit table, berth stay in berth visit table)
* Aggregation with DAX is straightforward. It is easy to answer: “How many port visits were there?”, “What is the average terminal stay?”
* No unnecessary repetition of port visit level fields in other tables

**Cons**

* Need to use DAX for checking the relationship between fact tables

  + Which is hardly needed for PTO Terminals, only on the Visit Details page and when displaying a small number of visuals
* Difficult to filter lower granularity fact tables (port visit) by higher granularity dimensions (berths)
* Have high cardinality visit ID, terminal visit ID fields in all fact tables

# Denormalized data model

* Employed in PTO Ports dashboards
* One star for visit related data (Berth Visit, Terminal Visit, Port Visit levels are all joined in Berth Visit table)

Pros

* No need to use DAX for checking the relationship
* Easy to filter lower granularity fact tables (port visit) by higher granularity dimensions (berths)

Cons

* Aggregation is needed with DAX
* Unnecessary repetition of port visit level
* Takes longer to refresh (since Power Query manages merging)

# Summary of Pros and Cons

**Pros of Denormalizing into One Fact Table (at Detail Level)**

1. **Simplified Data Model**

* Easier to understand and maintain: fewer relationships and tables.
* Fewer joins in DAX or visuals, which can improve performance and reduce complexity.

2. **Better Performance (Sometimes)**

* Power BI’s VertiPaq engine compresses columns well in a wide, flat table.
* Avoids costly joins at query time (especially if the model previously relied on many-to-many or inactive relationships).

3. **No Relationship Ambiguity**

* Avoids potential confusion with directionality, inactive relationships, or relationship filtering.

4. **Easier Measures**

* Simpler DAX—everything’s in one table, so fewer need for RELATED() or LOOKUPVALUE().

5. **Consistent Granularity**

* You avoid mismatched granularity issues between header and detail tables.

**Cons of Denormalizing into One Fact Table**

1. **Larger Table Size**

* Can significantly increase the number of columns and rows (if headers repeat per line).
* Potentially worse compression if many repeated values are poorly encoded.

2. **Redundancy**

* Header-level data (Port Visit, Terminal Visit) is repeated for each line.
* This can increase file size and memory usage unnecessarily.

3. **Loss of Semantic Clarity**

* You lose the natural business meaning of header-level vs. detail-level data (it becomes difficult to answer: “How many port visits were there?”).
* Makes auditing and tracing data back to source systems more difficult.

4. **Complex Updates or Changes**

* If source systems change, it's harder to re-ingest just part of the data (e.g., just header info).
* ETL may need to do more work to combine header + detail cleanly. → at the moment, this is done by Power Query at import.

5. **Less Flexible Aggregation**

* With normalized header/detail, you can more easily do header-level aggregations (like invoice count) without counting lines or using DISTINCTCOUNT.