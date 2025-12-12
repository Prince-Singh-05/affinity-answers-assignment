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

To count how many tiger types exists -

```
SELECT COUNT(*)
FROM taxonomy
WHERE tax_string LIKE '%Panthera tigris%';
```

**=> 0 tiger species exist in th etaxonomy table**

To get the ncbi_id of the Sumatran Tiger -

```
SELECT ncbi_id
FROM taxonomy
WHERE tax_string = '%Panthera tigris sumatrae%';
```

**=> The Sumatran Tiger (Panthera tigris sumatrae) is NOT present in the taxonomy table, so it has no ncbi_id in this dataset.**
