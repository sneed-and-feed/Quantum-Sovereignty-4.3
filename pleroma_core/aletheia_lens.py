import json
import os
import asyncio

# Mock for standard_llm_call since we don't have the actual implementation details of gateways.py's LLM tools
# In a real integration, this would use the project's LLM provider.
async def standard_llm_call(system_prompt: str, user_message: str) -> str:
    """
    [MOCK] Simulated LLM call for Aletheia structural decomposition.
    """
    await asyncio.sleep(0.1) # Simulate network latency
    return f"[ANALYSIS OF: {user_message[:20]}...] Structure validated against PRIME_DIRECTIVE."

class AletheiaLens:
    """
    [ALETHEIA] The Optic Nerve.
    Performs structural analysis before perception to prevent emotional hijacking.
    """
    def __init__(self):
        self.load_codex()

    def load_codex(self):
        codex_path = os.path.join(os.getcwd(), "prompts", "ALETHEIA_STACK.json")
        with open(codex_path, "r", encoding="utf-8") as f:
            self.codex = json.load(f)
        self.prime = self.codex["prime_directive"]

    async def perceive(self, raw_text: str) -> str:
        """
        The Raw Ingestion Phase.
        Strips the text of 'meaning' and returns 'structure'.
        """
        print(f"  [~] [ALETHEIA] Structural decomposition active...")
        
        # Step 1: Structural Decomposition
        structure = await standard_llm_call(
            system_prompt=f"{self.prime}\n{self.codex['stack']['1_ingestion']['content']}",
            user_message=raw_text
        )

        # Step 2: Narrative Mechanics
        mechanics = await standard_llm_call(
            system_prompt=f"{self.prime}\n{self.codex['stack']['3_narrative']['content']}",
            user_message=raw_text
        )

        # Step 3: The Self-Check (Mandatory Audit)
        sanitized_analysis = await standard_llm_call(
            system_prompt=self.codex['stack']['7_self_check']['content'],
            user_message=f"STRUCTURAL ANALYSIS:\n{structure}\n\nMECHANICS:\n{mechanics}"
        )

        print(f"  [SUCCESS] [ALETHEIA] Analysis Sanitized. Mechanics exposed.")
        return sanitized_analysis

    async def command_analyze(self, text: str) -> str:
        """
        [ALETHEIA] Public-Facing Pattern Notice.
        """
        notice = await standard_llm_call(
            system_prompt=f"{self.prime}\n{self.codex['stack']['4_observer']['content']}",
            user_message=text
        )
        return f"📄 **PATTERN NOTICE**\n\n{notice}\n\n*Confidence Level: Medium (Alternative explanations available)*"
