# 🚀 JSON Master Portal & LLM Anti-Hallucination Encyclopedia

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blue?style=flat&logo=github)](https://santoshadkar.github.io/json-master-portal/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standards](https://img.shields.io/badge/RFC-8259%20%7C%20ECMA--404-emerald)](https://datatracker.ietf.org/doc/html/rfc8259)
[![Structured Outputs](https://img.shields.io/badge/AI-Structured%20Outputs-purple)](https://platform.openai.com/docs/guides/structured-outputs)

> The definitive encyclopedic guide, interactive playground, and production code generator for JSON specifications, dialects, LLM hallucination mitigation, and multi-model structured outputs.

---

## 🌟 Why This Project Exists

Modern software engineering and AI systems live and die by structured data contracts. However:
1. **JSON is unforgiving:** A single trailing comma, single quote, or unescaped control character invalidates the entire document.
2. **LLMs are probabilistic:** Large Language Models frequently hallucinate schema fields, invent non-existent enum literals, fail at JSON syntax, or output conversational chatter.
3. **Engineering fragmentation:** Teams struggle to translate domain objects across JSON Schema, Pydantic V2, TypeScript Zod, and battle-tested prompts.

**JSON Master Portal** solves this by providing a unified, client-side, zero-dependency portal featuring interactive generators, diagnostic repair simulators, and exhaustive architectural documentation.

---

## 🛠️ Key Features

### 1. 📖 Deep Fundamentals & Formal Grammar
- Full **RFC 8259**, **ECMA-404**, and **RFC 7493 (I-JSON)** specifications.
- Mathematical **EBNF** (Extended Backus-Naur Form) production rules.
- IEEE 754 float limits ($2^{53}-1$) and the 64-bit ID precision trap.
- Complete matrix of strict RFC prohibitions (comments, trailing commas, single quotes, unquoted keys).

### 2. 🌐 The 8 Dialects & Flavors of JSON
- **Standard JSON (RFC 8259):** Universal web API contract.
- **JSON5:** ES5 extensions for human configurations (comments, trailing commas, hex numbers).
- **JSONC:** VS Code & TypeScript configuration standard.
- **NDJSON / JSON Lines (.jsonl):** High-throughput log streaming and LLM fine-tuning datasets.
- **GeoJSON (RFC 7946):** Geospatial geometries and FeatureCollections.
- **JSON-LD:** W3C Semantic Linked Data (`@context`, `@type`).
- **JSON Schema:** Draft 2020-12 meta-specifications.
- **BSON & CBOR:** Binary serialized formats with length prefixes.

### 3. 🧠 LLM Hallucination Taxonomy & Mechanics
- **BPE Tokenization Misalignment:** Why sub-word tokens trap models in syntax errors.
- **Auto-Regressive Blindness:** Missing lookahead causing token cutoff and unclosed braces.
- **3-Tier Hallucination Hierarchy:**
  - *Tier 1: Syntactic* (Markdown code fences, single quotes, trailing commas).
  - *Tier 2: Schema* (Invented keys, type inversions, enum drifts).
  - *Tier 3: Factual & Semantic* (Fabricated UUIDs, false certainty instead of `null`, math contradictions).

### 4. ⚡ 5-Tier Production Mitigation Architecture
1. **Constrained Decoding:** Logit masking with DFAs (OpenAI Structured Outputs, Outlines, GBNF).
2. **Strict Schema Contracts:** Pydantic V2 with `extra='forbid'` and Zod `.strict()`.
3. **Heuristic Pre-Repair:** Sub-millisecond CPU repair via `jsonrepair`.
4. **Closed-Loop Self-Correction:** Automated retries with parser diagnostic traces.
5. **Chain-of-Thought Scratchpad Separation:** `<scratchpad>` reasoning prior to `<json_payload>`.

### 5. 🤖 Multi-Model AI SDK Cheatsheet
Drop-in, copy-pasteable code for:
- **Google Gemini SDK** (`response_mime_type="application/json"` & `response_schema`)
- **OpenAI Structured Outputs** (`client.beta.chat.completions.parse`)
- **Anthropic Claude** (Tool choice schema gating)
- **Instructor Library** (Python & TypeScript automatic validation)
- **LangChain / LangGraph** (`with_structured_output`)

### 6. ⚡ Interactive Schema & Prompt Synthesizer
Paste any sample JSON object to automatically generate:
- Strict JSON Schema (Draft 2020-12)
- Pydantic V2 Model (`extra='forbid'`)
- TypeScript Zod Schema (`.strict()`)
- Calibrated Anti-Hallucination System Prompt

### 7. 🛡️ Enterprise Security, Streaming & Alternative Formats
- Defenses against **Prototype Pollution**, **JSON Bombs (DoS)**, and **Duplicate Key Attacks**.
- Real-time partial token parsing (`partial-json-parser`) for streaming UIs.
- Comparative matrix: **JSON vs YAML vs TOML vs Protocol Buffers vs Parquet**.

---

## 🚀 Quickstart & Local Usage

Clone the repository and open `index.html` directly in any modern browser:

```bash
git clone https://github.com/<your-username>/json-master-portal.git
cd json-master-portal

# On Windows:
start index.html

# On macOS:
open index.html

# On Linux:
xdg-open index.html
```

---

## 🌐 Deploy to GitHub Pages (Free Hosting)

1. Push this repository to GitHub.
2. In your repository on GitHub, navigate to:
   **Settings** ➔ **Pages**.
3. Under **Build and deployment**:
   - **Source:** Deploy from a branch.
   - **Branch:** `main` / `root`.
4. Click **Save**. Your portal will be live globally at:
   `https://<your-username>.github.io/json-master-portal/`

---

## 🧪 Testing

Run the automated integration test suite:

```bash
python tests/test_portal.py
```

---

## 📜 License

Licensed under the [MIT License](LICENSE). Contributions, stars, and pull requests are warmly welcomed!
