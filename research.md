# Research

**Problem (5 lines)**
- The snack stall outside the hostel gate fries samosas, bread puffs, and vada in batches every morning and again after lunch.
- On many evenings the owner discards 10–20 unsold pieces per item type because they go soggy and cold after 4 hours.
- On busy days (exam blocks, cricket finals) he runs out of samosas before 2 PM, turning away a steady queue of customers.
- He decides batch sizes by feel — "aaj thoda zyada lag raha hai" — with no record of which items waste most or which hours drive demand.
- Tracking per-item sales and waste over a few days would let a simple script suggest how many pieces of each type to fry each morning.

**Existing solutions (2) and why they do not fit**
1. **Square for Restaurants (POS system)** – tracks per-item sales and generates waste reports, but requires a tablet, monthly subscription (~₹1,500/month), and internet. Ramesh runs a bare counter with no electricity socket; a POS is physically impractical and financially out of scope for a stall with ₹1,200–1,800 daily revenue.
2. **Spreadsheet templates for food waste tracking** – several NGOs distribute Excel waste-log templates to small vendors. These require opening a laptop or phone spreadsheet after every batch, understanding formula auto-fill, and have no way to give a one-line recommendation. Ramesh is not comfortable with any spreadsheet software; he has never used one.

**Sources consulted**
- *Simulation-based approach for inventory management of packaged milk at an unorganized Indian retailer* (Atlantis Press, 2022). URL: https://www.atlantis-press.com/article/126019547.pdf — Note: Although the paper focuses on milk, its core finding applies directly here: small Indian roadside vendors consistently over-stock perishables by 15–30 % because they use intuition rather than any recorded baseline; a simple daily average reduces this waste reliably.
- *Zoho Inventory — Frequently Asked Questions* (official Zoho page, accessed November 2026). URL: https://www.zoho.com/us/inventory/inventory-faq/ — Note: Confirms the free plan includes low-stock alerts and basic item tracking, but the product is designed for shops with multiple SKUs, barcodes, and internet access — none of which apply to a roadside snack stall that sells three fried items and has no power socket at the counter.
