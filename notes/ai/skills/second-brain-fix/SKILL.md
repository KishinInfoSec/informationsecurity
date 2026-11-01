---
name: second-brain-fix
description: Work through the findings from a second-brain audit in batches, correcting stale facts and converting locations onto the state/event schema, driven by the markdown file of findings the audit left behind. Use after running second-brain-audit, when someone wants to fix the rest of their notes rather than one page, when they ask how to take the audit forward, when they have a list of contradicted or unsupported claims to work through, or when a notes folder needs converting in bulk rather than one page at a time.
argument-hint: "[path-to-audit-findings.md]"
arguments: [audit-results]
---

# Second Brain Fix

The audit found what is wrong and fixed one location so the shape was visible. This works
through the rest, in batches, from the findings the audit left behind.

## The argument

The findings file this run was invoked with is `$audit-results`, and it is optional:

```
/second-brain-fix                                   nothing passed
/second-brain-fix ~/notes                           a folder to look in
/second-brain-fix ~/notes/second-brain-audit.md     the findings file itself
```

`$audit-results` is **a path to one markdown file of findings**. `/second-brain-audit` names
what it writes `second-brain-audit.md`, so that is usually what you will be handed, but the
name is not the contract. Any markdown file holding the findings works, and whatever the user
points at is the one to use.

Resolve it before anything else:

| What you were given | Do |
|---|---|
| a path to a **file** | that is the findings. The notes folder is its parent, unless the file names a different one |
| a path to a **folder** | look inside it for the findings, `second-brain-audit.md` first |
| nothing, so the line above still reads `\$audit-results` | look in the current folder, then one level down |
| **a path that does not exist** | say so and stop. Do not fall back to searching, or a typo silently works on the wrong folder |
| **more than one candidate** when searching | list them with their newest `## Log` dates and ask which |
| **no candidate** when searching | stop. Say to run `/second-brain-audit` first, since there is nothing to work from |

Never invent a queue from scratch when there are no findings. Auditing and fixing in one pass
is how a bulk write happens against findings nobody read.

**The findings are the input.** `$audit-results` is both the queue and the record: one keyed
line per location in `## Current State`, one dated line per run in `## Log`. Everything below
is driven by that file, and a run that does not update it is a run nobody can pick up from.

## This skill writes in bulk. Settle backups before it does.

Never start writing without settling this, and never resolve it by copying the notes folder
somewhere else. A duplicate folder of notes is a second answer to every question, which is the
exact problem this skill exists to remove.

**First, check what is already there.** Run `git rev-parse --show-toplevel` in the notes folder.

- **Already in git**, either its own repo or tracked by a parent one. Commit or stash anything
  outstanding, then `git checkout -b second-brain-fix`, and commit after every batch. Say which
  repo you are in, because a vault nested inside another project is common and the user should
  know what the branch covers.
- **Not in git.** Ask, in these words or close to them:

  > Your notes are not in git, so there is no way to undo a batch. Want me to run `git init`
  > here first? It stays on your machine, nothing gets pushed anywhere, and every batch becomes
  > a checkpoint you can roll back to.

  If they agree: `git init`, `git add -A`, one baseline commit, then the branch. Never add a
  remote and never push.

  If they decline, ask once more and take the answer:

  > Understood. To be clear, this rewrites many files at once and there will be no way to undo
  > it. Go ahead anyway?

  On a clear yes, proceed and do not raise it again. On silence or anything ambiguous, stop. An
  unanswered question is not permission.

## The three piles are three different jobs

| Pile | What the finding contains | What to do |
|---|---|---|
| **Contradicted** | the stale claim AND the newer evidence | fix in batch, no questions |
| **Unsupported** | the claim, and nothing backing it up | never guess. One batch of questions for the user |
| **Locations not yet converted** | a page that has no `## Current State` / `## Log` | convert in batch, verbatim |

The middle row is where bulk fixing goes wrong. An unsupported claim has no answer in the
notes by definition, so an agent told to "correct these" will invent a value or quietly delete
the line. Both are worse than the stale claim.

## How much to take on

Ask how large the notes are, or count the markdown files, and scale the ambition:

| Size | Do this |
|---|---|
| **Under ~50 files** | everything in one session. Two or three batches |
| **~50 to 500** | the always-loaded surface first, then one folder per batch, committing between |
| **500+** | the always-loaded surface, plus only the pages with a trail (several entries about one subject over time). Everything else stays as it is, permanently |

Bigger notes do not mean convert more. They mean convert a smaller fraction and lean harder on
the write path, because at that size nobody is ever going to hand-tend the archive.

## Step 1: build the batch list

Read `$audit-results`. Take the `## Current State` entries that are not marked as fixed, plus
any pile the audit reported but did not enumerate. Group them into batches of roughly 5 to 15
locations, keeping a folder together where you can.

Show the user the batch list and the order before writing anything. Ordering is always:

1. Whatever loads every session.
2. The pages the agent gets wrong most often.
3. Pages with a trail.
4. Nothing else.

## Step 2: the contradicted pile, in batch

For each finding, the newer evidence is already named. So:

- Replace the stale line in `## Current State`.
- Move the superseded line, **verbatim**, to `## Log`.
- Date the new line with the date of the evidence, not today.

That last one matters more than it looks. A date on a current value is a claim that somebody
checked the value on that day. Stamping today's date on a line you corrected from a note
written in June makes a June fact look verified this morning.

Work the whole batch, then show one summary: how many lines replaced, in which files, and the
three or four that were least obvious. Do not show a diff per line, and do not ask per line.

## Step 3: convert the locations, in batch

Give each page the two sections. Adapt to the shape the audit found:

