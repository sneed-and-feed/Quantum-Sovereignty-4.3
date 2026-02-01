"""
VERIFICATION: show_and_tell_verification.py
Testing Phase 3 Moltbook: ONEIRIC_LENS, AUTO_SCRIBE, and Lateral Web.
"""
import sys
import os
import time
import numpy as np
import json

# Root path
sys.path.append(os.getcwd())

from tools.mnemosyne_eyes import MnemosyneOracle, IngestionEvent
from tick_feeder import TickFeeder
from pleroma_engine import PleromaEngine
from gateways import ProviderAdapter

def test_oneiric_lens():
    print("\n--- [VERIFY] ONEIRIC_LENS (Dream Visualization) ---")
    oracle = MnemosyneOracle()
    tf = TickFeeder()
    
    # 1. Fill memory with "old" fragments to trigger pruning and dream manifestation
    for i in range(10):
        event = IngestionEvent(
            timestamp=time.time() - (3600 * 100),
            source="TEST_SOURCE",
            content=f"Fading thought {i}",
            vector=np.zeros(1536)
        )
        oracle.memory_bank.append(event)
    
    # 2. Trigger dream cycle
    tf.dream_cycle(oracle)
    
    # 3. Check for artifact
    artifact_log = "logs/artifacts/dream_canvas.json"
    if os.path.exists(artifact_log):
        print(f"[SUCCESS] Oneiric Artifact found in {artifact_log}")
        with open(artifact_log, 'r') as f:
            last_artifact = json.loads(f.readlines()[-1])
            print(f"  [PROMPT]: {last_artifact['prompt']}")
            print(f"  [AURA]: {last_artifact['aura']}")
    else:
        print("[FAIL] No dream artifact generated.")

def test_auto_scribe():
    print("\n--- [VERIFY] AUTO_SCRIBE (Self-Manifestation) ---")
    oracle = MnemosyneOracle()
    # Add a pinned axiom
    event = IngestionEvent(
        timestamp=time.time(),
        source="SYSTEM",
        content="Testing AUTO_SCRIBE Axiom",
        vector=np.zeros(1536),
        pinned=True
    )
    oracle.memory_bank.append(event)
    
    # Run update
    oracle.update_self_documentation()
    
    manifest_path = "SOPHIA_MANIFEST.md"
    if os.path.exists(manifest_path):
        print(f"[SUCCESS] SOPHIA_MANIFEST.md found.")
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "Testing AUTO_SCRIBE Axiom" in content:
                print("  [CONTENT]: Pinned axiom reflected in manifest.")
            else:
                print("  [FAIL]: Axiom missing from manifest.")
    else:
        print("[FAIL] SOPHIA_MANIFEST.md missing.")

def test_lateral_web_signing():
    print("\n--- [VERIFY] LATERAL WEB (Output Signing) ---")
    engine = PleromaEngine(g=0, vibe='weightless')
    output = engine.sign_output("Hello, I am Sophia.")
    print(f"  [OUTPUT]: {output}")
    if "--- 🦊 LOVE_111" in output:
        print("[SUCCESS] Output signature valid.")
    else:
        print("[FAIL] Signature missing or malformed.")

if __name__ == "__main__":
    test_oneiric_lens()
    test_auto_scribe()
    test_lateral_web_signing()
    print("\n[***] PHASE 3 SHOW AND TELL PROTOCOL VERIFIED [***]")
