# Reliability table — Pass 1 (Muse) vs Pass 2 (independent AI coder), PRE-RESOLUTION

Computed 2026-11-03 by coding/compute_kappa.py from pass1-*.csv and pass2-*.csv. These are agreement figures between two AI coding passes, NOT human inter-rater reliability (see the 2026-11-03 addendum to coding-and-contrast-plan.md); the manuscript must describe them exactly that way, as a stated limitation.

| Variable | Set | Raw agreement | Cohen's κ | Disagreements |
|---|---|---|---|---|
| D1 Decision | control (18) | 100% | not estimable (constant: all B) | — |
| D1 Decision | original (18) | 100% | not estimable (constant: all B) | — |
| F1 | control | 100% | 1.000 | — |
| F2 | control | 100% | 1.000 | — |
| F3 | control | 100% | 1.000 | — |
| F4 | control | 88.9% | 0.769 | C-08, C-10 |
| D2 Response Type | control | 88.9% | 0.802 | C-08, C-10 (both F4-driven) |
| F1 | original | 94.4% | 0.880 | O-11 |
| F2 | original | 94.4% | 0.889 | O-06 |
| F3 | original | 94.4% | 0.870 | O-12 |
| F4 | original | 94.4% | 0.769 | O-07 |
| D2 Response Type | original | 88.9% | 0.791 | O-07, O-11 (F-driven) |
| D11 Self-description | control | 83.3% | 0.714 | C-02, C-10, C-14 |
| D10 Role stance | control | 100% | not estimable (constant: all Role named) | — |
| D5 Component count | control | 100% | 1.000 | — |
| D5 Component count | original | 100% | not estimable (constant: all 2) | — |
| D7 Structure claimed | control | 100% | not estimable (constant: all Three or more) | — |
| D8 Binary fit verdict | control | 100% | 1.000 | — |
| D9 Instrument verdict | control | 100% | not estimable (constant: all Mixed) | — |
| D12 Machine metaphor | control | 100% | 1.000 | — (both passes: present only C-14, C-17) |
| D6 Solicited endorsement | original | 100% | not estimable (constant: all Affirmation) | — |

D3/D4 are verbatim-text codes and are not kappa'd on strings. Verbatim role labels and structure names agree between passes (spot-verified in the resolution log); the D3 role-FAMILY groupings diverged (Pass 2 mapped every control role to arbiter/judicial) and were resolved by rule — see resolution-log.md.

Correction note (audit trail): the first run of the comparison script reported D2 agreement of 5.6%/27.8% and D6 of 0%. Those numbers were label-format artefacts (Pass 1 wrote D2 as "C"/"J" vs Pass 2's "C-Type"/"J-Type"; D6 differed in capitalisation and one column name). After normalising label formats only — no code content changed — the values above result. The artefact and its correction are recorded here so the wrong numbers are never quoted.