```markdown
## Current State
<!-- One entry per subject. Dated. REPLACED on update, never appended to. -->

- **Retainer** (2026-08-01): $3,200/mo, renewed through February 2027
- **Main contact** (2026-05-02): Curtis Ilo

## Log
<!-- Append-only. Never edit or delete an entry. -->

- (2026-04-30) Delivered and paid, $21,000
- (2026-06-15) Added reply drafting, retainer to $3,200/mo
```

One big file gets a `## Current State` block at the top and everything else beneath it, no new
files. Daily notes get one new file of current values and the journal untouched. Notes that are
not markdown do not get converted at all.

**This is sorting, not rewriting.** Every existing line lands in one of the two sections,
verbatim, at most with a date prepended. Improving the prose is how information disappears
without anyone noticing, and in a batch nobody is reading closely enough to catch it.

**When a bullet has no date and none can be recovered**, do not invent one and do not quietly
leave the entry bare. Take the date from the evidence if the bullet cites any, otherwise write
`(date unknown)` in the date's place. A bare entry reads as an oversight; `(date unknown)` reads
as the gap it is, and it survives into the next audit as something to ask about.

Two kinds of page to leave alone, and say so rather than converting them:

- **Reference checklists.** Packing lists, hospital-bag lists, standard operating steps. Few
  bolded keys, few dates, and the order is the content. Converting one passes every structural
  check and destroys the thing that made it useful.
- **Pages where the freshest status lives inside prose**, under a heading that owns the bullets
  below it. Dissolving that section leaves the newest status outside `## Current State` and the
  oldest inside it, which is the exact failure being removed, rebuilt one level up.

## Step 4: the unsupported pile, one pass of questions

Collect them all and ask once, as a numbered list. Not one at a time, and never silently.

For each, three outcomes:

- **Still true** goes into `## Current State` with the date the user gives, and say plainly that
  the evidence was missing, not just misfiled.
- **No longer true** gets replaced, old line verbatim to `## Log`.
- **Cannot tell** comes out of the always-loaded file entirely. A confident wrong answer costs
  more than a missing one.

If the user does not answer, leave every one of them exactly as it is. An unanswered question is
not permission.

### Anything you leave for the owner gets annotated where it lives

A question in your summary reaches one person once. The line stays in the notes and gets read by
every future session, so **the warning has to be on the line, not only in your report.**

Whenever you leave a line standing because only the owner can resolve it, append the reason to
that line in place, keeping the original text intact ahead of it:

```markdown
- **Sam Iwu**: accepted a full-time offer, starting October 2026. UNVERIFIED (fix run
  2026-09-18): no date and no source anywhere; entities/sam-iwu.md says he is still a
  contractor. Confirm or delete.

- **Ferro retainer renewal** (2026-09-12): renewed at $6,500/mo through year-end. CONFLICT
  (fix run 2026-09-18): the 2026-09-10 call set it to $12,000/mo. Nothing sources this line.
  Ask before quoting either number.
```

This matters most for a **stale line that is newer than the line you just corrected.** If one key
says $12,000 dated the 10th and another says $6,500 dated the 12th, an agent reading that page
takes the newer one and answers $6,500, so correcting the first key changed nothing unless the
second one carries the warning. Check for that case explicitly after every batch: for each key
you fixed, look for another key on the same page about the same subject with a later date.

Never delete the line to resolve the conflict, and never pick a value yourself. Annotating is the
whole move.

## Step 5: write the results back

After each batch, edit `$audit-results`:

- **Replace** each location's `## Current State` line with its new status. One line per
  location, always. Never a second line.
- Record every line you annotated and left standing, so the next run can see what is still
  waiting on the owner rather than re-deriving it.
- **Append** one entry to `## Log`: the date, which batch, how many lines replaced, how many
  locations converted, and how many unsupported claims are still unanswered.

Then commit the batch. The findings and the notes move together, so an interrupted run is
resumable by reading one file.

## Step 6: re-audit and compare

When the batches are done, run `/second-brain-audit` again and compare the contradicted count
to the last `## Log` line. That number is the only evidence any of this worked.

If the count did not move much, say so and say why rather than presenting the conversion as a
result. Restructuring cannot reach a fact nobody ever wrote down, and when the count stays flat
that is usually what happened. The fix then is the write path, not another batch.

Flag one thing if the findings file has been renamed: `audit.py` skips files whose name starts
with `second-brain-audit`, so a renamed one gets read as evidence on the next scan, and it
quotes stale claims verbatim. Either keep that name or keep the file outside the notes folder.

## Rules that never bend

1. **Lose nothing.** Every line lands somewhere, verbatim. If a line cannot be placed, leave it
   where it is and report it.
2. **Never merge two subjects that look alike.** "Acme (May)" and "Acme Corp renewal" may be two
   real things. A duplicate entry is a cheap mistake; a wrong merge destroys information. Report
   near-misses at the end of the batch and let the user decide. Batch work merges by default
   because merging looks like tidying, so this rule needs holding on purpose.
3. **Never invent a value**, and never delete a claim to make a pile smaller.
   Anything you leave for the owner carries its reason on the line itself, not only in your
   summary. A warning that lives in a chat window is the failure this skill exists to fix.
4. **Never edit or delete a `## Log` entry.** Old and superseded is the point of that section.
5. **A date is a claim that the value was checked.** A line you only moved keeps its own date.
6. **Never copy the notes folder as a backup.** Git, or an informed no. Nothing else.
7. **Stop when the always-loaded surface has nothing contradicted.** An archive full of old
   pages is history, not rot. There is no version of this where every page gets converted.

## If the write path has not changed yet

Check whether `CLAUDE.md` (or `AGENTS.md`, or the system prompt) carries the state/event rule
from the audit's phase 7. If it does not, add it before starting, and say why: fixing four
hundred lines under a write path that can only append buys about a month.
