from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from devopsprocessors.history.history_processor import init_history_processor


class SampleContainer(DeclarativeContainer):
    config = providers.Configuration()
    history_processor_service = providers.Resource(init_history_processor,
                                                   db_path=config.history.db_path,
                                                   input_file=config.history.input_file,
                                                   environment=config.history.environment
                                                   )
