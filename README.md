# COI-detector

Find out the PC Member with possible COI based on data source of dblp bibliography.

## How to use

1. Crawling PC member list from conference manager system (e.g., softconf, CMT, etc.)

A simple script is provided. You can use it to crawl PC member list from CMT system (customized for ICASSP conference).
You can also write your own crawler to fetch PC member list from other conference manager system.

```bash
python3 crawler_ICASSP23.py
```

2. Running COI-detector

```bash
python3 check.py --pc_list pc_list.txt --output coi.txt --dblp_id 233/1228
```
