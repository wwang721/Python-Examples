# A great python progress bar module
# See https://github.com/tqdm/tqdm for more information

from tqdm import tqdm
from tqdm import trange
from time import sleep

for i in tqdm(range(10), desc= "Text You want"):
	sleep(0.1)

for i in trange(10):
	sleep(0.1)

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)

with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)

pbar = tqdm(initial=900, total=1000)
for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()

# tqdm can also be used in a command line or a shell script directly, see the GitHub link on the top.


