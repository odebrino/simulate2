import torch
import time

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.rand((10000, 10000), device=device)
    start = time.time()
    y = torch.mm(x, x)
    end = time.time()
    print(f"Matrix multiply done on {y.device} in {end - start:.3f} seconds")
else:
    print("Running on CPU only.")
