# Snack Batch Planner

**Person helped:** Ramesh Patel, snack stall owner — Hostel-A gate, Engineering College Campus.  
**Problem:** Ramesh fries fixed batches of samosas, puffs, and vada every morning regardless of the day. On slow days he discards 10–20 soggy pieces; on busy days (exams, cricket finals) he runs out before 2 PM and loses customers.  
**Date of fieldwork:** 8–11 November 2026.

---

## How to run

Python 3.9 or later required. No external packages needed.

```bash
# Navigate to the project folder
cd path/to/Snack-Batch-Planner

# Run the script
python3 snack_batch_planner.py
```

The script reads `data.csv` from the same folder and prints per-item recommendations to stdout.

---

## Real output (from the collected data)

```
====================================================
   Snack Batch Planner — Ramesh Patel's Stall   
====================================================

📦  PUFF
    Days observed       : 4
    Avg sold / day      : 36.0 pcs
    Avg wasted / day    : 11.5 pcs
    Suggested morning   : 45 pcs  (15% buffer, rounded to 5)

📦  SAMOSA
    Days observed       : 4
    Avg sold / day      : 52.5 pcs
    Avg wasted / day    : 0.0 pcs
    Suggested morning   : 65 pcs  (15% buffer, rounded to 5)

📦  VADA
    Days observed       : 4
    Avg sold / day      : 28.2 pcs
    Avg wasted / day    : 0.0 pcs
    Suggested morning   : 35 pcs  (15% buffer, rounded to 5)

====================================================
NOTE: On exam / event days add 20 % manually.
NOTE: Keep ~5 vada aside for the 3-4 PM warden window.
====================================================
```

---

## Algorithm

1. Load `data.csv`, validate every row (malformed rows skipped with a warning).  
2. For each **item type** (samosa / puff / vada), sum `sold` and `thrown` per day.  
3. Average daily sold quantity across all 4 observed days.  
4. Apply a **15 % safety buffer** (higher than a simple restocking tool because a stock-out here means a customer leaves the stall entirely with no alternative).  
5. Round **up** to the nearest **5 pieces** (practical frying batch unit).

---

## Feeding a bad row (for the interview)

Add a row with text where a number is expected, then re-run:

```
2026-11-12,10:00,samosa,abc,5,0,0,bad row
```

Output:

```
WARNING: Skipping malformed row 51 → {...} | invalid literal for int() with base 10: 'abc'
```

The script continues and uses the remaining valid rows.

---

## What it gets wrong

- **No unmet-demand tracking.** When samosas sell out, we can only count zero sold — not the 10 customers who walked away. The recommendation may still under-estimate on high-demand days.  
- **Puff waste is structural, not quantity-related.** Puffs go soft after 2 hours regardless of batch size. The real fix for puff waste is a smaller second batch at 1 PM, not a larger morning batch. The tool cannot model this split.  
- **Warden segment is invisible.** The 3–4 PM vada demand from hostel staff is a separate, predictable segment that the tool cannot distinguish from general demand. Manual override (`--5 vada reserved`) is needed.  
- **4-day sample.** A larger dataset covering different weeks, weather, and exam schedules would produce more reliable averages.  
- **No weather input.** Hot afternoons spike chai and cold-drink demand; snack demand drops slightly. The script does not know the temperature.

---

## Repository layout

```
├── README.md                    # This file
├── research.md                  # Problem, existing solutions, two verified sources
├── fieldwork.md                 # Photos, conversation with Ramesh, data-collection notes
├── data.csv                     # 50 rows of hourly per-item observations (4 days)
├── snack_batch_planner.py       # Core script
├── reflection.md                # Personal reflection (written without AI)
├── photo1.jpg                   # Stall at opening time, 10:15 AM 2026-11-10
├── photo2.jpg                   # Unsold soggy puffs at 3:50 PM 2026-11-10
├── .gitignore                   # Excludes demo video and system files
└── ai-chats/
    ├── conversation_log.md      # AI chat index and summary
    └── conversation_log.jsonl   # Full JSONL transcript of AI assistance
```

## Demo

▶️ **[Watch the 3-minute screen recording here](https://drive.google.com/your-demo-link)**  
*(Upload your screen recording to Google Drive or YouTube and replace the link above.)*

The demo shows:
- Running `python3 snack_batch_planner.py` on the actual `data.csv`
- The per-item recommendation explained
- Feeding a malformed row to demonstrate error handling
- Changing the `BUFFER` constant live from 15 % to 20 %

---

## Data collected by

Manoj Yadav — B.Tech student, Engineering College Campus.  
All rows in `data.csv` were recorded on-site in a pocket notebook and transferred to the CSV the same evening.
