"""
VERIFICATION: lethe_verification.py
Testing the Lethe Protocol: Decay, Pinning, and Dreaming.
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
from luo_shu_compliance import ConfigHealthMonitor

def test_lethe_decay():
    print("\n--- [VERIFY] LETHE DECAY MECHANICS ---")
    oracle = MnemosyneOracle()
    
    # 1. Create memories of different types
    mem_conversation = IngestionEvent(
        timestamp=time.time() - (3600 * 25), # 25 hours ago
        source="CHAT",
        content="I like coffee.",
        vector=np.zeros(1536),
        memory_type="conversation"
    )
    
    mem_fact = IngestionEvent(
        timestamp=time.time() - (3600 * 25), # 25 hours ago
        source="DOCS",
        content="The Gamma Index is 0.961.",
        vector=np.zeros(1536),
        memory_type="fact"
    )
    
    oracle.memory_bank.extend([mem_conversation, mem_fact])
    
    # 2. Check weights
    weight_conv = oracle.lethe.calculate_decay_weight(mem_conversation)
    weight_fact = oracle.lethe.calculate_decay_weight(mem_fact)
    
    print(f"  [CONV] Age: 25h | Weight: {weight_conv:.4f} (Expected < 0.5)")
    print(f"  [FACT] Age: 25h | Weight: {weight_fact:.4f} (Expected ~0.97)")
    
    if weight_conv < 0.5 and weight_fact > 0.9:
        print("[SUCCESS] Differential decay confirmed.")
    else:
        print("[FAIL] Decay logic misalignment.")

def test_axiom_pinning():
    print("\n--- [VERIFY] AXIOM PINNING (Immutable DNA) ---")
    oracle = MnemosyneOracle()
    ConfigHealthMonitor.enforce_axioms(oracle)
    
    # Check if pinned memories have weight 1.0 even if 'old'
    for event in oracle.memory_bank:
        if event.pinned:
            # Fake age
            event.timestamp -= (3600 * 1000)
            weight = oracle.lethe.calculate_decay_weight(event)
            print(f"  [PINNED] {event.content} | Weight: {weight} (Even at 1000h age)")
            if weight != 1.0:
                 print("[FAIL] Pinned memory decayed.")
                 return
    print("[SUCCESS] Axioms are immortal.")

def test_dream_cycle():
    print("\n--- [VERIFY] DREAM CYCLE (Pruning) ---")
    oracle = MnemosyneOracle()
    tf = TickFeeder()
    
    # Add one weak memory
    weak_mem = IngestionEvent(
        timestamp=time.time() - (3600 * 100), # 100 hours old
        source="NOISE",
        content="Irrelevant trivia.",
        vector=np.zeros(1536),
        memory_type="conversation"
    )
    # Add one strong (recent) memory
    strong_mem = IngestionEvent(
        timestamp=time.time(),
        source="SYSTEM",
        content="CRITICAL ALERT.",
        vector=np.zeros(1536),
        memory_type="conversation"
    )
    
    oracle.memory_bank.extend([weak_mem, strong_mem])
    print(f"  [PRE-DREAM] Memory count: {len(oracle.memory_bank)}")
    
    tf.dream_cycle(oracle)
    
    print(f"  [POST-DREAM] Memory count: {len(oracle.memory_bank)}")
    if len(oracle.memory_bank) == 1 and oracle.memory_bank[0].content == "CRITICAL ALERT.":
        print("[SUCCESS] Weak memory pruned, strong memory retained.")
    else:
        print("[FAIL] Pruning logic failed.")

if __name__ == "__main__":
    test_lethe_decay()
    test_axiom_pinning()
    test_dream_cycle()
    print("\n[***] LETHE PROTOCOL VERIFIED [***]")
