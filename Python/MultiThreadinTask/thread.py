import threading

# Shared list to collect file contents (thread-safe approach)
file_contents = []
lock = threading.Lock()
# Function to read file content
def read_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    with lock:  # Ensure thread-safe appending
        file_contents.append(f"--- {file_name} ---\n{content}\n")

# Main
if __name__ == "__main__":
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    threads = []

    # Create threads for each file
    for file_name in file_list:
        t = threading.Thread(target=read_file, args=(file_name,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Write to merged.txt
    with open('merged.txt', 'w') as f:
        for content in file_contents:
            f.write(content)

    print("All files read and merged into 'merged.txt'")
