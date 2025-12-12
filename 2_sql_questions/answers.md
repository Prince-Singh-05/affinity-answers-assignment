## Problem Statement - SQL Questions

The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: https://docs.rfam.org/en/latest/database.html

1. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
2. Find all the columns that can be used to connect the tables in the given database.
3. Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)
4. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

## Run the Rfam Public Database locally

```
mysql --user rfamro --host mysql-rfam-public.ebi.ac.uk --port 4497 --database Rfam
```

### 1. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)

- **To count how many tiger types exists -**

  **SQL Query**

  ```sql
  SELECT COUNT(*)
  FROM taxonomy
  WHERE tax_string LIKE '%Panthera tigris%';
  ```

  **=> 0 tiger species exist in th etaxonomy table**

- **To get the ncbi_id of the Sumatran Tiger -**

  **SQL Query**

  ```sql
  SELECT ncbi_id
  FROM taxonomy
  WHERE tax_string = '%Panthera tigris sumatrae%';
  ```

  **=> The Sumatran Tiger (Panthera tigris sumatrae) is NOT present in the taxonomy table, so it has no ncbi_id in this dataset.**

### 2. Find all the columns that can be used to connect the tables in the given database.

**Key Join Columns in the Rfam Database**

| Column Name             | Tables Appearing In                                       | Purpose / Relation                                                                      |
| ----------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **`taxid` / `ncbi_id`** | `taxonomy`, `rfamseq`, `full_region`, `genome`            | Connects RNA sequences and families to their corresponding taxonomic classification.    |
| **`rfam_acc`**          | `family`, `full_region`, `seed_region`, `clan_membership` | Primary key for each RNA family; used to join family definitions with sequence regions. |
| **`rfam_id`**           | `family`, `clan`                                          | Human-friendly family identifier; alternative join with `family` table.                 |
| **`rfamseq_acc`**       | `rfamseq`, `full_region`, `seed_region`                   | Accession number for each RNA sequence; joins sequence metadata with regions.           |
| **`clan_acc`**          | `clan`, `clan_membership`                                 | Connects clans with the families belonging to them.                                     |
| **`genome_id`**         | `genome`, `genome_full_region`                            | Joins genomes with full sequence region mappings.                                       |
| **`motif_acc`**         | `motif`, `motif_match`                                    | Connects motifs to matching genomic regions.                                            |
| **`wgs_acc`**           | `wgs`, `rfamseq`                                          | Links Whole Genome Shotgun (WGS) assemblies with rfamseq entries.                       |

---

**Summary**

The most commonly used join keys across Rfam tables are:

- **`rfam_acc`** — connects RNA families
- **`rfamseq_acc`** — connects RNA sequences
- **`taxid` / `ncbi_id`** — links sequences to taxonomy
- **`clan_acc`** — connects families to clans
- **`genome_id`** — connects genomic region tables
- **`motif_acc`** — connects motifs with matching sequences

These columns form the backbone of the schema and allow querying relationships between sequences, families, taxonomy, genomes, and motifs.

### 3. Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)

To determine which rice species has the longest DNA sequence, we need to join:

- `rfamseq` → contains sequence lengths (`length`) and taxonomy reference (`taxid`)
- `taxonomy` → contains species names (`species`, `tax_string`)

We filter for rice by matching `"Oryza"` in the taxonomy.

**SQL Query**

```sql
SELECT
    t.species AS rice_species,
    MAX(r.length) AS longest_sequence_length
FROM rfamseq r
JOIN taxonomy t
    ON r.taxid = t.ncbi_id
WHERE t.tax_string LIKE '%Oryza%'
GROUP BY t.species
ORDER BY longest_sequence_length DESC
LIMIT 1;
```
