import os
import sys

from assertpy import assert_that

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from devopsprocessors.container import SampleContainer  # noqa: E402
from devopsprocessors.history.history_processor import HistoryProcessor  # noqa: E402


def test_history_from_di_container():
    container: SampleContainer = SampleContainer()
    container.config.from_ini(os.path.join(os.path.dirname(__file__), '../../app.ini'))
    container.init_resources()
    proc = container.history_processor_service()
    assert_that(proc).is_instance_of(HistoryProcessor)
