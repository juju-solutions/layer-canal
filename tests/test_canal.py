from reactive import canal


def test_series_upgrade():
    assert canal.status.blocked.call_count == 0
    canal.pre_series_upgrade()
    assert canal.status.blocked.call_count == 1
