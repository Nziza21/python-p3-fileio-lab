from lib.file_io import write_file, append_file, read_file

def test_write_and_read_file(tmp_path):
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."

    write_file(file_name, file_content)

    result = read_file(file_name)
    assert result == file_content

def test_append_and_read_file(tmp_path):
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "\nAppended content."

    write_file(file_name, file_content)
    append_file(file_name, append_content)

    result = read_file(file_name)
    expected_result = file_content + append_content
    assert result == expected_result