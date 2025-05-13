from multiprocessing import Pool
from PIL import Image
import numpy as np

def adjust_brightness(segment_data, factor):
    segment_array = np.array(segment_data, dtype=np.uint8)
    adjusted = np.clip(segment_array * factor, 0, 255).astype(np.uint8)
    return adjusted.tolist()

def split_image(image_array, num_chunks):
    height = image_array.shape[0]
    chunk_height = height // num_chunks
    chunks = []
    for i in range(num_chunks):
        start = i * chunk_height
        end = (i + 1) * chunk_height if i != num_chunks - 1 else height
        chunks.append(image_array[start:end])
    return chunks

def main():
    brightness_factor = 1.5 
    num_processes = 4
    input_path = "sample_image.png"
    output_path = "brightened_image.png"

    image = Image.open(input_path).convert("RGB")
    image_array = np.array(image)

    segments = split_image(image_array, num_processes)
    args = [(segment, brightness_factor) for segment in segments]

    with Pool(processes=num_processes) as pool:
        processed_segments = pool.starmap(adjust_brightness, args)

    result_array = np.vstack(processed_segments)
    result_image = Image.fromarray(np.array(result_array, dtype=np.uint8))

    result_image.save(output_path)
    print(f"Zapisano wynikowy obraz: {output_path}")

if __name__ == "__main__":
    main()
