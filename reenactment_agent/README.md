# 🛡️ Reenactment Agent

An OpenAI-powered multi-agent system designed to help historical reenactors build accurate military kits from specific time periods and regions. This system guides users from choosing a persona to sourcing historically accurate gear, complete with museum references and vetted vendors.

---

## 🔧 Project Features

- **Persona Selector Agent**: Helps users narrow down their historical role (e.g., 14th-century French archer, 15th-century English knight).
- **Kit Recommender Agent**: Generates a detailed gear list based on selected persona.
- **Reference Finder Agent**: Finds museum artifacts and period illustrations for each piece of gear.
- **Vendor Finder Agent**: Recommends respected, community-endorsed vendors or searches for options when no known supplier is found.

---

## 🧱 Project Structure

```bash
reenactment_agent/
├── agents/
│   ├── persona_selector.py         # Selects a persona based on user input
│   ├── kit_recommender.py          # Outputs kit list for that persona
│   ├── reference_finder.py         # Finds visual/museum references
│   ├── supplier_recommender.py     # Finds suppliers for each kit item
│
├── tools/
│   ├── suggest_persona.py
│   ├── generate_kit.py
│   ├── fetch_references.py
│   ├── recommend_suppliers.py
│
├── data/
│   └── supplier_list.json          # Source for known RAG vendors
│
├── runner.py                      # Orchestrates multi-agent handoffs
├── README.md                      # You're reading this
```

---

## 🚀 Getting Started

1. **Install dependencies**:
```bash
pip install openai pydantic
```

2. **Run the system**:
```bash
python runner.py
```

---

## 🧠 How It Works

1. **User Input**: User provides century, region, and role.
2. **Agent Chain**:
   - `PersonaSelectorAgent` ➝ chooses a persona
   - `KitRecommenderAgent` ➝ suggests a kit
   - `ReferenceFinderAgent` ➝ returns museum links and images
   - `VendorFinderAgent` ➝ provides a list of vendors or searches new ones

---

## 📌 Future Enhancements

- FastAPI or Streamlit frontend
- Vision input (upload a picture of your kit for feedback)
- Multi-lingual support
- Checklist export to PDF

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

MIT License
