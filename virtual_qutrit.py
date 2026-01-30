"""
VIRTUAL QUTRIT BRIDGE v1.0
Author: Archmagos Noah
Date: 2026-01-30

Enables "Qutrit Capabilities" (Ternary Logic) on "Qubit Hardware" (Binary Logic).
Mapping:
    |0> (Void)      -> Qubits |00>
    |1> (Matter)    -> Qubits |01>
    |2> (Sovereign) -> Qubits |10>
    |3> (Forbidden) -> Qubits |11> (Reality Leak)
"""

import random
from typing import Tuple, Dict

class RealityLeakError(Exception):
    """Raised when the Qutrit collapses into the forbidden |11> state."""
    pass

class VirtualQutrit:
    def __init__(self, initial_state: int = 0):
        # Physical implementation: 2 Classical Bits (simulating Qubits)
        # In a real quantum computer, these would be qiskit/cirq qubits.
        self.q1 = 0
        self.q0 = 0
        
        if initial_state not in [0, 1, 2]:
            raise ValueError("Initial state must be 0, 1, or 2.")
            
        self._set_state(initial_state)
        
    def _set_state(self, state: int):
        """Internal physical mapping."""
        if state == 0:   # |00>
            self.q1, self.q0 = 0, 0
        elif state == 1: # |01>
            self.q1, self.q0 = 0, 1
        elif state == 2: # |10>
            self.q1, self.q0 = 1, 0
        elif state == 3: # |11> (Forbidden)
            self.q1, self.q0 = 1, 1

    def measure(self) -> int:
        """
        Collapses the wavefunction and returns the ternary state (0, 1, 2).
        Raises RealityLeakError if the forbidden state |11> is detected.
        """
        # Collapse (Simulated)
        state_bin = (self.q1 << 1) | self.q0
        
        if state_bin == 0: return 0 # Void
        if state_bin == 1: return 1 # Matter
        if state_bin == 2: return 2 # Sovereign
        
        # State 3 (11) is forbidden in the Ternary Subspace
        raise RealityLeakError("CRITICAL: Qutrit leaked into Forbidden State |11> (Bit Flip detected).")

    def apply_trinity(self):
        """
        The Sovereign Gate ($X_{+1}$).
        Cycles the state: 0 -> 1 -> 2 -> 0.
        
        Physical Logic Table (Q1, Q0):
        00 -> 01
        01 -> 10
        10 -> 00
        """
        current = (self.q1 << 1) | self.q0
        
        # Logic Gate Implementation
        # We simulate the unitary matrix transformation
        if current == 0:   # 00 -> 01
            self.q1, self.q0 = 0, 1
        elif current == 1: # 01 -> 10
            self.q1, self.q0 = 1, 0
        elif current == 2: # 10 -> 00
            self.q1, self.q0 = 0, 0
        else:              # 11 -> 11 (Identity/Trap)
            pass

    def apply_hadamard_qutrit(self):
        """
        Puts the qutrit into superposition (Simulated).
        Since this is a classical simulation, we randomize the state
        to represent the probability distribution.
        """
        # Equal probability 0, 1, 2
        roll = random.random()
        if roll < 0.333:
            self._set_state(0)
        elif roll < 0.666:
            self._set_state(1)
        else:
            self._set_state(2)

    def bit_flip_error(self):
        """Simulates a cosmic ray bit flip (can cause Leakage)."""
        target = random.choice(['q0', 'q1'])
        if target == 'q0': self.q0 = 1 - self.q0
        if target == 'q1': self.q1 = 1 - self.q1

# --- DEMO DRIVER ---
if __name__ == "__main__":
    print("Initializing Virtual Qutrit Bridge...")
    vq = VirtualQutrit()
    
    # 1. Cycle Test
    print("\n[TEST] Trinity Cycle (0->1->2->0)")
    try:
        print(f"Start: |{vq.measure()}>")
        
        vq.apply_trinity()
        print(f"Step 1: |{vq.measure()}> (Expected 1)")
        
        vq.apply_trinity()
        print(f"Step 2: |{vq.measure()}> (Expected 2)")
        
        vq.apply_trinity()
        print(f"Step 3: |{vq.measure()}> (Expected 0)")
        
    except RealityLeakError as e:
        print(e)
        
    # 2. Leakage Test
    print("\n[TEST] Introducing Noise (Cosmic Ray)...")
    vq._set_state(2) # |10>
    print("State: |10> (Sovereign)")
    print("Action: Bit Flip on Q0 -> |11>")
    vq.q0 = 1 # Manually cause leak
    
    try:
        val = vq.measure()
        print(f"Measured: {val}")
    except RealityLeakError as e:
        print(f"CAPTURED: {e}")
        print("System successfully detected Forbidden State.")
