# LLM-Driven Image Analysis Framework

A modular, Python-based framework for quickly building custom image-analysis pipelines with help from Large Language Models (LLMs). The system uses a two-stage workflow:

- **Stage 1 — Plan (no code):** propose a short, practical pipeline (3–6 steps) for a specific task.  
- **Stage 2 — Generate (code):** for each step, generate a module (Python + JSON UI) and chain them in the GUI; export a runnable script.  

Designed for domain experts who need working tools without deep programming.

---

## Two-Stage Workflow

### Stage 1 — Pipeline planning (no code)

Use this prompt to get a concise, classical-CV-first plan:

**Stage-1: Pipeline Planner Prompt**

You are an image-analysis expert. 
I am using a python framework to generate image analysis workflow that consists of layered process of using various methods.
I am asking for a pipeline for it. Propose a short, practical workflow to achieve the goal (no code). Keep it to 1–4 steps. Prefer classical computer-vision methods; if deep learning is clearly better, say so and why. For each step, give:
- Step name suitable for function and .py file name and one-line purpose
- Input → Output (what it expects, what it produces)
- 1–2 key tunables (e.g., kernel size, threshold)
End with:
- Quick validation plan (what to check, simple metric/target)
- Common pitfalls & fixes (very brief)

Suggest an image analysis pipeline for plywood knot detection and counting

---

### Stage 2 — Module generation (code)

For each planned step, use the Module Generator prompt (Stage-2_Processing Module_LLM_Prompt_Template.txt) to produce:

- a Python function (in `config/methods.py`)  
- a JSON UI schema (in `config/methods.json`)  

Then modules are shown and run in the GUI according to the order in the methods.json → test → tune parameters → test..

---

## Quick Start (PyCharm)

1. Open the project for example with Pycharm.
2. Set the interpreter (any Python 3.x you already use).  
3. Run `A_Main.py`.  
4. Load an image → adjust parameters for each module until satisfactory results.
5. Export the pipeline (JSON) and Generate Script (single `.py`) for headless/embedded use.  

---

## Typical Flow for Tailored Image Analysis Pipeline

1. Plan a workflow (Stage-1 prompt).  
2. Generate each module (Stage-2 prompt) → copy JSON to `config/methods.json`, Python to `config/methods.py`.  
3. Modules are chained in the GUI; use UI to tune parameters.  
(4. Export the pipeline JSON and Generate Script with using LLM (single `.py`). )

---

## Contributing

PRs welcome for:
- New modules (with matching JSON UI),
- UI/UX improvements,
- Sample pipelines and datasets,
- Documentation tweaks.

---

## Citation
If this framework helps your work, please cite:

LLM-Assisted Workflow Generation for Low-Cost Visual Inspection and Image Analysis (Updated with venue when available)
