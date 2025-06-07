# runner.py
from openai import Runner
from .agents.persona_selector import persona_selector_agent
from .agents.kit_recommender_agent import kit_recommender_agent
from .agents.reference_finder_agent import reference_finder_agent
from .agents.supplier_recommender_agent import supplier_recommender_agent


def run_pipeline(century: str, region: str, role: str):
    """Run the multi-agent pipeline for a given persona."""

    persona_input = {
        "century": century,
        "region": region,
        "role": role,
    }
    persona = Runner.run_sync(
        agent=persona_selector_agent,
        input=persona_input
    ).final_output
    print("\n🛡 Persona Selected:", persona.persona)

    # Step 2: Get kit list from persona
    kit_list = Runner.run_sync(
        agent=kit_recommender_agent,
        input=persona.persona
    ).final_output
    print("\n⚔ Kit Items:", kit_list.items)

    # Step 3: Get references for each kit item
    references = {}
    for item in kit_list.items:
        ref = Runner.run_sync(
            agent=reference_finder_agent,
            input=item
        ).final_output
        references[item] = ref
        print(f"\n📜 Reference for {item}:", ref)

    # Step 4: Get suppliers for each kit item
    suppliers = {}
    for item in kit_list.items:
        sup = Runner.run_sync(
            agent=supplier_recommender_agent,
            input=item
        ).final_output
        suppliers[item] = sup
        print(f"\n🏷 Suppliers for {item}:", sup)

    return {
        "persona": persona,
        "kit": kit_list,
        "references": references,
        "suppliers": suppliers
    }


if __name__ == "__main__":
    result = run_pipeline("15th", "Western Europe", "knight")
