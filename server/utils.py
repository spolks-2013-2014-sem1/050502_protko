def read_file_by_chunks(file_obj, chunk_size):
    """ Reads file by fixed-length chunks
    :type file_obj: file
    """
    file_obj.seek(0)
    while True:
        chunk = file_obj.read(chunk_size)
        if not chunk:
            break
        yield chunk