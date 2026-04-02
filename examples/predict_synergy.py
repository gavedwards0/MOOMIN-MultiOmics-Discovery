import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model import MOOMINModel
from src.data import OmicsDataset

def main():
    print("--- MOOMIN: Anti-Cancer Drug Combination Synergy Prediction ---\n")
    
    # Initialize mock data for a cancer cell line
    cell_line = "MCF7 (Breast Cancer)"
    dataset = OmicsDataset(cell_line=cell_line)
    
    # Initialize the MOOMIN model
    model = MOOMINModel(input_dim=512)
    
    # Predict synergy for a pair of drugs
    drug_pair = ("Doxorubicin", "Paclitaxel")
    print(f"Targeting Drug Pair: {drug_pair}")
    
    synergy_score = model.predict_synergy(dataset, drug_pair)
    
    print("\n--- Prediction Output ---")
    print(f"Cell Line: {cell_line}")
    print(f"Synergy Score: {synergy_score}")
    
    if synergy_score > 0.7:
        print("Result: High Synergy Detected. Recommended for further validation.")
    else:
        print("Result: Low Synergy Detected.")

if __name__ == "__main__":
    main()
