"""
snack_batch_planner.py
----------------------
Reads data.csv (collected at Ramesh Patel's snack stall, Hostel-A gate) and
recommends how many pieces of each snack type (samosa / puff / vada) to fry
each morning to minimise waste while avoiding stock-outs.

Problem
-------
Ramesh fries three items every morning in fixed batches (30 samosas, 30 puffs,
20 vada) regardless of the day. Some items sell out early (lost sales); others
go soggy within 2 hours and must be discarded (direct cost loss).

Algorithm
---------
For each item type:
  1. Load all rows where batch_fried > 0 (new batch events only).
  2. Compute SOLD across the full day for that item.
  3. Compute THROWN (wasted) across the full day for that item.
  4. Net useful output = sold + carry_over at day-end (carry_over that was
     eventually sold the next slot does not count as waste but also not as
     a certain sale — we conservatively ignore it).
  5. Average daily sold quantity per item over all observed days.
  6. Add a 15 % buffer (higher than milk because stock-outs here directly lose
     customers — a person who cannot get a samosa leaves entirely).
  7. Round UP to the nearest 5 pieces (practical frying batch size).

Limitations
-----------
- Does not capture unmet demand (we cannot count the customers who turned away
  when samosas ran out).
- The warden's 3-4 PM vada demand is a separate segment not modelled here;
  Ramesh should manually reserve ~5 vada for that window.
- Puff waste is high because they go soft after 2 hours; a better fix would be
  a smaller second batch at 1 PM rather than a larger morning batch.
- 4 days is a small sample; exam days skew the average upward.
"""

import csv
import sys
import math
from pathlib import Path
from collections import defaultdict

REQUIRED_COLUMNS = {
    'date', 'time', 'item',
    'batch_fried', 'sold', 'thrown', 'carry_over'
}
BUFFER = 1.15        # 15 % safety buffer
ROUND_TO = 5         # round up to nearest 5 pieces


def load_data(csv_path: Path) -> list[dict]:
    """Load and validate every row from data.csv."""
    rows = []
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            print(f"ERROR: CSV missing required columns: {missing}", file=sys.stderr)
            sys.exit(1)

        for i, r in enumerate(reader, start=2):
            try:
                batch_fried  = int(r['batch_fried'])
                sold         = int(r['sold'])
                thrown       = int(r['thrown'])
                carry_over   = int(r['carry_over'])

                if any(v < 0 for v in [batch_fried, sold, thrown, carry_over]):
                    raise ValueError("Counts cannot be negative")

                rows.append({
                    'date':        r['date'].strip(),
                    'time':        r['time'].strip(),
                    'item':        r['item'].strip().lower(),
                    'batch_fried': batch_fried,
                    'sold':        sold,
                    'thrown':      thrown,
                    'carry_over':  carry_over,
                })
            except (ValueError, KeyError) as e:
                print(f"WARNING: Skipping malformed row {i} → {dict(r)} | {e}",
                      file=sys.stderr)
    return rows


def daily_sold_per_item(rows: list[dict]) -> dict[str, dict[str, int]]:
    """
    Returns { item: { date: total_sold } }
    """
    result: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in rows:
        result[r['item']][r['date']] += r['sold']
    return result


def daily_thrown_per_item(rows: list[dict]) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in rows:
        result[r['item']][r['date']] += r['thrown']
    return result


def suggest_batch(avg_sold: float) -> int:
    """Apply buffer and round UP to nearest ROUND_TO pieces."""
    buffered = avg_sold * BUFFER
    return math.ceil(buffered / ROUND_TO) * ROUND_TO


def main() -> None:
    csv_path = Path(__file__).with_name('data.csv')
    if not csv_path.exists():
        print("ERROR: data.csv not found.", file=sys.stderr)
        sys.exit(1)

    rows = load_data(csv_path)
    if not rows:
        print("ERROR: No valid rows found.", file=sys.stderr)
        sys.exit(1)

    sold_data   = daily_sold_per_item(rows)
    thrown_data = daily_thrown_per_item(rows)
    items       = sorted(sold_data.keys())

    print("=" * 52)
    print("   Snack Batch Planner — Ramesh Patel's Stall   ")
    print("=" * 52)

    for item in items:
        daily = sold_data[item]
        daily_waste = thrown_data[item]
        num_days = len(daily)
        avg_sold  = sum(daily.values()) / num_days
        avg_waste = sum(daily_waste.values()) / num_days
        suggestion = suggest_batch(avg_sold)

        print(f"\n📦  {item.upper()}")
        print(f"    Days observed       : {num_days}")
        print(f"    Avg sold / day      : {avg_sold:.1f} pcs")
        print(f"    Avg wasted / day    : {avg_waste:.1f} pcs")
        print(f"    Suggested morning   : {suggestion} pcs  (15% buffer, rounded to 5)")

    print("\n" + "=" * 52)
    print("NOTE: On exam / event days add 20 % manually.")
    print("NOTE: Keep ~5 vada aside for the 3-4 PM warden window.")
    print("=" * 52)


if __name__ == '__main__':
    main()
# script tested on data
