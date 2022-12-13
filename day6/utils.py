def read_char(input_file, buffer_size=10240):
    with open(input_file, "r", encoding="utf-8") as f:
        while True:
            buffered = f.read(buffer_size)
            if not buffered:
                break
            for char in buffered:
                yield char
        yield ''  # Handling empty file
