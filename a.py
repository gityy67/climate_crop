import pickle5 as pickle
import gzip

# Function to compress a pickle file using pickle5
def compress_pickle(input_file, output_file):
    # Read the original pickle file
    with open(input_file, 'rb') as f_in:
        data = pickle.load(f_in)
    
    # Compress the data and write to the new file using pickle5
    with gzip.open(output_file, 'wb') as f_out:
        pickle.dump(data, f_out, protocol=pickle.HIGHEST_PROTOCOL)

# Specify the input and output file paths
input_file = 'models.pkl'
output_file = 'compressed_data.pkl.gz'

# Compress the pickle file
compress_pickle(input_file, output_file)

# Check the size of the compressed file
import os
compressed_size = os.path.getsize(output_file)
print(f"Compressed file size: {compressed_size / (1024 * 1024)} MB")

# Ensure the size is within the limit
if compressed_size <= 20 * 1024 * 1024:
    print("The file size is within the 20 MB limit.")
else:
    print("The file size exceeds the 20 MB limit.")
