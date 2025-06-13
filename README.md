# Life Log Portfolio

This repository serves as a **Life Log**—a chronological record of activities committed over time. To ensure that the timeline is **authentic**, **unalterable**, and **verifiable by anyone**, it uses a combination of Git’s immutable commit structure and decentralized cryptographic timestamping via [OpenTimestamps](https://opentimestamps.org).

The approach guarantees that every log entry (commit) is:
- **Authentic**: Created and stored exactly as recorded
- **Immutable**: Cannot be altered without detection
- **Timestamped**: Proven to exist at or before a specific point in time

---

## 🛡️ Why Life Log Is Trustable

1. **Git Commit Hashes Are Immutable by Design**

Each Git commit generates a **SHA-1 hash** that is calculated from:
- The complete snapshot of files
- The author and timestamp
- The parent commit hash
- The commit message

This means even a single-character change in any of these fields will produce a completely different commit ID. Once a commit is made, it becomes **cryptographically locked**.

2. **OpenTimestamps Anchors the Commit in Time**

After a new commit is created, a follow-up commit generates a `.ots` file using the OpenTimestamps protocol:
- The hash of the previous commit is saved to a file (e.g., `latest.commit`)
- That file is timestamped and a `.ots` proof is created
- The `.ots` file is committed to the repository

This `.ots` proof anchors the commit hash into the **Bitcoin blockchain**, providing an independent, tamper-proof record of its existence at a specific time.

3. **Independent, Offline Verification**

Anyone can independently verify the timestamped commit using the OpenTimestamps client:

```bash
ots verify latest.commit
```

## 🔍 How to Validate If a Life Log Entry Is Legit

Anyone can independently verify that a specific log entry is authentic and existed at a certain point in time by following these steps:

### 1. Locate the Log Entry

Find the log entry you want to verify inside the `life-log.md` (or equivalent) file.

Run:

```bash
git blame life-log.md
```

This will show which commit added or modified each line. Identify the **commit hash** associated with the specific log entry (let’s call it `COMMIT_A`).

### 2. Identify the Timestamp Commit

Each log entry is timestamped in a **follow-up commit** using OpenTimestamps. To find it:

* Run `git log` and look for the **next commit** after `COMMIT_A` that includes a file like `timestamp-COMMIT_A.ots` or references the hash in `latest.commit`.

This is the **timestamp commit**, which contains the `.ots` proof for `COMMIT_A`.

### 3. Retrieve the `.ots` Proof File

Locate the corresponding `.ots` file in the repository, typically stored as:

```
ots/timestamp-COMMIT_A.ots
```

or simply:

```
latest.commit   # contains the commit hash
latest.ots      # contains the proof
```

### 4. Verify Using OpenTimestamps

You have two options to verify the timestamp:

**Option A: Local verification**

Install [OpenTimestamps client](https://github.com/opentimestamps/opentimestamps-client):

```bash
pip install opentimestamps-client
ots verify latest.commit
```

This checks that the `.ots` proof is valid and proves that the commit existed before it was anchored in the Bitcoin blockchain.

**Option B: Online verification**

Visit the public OpenTimestamps verifier:
👉 [https://opentimestamps.org](https://opentimestamps.org)

Upload the `.ots` file and the corresponding `latest.commit` text file to confirm the timestamp.

---

If the proof is valid, it guarantees:

* The commit hash has **not been altered**
* The content of that commit existed **at or before** the blockchain timestamp

Any mismatch indicates tampering or falsification.

## ✍️ How to Add a New Entry to the Life Log (With Timestamp)

Follow these steps **every time** you want to add a new entry to the Life Log and generate a verifiable timestamp:

---

### ✅ Step 1: Add Your Log Entry

Edit the `life-log.md` (or relevant file) and append your new entry. For example:

```markdown
## 2025-06-13
- Completed project milestone X
- Learned about OpenTimestamps
````

---

### ✅ Step 2: Commit the Entry

Save the file and create a normal Git commit:

```bash
git add life-log.md
git commit -m "Log: 2025-06-13 — added daily reflection"
```

This will generate a new commit (e.g., `abc1234`) representing your log entry.

---

### ✅ Step 3: Create Timestamp Proof

Save the commit hash to a file:

```bash
git rev-parse HEAD > latest.commit
```

Then generate the OpenTimestamps proof:

```bash
ots stamp latest.commit
```

This creates a file called `latest.commit.ots`.

---

### ✅ Step 4: Commit the Timestamp Proof

Add the two generated files and commit them:

```bash
git add latest.commit latest.commit.ots
git commit -m "Timestamp: Proof for commit abc1234"
```

(Optionally rename the `.ots` file to include the commit ID: `ots/timestamp-abc1234.ots` for clarity.)

---

### ✅ Step 5: Push Everything

Push both commits to GitHub:

```bash
git push
```

---

### 🎉 Done!

Your log entry is now:

* Recorded in Git with a unique hash
* Timestamped via OpenTimestamps
* Publicly auditable and tamper-evident

Repeat this process for each new log entry you want to preserve with trustable integrity.

