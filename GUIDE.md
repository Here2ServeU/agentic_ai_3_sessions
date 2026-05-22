# Your Setup Map — Read This First

This page gets you ready, then walks you through each day. Take it slow. Every
step tells you **what to type** and **why**.

> See a word you don't know? Check the **[Word Helper (Glossary)](GLOSSARY.md)**.

---

## Part 1: One-Time Setup (do this once)

You only have to do this part **one time**. After that, you're ready for all 3 days.

### Step 0 — Set up VS Code (recommended)

VS Code is a free program for writing and running code. It gives you a place to
read the lessons, edit files, and type commands — all in one window. You don't
have to use it, but it makes everything easier for beginners.

1. **Install VS Code.** Download it from **<https://code.visualstudio.com>** and
   open it.
2. **Install the Python extension.** On the left side, click the squares icon
   (Extensions), search for **Python** (made by Microsoft), and click *Install*.
   This file already lists it for you, so VS Code may pop up and offer to install
   the "recommended extensions" — just click *Install*.
3. **Open the course folder.** Click *File → Open Folder...* and pick the
   `agentic_ai_3_sessions` folder (after Step 1 puts it on your computer).
4. **Open the built-in terminal.** Click *Terminal → New Terminal* from the top
   menu (or press the **Ctrl + `** keys — that's the little backtick key, usually
   above Tab). A text box opens at the bottom. This is where you'll type the
   commands in the next steps.
5. **(After Step 2) Pick the right Python.** Once Step 2 makes the `.venv` box,
   tell VS Code to use it: press **Cmd + Shift + P** (Mac) or
   **Ctrl + Shift + P** (Windows/Linux), type **Python: Select Interpreter**, and
   choose the one that says `.venv`.

> From now on, every command in this guide can be typed into the VS Code terminal
> you opened in step 4. If you'd rather use your computer's normal terminal app,
> that works too.

### Step 1 — Get the course onto your computer

This downloads ("clones") the course folder.

```bash
git clone https://github.com/Here2ServeU/agentic_ai_3_sessions.git
cd agentic_ai_3_sessions
```

> `git clone` = copy the project. `cd` = "go into" that folder.

### Step 2 — Make a clean work area (recommended)

This makes a little box (a *virtual environment*) so this project keeps its own
tools tidy and separate from the rest of your computer.

```bash
python3 -m venv .venv && source .venv/bin/activate
```

> You'll know it worked when you see `(.venv)` at the start of your terminal line.

### Step 3 — Install the extra pieces

Our helpers need a few extra pieces of code (we call them *dependencies*). This
one command installs all of them.

```bash
pip install -r requirements.txt
```

> `requirements.txt` is just a shopping list of pieces. `pip install` buys them.

### Step 4 — Give your helper a brain

Your AI helper needs an AI brain to think with. **Pick ONE** of these:

**Option A — OpenAI (needs a key from openai.com):**

```bash
export OPENAI_API_KEY=sk-...      # paste your real key after the =
```

**Option B — Ollama (free, runs on your own computer):**

First install Ollama from **<https://ollama.com>**, then tell the course to use it:

```bash
export AGENT_BACKEND=ollama
```

> `export` leaves a note your programs can read. The API key is a secret —
> keep it private, like a password.

Every `run.sh` reads the `AGENT_BACKEND` note, so you can switch brains any time
without changing any code.

**Setup done!** Now do the days in order.

---

## Part 2: The Lessons

Each **Day (1-3)** has its own "start button" called `run.sh`. You run it, and it
does the day's work for you — checking your tools, installing pieces, and running
the helpers in order.

---

### Session 0 — Scripting Foundations (optional, but recommended)

Brand new to coding? Start here. This is a **read-through lesson** (no `run.sh`,
nothing to install) that teaches the three languages used in this course:
**Python**, **Bash**, and **Kubernetes YAML**. It walks through the real scripts
line by line, so Days 1-3 make sense.

Full lesson: **[session0/README.md](session0/README.md)**

---

### Day 1 — Your First AI Helper + Reading Logs

You'll run your very first AI helper, then build one that reads a computer's
*logs* (its diary of what happened) to find problems.

```bash
cd session1
./run.sh
```

**What happens:**

1. It installs the needed pieces.
2. It runs `agent_unified.py` → your AI writes Kubernetes settings (a file that
   tells the container manager what to run).
3. It runs `agent_log_troubleshooter.py` → your AI reads this computer's logs and
   says what looks wrong, with commands to fix it.

**What you need:**

| You need... | Why |
|-------------|-----|
| `python3` | runs the helpers |
| An OpenAI key **or** Ollama | gives the helper a brain |

Full lesson: **[session1/README.md](session1/README.md)**

---

### Day 2 — Security Check + Saving Money

You'll use AI two ways: to find **security weak spots** in a container, and to
find ways to **spend less money** in the cloud.

```bash
cd session2
./run.sh
```

**What happens:**

1. It installs the needed pieces.
2. **Security part:** if a scan file (`trivy_nginx.json`) is missing, it runs
   **Trivy** (a safety scanner) when Trivy is installed. Then `agent_devsecops_trivy.py`
   asks the AI which problems to fix first.
3. **Money part:** if it finds working AWS login info, `agent_finops_aws.py`
   reads your cloud spending and suggests ways to save.

**What you need:**

| You need... | Why |
|-------------|-----|
| `python3` + an AI brain | runs the helpers |
| `trivy` *(optional)* | makes the security report |
| AWS login *(optional)* | lets the helper read your cloud bill |

> Don't have Trivy or AWS set up? No worries. Those parts are **skipped** with a
> friendly message. The day won't fail.

Full lesson: **[session2/README.md](session2/README.md)**

---

### Day 3 — Fixing a Broken App (Kubernetes)

You'll break an app **on purpose**, then let your AI helper find the cause and
suggest a safe fix — just like a real on-call engineer.

```bash
cd session3
./run.sh            # break the app + run the AI helper
./run.sh --cleanup  # remove the broken app when you're finished
```

**What happens:**

1. It installs the needed pieces.
2. It starts `bad-deploy.yaml`, an app with a wrong image name. Kubernetes can't
   find it, so you get an `ImagePullBackOff` error (on purpose!).
3. It runs `agent_k8s_triage.py` → the AI looks at the cluster and tells you the
   impact, the root cause, and safe fixes.

**What you need:**

| You need... | Why |
|-------------|-----|
| `python3` + an AI brain | runs the helper |
| `kubectl` + a running cluster | starts and inspects the app |

> **Always clean up** when you finish, so the broken app doesn't keep
> running. Just run `./run.sh --cleanup` in the `session3` folder.

Full lesson: **[session3/README.md](session3/README.md)**

---

## If Something Goes Wrong

Errors are normal — even experts get them. Here are the common ones:

| Message you see | What to do |
|-----------------|------------|
| `OPENAI_API_KEY is not set` | Set your key, or switch to Ollama: `export AGENT_BACKEND=ollama` |
| `no reachable Kubernetes cluster` (Day 3) | Run `kubectl cluster-info` to check your cluster is on |
| `FinOps step skipped` (Day 2) | Run `aws configure` and make sure your AWS user can read Cost Explorer |
| Dependency / install errors | Run `pip install -r requirements.txt` again inside your `.venv` |

Still stuck? Re-read the message slowly — it usually points right at the fix.
And the **[Glossary](GLOSSARY.md)** explains any word that's tripping you up.

---

## Who Made This

This course was created by **Emmanuel Naweji**. Read his story in **[BIO.md](BIO.md)**.

[LinkedIn](https://linkedin.com/in/ready2assist) | [GitHub](https://github.com/Here2ServeU)
