import ray
from PIL import Image
import numpy as np

ray.init(local_mode=True, include_dashboard=False)  

@ray.remote
def brighten(part, factor):
    return np.clip(part * factor, 0, 255).astype(np.uint8)

def main():
    image = Image.open("image.jpg").convert("RGB")
    img_array = np.array(image)

    parts = np.array_split(img_array, 4, axis=0)

    futures = [brighten.remote(part, 3) for part in parts]
    results = ray.get(futures)

    final = np.vstack(results)
    Image.fromarray(final).save("output.jpg")

if __name__ == "__main__":
    main()
