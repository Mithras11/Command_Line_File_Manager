import logging

from app.logs import logger_types


class LoggerFactory:
    # TODO: etract ass CONFIG map outside class
    FILES = "/list.txt"
    CATALOG = "/catalog.txt"
    RECURSIVE_CATALOG = "/recursive_catalog.txt"
    TREE = "/tree.txt"
    SEARCH = "/search.txt"
    ORGANIZE = "/organize.txt"

    @classmethod
    def get_logger(cls, logger_type, output_dir):
        if logger_type == logger_types.BASIC:
            return cls._configure_logger(logger_types.BASIC, output_dir + cls.FILES)
        elif logger_type == logger_types.CATALOG:
            return cls._configure_logger(logger_types.CATALOG, output_dir + cls.CATALOG)
        elif logger_type == logger_types.RECURSIVE:
            return cls._configure_logger(logger_types.RECURSIVE, output_dir + cls.RECURSIVE_CATALOG)
        elif logger_type == logger_types.TREE:
            return cls._configure_logger(logger_types.TREE, output_dir + cls.TREE)
        elif logger_type == logger_types.SEARCH:
            return cls._configure_logger(logger_types.SEARCH, output_dir + cls.SEARCH)
        elif logger_type == logger_types.ORGANIZE:
            return cls._configure_logger(logger_types.ORGANIZE, output_dir + cls.ORGANIZE)

    @staticmethod
    def _configure_logger(logger_name, output_file_name):
        logger = logging.getLogger(logger_name)
        f_handler = logging.FileHandler(filename=output_file_name, mode="w")
        formatter = logging.Formatter("%(message)s")
        f_handler.setFormatter(formatter)
        logger.addHandler(f_handler)
        logger.setLevel(logging.INFO)
        return logger
