# Word Helper (Glossary)

This course uses some big words. Don't worry! Here is what each one means in
plain English. Come back to this page any time you see a word you don't know.

> **Tip:** You do **not** need to memorize these. Just read them once, then use
> this page like a dictionary when you get stuck.

---

**AI (Artificial Intelligence)** — A computer program that can answer questions
and help with tasks, kind of like a very fast helper that has read a LOT of books.

**AI Agent** — An AI helper that you give a job to do. You tell it what you want,
and it does the thinking and gives you an answer. In this course, our agents read
computer problems and suggest fixes.

**LLM (Large Language Model)** — The "brain" behind the AI. It is a program that
is really good with words. When you ask it something, it writes back an answer.
**ChatGPT** uses an LLM.

**OpenAI** — A company that makes a powerful AI brain. We can borrow their brain
over the internet by using a special key (see **API Key**).

**Ollama** — A free AI brain you can run on your **own** computer, with no
internet needed. It's a backup option if you don't have an OpenAI key. Website:
<https://ollama.com>

**API** — Think of it as a waiter at a restaurant. You (your program) tell the
waiter what you want, the waiter brings your order to the kitchen (another
program), and then brings the food (the answer) back to you.

**API Key** — A secret password that lets your program use OpenAI's AI brain.
Keep it private, just like you keep your house key private. It usually starts
with `sk-`.

**Terminal (or Command Line)** — A text window where you type commands to tell
the computer what to do, instead of clicking buttons. It can look scary but it's
just typing.

**Command** — One line of text you type into the terminal to make something
happen. Like giving the computer a single instruction.

**Python** — A popular, friendly programming language. The "brains" of our little
helpers (the `.py` files) are written in Python.

**Script** — A file full of instructions for the computer to run, one after
another. Our `.py` and `.sh` files are scripts.

**`run.sh`** — A "start button" file. Instead of typing many commands, you run
this one file and it does all the steps for that day for you.

**Dependencies** — Extra pieces of code your program needs to work, kind of like
the ingredients a recipe needs. We install them with `pip install`.

**`pip`** — A tool that downloads and installs the extra Python pieces
(dependencies) your program needs.

**Virtual Environment (venv)** — A clean, separate box where your project keeps
its own tools, so it doesn't mix with the rest of your computer. Like having a
labeled lunchbox just for this project.

**Environment Variable** — A note you leave for your programs to read, such as
your secret API key. You set one with the `export` command, like writing it on a
sticky note the computer can see.

**DevOps** — The job of building, shipping, and taking care of software so apps
stay online and run smoothly. Short for "Development + Operations."

**SRE (Site Reliability Engineering)** — A type of DevOps work focused on keeping
websites and apps healthy and online, and fixing them fast when they break.

**DevSecOps** — DevOps with **security** added in. The "Sec" means we also check
for safety problems so bad guys can't break in.

**FinOps** — Watching cloud **costs** (money) and finding smart ways to spend
less. "Fin" is short for "Finance."

**Cloud** — Other people's powerful computers that you can rent over the
internet. Big clouds include **AWS** (Amazon), **Azure** (Microsoft), and
**GCP** (Google).

**AWS (Amazon Web Services)** — Amazon's cloud. You can rent computers and tools
from it. We use one of its tools to check spending in Session 2.

**Cost Explorer** — An AWS tool that shows you how much money you spent and on
what. Like a receipt for your cloud bill.

**Container** — A neat, sealed box that holds an app and everything it needs to
run. It runs the same way on any computer. **Docker** is the most popular way to
make containers.

**Image (container image)** — A frozen, ready-to-use copy of a container. You
"pull" (download) an image and then run it. Example: `nginx:latest`.

**nginx** — A very popular web server (a program that serves web pages). We use
its container image as a simple example.

**Kubernetes (often written "K8s")** — A manager for lots of containers. It
starts them, restarts them if they crash, and keeps the right number running.
Think of it as a traffic controller for containers.

**Pod** — The smallest unit Kubernetes runs. Usually one container lives inside
one pod.

**Deployment** — A set of instructions that tells Kubernetes, "Please keep this
many copies of my app running." If one dies, Kubernetes makes a new one.

**YAML** — A simple file format used to write settings and instructions. It uses
spaces and colons. Kubernetes reads YAML files to know what to do. (File ends in
`.yaml`.)

**kubectl** — The command tool you type to talk to Kubernetes. Say it like
"kube control."

**ImagePullBackOff** — A Kubernetes error that means "I tried to download the
app's image, but I couldn't find it, so I'm waiting and trying again." Often it's
a typo in the image name. We create this on purpose in Session 3 to practice
fixing it.

**CrashLoopBackOff** — A Kubernetes error that means "the app keeps starting and
then crashing, over and over." Kubernetes slows down between tries.

**Trivy** — A free safety scanner. It looks inside a container image and lists
known security problems (see **Vulnerability**).

**Vulnerability** — A weak spot in software that a bad guy could use to break in.
Finding and fixing these keeps systems safe.

**Triage** — Deciding what to fix first, based on what matters most. Doctors do
this with patients; we do it with computer problems.

**Root Cause** — The real, underlying reason something broke — not just the
symptom. Fixing the root cause stops the problem from coming back.

**Terraform** — A tool that builds cloud resources (like servers) by writing them
down in a file instead of clicking around. "Infrastructure as Code."

**Git** — A tool that saves the history of your files so you can track changes
and share code. Like an unlimited "undo" plus a sharing system.

**Repository (repo)** — A folder full of project files that Git keeps track of.
This course is a repo.

---

Still stuck on a word? That's totally normal. Re-read its line above, or look it
up online — every expert was once a beginner looking up the same word.
