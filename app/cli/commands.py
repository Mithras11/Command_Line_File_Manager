import click
from directory_tree import display_tree

from app.logs.config import log_messages, logger_types
from app.utils import scanner
from app.utils.common import save_logs_to_file


# ### scan ###
@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "--sort",
    type=click.Choice(["name", "size", "date", "modified", "type"], case_sensitive=False),
    default="name",
    show_default=True,
    help="Sorting criteria.",
)
@click.option(
    "--desc",
    is_flag=True,
    help="Display result in descending order.",
)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def scan_files(dir_path: str, sort: str, desc: bool, save: bool, output: str) -> None:
    """DIR_PATH: Path to directory to be scanned"""

    message = scanner.scan_files(dir_path, sort, desc)
    click.echo(message)
    if save:
        save_logs_to_file(output, dir_path, message, logger_types.BASIC)


@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "--sort",
    type=click.Choice(["name", "size", "date", "modified"], case_sensitive=False),
    default="name",
    show_default=True,
    help="Sorting criteria.",
)
@click.option(
    "--desc",
    is_flag=True,
    help="Display result in descending order.",
)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def scan_subdirs(dir_path: str, sort: str, desc: bool, save: bool, output: str) -> None:
    """DIR_PATH: Path to directory to be scanned"""

    message = scanner.scan_subdirs(dir_path, sort, desc)
    click.echo(message)
    if save:
        save_logs_to_file(output, dir_path, message, logger_types.BASIC)


#############################################################
@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def build_catalog(dir_path: str, save: bool, output: str):
    """DIR_PATH: Path to directory to be scanned"""

    message = scanner.build_catalog(dir_path, save, output)
    click.echo(message)
    if save:
        save_logs_to_file(output, dir_path, message, logger_types.CATALOG)


@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def build_catalog_recursively(dir_path: str, save: bool, output: str) -> None:
    """DIR_PATH: Path to directory to be scanned"""

    message = scanner.get_recursive_catalog(dir_path, None)
    click.echo(message)
    if save:
        save_logs_to_file(output, dir_path, message, logger_types.RECURSIVE)


#############################################################
@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "-h",
    "--hidden",
    is_flag=True,
    help="Include hidden files and folders.",
)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def build_tree(dir_path: str, hidden: bool, save: bool, output: str) -> None:
    """DIR_PATH: Path to directory to be scanned"""

    tree_msg = scanner.build_tree(dir_path, hidden)
    click.echo(tree_msg)
    if save:
        save_logs_to_file(output, dir_path, tree_msg, logger_types.TREE)


@click.command()
@click.argument("dir_path", type=click.STRING)
@click.option(
    "-h",
    "--hidden",
    is_flag=True,
    help="Include hidden files and folders.",
)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def build_pretty_tree(dir_path: str, hidden: bool, save: bool, output: str) -> None:
    """DIR_PATH: Path to directory to be scanned"""

    tree_msg = display_tree(dir_path, string_rep=True, show_hidden=hidden)
    click.echo(tree_msg)
    if save:
        save_logs_to_file(output, dir_path, tree_msg, logger_types.TREE)


#############################################################
@click.command()
@click.argument("dir_path", type=click.STRING)
@click.argument("name", type=click.STRING)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def search_by_name(dir_path: str, name: str, save: bool, output: str) -> None:
    """
    Search by NAME inside DIR_PATH
    """
    log_msg = scanner.search_by_name(dir_path, name)
    click.echo(log_msg)
    if save:
        save_logs_to_file(output, dir_path, log_msg, logger_types.SEARCH)


@click.command()
@click.argument("dir_path", type=click.STRING)
@click.argument("name", type=click.STRING)
@click.option(
    "-s",
    "--save",
    is_flag=True,
    help="Save log message to file.",
)
@click.option(
    "-o",
    "--output",
    type=click.STRING,
    default=None,
    show_default=True,
    help="Path to output directory for the saved log file",
)
def search_by_name_recursively(dir_path: str, name: str, save: bool, output: str) -> None:
    """
    Search recursively by NAME inside DIR_PATH
    """

    log_msg = scanner.get_search_result(dir_path, None, name)
    if not log_msg:
        log_msg = log_messages.NOT_FOUND
    click.echo(log_msg)
    if save:
        save_logs_to_file(output, dir_path, log_msg, logger_types.SEARCH)


#############################################################

# ### organize ###
