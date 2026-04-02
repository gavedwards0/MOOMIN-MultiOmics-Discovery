class OmicsDataset:
    """Mock dataset for omics data."""
    def __init__(self, cell_line: str):
        self.cell_line = cell_line
        self.features = {
            "transcriptomics": [0.1, 0.5, 0.2],
            "proteomics": [0.9, 0.3, 0.4]
        }
        print(f"[Data] Loaded Multi-Omics data for cell line: {cell_line}")
