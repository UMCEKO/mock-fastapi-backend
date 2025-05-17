from app.utils.parser import mock_parse_file, MockParseResult

def test_mock_parse_file():
    mock_data = mock_parse_file(b"dummy bytes")

    assert isinstance(mock_data, list)
    assert 1 <= len(mock_data) <= 10

    for i, item in enumerate(mock_data):
        assert isinstance(item, MockParseResult)
        assert isinstance(item.content, str)
        assert isinstance(item.page, int)
        assert item.page == i
        assert 1 <= item.page <= 10