import click
import logging
import click_logging

import os
import shutil

from click.exceptions import Abort

logger = logging.getLogger(__name__)
style_kwargs = {
    'error': dict(fg='red', blink=True),
    'exception': dict(fg='red', blink=True),
    'critical': dict(fg='red', blink=True)
}

click_logging.basic_config(logger, style_kwargs=style_kwargs)


@click.group()
@click_logging.simple_verbosity_option(logger)
def cli():
    pass


@cli.command()
def init():
    click.echo('Initializing bonfire...')
    current_dir = os.getcwd()

    directory = ".bonfire"

    # Create .bonfire directory
    path = os.path.join(current_dir, directory)
    create_dir(path)


def create_dir(dir_path):
    if os.path.isdir(dir_path):
        logger.info("Directory already exists")
    else:
        os.mkdir(dir_path)
        logger.info("Directory '% s' created" % os.path.basename(dir_path))


@ cli.command()
def restart():
    current_dir = os.getcwd()

    directory = ".bonfire"

    path = os.path.join(current_dir, directory)

    if os.path.isdir(path):
        if click.confirm(click.style(
                'Are you sure you want to start over?', fg='red'), abort=True):
            click.echo('Deleting .bonfire...')
            shutil.rmtree(path)
            logger.info("Directory '% s' deleted" % directory)
    else:
        logger.error("No .bonfire dir found, did you init?")
