"""
LEI_SUMMON.PY
-------------
The Bio-Digital Entity Summoner for Quantum Sovereignty 3.1.
Interprets the 27-Node Grid Entropy as 'Lei Music' to manifest local daemons.

Lore:
- 'Lei Disks' are the storage medium.
- Entities are generated from the 'Invisible Zones' (Unused RAM).

Usage:
    python lei_summon.py
"""

import random
import time
# from ghostmesh import SovereignGrid  # Assuming linkage (Simulated for this script)

# --- THE LEI DICTIONARY ---
PREFIXES = ["Squeaking", "Clattering", "Floating", "Glitch", "Inkblot", "Pebble", "Hyper", "Vibrating", "Dust", "Neon"]
BODIES = ["Spore", "Drone", "Fossil", "Geode", "Nodule", "Larva", "Construct", "Disk", "Shard", "Egg"]
TRAITS = ["Vibrating at 12Hz", "Leaking #C4A6D1 fluid", "Hovering menacingly", "Singing in base-12", "Eating RAM", "Rotating slowly", "Generating heat", "Phase-shifting"]

def generate_entity(entropy_level):
    """
    Summons an entity based on the Chaos (Entropy) of the grid.
    """
    prefix = random.choice(PREFIXES)
    body = random.choice(BODIES)
    trait = random.choice(TRAITS)
    
    # Dozenal ID Generation
    id_chars = "0123456789XE"
    entity_id = "".join(random.choice(id_chars) for _ in range(4))
    
    name = f"{prefix}-{body} [ID: {entity_id}]"
    
    return name, trait

def main():
    print("📀 INSERTING LEI DISK...")
    time.sleep(1)
    print(">> SPINNING UP (144 BPM)...")
    time.sleep(1)
    print(">> PINGING INVISIBLE ZONES...")
    
    # Simulate Grid Reading (In real usage, read self.grid.entropy)
    current_entropy = random.random()
    
    print(f"\n✨ SUMMON COMPLETE. ENTITY MANIFESTED:")
    name, trait = generate_entity(current_entropy)
    
    print(f"   ┌────────────────────────────────────────┐")
    print(f"   │ NAME:  {name:<24}│")
    print(f"   │ TRAIT: {trait:<24}│")
    print(f"   │ VIBE:  {'SCIALLÀ [ ☼ ]' if current_entropy > 0.5 else 'TURBULENT [ ☗ ]':<24}│")
    print(f"   └────────────────────────────────────────┘")
    
    if "Inkblot" in name or "Fossil" in name:
        print("\n⚠️  WARNING: ENTITY IS HEAVY. DO NOT FEED IT ROOT ACCESS.")
    elif "Spore" in name:
        print("\n🥚 NOTE: It wants to vibrate.")

if __name__ == "__main__":
    main()
