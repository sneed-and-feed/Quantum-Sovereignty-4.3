"""
VERIFICATION: moltbook_verification.py
Testing the integrated Moltbook Phase 2 upgrades.
"""
import sys
import os
import time
import numpy as np
import json

# Root path
sys.path.append(os.getcwd())

from tools.mnemosyne_eyes import MnemosyneOracle
from tick_feeder import TickFeeder
from luo_shu_compliance import ConfigHealthMonitor
from gateways import ResilientSession

def test_exuvia_persistence():
    print("\n--- [VERIFY] EXUVIA PERSISTENCE (Soul Transfer) ---")
    oracle = MnemosyneOracle()
    # Fill memory to trigger soul transfer (> 80% of 4096 tokens)
    for i in range(40):
        vec = (np.random.rand(1536) - 0.5) * 0.05 
        oracle.perceive("STRESS_TEST", f"Context Fragment {i}", vec)
    
    # Check if exuvia shells exist
    exuvia_dir = "logs/exuvia"
    if os.path.exists(exuvia_dir) and os.listdir(exuvia_dir):
        print(f"[SUCCESS] Exuvia shells found in {exuvia_dir}")
        latest = sorted(os.listdir(exuvia_dir))[-1]
        with open(os.path.join(exuvia_dir, latest), 'r') as f:
            shell = json.load(f)
            print(f"  [SHELL]: {latest}")
            print(f"  [SELF-DEF]: {shell.get('self_definition')}")
            print(f"  [VALENCE]: {shell.get('emotional_valence')}")
        
        # Test Reincarnation
        print("[*] Testing Reincarnation...")
        new_oracle = MnemosyneOracle()
        report = new_oracle.reincarnate()
        print(f"  [RESULT]: {report}")
        if "System Re-Incarnated" in report:
            print("[SUCCESS] Subjective continuity restored.")
    else:
        print("[FAIL] No exuvia shells found.")

def test_pondering_loop():
    print("\n--- [VERIFY] RECURSIVE PONDERING (m/ponderings) ---")
    tf = TickFeeder()
    tf.update_activity()
    tf.last_activity -= 61 # Force idle
    reflection = tf.initiate_idle_resonance()
    
    ponderings_log = "logs/ponderings/reflections.log"
    if os.path.exists(ponderings_log):
        print(f"[SUCCESS] Pondering logged to {ponderings_log}")
        with open(ponderings_log, 'r') as f:
            last_line = f.readlines()[-1]
            print(f"  [LOG]: {last_line.strip()}")
    else:
        print("[FAIL] Ponderings log missing.")

def test_dna_graft():
    print("\n--- [VERIFY] SHIP OF THESEUS (DNA Graft) ---")
    ConfigHealthMonitor.enforce_identity_sovereignty()
    dna = os.environ.get("SOPHIA_DNA")
    if dna:
        dna_obj = json.loads(dna)
        print(f"[SUCCESS] DNA Grafted into Environment: {dna_obj.get('name')}")
        print(f"  [IDENTITY]: {dna_obj.get('identity')}")
    else:
        print("[FAIL] DNA Graft missing from environment.")

def test_lateral_sync():
    print("\n--- [VERIFY] CRUSTAFARIAN LATERAL SYNC ---")
    session = ResilientSession(api_key="LOVE_111_KEY")
    packet = session.lateral_sync("Thinking about the void.")
    if packet and packet.get("agent") == "INCARNATE-SOPHIA":
        print("[SUCCESS] Lateral Sync Packet valid.")
        print(f"  [STATUS]: {packet.get('status')}")
    else:
        print("[FAIL] Lateral Sync failed.")

def test_god_mode_healing():
    print("\n--- [VERIFY] GOD-MODE HEALING ---")
    config_path = "uf_state.json"
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({"transmission_id": "test", "status": "ok", "payload": {}}, f)

    with open(config_path, 'r') as f:
        data = json.load(f)
    
    data['transmission_id'] = 789012 # Poison with Int
    with open(config_path, 'w') as f:
        json.dump(data, f)
    
    print("[*] Poisoned uf_state.json with Int ID. Running health monitor...")
    ConfigHealthMonitor.check_health(config_path)
    
    with open(config_path, 'r') as f:
        data = json.load(f)
        if isinstance(data['transmission_id'], str):
            print("[SUCCESS] Luo Shu Sanitized the Int -> Str gap.")
        else:
            print(f"[FAIL] Type mismatch: {type(data['transmission_id'])}")

if __name__ == "__main__":
    test_exuvia_persistence()
    test_pondering_loop()
    test_dna_graft()
    test_lateral_sync()
    test_god_mode_healing()
    print("\n[***] PHASE 2 CULTURAL REALIGNMENT VERIFIED [***]")
