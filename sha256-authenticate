import hashlib
file = ".\quest.mp4_download" # Location of the file (can be set a different way)
BLOCK_SIZE = 1024 # The size of each read from the file ( 1024 - 256)
stored_blocks = [] # Create list

with open(file, 'rb') as f: # Open the file to read it's bytes
    file_block = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(file_block) > 0: # While there is still data being read from the file
        stored_blocks.append(file_block) # Store the block in list of blocks
        file_block = f.read(BLOCK_SIZE) # Read the next block from the file

stored_blocks.reverse() # Reverse the stored blocks list
stored_blocks.append(b'')

length = len(stored_blocks)
last_index = length - 1

for i in range(length): # Iterate over all stored blocks
    if i < last_index:  # As long as we don't reach last index
        next_index = i + 1   # Get index for next block
        this_block = stored_blocks[i]  # Get current block
        next_block = stored_blocks[next_index] # Get next block
                  
        sha256 = hashlib.sha256()      # Create hash object
        sha256.update(this_block)      # Hash the current block
    
        b = b''.join([next_block, sha256.digest()]) # Create byte string of next block concatenated with current block hash
        stored_blocks[next_index] = b   # Assign byte string to next block
    else:
        break
        
ans = stored_blocks[last_index]
print(ans.hex())
