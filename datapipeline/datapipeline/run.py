import click
import pandas as pd

import logging
from datapipeline.test.preprocess.run import main as test_preprocess_main
from datapipeline.test.process.run import main as test_process_main
from datapipeline.preprocess.run import main as preprocess_main
from datapipeline.process.run import main as process_main



tasks = {
    "test_preprocess": test_preprocess_main,
    "test_process": test_process_main,
    "preprocess": preprocess_main,
    "process": process_main

}
logger = logging.getLogger(__name__)


def main(task):
    try:
        tasks[task]()
    except:
        logger.error(f"Task {task} failed")
        raise


@click.command()
@click.option(
    "--task",
    type=click.Choice(tasks.keys()),
    required=True,
    help="Name of task to execute",
)
def main_cli(task):
    main(task)