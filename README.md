# Family Devotions

Nightly Lutheran (LCMS) family devotions with ESV Scripture and a printable kids' activity sheet for each day.

**Site:** https://samahlersmeyer-prog.github.io/Family-Devotions/

## Each night
1. Invocation
2. Hymn of the week
3. Scripture (ESV), with a rotating reader
4. Story
5. Short teaching
6. Small Catechism part of the week
7. Questions for K–2nd, 3rd–5th, and older kids
8. Highs, lows, and prayer requests
9. Doxology (tap ♪ for the starting note)
10. Closing prayer and the Lord's Prayer

Highs, lows, and standing prayer requests are woven into the closing prayer automatically.

## Tabs
- **Prayers**: a standing prayer list. Requests stay in the closing prayer until you mark them answered, and answered prayers collect in their own list.
- **Journal**: every night's highs and lows.
- **Verses**: every memory verse so far, with a quiz mode.
- **⚙︎**: family members, who takes turns reading, the optional family-PIN sync, and backups.

## Family PIN sync (optional)
Set `window.FB_CONFIG` in `sync-config.js` to a Firebase web config to turn it on. Families who never set a PIN keep everything on their own device. Each PIN maps to one Firestore doc at `families/<sha256>`; see `firestore.rules`.

The page color follows the church year (green, Advent blue, white for feasts, red for Reformation and martyrs).

The **Kids' page** tab has a coloring picture, fill-in-the-blanks, a word search, circle-the-answer questions, a drawing prompt, and a memory verse. Tap **Show answers** for the answer key, or **Print kids' sheet** for a one-page printout.

## Schedule
- Oct 19–30: Reformation weeks
- Oct 31 – Nov 8: Reformation Day, All Saints', In the Beginning
- Nov 9–15: Joseph
- Nov 16–22: Moses
- Nov 23–29: Give Thanks (Thanksgiving)
- Nov 30 – Dec 20: Advent
- Dec 21–31: Christmas through New Year's Eve

## Updating
Content lives in `src/content/*.py`, one file per week. Weekly hymns and catechism parts are in `weekly.js`. Run `python3 src/build.py` to regenerate `days.json`.

Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved.
