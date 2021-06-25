import logging
import os
import sys
from typing import Text

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from devopsprocessors.history.history import History    # noqa: E402


def test_should_initialise_db() -> None:
    input_file: Text = str({'param1': 'value1'})
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/test.db'))
    logging.info(db_path)
    history = History(db_path=db_path, context=(input_file, 'test'))
    history.persist('hello')
