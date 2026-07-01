import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(0);G=12000
abund=rng.exponential(1,G);abund/=abund.sum()
depths=np.linspace(1e4,3e6,25);det=[]
for d in depths:
    exp=d*abund;det.append(int((1-np.exp(-exp)).sum()))
plt.figure(figsize=(7,4));plt.plot(depths/1e6,det,marker="o")
plt.xlabel("reads (millions)");plt.ylabel("genes detected");plt.title("Sequencing saturation (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"plateau ~{det[-1]} genes\n");print("ok")