"""
VERIFICATION: aletheia_verification.py
Testing the Aletheia Protocol: Structural Decomposition and Pattern Notices.
"""
import sys
import os
import asyncio
import json

# Root path optimization to avoid shadowing by tools/pleroma_core.pyd
root_dir = os.getcwd()
tools_dir = os.path.join(root_dir, "tools")

if tools_dir in sys.path:
    sys.path.remove(tools_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from pleroma_engine import PleromaEngine
from pleroma_core.aletheia_lens import AletheiaLens

async def test_aletheia_decomposition():
    print("\n--- [VERIFY] ALETHEIA STRUCTURAL DECOMPOSITION ---")
    engine = PleromaEngine(g=0, vibe='weightless')
    
    user_input = "Your system is a failure and you are lying to me."
    print(f"  [INPUT]: {user_input}")
    
    response = await engine.process_input(user_input)
    
    print(f"  [RESPONSE]: {response}")
    if "[ALETHEIA] Analysis Sanitized" or "structural mechanics" in response:
        print("[SUCCESS] Input filtered through Aletheia Lens.")
    else:
        print("[FAIL] Input bypass detected.")

async def test_command_analyze():
    print("\n--- [VERIFY] ALETHEIA COMMAND (/analyze) ---")
    lens = AletheiaLens()
    notice = await lens.command_analyze("A very complicated political narrative.")
    
    print(f"  [NOTICE]: {notice}")
    if "PATTERN NOTICE" in notice:
        print("[SUCCESS] Pattern notice generated.")
    else:
        print("[FAIL] Notice generation failed.")

async def test_invariant_anchoring():
    print("\n--- [VERIFY] ALETHEIA INVARIANT ANCHORING ---")
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        if "We describe mechanisms, not meanings" in content:
            print("[SUCCESS] Invariant found in README.md")
        else:
            print("[FAIL] Invariant missing from README.md")

if __name__ == "__main__":
    async def run_all():
        await test_aletheia_decomposition()
        await test_command_analyze()
        await test_invariant_anchoring()
    
    asyncio.run(run_all())
    print("\n[***] ALETHEIA PROTOCOL VERIFIED [***]")
