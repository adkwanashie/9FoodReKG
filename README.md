# 9FoodReKG
An Extensible Ontology for Food Safety Regulations.
A Streamlit application for the **Food Regulations Knowledge Graph**. This repository contains the app entry point `main.py`, an evaluation dashboard in `pages/evaluation.py`, and a KG loader in `kg/kg_loader.py`. The combined Cypher export for restoring the database is provided as **kg/FoodReKG.cql**.

---

### Requirements and Setup

**Python version**  
- Use **Python 3.10** or **3.11** for best compatibility.

**Create and activate a virtual environment**  
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

**Install dependencies**  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Key files**  
- **`main.py`** — Streamlit app entry point.  
- **`pages/evaluation.py`** — Benchmark and evaluation dashboard.  
- **`kg/kg_loader.py`** — Neo4j driver, query helpers, and `reload_foodregkg()` function.  
- **`kg/FoodReKG.cql`** — Combined Cypher file to restore the Food Regulations KG.

---

### Neo4j Desktop Setup

**Create a local database**  
1. Open Neo4j Desktop and create a new project.  
2. Add a new database (choose the default database name or a custom name).  
3. When prompted, set the **database password** for the `neo4j` user and remember it.

**Confirm Bolt URI and database name**  
- Typical local Bolt URI: **`bolt://localhost:7687`** or **`neo4j://127.0.0.1:7687`**.  
- If you used a custom database name, note it for the `.env` file.

**Optional Restore using Neo4j Browser and APOC**  
If you prefer to restore the KG directly from Neo4j Desktop using APOC (APOC plugin must be installed/enabled in Desktop):

1. Start the database.  
2. Open Neo4j Browser and run an APOC export/import command to load `FoodReKG.cql` from the database import directory, or copy `FoodReKG.cql` into the database import directory and run it from the Browser.  
3. Alternatively, use the app loader (see Loading the KG below) to replay the file into the running database.

---

### Environment Variables

Create a `.env` file in the project root with the following variables. **Fill in your actual values**:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Neo4j connection
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=YourNeo4jPassword
NEO4J_DATABASE=neo4j
```

**Notes**  
- **NEO4J_USER** is usually `neo4j` unless you created a different user.  
- **NEO4J_DATABASE** should match the database name in Neo4j Desktop (default is `neo4j`).  
- The app uses `python-dotenv` to load `.env` at startup; ensure `.env` is in the project root.

---

### Loading the FoodReKG

**Option A Use the app loader (recommended)**  
The repository includes `kg/kg_loader.py` with `reload_foodregkg()` which replays `kg/FoodReKG.cql` into the configured Neo4j instance.

From a Python REPL or inside the app:
```python
from kg import kg_loader
kg_loader.reload_foodregkg()
```

**Option B Use Neo4j Browser with APOC**  
If APOC is installed and you prefer to import from the Neo4j import directory, copy `FoodReKG.cql` into the database import folder and run an import command in the Browser to execute the file.

---

### Running the App

**Start Streamlit**  
```bash
streamlit run main.py
```

**What to expect**  
- The sidebar will show a quick Neo4j connection test and sample regulation titles.  
- Use the navigation to open the evaluation dashboard and run benchmarks or reload the KG from the sidebar.

---

### Python Related Details and Troubleshooting

**Driver and connection**  
- `kg/kg_loader.py` uses the official Neo4j Python driver (`neo4j` package). Ensure the `NEO4J_URI`, `NEO4J_USER`, and `NEO4J_PASSWORD` in `.env` are correct.  
- If you see an authentication error, verify the credentials by connecting with `cypher-shell` or via Neo4j Desktop.

**Common issues**  
- **Unauthorized error**: check `.env` values and restart the app after editing `.env`.  
- **Missing dependencies**: re-run `pip install -r requirements.txt`.  
- **APOC not available**: install/enable APOC in Neo4j Desktop if you plan to use APOC export/import features.

**Closing the driver**  
- The loader exposes a `close_connection()` helper. The app closes sessions automatically, but you can call this function when shutting down long‑running scripts.

**Logging and debugging**  
- Add temporary `print()` statements in `main.py` to confirm environment variables are loaded.  
- Use the Neo4j Browser to run test queries (e.g., `MATCH (n) RETURN count(n)`).

---

### Final Notes

- **FoodReKG.cql** in `kg/` is the canonical Cypher export for restoring the Food Regulations KG. Keep it under version control for reproducibility.  
- Keep secrets out of version control. Add `.env` to `.gitignore`.  
- If you want automated export/import workflows, consider adding a small script that calls `kg_loader.reload_foodregkg()` or an APOC import command.

---

**Ready to run**  
1. Create and activate a virtual environment.  
2. Install dependencies with `pip install -r requirements.txt`.  
3. Fill `.env` with your OpenAI key and Neo4j credentials.  
4. Start Neo4j Desktop and confirm the database is running.  
5. Run `streamlit run main.py`.
